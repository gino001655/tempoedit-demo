# TempoEdit

Project page for **TempoEdit: Training-Free Temporal Audio Editing Through Pretrained Text-to-Audio Models**.

Public site: <https://gino001655.github.io/tempoedit-demo/>

## Preview locally

From the repository root, run:

```bash
python3 -m http.server 8000
```

Then open <http://localhost:8000/>. Stop the server with `Ctrl+C`.

## Update the page

- Edit project text and page structure in `index.html`.
- Edit colors, spacing, and responsive layout in `style.css`.
- Run `python3 -m unittest tests/test_site.py -v` before committing.
- Push the verified commit to `main`; GitHub Pages will publish the update.

The first release intentionally avoids unverified experimental claims. Add results and audio comparisons only after they are ready for public review.

## Enable GitHub Pages

In the GitHub repository, open **Settings → Pages**. Under **Build and deployment**, select **Deploy from a branch**, choose `main` and `/(root)`, then save. The site will be available at the public URL above after the first deployment finishes.
