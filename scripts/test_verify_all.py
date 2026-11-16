"""Focused harness controls; mathematical controls reside in each checker."""
from pathlib import Path
import json
import tempfile
import unittest
import verify_all as V


class RunnerContract(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name).resolve()
        self.task = {"id": "fixture", "kind": "self-contained", "script": "child.py",
                     "arguments": [], "expected": {"status": "PASS", "cases": 3},
                     "timeout_seconds": 2}

    def tearDown(self):
        self.tmp.cleanup()

    def child(self, text):
        (self.root / "child.py").write_text(text)
        return V.execute_task(self.root, self.task)

    def test_healthy_child_reaches_json_consumer(self):
        result = self.child('print(\'{"status":"PASS","cases":3}\')\n')
        self.assertEqual(result["state"], "VERIFIED_REPLAY")

    def test_nonzero_exit_cannot_be_masked_by_pass_json(self):
        result = self.child('print(\'{"status":"PASS","cases":3}\')\nraise SystemExit(7)\n')
        self.assertEqual(result["state"], "FAILED")
        self.assertEqual(result["returncode"], 7)

    def test_wrong_membership_count_is_not_pass(self):
        self.assertEqual(self.child('print(\'{"status":"PASS","cases":2}\')')["state"], "FAILED")

    def test_boolean_does_not_equal_integer_contract(self):
        self.task["expected"]["cases"] = 1
        self.assertEqual(self.child('print(\'{"status":"PASS","cases":true}\')')["state"], "FAILED")

    def test_missing_json_is_not_pass(self):
        self.assertEqual(self.child('print("looks successful")')["state"], "FAILED")

    def test_false_verdict_is_not_pass(self):
        self.assertEqual(self.child('print(\'{"status":"FAIL","cases":3}\')')["state"], "FAILED")

    def test_timeout_is_failure(self):
        self.task["timeout_seconds"] = 1
        self.assertEqual(self.child('import time;time.sleep(3)')["state"], "FAILED")

    def test_external_input_absence_is_explicit(self):
        self.task["kind"] = "external-input"
        result = V.execute_task(self.root, self.task)
        self.assertEqual(result["state"], "MISSING_EXTERNAL_INPUT")
        self.assertNotEqual(result["state"], "VERIFIED_REPLAY")

    def test_parent_traversal_rejected(self):
        with self.assertRaises(ValueError):
            V.inside(self.root, "../outside.py")

    def test_missing_mandatory_check_rejected(self):
        (self.root / "VERIFICATION_PLAN.json").write_text(json.dumps({
            "schema": "OPF_REPLAY_PLAN_V1", "checks": []}))
        with self.assertRaisesRegex(ValueError, "mandatory"):
            V.check_plan(self.root)


if __name__ == "__main__":
    unittest.main()
