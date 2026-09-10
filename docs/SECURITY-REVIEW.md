# Security review

Reviewed 2026-09-10. Scope: static website, Markdown rendering, local installer, generated downloads, and cookbook dependencies. No critical or high findings identified in this review.

## SEC-01: medium, fixed: private files could enter downloads

The distribution helper previously followed file symlinks and included arbitrary files inside skill folders. A synthetic fixture confirmed that an `.env` file and a symlink to a file outside the toolkit were both packaged. A maintainer could accidentally distribute local credentials. This was a build-time disclosure risk, not a demonstrated remote compromise.

[Source validation](../scripts/toolkit.py#L16) now rejects symlinks, parent traversal, sources outside the repository, and common credential filenames and extensions. Shared references use the same validation. [The builder](../scripts/build-toolkit.py) includes only named generated downloads in the source bundle. Seven Python regression tests cover these boundaries.

## SEC-02: low, hardened: browser content restrictions

The page now sets a restrictive [Content Security Policy](../web/dist/index.html#L6) and no-referrer policy. Scripts and styles must come from the same origin; object loads, forms, and network connections are denied. The existing Markdown renderer escapes HTML and rejects active URL schemes. Five Node regression tests exercise literal HTML, event handlers, malicious links, attribute injection, fenced code, and normal links.

This is defense in depth. No exploitable script injection was found. Hosting response headers and browser enforcement were not independently penetration-tested. A meta policy cannot enforce framing restrictions; those require a hosting response header. See [MDN CSP guidance](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP).

## Validation and limits

- Fifteen Python tests and five JavaScript tests pass.
- `npm audit --prefix cookbook --omit=dev` reports zero known dependency vulnerabilities.
- Distribution checks compare generated package contents against their canonical sources and verify local links and prompt text.
- The site has no model API calls, credential input, uploads, student-data storage, or third-party JavaScript.
- Skill instructions treat retrieved content as evidence and retain human review for student-facing actions. The two incoming syllabus and schedule skills receive the same agent guidance.

Filename checks cannot detect every secret or student record in ordinary documents. Review source material before distribution. The builder assumes a trusted local checkout, not a hostile process changing files during the build. Python path handling is documented in [pathlib](https://docs.python.org/3/library/pathlib.html). This review does not certify connected accounts, LMS configurations, or future dependencies.
