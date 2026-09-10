const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { test } = require('node:test');
const source = fs.readFileSync(path.join(__dirname, '../web/dist/app.js'), 'utf8');
// Exercise the actual rendering helpers without a browser or an extra dependency.
const helpers = source.slice(source.indexOf('  const escape ='), source.indexOf('  function notify('));
const { markdown, safeURL } = vm.runInNewContext(`(() => { ${helpers}\nreturn { markdown, safeURL }; })()`, {
  URL, location: { hash: '' }, data: { skills: [{ id: 'announcement-writer' }] }
});
test('HTML and event handlers remain literal text', () => {
  const result = markdown('<img src=x onerror=alert(1)>\n<svg onload=alert(1)>');
  assert.ok(result.includes('&lt;img'));
  assert.doesNotMatch(result, /<(?:img|svg|script)\b/i);
});
test('active URL schemes are rejected', () => {
  for (const url of ['javascript:alert(1)', 'data:text/html,<script>', 'vbscript:msgbox(1)', 'file:///tmp/private', 'java\nscript:alert(1)']) {
    assert.equal(safeURL(url), '#');
  }
});
test('links are encoded and cannot gain HTML attributes', () => {
  const result = markdown('[source](https://example.invalid/" onmouseover="alert)');
  assert.doesNotMatch(result, /"\s+onmouseover=/i);
  assert.ok(result.includes('rel="noopener noreferrer"'));
});
test('fenced code cannot create elements', () => {
  const result = markdown('```html\n</pre><script>alert(1)</script>\n```');
  assert.ok(result.includes('&lt;/pre&gt;'));
  assert.doesNotMatch(result, /<script/i);
});
test('normal links keep their destination and relative base', () => {
  assert.equal(safeURL('README.md', 'skills/quiz-builder/SKILL.md'), 'https://github.com/TaylorONeal/ai-education/blob/main/skills/quiz-builder/README.md');
  assert.ok(markdown('[Docs](https://example.invalid/docs)').includes('href="https://example.invalid/docs"'));
});
