# TempoEdit Demo Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and publish a credible, responsive one-page research-project website for graduate-admission materials.

**Architecture:** A static `index.html` contains all semantic content and loads one local stylesheet. A standard-library Python test validates page structure and deployment-sensitive metadata; GitHub Pages serves the `main` branch root without a build step.

**Tech Stack:** HTML5, CSS3, Python 3 standard-library tests, GitHub Pages

**Spec:** `docs/superpowers/specs/2026-10-02-tempoedit-demo-design.md`

## Global Constraints

- Use no runtime dependencies, package manager, JavaScript, database, or build step.
- Publish from the repository's `main` branch root at `https://gino001655.github.io/tempoedit-demo/`.
- Identify Chih-Yao Chen, the Department of Electrical Engineering at National Taiwan University, and the project as ongoing work.
- Do not claim unpublished experimental results or expose contact details that the user did not provide.
- Keep the page readable on mobile and desktop, with reduced-motion and visible-focus support.

## Review Focus

- A narrow 320 px viewport must not overflow horizontally; covered by the responsive-layout assertions in Task 2.
- Missing CSS must still leave meaningful content order; covered by semantic-section assertions in Task 1.
- Link previews must show the correct title and summary; covered by metadata assertions in Task 1.
- GitHub project-path hosting must not use root-relative local assets; covered by the stylesheet-path assertion in Task 1.
- Unfinished placeholder language must never reach the public page; covered by the placeholder scan in Task 1.

---

### Task 1: Semantic research-project page

**Files:**
- Create: `tests/test_site.py`
- Create: `index.html`

**Interfaces:**
- Consumes: Title, author, affiliation, summary, status, and public URL from the approved spec.
- Produces: Semantic elements with IDs `overview`, `approach`, and `status`, plus a relative `style.css` stylesheet reference used by Task 2.

- [ ] **Step 1: Write the failing structure and metadata tests**

Create `tests/test_site.py` with `unittest` cases that parse `index.html` using `html.parser` and assert the exact title, description, canonical URL, author, affiliation, required section IDs, relative stylesheet path, one `h1`, and absence of `TBD`, `TODO`, `PLACEHOLDER`, and template result claims.

- [ ] **Step 2: Run the tests and verify they fail**

Run: `python3 -m unittest tests/test_site.py -v`

Expected: FAIL because `index.html` does not exist.

- [ ] **Step 3: Implement the semantic page**

Create `index.html` with accessible landmarks, project identity, concise research motivation, three temporal operations (relocate, extend, shorten), the training-free approach, honest ongoing-work status, canonical and social-preview metadata, and a footer with the current year.

- [ ] **Step 4: Run the focused tests**

Run: `python3 -m unittest tests/test_site.py -v`

Expected: all Task 1 tests PASS.

- [ ] **Step 5: Commit the semantic page**

Run: `git add index.html tests/test_site.py && git commit -m "feat: add TempoEdit project page"`

### Task 2: Responsive presentation and maintenance guide

**Files:**
- Modify: `tests/test_site.py`
- Create: `style.css`
- Create: `.nojekyll`
- Create: `README.md`

**Interfaces:**
- Consumes: Classes and section IDs in Task 1's `index.html`.
- Produces: A dependency-free responsive layout and exact local-preview and GitHub Pages instructions.

- [ ] **Step 1: Add failing deployment and responsive-style tests**

Extend `tests/test_site.py` to assert that `style.css`, `.nojekyll`, and `README.md` exist; the CSS defines a narrow-screen media query, overflow-safe sizing, `:focus-visible`, `prefers-reduced-motion`, and system fonts; and the README contains the preview command and public URL.

- [ ] **Step 2: Run the tests and verify they fail**

Run: `python3 -m unittest tests/test_site.py -v`

Expected: FAIL because the stylesheet, Pages marker, and README do not exist.

- [ ] **Step 3: Implement the visual system and documentation**

Create `style.css` with an academic navy-and-cyan palette, responsive grid, CSS waveform motif, cards for the three operations, accessible contrast, overflow protection, focus treatment, and reduced-motion behavior. Add an empty `.nojekyll` and a concise `README.md` covering `python3 -m http.server 8000`, content editing, and Pages configuration.

- [ ] **Step 4: Run automated and local-server verification**

Run: `python3 -m unittest tests/test_site.py -v`

Expected: all tests PASS.

Run the local server and request `/index.html`; expect HTTP 200 and no missing local resources.

- [ ] **Step 5: Inspect the rendered page**

Capture narrow and wide viewport screenshots. Verify no horizontal overflow, clipped text, missing styles, broken focus states, or console errors.

- [ ] **Step 6: Commit the finished static site**

Run: `git add .nojekyll README.md style.css tests/test_site.py && git commit -m "feat: style and document TempoEdit demo"`

### Task 3: Publish and validate GitHub Pages

**Files:**
- Modify only if the deployed project-path environment exposes a defect in the static files.

**Interfaces:**
- Consumes: Verified commits on local `main` and GitHub account `gino001655`.
- Produces: Repository `gino001655/tempoedit-demo` and public HTTPS URL `https://gino001655.github.io/tempoedit-demo/`.

- [ ] **Step 1: Verify GitHub authentication and repository availability**

Run read-only checks for authenticated GitHub CLI access and whether `gino001655/tempoedit-demo` already exists. Never overwrite an existing repository without explicit confirmation.

- [ ] **Step 2: Create and push the repository when the name is available**

Create a public repository from the current directory, add it as `origin`, and push `main`. If authentication is unavailable, provide the shortest browser-based repository creation and push steps for the user.

- [ ] **Step 3: Enable branch-based Pages publishing**

Set the Pages source to the `main` branch root through the GitHub API or direct the user to `Settings → Pages → Deploy from a branch → main → /(root)` if API authorization is unavailable.

- [ ] **Step 4: Verify the deployed URL**

Request `https://gino001655.github.io/tempoedit-demo/` until GitHub reports deployment completion. Expect HTTP 200, the exact TempoEdit title, HTTPS, and successful loading of `style.css`.

- [ ] **Step 5: Run final repository verification**

Run the full unittest suite, `git diff --check`, and `git status --short`; expect passing tests, no whitespace errors, and a clean working tree.

- [ ] **Step 6: Commit only if deployment validation required a source fix**

If needed, commit the minimal verified fix and push `main`; otherwise no additional commit is necessary.
