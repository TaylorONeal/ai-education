---
name: canvas-page-generator
description: Turn plain text into a clean, styled course page for Canvas or another LMS, so you write the content and skip the formatting grind in a clunky editor. Use for assignment pages, reading pages, and info pages.
---

# Course Page Generator

## The problem

The editor in most learning management systems makes a decent-looking page painful to build. You fight with formatting, the styling gets stripped when you paste, and a page that should take five minutes takes forty. So pages end up as walls of plain text, and students skim past the thing you wanted them to read.

This skill lets you write the page in plain text and get back a finished, styled, consistent page. The formatting time drops to near zero, so the time goes into writing clearer content instead.

## What you need

- The content of the page, in plain text or bullet points.
- Your three accent colors (or use the neutral default below). Pick one primary, one secondary, one highlight, with enough contrast to pass accessibility on your chosen background.

## Set your style once

Decide your look and reuse it. The version that survives a clunky LMS editor follows a few hard rules, learned the hard way:

- One outer container, everything inline. Output a single wrapper element and put every style inline. Many editors strip class-based and external CSS on paste, so class selectors and stylesheets will not survive. Inline styles do.
- Build from a small set of repeatable blocks, so every page looks like it belongs to the same course:
  - Header band: the page title, with an optional subtitle and a metadata line (due date, points, module).
  - Short-version box: a summary at the very top so a student gets the point in five seconds.
  - Section block: the core unit. A small uppercase label badge, a heading in an accent color, a colored left border, body text.
  - Tip and warning callouts: a left border and a subtle tinted background, labeled in text (TIP, WARNING, COMMON MISTAKE) so meaning never rides on color alone.
  - Table: a bordered container with a header row, horizontally scrollable so it survives narrow screens.
  - Call-to-action button: a link styled as a pill button, at least a 44-pixel touch target.
  - Image: responsive, bordered, with real alt text.
  - Model-answer block and common-mistakes block: for assignment pages, to show the level of work expected and the pitfalls that cost points.
  - Resource list: a labeled set of links in a section of its own.
- Pick three accent colors and cycle them across sections (primary, secondary, highlight, then repeat) so the page has rhythm. A neutral, accessible default that is not tied to any institution: a deep slate `#1f2d3d` background, near-white `#ffffff` body text, and three accents, primary `#2563eb`, secondary `#0f9d8f`, highlight `#f4b400`. Swap in your own brand colors if you have them. Never use gray for body text on a dark background.
- Readable body text at 16px, line height around 1.7, a web-safe font stack with a system fallback, generous padding. Accessibility is not optional: semantic heading order (one page title, a heading per section), real alt text on images and a title on any embedded video, links visibly distinct with enough contrast, and touch targets large enough to tap.

Save your filled-in colors. Every future page becomes: paste plain text, run the saved prompt, preview, publish.

## Capture your brand once (brand guidelines)

Instead of picking colors by hand, capture them from a real source and store them as a reusable brand document. Three sources, in order of how official they are:

- Your university brand or style guide. Most institutions publish their official palette and type. Pull the colors from there so your pages match the institution.
- Your course or existing pages. If your course already has a look, pull the palette from a current page so new pages are consistent with what students already see.
- An inspiration source. If you are starting fresh, pull a palette from a site whose feel you like, then make it your own. Do not copy another organization's identity wholesale.

To capture, point a browser surface (an AI browser extension or agentic browser) at the source and have it extract the palette and type:

> Open [URL]. Extract the brand: the main colors as hex values with what each is used for, the heading and body fonts, and any obvious type sizing. Map the colors to a background, a body-text color, and three accents (primary, secondary, highlight), checking that body text and accents have enough contrast on the background. Write it into the brand-guidelines template.

Save the result as `brand-guidelines.md` (a template ships with this skill). From then on, feed that document to the page prompt instead of typing colors, and every page matches your brand. If you use the prof-brain skill, store the brand note there so all your tools share one source of truth.

## Know what your editor strips

Most LMS rich-content editors quietly modify HTML. Build around it from the start:

- Script tags are stripped. Never rely on JavaScript.
- Use links styled as buttons, not real button elements, which pick up the editor's own styling.
- Avoid fixed and sticky positioning and viewport units (vw, vh). They behave unreliably inside an LMS frame. Percentage widths and relative or absolute positioning are safe.
- Do not use line-break tags for spacing. Use margin and padding on paragraphs.
- Pair any link that opens a new tab with a no-opener relationship attribute.
- Treat animations, pseudo-elements, and custom fonts as progressive enhancement. The page must look right without them.
- Give images real alt text and videos a title, set explicit list styles (the editor may reset them), and keep heading order semantic: one page title, a heading per section, subheadings under that.

## The prompt

> Turn the content below into a single self-contained HTML container for my [LMS, e.g. Canvas] course page. Use only inline styles so the editor does not strip them. Output only the HTML, nothing before or after it.
>
> Style:
> - One outer container with a [BACKGROUND COLOR] background and readable [BODY TEXT COLOR] body text, max width around 960px, generous padding.
> - A header band at the top with the page title.
> - A short summary box labeled "The short version" right under the header.
> - Each content section gets a small uppercase label badge, a heading in an accent color, and a colored left border. Cycle the three accents [PRIMARY], [SECONDARY], [HIGHLIGHT] across sections.
> - Readable body text, good contrast, accessible color choices. No external fonts or scripts. No fixed or sticky positioning. Links that open new tabs include rel="noopener". Images have alt text.
>
> Page type: [ASSIGNMENT | READING/INFO | ANNOUNCEMENT]
>
> Content:
> [PASTE YOUR PLAIN-TEXT CONTENT, WITH SECTION HEADINGS]

## Page types, so the structure fits the purpose

- Assignment page: header with due date and points, an overview with the scenario and objectives, numbered step sections, a grading section, a submission section, and optionally a model-answer example and a common-mistakes block.
- Reading or info page: header, an overview of why the topic matters, content sections for each concept, and a resources section. No submission, no numbered steps.
- Announcement: short and scannable. Header, one to three tight paragraphs with any deadline called out in bold, one clear action link, optionally a few quick links. Keep it under about 400 words of visible text.

## What to check before you publish

1. Preview it in the browser before students see it. Open the HTML or use your LMS preview. Confirm it renders, the colors are readable, and nothing is broken.
2. Check it on a phone. Many students read course pages on their phones. Confirm it does not overflow or shrink to unreadable.
3. Check contrast. If your accent color makes text hard to read, change it. Accessibility is not optional. Do not rely on color alone to carry meaning, use text labels (REQUIRED, OPTIONAL, TIP, DUE DATE).
4. Verify every link and value. Same rule as everywhere: confirm any link or due date, do not trust a generated one.

## The guardrail

The AI builds the page. You read the content and publish it. It is a formatter, not an author. The words students read are still yours.

## Automated version

Connected to your LMS, it can take your plain-text content, build the page in your saved style, and push it to the right page or assignment through the LMS API on your confirmation. It still shows you a preview first. Consistency across your pages is itself a small kindness to students, who learn where to look.

## Automate even better

Push a whole set of pages across the course in one agentic pass, or re-skin every existing page to a new style, rather than pasting them one at a time. The agent can walk the course, apply the template to each page, and report what changed for your review. See `../../guides/automation.md` for the pull, unify, store, analyze pattern.
