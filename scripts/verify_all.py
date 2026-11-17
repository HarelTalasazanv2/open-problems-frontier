"""Replay published finite certificates. Analytic proofs are not machine-checked.

Credit and source roles: ../REFERENCES.md and ../ATTRIBUTION.txt.
Only the checked-in explicit plan is executed; no downloads or installations.
"""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import os
import subprocess
import sys
import time


BASE_CHECKS = frozenset({"c197", "graph-base", "graph-extension", "graph-chain",
                         "finite-fields", "quartics", "graph-counting", "periods",
                         "finite-sieve", "unit-fractions", "external-graph",
                         "curvature", "elliptic", "degree-projection", "geometry181",
                         "external-matrices", "external-relations", "external-csv668"})
EXTERNAL_CONTRACTS = {
    "external-graph": ("graph-seed", "{EXTERNAL_SEED}"),
    "external-matrices": ("matrix-root", "{MATRIX_ROOT}"),
    "external-relations": ("matrix-root", "{MATRIX_ROOT}"),
    "external-csv668": ("matrix-root", "{MATRIX_ROOT}"),
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def inside(root, relative):
    require(isinstance(relative, str) and relative and not Path(relative).is_absolute(),
            "A nonempty repository-relative path is required")
    require(".." not in Path(relative).parts, "Parent traversal is forbidden")
    path = (root / relative).resolve()
    require(path.is_relative_to(root.resolve()), "Path escapes repository")
    return path


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def check_integrity(root):
    manifest = load(root / "VERIFICATION_MANIFEST.json")
    require(manifest["schema"] == "OPF_FILE_SHA256_V1", "Manifest schema")
    entries = manifest["files"]
    paths = [entry["path"] for entry in entries]
    require(paths and len(paths) == len(set(paths)), "Empty or duplicate file membership")
    required = {"RESULTS.json", "RESULTS.md", "PUBLISHED_RECORD_IDS.json",
                "VERIFICATION_PLAN.json", "scripts/verify_all.py",
                "scripts/test_verify_all.py", ".github/workflows/verify.yml"}
    require(required <= set(paths), "Missing verification infrastructure membership")
    for entry in entries:
        path = inside(root, entry["path"])
        require(path.is_file(), "Missing file: " + entry["path"])
        data = path.read_bytes()
        require(type(entry["bytes"]) is int and len(data) == entry["bytes"],
                "Wrong byte size: " + entry["path"])
        require(sha256(data).hexdigest() == entry["sha256"],
                "Wrong file hash: " + entry["path"])
    return len(entries)


def check_plan(root):
    plan = load(root / "VERIFICATION_PLAN.json")
    require(plan["schema"] == "OPF_REPLAY_PLAN_V1", "Plan schema")
    tasks = plan["checks"]
    ids = [task["id"] for task in tasks]
    require(len(ids) == len(set(ids)) and BASE_CHECKS <= set(ids),
            "Missing or duplicate mandatory checker")
    for task in tasks:
        require(task["kind"] in {"self-contained", "external-input"}, "Checker kind")
        script = inside(root, task["script"])
        require(script.is_file() and script.suffix == ".py", "Missing checker script")
        require(isinstance(task["arguments"], list) and
                all(isinstance(arg, str) for arg in task["arguments"]), "Checker arguments")
        require(isinstance(task["expected"], dict) and task["expected"], "Empty success contract")
        require(type(task["timeout_seconds"]) is int and
                0 < task["timeout_seconds"] <= 240, "Unbounded checker timeout")
        tokens = [a for a in task["arguments"] if a in {"{EXTERNAL_SEED}", "{MATRIX_ROOT}"}]
        if task["kind"] == "external-input":
            require(task["id"] in EXTERNAL_CONTRACTS, "Unknown external checker")
            kind, token = EXTERNAL_CONTRACTS[task["id"]]
            require(task.get("external_input", "graph-seed") == kind and tokens == [token],
                    "External input type/token mismatch")
        else:
            require(not tokens and task["id"] not in EXTERNAL_CONTRACTS,
                    "External obligation cannot become self-contained")
    return tasks


def check_results(root, tasks):
    data = load(root / "RESULTS.json")
    records = data["results"]
    ids = [record["id"] for record in records]
    expected = load(root / "PUBLISHED_RECORD_IDS.json")["ids"]
    require(ids and len(ids) == len(set(ids)), "Empty or duplicate result membership")
    require(len(expected) == len(set(expected)) and set(ids) == set(expected),
            "Published result membership mismatch")
    check_ids = {task["id"] for task in tasks}
    for record in records:
        require(record["statement"] and record["scope"] and record["novelty"],
                "Missing statement, scope or novelty ceiling")
        require(record["outcome"] in {"PROVED", "CONDITIONALLY_PROVED", "CERTIFIED_RANGE"},
                "Unsupported publication outcome")
        require(record["verification"] in {"finite-certificate", "analytic-proof",
                                           "external-input-required", "mixed", "source-contract"},
                "Unknown verification class")
        for key in ["proofs", "evidence"]:
            require(isinstance(record[key], list) and record[key], "Missing evidence list")
            for relative in record[key]:
                require(inside(root, relative).is_file(), "Missing result evidence: " + relative)
        require(set(record["checks"]) <= check_ids, "Unknown checker reference")
        if record["verification"] not in {"analytic-proof", "source-contract"}:
            require(record["checks"], "Computational result without checker")
        if record["verification"] == "external-input-required":
            require(any(t["kind"] == "external-input" and t["id"] in record["checks"]
                        for t in tasks), "Lost external-input dependency")
    return len(records), sum(r["verification"] == "analytic-proof" for r in records)


def execute_task(root, task, seed=None, matrix_root=None):
    input_type = task.get("external_input", "graph-seed")
    supplied = seed if input_type == "graph-seed" else matrix_root
    if task["kind"] == "external-input" and supplied is None:
        return {"id": task["id"], "state": "MISSING_EXTERNAL_INPUT",
                "detail": "Exact external " + input_type + " required; this package was not replayed."}
    script = inside(root, task["script"])
    substitutions = {"{EXTERNAL_SEED}": seed, "{MATRIX_ROOT}": matrix_root}
    arguments = [str(substitutions[arg]) if arg in substitutions and substitutions[arg] is not None else arg
                 for arg in task["arguments"]]
    require(not any(a in substitutions for a in arguments), "Unresolved external input")
    mode = ["-" + "O" * sys.flags.optimize] if sys.flags.optimize else []
    command = [sys.executable, "-B"] + mode + [str(script)] + arguments
    started = time.monotonic()
    try:
        child = subprocess.run(command, cwd=script.parent, capture_output=True,
                               text=True, timeout=task["timeout_seconds"],
                               env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    except subprocess.TimeoutExpired:
        return {"id": task["id"], "state": "FAILED", "reason": "Checker timeout"}
    result = {"id": task["id"], "returncode": child.returncode,
              "seconds": round(time.monotonic() - started, 6)}
    if child.returncode:
        return {**result, "state": "FAILED", "reason": "Nonzero child exit",
                "stdout": child.stdout[-4000:], "stderr": child.stderr[-4000:]}
    try:
        output = json.loads(child.stdout)
    except (ValueError, TypeError):
        return {**result, "state": "FAILED", "reason": "No single valid JSON result",
                "stdout": child.stdout[-4000:]}
    if not isinstance(output, dict) or any(type(output.get(k)) is not type(v) or
            output.get(k) != v for k, v in task["expected"].items()):
        return {**result, "state": "FAILED", "reason": "Checker success contract mismatch",
                "observed": output}
    return {**result, "state": "VERIFIED_REPLAY", "observed": output}


def verify(root, seed=None, require_external=False, matrix_root=None):
    files = check_integrity(root)
    tasks = check_plan(root)
    count, analytic = check_results(root, tasks)
    results = [execute_task(root, task, seed, matrix_root) for task in tasks]
    failed = [row["id"] for row in results if row["state"] == "FAILED"]
    missing = [row["id"] for row in results if row["state"] == "MISSING_EXTERNAL_INPUT"]
    success = not failed and not (require_external and missing)
    state = "FAILED" if not success else (
        "SELF_CONTAINED_REPLAYS_VERIFIED_EXTERNAL_INPUT_PENDING" if missing else
        "DECLARED_REPLAYS_VERIFIED")
    return {"status": state, "success_at_declared_scope": success,
            "all_declared_replays_verified": success and not missing,
            "files_hash_checked": files, "indexed_records": count,
            "analytic_only_records_not_machine_proved": analytic,
            "source_contract_records_not_theorems": sum(
                r["verification"] == "source-contract" for r in load(root / "RESULTS.json")["results"]),
            "optimization": sys.flags.optimize, "python": sys.version,
            "missing_external_checks": missing, "failed_checks": failed,
            "checks": results,
            "claim_ceiling": "Replay of declared certificates and index/integrity checks only. "
                             "No machine proof of analytic arguments, novelty, or global resolution."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--external-seed", type=Path)
    parser.add_argument("--matrix-root", type=Path,
                        help="Folder containing the exact separately supplied Hadamard/source inputs")
    parser.add_argument("--require-external", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    seed = args.external_seed.resolve() if args.external_seed else None
    matrix_root = args.matrix_root.resolve() if args.matrix_root else None
    try:
        result = verify(root, seed, args.require_external, matrix_root)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        result = {"status": "FAILED", "success_at_declared_scope": False,
                  "all_declared_replays_verified": False,
                  "reason": type(exc).__name__ + ": " + str(exc)}
    text = json.dumps(result, indent=2) + "\n"
    if args.report:
        with args.report.open("x", encoding="utf-8") as output:
            output.write(text)
    print(text, end="")
    return 0 if result["success_at_declared_scope"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
