#!/usr/bin/env node
/*
 * build-cookbook.js
 *
 * Generates AI-Teaching-Cookbook.docx FROM the seven skill files in ../skills.
 * The skills are the single source of truth. This script never invents content;
 * it extracts each skill's problem statement, its prompt blocks (verbatim),
 * what-to-check list, and guardrail, and lays them out for a non-technical reader.
 *
 * If a prompt changes, change it in the skill, then re-run this script.
 * Do not hand-edit the .docx.
 *
 * Usage:
 *   npm install docx
 *   node build-cookbook.js
 */

const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, BorderStyle,
} = require('docx');

const SKILLS_DIR = path.join(__dirname, '..', 'skills');
const OUT = path.join(__dirname, 'AI-Teaching-Cookbook.docx');

// Render order matches the toolkit's documented order.
// The teaching and authoring skills go in the cookbook. The operational
// skills (canvas-lms, prof-brain) are not copy-paste prompts and are excluded.
const ORDER = [
  'participation-scoring',
  'grading-assistant',
  'ai-output-checker',
  'class-content-analysis',
  'exam-rebalance',
  'exam-predictor',
  'announcement-writer',
  'canvas-page-generator',
  'quiz-builder',
];

function readSkill(name) {
  const p = path.join(SKILLS_DIR, name, 'SKILL.md');
  const raw = fs.readFileSync(p, 'utf8');
  return raw.replace(/^---[\s\S]*?\n---\n/, ''); // strip YAML frontmatter
}

