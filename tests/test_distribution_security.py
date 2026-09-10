import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import toolkit

class DistributionSecurityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.patch = patch.object(toolkit, 'ROOT', self.root)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        self.skill = self.root / 'skills' / 'example'
        self.skill.mkdir(parents=True)
        (self.skill / 'SKILL.md').write_text('Synthetic test skill')
        (self.root / 'guides').mkdir()
        (self.root / 'PRINCIPLES.md').write_text('Synthetic principles')
    def test_normal_assets_are_preserved(self):
        (self.skill / 'template.txt').write_text('example')
        self.assertEqual(toolkit.portable_files(self.skill)['template.txt'], b'example')
    def test_credential_files_are_rejected(self):
        for name in ['.env', '.env.local', 'credentials.json', 'private.pem', '.npmrc']:
            with self.subTest(name=name):
                source = self.skill / name
                source.write_text('synthetic secret')
                with self.assertRaisesRegex(ValueError, 'credential-like'):
                    toolkit.portable_files(self.skill)
                source.unlink()
    def test_linked_file_is_not_dereferenced(self):
        external = self.root / 'private.txt'; external.write_text('synthetic private content')
        (self.skill / 'linked.txt').symlink_to(external)
        with self.assertRaisesRegex(ValueError, 'linked'):
            toolkit.portable_files(self.skill)
    def test_linked_directory_is_rejected(self):
        (self.skill / 'linked-folder').symlink_to(self.root / 'guides', target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'linked'):
            toolkit.portable_files(self.skill)
    def test_linked_shared_guide_is_rejected(self):
        external = self.root / 'private.txt'; external.write_text('synthetic private content')
        (self.root / 'guides' / 'linked.md').symlink_to(external)
        with self.assertRaisesRegex(ValueError, 'linked'):
            toolkit.portable_files(self.skill)
    def test_parent_traversal_is_rejected(self):
        with self.assertRaises(ValueError):
            toolkit.read_public_file(self.root / '..' / 'outside.txt')
    def test_build_cache_is_not_distributed(self):
        cache = self.skill / '__pycache__'; cache.mkdir()
        (cache / 'temp.pyc').write_bytes(b'cache')
        self.assertNotIn('__pycache__/temp.pyc', toolkit.portable_files(self.skill))

if __name__ == '__main__': unittest.main()
