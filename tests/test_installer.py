import contextlib
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from install import install, identical
from toolkit import portable_files, skills
from unittest.mock import patch

class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.dest = self.base / 'agent' / 'skills'
        self.files = {'SKILL.md': b'original', 'references/guide.md': b'guide'}
    def run_install(self, files=None, dry=False):
        with contextlib.redirect_stdout(io.StringIO()):
            install(self.dest, 'example', self.files if files is None else files, dry)
    def test_dry_run_has_no_side_effects(self):
        self.run_install(dry=True)
        self.assertFalse(self.dest.parent.exists())
    def test_install_and_unchanged(self):
        self.run_install()
        self.assertTrue(identical(self.dest/'example', self.files))
        self.run_install()
        self.assertFalse((self.dest.parent/'skills-toolkit-backups').exists())
    def test_update_preserves_custom_files_in_backup(self):
        self.run_install()
        (self.dest/'example/custom.md').write_text('my edits')
        self.run_install({'SKILL.md': b'new'})
        self.assertEqual((self.dest/'example/SKILL.md').read_bytes(), b'new')
        backups = list((self.dest.parent/'skills-toolkit-backups').glob('*/example'))
        self.assertEqual(len(backups), 1)
        self.assertEqual((backups[0]/'custom.md').read_text(), 'my edits')
        self.assertEqual((backups[0]/'SKILL.md').read_bytes(), b'original')
        self.assertFalse((self.dest/'example/custom.md').exists())
    def test_failed_replacement_restores_previous_copy(self):
        self.run_install()
        original_rename = Path.rename
        def fail_stage(path, target):
            if path.parent.name.startswith('toolkit-stage-'):
                raise OSError('simulated replacement failure')
            return original_rename(path, target)
        with patch.object(Path, 'rename', fail_stage):
            with self.assertRaises(OSError): self.run_install({'SKILL.md': b'new'})
        self.assertTrue(identical(self.dest/'example', self.files))
    def test_symlink_rejected_without_touching_target(self):
        real = self.base/'real'; real.mkdir()
        self.dest.parent.mkdir(parents=True)
        self.dest.symlink_to(real, target_is_directory=True)
        with self.assertRaises(ValueError): self.run_install()
        self.assertEqual(list(real.iterdir()), [])
    def test_unknown_skill_leaves_destination_absent(self):
        result = subprocess.run([sys.executable, str(ROOT/'scripts/install.py'), '--dest', str(self.dest), '--skill', '../wrong'], capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.dest.exists())
    def test_portable_packages_contain_guides_and_assets(self):
        for skill in skills():
            files = portable_files(skill)
            self.assertIn('references/toolkit/guides/agents.md', files)
            self.assertNotIn(b'../../guides/', files['SKILL.md'])
        grading = portable_files(ROOT/'skills/grading-assistant')
        self.assertIn('grading-template.xlsx', grading)
    def test_project_scope_cli(self):
        result = subprocess.run([sys.executable, str(ROOT/'scripts/install.py'), '--agent', 'copilot', '--project', str(self.base/'project'), '--skill', 'start-here'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.base/'project/.github/skills/start-here/SKILL.md').exists())

if __name__ == '__main__': unittest.main()