function getTitle(body) {
  const m = body.match(/^#\s+(.+)$/m);
  return m ? m[1].trim() : 'Skill';
}

// Split a skill body into [{heading, lines[]}] by level-2 headings.
function sections(body) {
  const lines = body.split('\n');
  const out = [];
  let cur = null;
  for (const line of lines) {
    const h = line.match(/^##\s+(.+)$/);
    if (h) {
      if (cur) out.push(cur);
      cur = { heading: h[1].trim(), lines: [] };
    } else if (cur) {
      cur.lines.push(line);
    }
  }
  if (cur) out.push(cur);
  return out;
}

function hasBlockquote(sec) {
  return sec.lines.some((l) => l.trimStart().startsWith('>'));
}

// Decide which sections land in the cookbook: the problem, every section that
// carries a prompt, the what-to-check list, and the guardrail.
function includeSection(sec) {
  const h = sec.heading.toLowerCase();
  if (h === 'the problem') return true;
  if (h.startsWith('what to check')) return true;
  if (h === 'the guardrail') return true;
  if (hasBlockquote(sec)) return true;
  return false;
}

// Convert a section's lines into ordered render blocks.
// A block is either {type:'text', text} or {type:'prompt', text} or {type:'bullet', text}.
function blocks(sec) {
  const out = [];
  let quote = [];
  const flushQuote = () => {
    if (quote.length) {
      out.push({ type: 'prompt', text: quote.join('\n').replace(/\n{3,}/g, '\n\n').trim() });
      quote = [];
    }
  };
  for (const raw of sec.lines) {
    const line = raw.replace(/\s+$/, '');
    if (line.trimStart().startsWith('>')) {
      quote.push(line.replace(/^\s*>\s?/, ''));
      continue;
    }
    flushQuote();
    if (!line.trim()) continue;
    const b = line.match(/^\s*[-*]\s+(.+)$/);
    const n = line.match(/^\s*\d+\.\s+(.+)$/);
    if (b) out.push({ type: 'bullet', text: clean(b[1]) });
    else if (n) out.push({ type: 'bullet', text: clean(n[1]) });
    else out.push({ type: 'text', text: clean(line.trim()) });
  }
  flushQuote();
  return out;
}

// Strip inline markdown emphasis/backticks for clean prose; keep the words.
function clean(s) {
  return s
    .replace(/\*\*(.+?)\*\*/g, '$1')
    .replace(/\*(.+?)\*/g, '$1')
    .replace(/`(.+?)`/g, '$1');
}

const NAVY = '1F2D3D';
const ACCENT = '2563EB';
const PROMPT_BG = 'EEF2F7';

function promptParagraphs(text) {
  // Each line of the prompt becomes a monospace paragraph inside a shaded box.
  const rows = text.split('\n');
  return rows.map((r, i) =>
    new Paragraph({
      shading: { type: 'clear', fill: PROMPT_BG },
      spacing: { after: 0, before: 0, line: 264 },
      border: {
        left: { style: BorderStyle.SINGLE, size: 18, color: ACCENT, space: 6 },
      },
      children: [new TextRun({ text: r || ' ', font: 'Consolas', size: 19 })],
    })
  );
}

const children = [];

// Cover
children.push(
  new Paragraph({ spacing: { before: 1200, after: 120 }, alignment: AlignmentType.CENTER,
    children: [new TextRun({ text: 'The AI Teaching Cookbook', bold: true, size: 56, color: NAVY })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 80 },
    children: [new TextRun({ text: 'Copy-paste prompts for the parts of teaching that eat your week', italics: true, size: 26, color: '555555' })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 600 },
    children: [new TextRun({ text: 'github.com/TaylorONeal/ai-education', size: 20, color: ACCENT })] }),
  new Paragraph({ spacing: { before: 200, after: 120 },
    children: [new TextRun({ text: 'The one rule', bold: true, size: 28, color: ACCENT })] }),
  new Paragraph({ spacing: { after: 120 },
    children: [new TextRun({ text: 'AI does the draft. You make the call. Nothing reaches a student without a human reading it first.', size: 24 })] }),
  new Paragraph({ spacing: { after: 120 },
    children: [new TextRun({ text: 'How to use this cookbook: find your task, copy the prompt in the shaded box, replace the [BRACKETED] placeholders with your real details, and paste it into Claude, ChatGPT, or any AI tool. Then read what comes back before you use it. Every recipe tells you exactly what to check.', size: 22 })] }),
  new Paragraph({ spacing: { after: 120 },
    children: [new TextRun({ text: 'These prompts are generated from the skill files in the open-source repo. If a prompt here ever differs from the repo, the repo is right.', italics: true, size: 20, color: '555555' })] }),
  new Paragraph({ pageBreakBefore: true, children: [] }),
);

ORDER.forEach((name, idx) => {
  const body = readSkill(name);
  const title = getTitle(body);

  if (idx > 0) children.push(new Paragraph({ pageBreakBefore: true, children: [] }));

  children.push(new Paragraph({
    spacing: { after: 160 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: ACCENT, space: 4 } },
    children: [new TextRun({ text: title, bold: true, size: 36, color: NAVY })],
  }));

  for (const sec of sections(body)) {
    if (!includeSection(sec)) continue;
    children.push(new Paragraph({
      spacing: { before: 200, after: 80 },
      children: [new TextRun({ text: sec.heading, bold: true, size: 26, color: ACCENT })],
    }));
    for (const blk of blocks(sec)) {
      if (blk.type === 'prompt') {
        children.push(new Paragraph({ spacing: { before: 60 }, children: [] }));
        promptParagraphs(blk.text).forEach((p) => children.push(p));
        children.push(new Paragraph({ spacing: { after: 60 }, children: [] }));
      } else if (blk.type === 'bullet') {
        children.push(new Paragraph({ bullet: { level: 0 }, spacing: { after: 40 },
          children: [new TextRun({ text: blk.text, size: 22 })] }));
      } else {
        children.push(new Paragraph({ spacing: { after: 80 },
          children: [new TextRun({ text: blk.text, size: 22 })] }));
      }
    }
  }
});

const finalDoc = new Document({
  styles: { default: { document: { run: { font: 'Calibri', size: 22 } } } },
  sections: [{ properties: {}, children }],
});

Packer.toBuffer(finalDoc).then((buf) => {
  fs.writeFileSync(OUT, buf);
  const pages = Math.max(1, Math.round(children.length / 22));
  console.log('Wrote ' + OUT + ' (' + children.length + ' paragraphs, ~' + pages + ' pages est.)');
});
