"""Input-boundary regressions; these tests do not prove the research claims."""
from pathlib import Path
from hashlib import sha256
import copy
import json
import shutil
import tempfile
import unittest
import warnings
import zipfile
import prepare_inputs as P

REPOSITORY = Path(__file__).resolve().parents[1]


class FrozenInputs(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=REPOSITORY)
        self.root = Path(self.tmp.name)
        self.folder = self.root / 'verification-inputs'
        self.folder.mkdir()
        self.archive = self.root / P.ARCHIVE_PATH
        for name in ('INPUTS.json', 'inputs-v1.zip'):
            shutil.copyfile(REPOSITORY/'verification-inputs'/name, self.folder/name)
        self.manifest = json.loads((self.folder/'INPUTS.json').read_text())

    def tearDown(self):
        self.tmp.cleanup()

    def save_manifest(self):
        (self.folder/'INPUTS.json').write_text(json.dumps(self.manifest))

    def rewrite_archive(self, change):
        with zipfile.ZipFile(self.archive) as bundle:
            rows = [(copy.copy(i), bundle.read(i)) for i in bundle.infolist()]
        rows = change(rows)
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)  # Intentional duplicate fixture.
            with zipfile.ZipFile(self.archive, 'w') as bundle:
                for info, raw in rows:
                    bundle.writestr(info, raw)
        raw = self.archive.read_bytes()
        self.manifest['archive'].update(bytes=len(raw), sha256=sha256(raw).hexdigest())
        self.save_manifest()

    def test_healthy_exact21_inputs_reach_materializer(self):
        out = self.root/'fresh inputs'
        result = P.materialize(self.root, out)
        self.assertEqual(result['members'], 21)
        self.assertEqual(result['status'], 'EXACT_INPUTS_MATERIALIZED')
        self.assertFalse(result['source_program_executed'])
        self.assertEqual({q.relative_to(out).as_posix() for q in out.rglob('*') if q.is_file()}, P.EXPECTED_FILES)
        for row in self.manifest['files']:
            self.assertEqual(sha256((out/row['path']).read_bytes()).hexdigest(), row['sha256'])

    def test_damaged_archive_hash_rejected(self):
        raw = bytearray(self.archive.read_bytes()); raw[-1] ^= 1
        self.archive.write_bytes(raw)
        with self.assertRaisesRegex(ValueError, 'Archive hash'):
            P.read_members(self.root)

    def test_missing_archive_rejected(self):
        self.archive.unlink()
        with self.assertRaisesRegex(ValueError, 'Regular input archive'):
            P.read_members(self.root)

    def test_missing_member_even_with_new_archive_hash_rejected(self):
        self.rewrite_archive(lambda rows: rows[1:])
        with self.assertRaisesRegex(ValueError, 'archive membership'):
            P.read_members(self.root)

    def test_duplicate_member_even_with_new_archive_hash_rejected(self):
        self.rewrite_archive(lambda rows: rows + [rows[0]])
        with self.assertRaisesRegex(ValueError, 'duplicates forbidden'):
            P.read_members(self.root)

    def test_extra_member_even_with_new_archive_hash_rejected(self):
        self.rewrite_archive(lambda rows: rows + [(zipfile.ZipInfo('extra.txt'), b'x')])
        with self.assertRaisesRegex(ValueError, 'archive membership'):
            P.read_members(self.root)

    def test_traversal_name_rejected_before_writing(self):
        def mutate(rows):
            rows[0][0].filename = '../escape.txt'
            return rows
        self.rewrite_archive(mutate)
        with self.assertRaisesRegex(ValueError, 'archive membership'):
            P.materialize(self.root, self.root/'output')
        self.assertFalse((self.root/'output').exists())

    def test_symlink_member_rejected(self):
        def mutate(rows):
            rows[0][0].external_attr = 0o120777 << 16
            return rows
        self.rewrite_archive(mutate)
        with self.assertRaisesRegex(ValueError, 'links forbidden'):
            P.read_members(self.root)

    def test_wrong_member_bytes_even_with_new_archive_hash_rejected(self):
        def mutate(rows):
            info, raw = rows[0]
            data = bytearray(raw); data[0] ^= 1
            rows[0] = (info, bytes(data))
            return rows
        self.rewrite_archive(mutate)
        with self.assertRaisesRegex(ValueError, 'Member byte/hash'):
            P.read_members(self.root)

    def test_manifest_cannot_drop_expected_input(self):
        self.manifest['files'].pop(); self.save_manifest()
        with self.assertRaisesRegex(ValueError, 'manifest membership'):
            P.read_members(self.root)

    def test_manifest_cannot_duplicate_expected_input(self):
        self.manifest['files'].append(self.manifest['files'][0]); self.save_manifest()
        with self.assertRaisesRegex(ValueError, 'manifest membership'):
            P.read_members(self.root)

    def test_boolean_byte_count_is_not_integer_contract(self):
        self.manifest['files'][0]['bytes'] = True; self.save_manifest()
        with self.assertRaisesRegex(ValueError, 'Bounded member'):
            P.read_members(self.root)

    def test_oversized_member_metadata_rejected(self):
        self.manifest['files'][0]['bytes'] = P.MAX_MEMBER_BYTES + 1; self.save_manifest()
        with self.assertRaisesRegex(ValueError, 'Bounded member'):
            P.read_members(self.root)

    def test_existing_output_is_preserved(self):
        out = self.root/'existing'; out.mkdir(); (out/'keep.txt').write_text('keep')
        with self.assertRaisesRegex(ValueError, 'no overwrite'):
            P.materialize(self.root, out)
        self.assertEqual((out/'keep.txt').read_text(), 'keep')

    def test_outside_checkout_output_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'inside this checkout'):
            P.materialize(self.root, self.root.parent/'not-allowed')

    def test_dangling_output_symlink_is_rejected(self):
        out = self.root/'linked-output'
        out.symlink_to('uncreated-target', target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'Symbolic-link output'):
            P.materialize(self.root, out)
        self.assertFalse((self.root/'uncreated-target').exists())


if __name__ == '__main__':
    unittest.main()
