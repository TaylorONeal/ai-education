# Visual teaching guide

A static, offline-friendly interface for choosing a task, copying canonical prompts, downloading complete skills, and preparing installation or agent handoff instructions. It does not call a model or collect course/student data.

## Open it

Open `dist/index.html` directly in a browser. No server or dependencies are required. Clipboard permissions vary; when automatic copying is unavailable, the interface selects the text for manual copying.

For a local HTTP preview, run from the repository root:

```sh
python3 scripts/build-toolkit.py
python3 -m http.server 4173 --bind 127.0.0.1 --directory web/dist
```

Open `http://127.0.0.1:4173`. Stop the server with Ctrl+C when finished.

## Edit and regenerate

- `dist/index.html`: accessible page structure and controls.
- `dist/styles.css`: responsive layout and visual style.
- `dist/app.js`: task selection, copy fallbacks, install commands, and document reader.
- `dist/catalog.js` and `dist/downloads/`: generated from skills and docs. Do not edit by hand.
- `../scripts/build-toolkit.py`: shared generation step.

Run `python3 scripts/check-toolkit.py` and `python3 -m unittest discover -s tests` after building. Syntax-check JavaScript with `node --check web/dist/app.js`. For browser testing when requested, verify task switching, prompt steps, copies and manual fallback, all agent/scope combinations, downloads, keyboard navigation, modal focus, phone layout, and enlarged text.

## Host it

Publish only the contents of `dist/` on a static host. Use the Sites manifest for Sites hosting. The directory contains only public toolkit instructions and generated packages. Do not add course records, credentials, or restricted answer keys. A private preview does not make the site public for other teachers; change its audience only through an authorized hosting action.

The page has no external fonts or script dependencies. Links to product documentation and the source repository require internet access.
