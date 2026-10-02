# TempoEdit Demo Website Design

## Purpose

Create a public project page that Chih-Yao Chen can link in graduate-admission materials immediately, while keeping the page simple enough to update as the research develops.

## Audience and success criteria

The primary audience is an admissions reviewer who may open the link on a phone or desktop. The first release succeeds when:

- the project title, author, affiliation, research summary, and ongoing status are clearly visible;
- the page works over HTTPS at `https://gino001655.github.io/tempoedit-demo/`;
- the layout remains readable on mobile and desktop;
- future content can be added without introducing a framework or build system.

## Technical approach

Use a static GitHub Pages site with no runtime dependencies and no build step. The repository will contain:

- `index.html` for semantic page content;
- `style.css` for responsive presentation;
- `README.md` for local preview, editing, and deployment instructions;
- `.nojekyll` so GitHub Pages serves the static files directly.

GitHub Pages will publish the repository's `main` branch from its root directory. This keeps deployment transparent: pushing an update to `main` updates the public page.

## Initial page content

The page will use the short project name **TempoEdit** and the full research title **Training-Free Temporal Audio Editing Through Pretrained Text-to-Audio Models**. It will identify:

- Chih-Yao Chen as the author;
- the Department of Electrical Engineering, National Taiwan University as the affiliation;
- the work as an ongoing research project;
- the research problem and proposed direction in a short, non-quantitative summary.

The first release will not claim experimental results that are still placeholders in the report. It will also avoid unpublished technical details, downloadable artifacts, and contact information not supplied by the user.

## Visual direction

Use a restrained academic presentation: light background, dark text, one accent color, generous spacing, and a compact waveform-inspired decorative element made with CSS. Typography will use system fonts so the page has no external font dependency. Motion will be minimal and respect `prefers-reduced-motion`.

## Interaction and resilience

The first release is informational and requires no JavaScript. Semantic HTML and visible keyboard focus styles will support accessibility. If CSS fails to load, the document will remain readable in source order.

## Verification

Before deployment:

- validate that all expected files exist and contain no placeholder markers;
- serve the directory locally and request the page over HTTP;
- check the page at narrow and wide viewport sizes;
- confirm there are no missing local assets or browser console errors.

After deployment:

- confirm the public URL returns successfully over HTTPS;
- verify that the displayed title and canonical URL match the deployed repository;
- document the exact GitHub Pages setting if user interaction is required.

## Deferred scope

Later revisions may add architecture diagrams, audio comparisons, experimental results, a publication link, and source-code links. These are intentionally excluded from the first release so a credible public URL can be obtained quickly.
