"""Verify and materialize the21 frozen data inputs. Never execute their contents.

Credit and source roles: ../verification-inputs/REFERENCES.md.
The output must be a fresh directory inside this checkout, with one writer.
"""
from pathlib import Path, PurePosixPath
from hashlib import sha256
import argparse
import json
import stat
import tempfile
import zipfile

ORDERS = (716, 892, 1132, 1212, 1244, 1388, 1436, 1676, 1772, 1916,
          1940, 1948, 1964, 2092, 2292)
EXPECTED_FILES = frozenset(
    ['matrices/H' + str(n) + '.gz' for n in ORDERS] +
    ['graph/seed.g6', 'matrices/H668.csv', 'matrices/author_x.data',
     'matrices/author_decoder_actual.html', 'matrices/author_payload.signs',
     'matrices/decoded_author_program_source.txt'])
ARCHIVE_PATH = 'verification-inputs/inputs-v1.zip'
MAX_TOTAL_BYTES = 8_000_000
MAX_MEMBER_BYTES = 2_000_000


def need(ok, message):
    if not ok:
        raise ValueError(message)


def digest(value):
    return (isinstance(value, str) and len(value) == 64 and
            all(c in '0123456789abcdef' for c in value))


def read_contract(root):
    manifest = json.loads((root / 'verification-inputs/INPUTS.json').read_text('utf8'))
    need(manifest['schema'] == 'OPF_REPLAY_INPUT_BUNDLE_V1', 'Input manifest schema')
    rows = manifest['files']
    need(type(rows) is list, 'Input member list')
    names = [r['path'] for r in rows]
    need(len(names) == len(set(names)) and set(names) == EXPECTED_FILES,
         'Exact21-member manifest membership')
    for row in rows:
        name = row['path']
        need(not PurePosixPath(name).is_absolute() and
             '..' not in PurePosixPath(name).parts and '\\' not in name,
             'Safe member path')
        need(type(row['bytes']) is int and 0 < row['bytes'] <= MAX_MEMBER_BYTES,
             'Bounded member byte count')
        need(digest(row['sha256']), 'Member digest format')
    need(sum(r['bytes'] for r in rows) <= MAX_TOTAL_BYTES, 'Bounded total byte count')
    archive = manifest['archive']
    need(archive['path'] == ARCHIVE_PATH and digest(archive['sha256']),
         'Exact archive location and digest')
    need(type(archive['bytes']) is int and 0 < archive['bytes'] <= MAX_TOTAL_BYTES,
         'Bounded archive byte count')
    return manifest


def read_members(root):
    manifest = read_contract(root)
    archive = manifest['archive']
    path = root / ARCHIVE_PATH
    need(path.is_file() and not path.is_symlink(), 'Regular input archive required')
    need(path.stat().st_size == archive['bytes'], 'Archive byte identity')
    raw = path.read_bytes()
    need(sha256(raw).hexdigest() == archive['sha256'], 'Archive hash identity')
    expected = {r['path']: r for r in manifest['files']}
    payloads = {}
    with zipfile.ZipFile(path) as bundle:
        infos = bundle.infolist()
        names = [i.filename for i in infos]
        need(len(names) == len(set(names)) and set(names) == EXPECTED_FILES,
             'Exact21-member archive membership; duplicates forbidden')
        for info in infos:
            row = expected[info.filename]
            mode = stat.S_IFMT(info.external_attr >> 16)
            need(not info.is_dir() and mode in (0, stat.S_IFREG),
                 'Regular input member; links forbidden')
            need(not info.flag_bits & 1 and
                 info.compress_type in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED),
                 'Unencrypted supported data compression')
            need(info.file_size == row['bytes'], 'Declared member byte identity')
            with bundle.open(info) as source:
                data = source.read(row['bytes'] + 1)
            need(len(data) == row['bytes'] and
                 sha256(data).hexdigest() == row['sha256'], 'Member byte/hash identity')
            payloads[info.filename] = data
    return manifest, payloads


def materialize(root, output):
    root = root.resolve()
    need(not output.is_symlink(), 'Symbolic-link output forbidden')
    output = output.resolve()
    need(output.is_relative_to(root) and output != root,
         'Output must stay inside this checkout')
    need(not output.exists(), 'Fresh output directory required; no overwrite')
    manifest, payloads = read_members(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.opf-input-stage-', dir=output.parent) as tmp:
        stage = Path(tmp) / 'contents'
        stage.mkdir()
        for name, data in sorted(payloads.items()):
            target = stage / name
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open('xb') as stream:
                stream.write(data)
        need(not output.exists(), 'Fresh single-writer output required')
        stage.rename(output)
    return {'status': 'EXACT_INPUTS_MATERIALIZED', 'success': True,
            'members': len(payloads), 'bytes': sum(map(len, payloads.values())),
            'archive_sha256': manifest['archive']['sha256'],
            'directory': output.relative_to(root).as_posix(),
            'source_program_executed': False,
            'claim_ceiling': 'Exact data materialization only. Mathematical consumers must still replay; no source-authentication, rights or theorem inference.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('.verification-inputs'))
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    output = args.output if args.output.is_absolute() else root / args.output
    try:
        # Check the complete published file manifest before materializing any data.
        import verify_all
        verify_all.check_integrity(root)
        result = materialize(root, output)
    except (ValueError, KeyError, TypeError, OSError, RuntimeError, zipfile.BadZipFile) as exc:
        result = {'status': 'FAILED_INPUT_MATERIALIZATION', 'success': False,
                  'reason': type(exc).__name__ + ': ' + str(exc)}
    text = json.dumps(result, indent=2) + '\n'
    if args.report:
        with args.report.open('x', encoding='utf8') as stream:
            stream.write(text)
    print(text, end='')
    return 0 if result['success'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
