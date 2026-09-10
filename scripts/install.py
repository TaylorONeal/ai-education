#!/usr/bin/env python3
"""Install complete skills with dry-run support and recoverable folder replacement."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil
import sys
import tempfile
import uuid
from toolkit import ROOT, skills, portable_files

TARGETS = {
    'agents': ('.agents/skills', '.agents/skills'),
    'codex': ('.agents/skills', '.agents/skills'),
    'claude': ('.claude/skills', '.claude/skills'),
    'gemini': ('.gemini/skills', '.gemini/skills'),
    'copilot': ('.copilot/skills', '.github/skills'),
    'cursor': ('.cursor/skills', '.cursor/skills'),
}

def identical(folder, files):
    if not folder.is_dir() or folder.is_symlink():
        return False
    actual = {p.relative_to(folder).as_posix(): p for p in folder.rglob('*') if p.is_file()}
    return actual.keys() == files.keys() and all(not p.is_symlink() and p.read_bytes() == files[k] for k, p in actual.items())

def install(folder, name, files, dry_run=False):
    target = folder / name
    if any(p.is_symlink() for p in [folder, target]):
        raise ValueError('Refusing a symlink destination: ' + str(target))
    if target.exists() and not target.is_dir():
        raise ValueError('Destination is not a skill folder: ' + str(target))
    if identical(target, files):
        print('Unchanged: ' + str(target))
        return
    action = 'Update with backup' if target.exists() else 'Install'
    print(('Would ' if dry_run else '') + action + ': ' + str(target))
    if dry_run:
        return
    folder.mkdir(parents=True, exist_ok=True)
    # Stage outside discovery so incomplete SKILL.md files cannot be discovered.
    with tempfile.TemporaryDirectory(prefix='toolkit-stage-', dir=folder.parent) as temp:
        stage = Path(temp) / name
        for relative, data in files.items():
            out = stage / relative
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(data)
        backup = None
        if target.exists():
            stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8]
            backup = folder.parent / (folder.name + '-toolkit-backups') / stamp / name
            backup.parent.mkdir(parents=True, exist_ok=True)
            target.rename(backup)
            print('Backup: ' + str(backup))
        try:
            stage.rename(target)
        except OSError:
            if backup and not target.exists():
                backup.rename(target)
            raise

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agent', choices=TARGETS, default='claude')
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument('--project', type=Path, help='Project root for project-scoped discovery')
    scope.add_argument('--dest', type=Path, help='Custom skills directory')
    parser.add_argument('--skill', action='append', help='Select one skill; repeat to select several')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--list', action='store_true')
    args = parser.parse_args()
    available = {p.name: p for p in skills()}
    if args.list:
        print('\n'.join(available))
        return
    selected = list(dict.fromkeys(args.skill or available))
    unknown = set(selected) - available.keys()
    if unknown:
        parser.error('Unknown skill: ' + ', '.join(sorted(unknown)))
    personal, project = TARGETS[args.agent]
    folder = args.dest or (args.project / project if args.project else Path.home() / personal)
    folder = folder.expanduser().absolute()
    source_root = (ROOT / 'skills').resolve()
    if folder.resolve() == source_root or source_root in folder.resolve().parents:
        parser.error('The install destination must not overlap the canonical skills source.')
    # Prepare and validate the entire selection before any mutation.
    plans = [(name, portable_files(available[name])) for name in selected]
    for name, _ in plans:
        target = folder / name
        if any(p.is_symlink() for p in [folder, target]):
            parser.error('Refusing a symlink destination: ' + str(target))
        if target.exists() and not target.is_dir():
            parser.error('Destination is not a folder: ' + str(target))
    for name, files in plans:
        install(folder, name, files, args.dry_run)
    print('Preview complete; no files changed.' if args.dry_run else 'Done. Refresh your agent and verify the installed SKILL.md files.')

if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError) as error:
        print('Installation failed: ' + str(error), file=sys.stderr)
        sys.exit(1)
