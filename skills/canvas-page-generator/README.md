# Course Page Generator, in depth

This builds on the top-level README and the prompt in SKILL.md. Read those first. This is the full design system and the editor reality: why the styling has to be done a particular way, the component library you can reuse, and how it works across learning management systems. For pushing finished pages into a platform through its API, see the platform guides in `../../guides/`.

## The problem

The editor in most learning management systems makes a decent-looking page painful to build. You fight formatting, the styling gets stripped on paste, and a page that should take five minutes takes forty. So pages become walls of plain text and students skim past the thing you wanted them to read. This skill lets you write in plain text and get back a finished, styled, consistent page, so the time goes into clearer content instead of formatting.

## The one styling rule that makes pages survive

Most rich-content editors quietly strip class-based and external CSS on paste. The fix learned the hard way: put every style inline, on the element, and in stubborn editors force each declaration so the editor's own stylesheet cannot override it. That means a single outer container, every visual property written inline on each element, and no reliance on a stylesheet or class selectors. It is verbose, but it is the only thing that reliably renders the same after the editor has had its way with your HTML. A single scoped style block for one progressive-enhancement animation is the only safe exception, and the page must look right without it.

## What the editor will strip or mangle

Build around these from the start, because finding them after publishing wastes an afternoon:

- Script tags are removed entirely. Never rely on JavaScript.
- Style buttons as links, not real button elements, which pick up the editor's default styling.
- Avoid fixed and sticky positioning and viewport units (vw, vh). They misbehave inside an LMS frame. Use relative or absolute positioning and percentage widths.
- Do not use line-break tags for spacing. Use margin and padding on paragraphs; line-break tags get mangled.
- Pair any link that opens a new tab with a no-opener relationship attribute.
- Set list styles explicitly. The editor may reset list markers and types, including marker color on a dark background.
- Treat pseudo-elements, custom fonts, and animations as progressive enhancement. The page must be fully usable without them.

## The component library

Build pages from a small set of repeatable blocks so every page looks like it belongs to the same course:

- Header band: the page title at the top, with an optional subtitle and a metadata line (due date, points, module).
- Short-version box: a summary at the very top so a student gets the point in five seconds.
- Section block: the core unit. A small uppercase label badge, a heading in an accent color, a colored left border, body text. Cycle three accent colors across sections so the page has rhythm.
- Tip and warning callouts: a left border and a subtle tinted background, labeled in text (TIP, WARNING, COMMON MISTAKE) so meaning never rides on color alone.
- Table: a bordered container with a header row, horizontally scrollable so it survives narrow screens.
- Call-to-action button: a link styled as a pill button, at least a 44-pixel touch target.
- Image: responsive, bordered, with real alt text.
- Model-answer block and common-mistakes block: for assignment pages, to show the level of work expected and the pitfalls that cost points.
- Resource list: a labeled set of links in a section of its own.

### Accent cycling and accessibility

Cycle the three accents across section blocks (primary, secondary, highlight, then repeat). Give a few sections a fixed accent by meaning if you like (for example, the grading section always one color). On accessibility, the rules are not optional: semantic heading order (one page title, a heading per section), real alt text on images and a title on any embedded video, text labels rather than color alone, links visibly distinct with enough contrast, and touch targets large enough to tap.

## Choosing colors, and capturing your brand once

The base skill ships a neutral, accessible default palette rather than any institution's brand colors, on purpose: this toolkit is generic by design. Swap in your own three accents if you have them. Whatever you pick, check contrast against your background before you publish; if an accent makes text hard to read, change it.

Better than picking by hand is capturing your brand from a real source and storing it as a reusable design document. There are three sources, in descending order of officialness:

- The university brand or style guide. Most institutions publish their official palette and type. Pulling from there makes your pages look like they belong to the institution, which is its own small signal of legitimacy to students.
- The course's existing pages. If the course already has a look, pull the palette from a current page so new pages are consistent with what students already know.
- An inspiration source. Starting fresh, pull a palette from a site whose feel you like, then adapt it into your own. Do not lift another organization's identity wholesale; take the feel, not the logo.

The capture itself is a browser-surface job, because brand colors live on rendered web pages: point an AI browser extension or an agentic browser at the source and have it extract the palette (hex values and what each is used for), the fonts, and the sizing, then map them to a background, a body-text color, and three accents, checking contrast as it goes. The output goes into `brand-guidelines.md`, a template that ships with this skill, with fields for each color role, the type stack, the accent-cycling map, and a note on where the brand came from so it is traceable and refreshable.

From then on, the brand document is your style input. Feed it to the page prompt instead of typing colors, and every page matches without you thinking about it. If you run the prof-brain skill, store the brand note in the brain so the page generator, announcements, and anything else you build all draw from one source of truth. When the university refreshes its palette, you recapture once and every future page follows.

## The page types

- Assignment page: header with due date and points, an overview with the scenario and objectives, numbered step sections, a grading section, a submission section, and optionally a model-answer example and a common-mistakes block.
- Reading or info page: header, an overview of why the topic matters, content sections per concept, and a resources section. No submission, no numbered steps.
- Announcement page: short and scannable. Header, one to three tight paragraphs with any deadline in bold, one clear action link, optionally a few quick links. Under about 400 words of visible text.

## Across learning management systems

Any editor that accepts inline-styled HTML in a source view can render these pages: Canvas, Blackboard, Moodle, Brightspace, Schoology. The generation is identical everywhere; only the paste-or-push step differs. To paste, use your editor's raw-HTML or source view. To push automatically through an API (and to handle large pages without truncation), see `../../guides/canvas-lms.md` for Canvas, including the chunking technique for large page bodies, and `../../guides/other-lms.md` for the others.

## The guardrail

The AI builds the page. You read the content and publish it. It is a formatter, not an author. Preview in a browser and on a phone before students see it, and verify every link and due date, because a generated link is exactly the thing to confirm before it goes live.
