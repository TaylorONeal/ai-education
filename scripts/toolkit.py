"""Shared, deterministic packaging helpers. No network or third-party dependencies."""
from pathlib import Path
import hashlib
import re
import zipfile

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = 'https://github.com/TaylorONeal/ai-education/blob/main/'

# Distribution is public content. Reject credentials and links rather than copying
# their targets into a downloadable artifact. This is not a general PII detector.
IGNORED_PARTS = {'.git', '.DS_Store', '__pycache__', '.pytest_cache', 'node_modules', '.venv'}
SENSITIVE_NAMES = {'credentials.json', 'service-account.json', 'id_rsa', 'id_ed25519', '.npmrc', '.pypirc', '.netrc', '.ssh', '.aws'}
SENSITIVE_SUFFIXES = {'.pem', '.key', '.p12', '.pfx', '.jks'}

def validate_public_source(source):
    source = source.absolute()
    try:
        relative = source.relative_to(ROOT)
    except ValueError:
        raise ValueError('Distribution source is outside the toolkit') from None
    if '..' in relative.parts:
        raise ValueError('Distribution source contains parent traversal')
    current = ROOT
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError('Refusing linked distribution source: ' + str(relative))
        lowered = part.lower()
        if lowered.startswith('.env') or lowered in SENSITIVE_NAMES or Path(part).suffix.lower() in SENSITIVE_SUFFIXES:
            raise ValueError('Refusing credential-like distribution source: ' + str(relative))
    return source

def public_files(folder):
    validate_public_source(folder)
    for source in sorted(folder.rglob('*')):
        if any(part in IGNORED_PARTS for part in source.relative_to(folder).parts) or source.suffix == '.pyc':
            continue
        validate_public_source(source)
        if source.is_file():
            yield source

def read_public_file(source):
    return validate_public_source(source).read_bytes()

def skills():
    return sorted(p.parent for p in (ROOT / 'skills').glob('*/SKILL.md') if not p.parent.name.startswith('_'))

def sections(text):
    result = []
    for part in re.split(r'^## ', text, flags=re.M)[1:]:
        heading, _, body = part.partition('\n')
        result.append((heading.strip(), body.strip()))
    return result

def prompt_blocks(text):
    result = []
    for heading, body in sections(text):
        for match in re.finditer(r'(?:^>[^\n]*(?:\n|$))+', body, flags=re.M):
            prompt = '\n'.join(re.sub(r'^> ?', '', line) for line in match.group().rstrip().splitlines()).strip()
            if prompt:
                result.append({'heading': heading, 'text': prompt})
    return result

def portable_files(skill):
    """Resolve shared guide references without installing guides as separate skills."""
    files = {}
    for source in public_files(skill):
        relative = source.relative_to(skill)
        data = read_public_file(source)
        if source.suffix == '.md':
            text = data.decode('utf-8')
            # References in this toolkit's skill entrypoints and READMEs are root-relative.
            text = text.replace('../../guides/', 'references/toolkit/guides/')
            text = text.replace('../../PRINCIPLES.md', 'references/toolkit/PRINCIPLES.md')
            text = text.replace('../../INSTALL.md', REPO_URL + 'INSTALL.md')
            text = text.replace('../../AGENTS.md', REPO_URL + 'AGENTS.md')
            text = re.sub(r'\.\./([a-z][a-z-]+)/SKILL\.md', lambda m: REPO_URL + 'skills/' + m[1] + '/SKILL.md', text)
            data = text.encode()
        files[relative.as_posix()] = data
    for source in sorted((ROOT / 'guides').glob('*.md')):
        files['references/toolkit/guides/' + source.name] = read_public_file(source)
    files['references/toolkit/PRINCIPLES.md'] = read_public_file(ROOT / 'PRINCIPLES.md')
    return files

def archive_bytes(destination, entries):
    """Stable bytes make update detection meaningful and eliminate stale ZIP members."""
    with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(entries.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)

def digest(data):
    return hashlib.sha256(data).hexdigest()
