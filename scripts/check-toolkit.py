#!/usr/bin/env python3
"""Repository gates. Pattern scans flag risks; they do not certify absence of PII."""
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
from toolkit import ROOT, skills, sections, prompt_blocks, portable_files

errors = []
def check(condition, message):
    if not condition:
        errors.append(message)

catalog_file = ROOT / 'web/dist/catalog.js'
try:
    catalog = json.loads(catalog_file.read_text().split('window.TOOLKIT = ', 1)[1].rstrip().removesuffix(';'))
except (OSError, ValueError, IndexError) as error:
    print('Build the toolkit first:', error); sys.exit(1)
entries = {s['id']: s for s in catalog['skills']}
for skill in skills():
    text = (skill / 'SKILL.md').read_text()
    check(bool(re.search(r'^name: ' + re.escape(skill.name) + '$', text, re.M)), str(skill) + ': invalid name')
    check(bool(re.search(r'^description: .+', text, re.M)), str(skill) + ': missing description')
    try:
        description = json.loads(re.search(r'^description: (.+)$', text, re.M)[1])
        check(isinstance(description, str) and bool(description.strip()), skill.name + ': empty description')
    except (ValueError, TypeError):
        errors.append(skill.name + ': description must be a double-quoted JSON-compatible YAML string')
    headings = [heading.lower() for heading, _ in sections(text)]
    required = ['the guardrail', 'automated version', 'automate even better']
    if skill.name != 'start-here': required += ['the problem', 'what you need']
    for heading in required:
        check(heading in headings, skill.name + ': missing section ' + heading)
    check(any(h.startswith('what to check') for h in headings), skill.name + ': missing checks')
    check(entries.get(skill.name, {}).get('markdown') == text, skill.name + ': stale catalog')
    check(entries.get(skill.name, {}).get('prompts') == prompt_blocks(text), skill.name + ': prompt mismatch')
    archive = ROOT / 'web/dist/downloads' / (skill.name + '.zip')
    with zipfile.ZipFile(archive) as package:
        expected = {skill.name + '/' + key: value for key, value in portable_files(skill).items()}
        check(set(package.namelist()) == set(expected), skill.name + ': package members mismatch')
        for name, data in expected.items():
            check(package.read(name) == data, name + ': stale package content')
            if name.endswith('.md'):
                for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', data.decode()):
                    if re.match(r'\w+:|#', target): continue
                    import posixpath
                    path = posixpath.normpath(posixpath.join(posixpath.dirname(name), target.split('#')[0]))
                    check(path in expected, name + ': broken portable link ' + target)

text_files = list((ROOT/'skills').rglob('*.md')) + list((ROOT/'guides').glob('*.md')) + list((ROOT/'docs').glob('*.md')) + [ROOT/n for n in ['README.md','INSTALL.md','GETTING-STARTED.md','FAQ.md','GLOSSARY.md','LinkedIn-Article.md','CONTRIBUTING.md','PRINCIPLES.md']]
for path in text_files:
    text = path.read_text()
    check('—' not in text, str(path.relative_to(ROOT)) + ': em dash')
    for line in text.splitlines():
        banned = re.search(r'\b(pivotal|crucial|leverage|foster|delve|robust|seamless)\b', line, re.I)
        if banned and not ('cut inflated words' in line.lower()):
            errors.append(str(path.relative_to(ROOT)) + ': banned word ' + banned[0])
    check(not re.search(r'/Users/|/home/[a-zA-Z]|[A-Z]:\\Users\\|[\w.+-]+@[\w.-]+\.[a-z]{2,}', text), str(path.relative_to(ROOT)) + ': possible personal path or email')
    # Markdown placeholders are intentional; only literal local destinations are checked.
    for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', text):
        if re.match(r'\w+:|#', target) or '[' in target or '<' in target: continue
        dest = (path.parent / target.split('#')[0]).resolve()
        check(dest.exists(), str(path.relative_to(ROOT)) + ': broken link ' + target)

cookbook = ROOT / 'cookbook/AI-Teaching-Cookbook.docx'
with zipfile.ZipFile(cookbook) as archive:
    xml = ET.fromstring(archive.read('word/document.xml'))
    ns = {'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    paragraphs = [''.join(p.itertext()) for p in xml.findall('.//w:p', ns)]
    # Use actual text nodes; properties and layout do not count as prompt text.
    paragraphs = [''.join(t.text or '' for t in p.findall('.//w:t', ns)).strip() for p in xml.findall('.//w:p', ns)]
    for skill in skills():
        if skill.name in ['start-here', 'canvas-lms', 'prof-brain']: continue
        for prompt in prompt_blocks((skill/'SKILL.md').read_text()):
            wanted = [line.strip() for line in prompt['text'].splitlines()]
            check(any(paragraphs[i:i+len(wanted)] == wanted for i in range(len(paragraphs))), skill.name + ': cookbook prompt mismatch in ' + prompt['heading'])
    book_text = '\n'.join(paragraphs)
    check('—' not in book_text, 'Cookbook: em dash')
    check(not re.search(r'/Users/|/home/[a-zA-Z]|[\w.+-]+@[\w.-]+\.[a-z]{2,}', book_text), 'Cookbook: possible PII')

html = (ROOT/'web/dist/index.html').read_text()
for target in re.findall(r'(?:src|href)="([^"]+)"', html):
    if re.match(r'\w+:|#', target): continue
    check((ROOT/'web/dist'/target).exists(), 'Website: missing asset ' + target)
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('PASS: 12 skill structures, voice/PII patterns, local links, portable packages, catalog prompts, cookbook prompts, and site assets.')
