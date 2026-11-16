# Nevolra public website — updateable version

This folder contains the same public Nevolra overview design, **plus a safe progress-update workflow**. It is a static website: no server, database, analytics, external code, or visitor sign-in required.

## Who can publish?

Only the GitHub repository owner and explicitly authorized accounts with **write permission** can change the site source or deploy through this workflow. A visitor cannot edit the website. GitHub may also allow authorized organization administrators and installed apps with write permissions; review **Settings → Collaborators and teams** and any GitHub Apps. The site itself has **no visitor editing form**. Do not give write access to strangers. Require approval for changes to `main` if you enable branch rules. Publication is public to anyone who has the URL; noindex is *not* access protection.

## Publish — once, using GitHub Pages

1. On GitHub, create a dedicated **public** repository (e.g., `nevolra-public-site`) under your own account. **Do not publish the private Nevolra source repositories.** Review this entire folder before uploading. A public repo exposes all published source files and commit history.
2. Upload **everything in this folder**, including the hidden `.github/workflows/pages.yml`, to that repository's `main` branch. For easiest first upload, extract the ZIP on a PC and use GitHub Desktop or Git. The ZIP is not itself a Pages deployment.
3. In **Settings → Pages → Build and deployment**, select **GitHub Actions** as the source. If prompted, enable Actions. The existing workflow builds the site and deploys after a push to `main`.
4. Find the permanent link under **Settings → Pages** or the successful deployment. Future pushes update **the same URL**.
5. Test from a phone and a separate browser session. Leave private files, authorization systems, live repositories, and personal information off the public site.

### Publish a new progress milestone (no HTML editing)

Open **`data/updates.json`** in the GitHub web editor. Add another entry inside `entries`, for example:

```json
{
  "entries": [
    {
      "id": "2026-11-20-tested-stream-chat",
      "date": "2026-11-20",
      "title": "Streaming companion demo",
      "body": "A controlled, opt-in demonstration tested respectful chat interaction. Replace this example with only results you actually verified.",
      "status": "In development"
    }
  ]
}
```

You can add multiple entries separated by commas. `id` must be unique and never change after publication. Supported `status` values are `Verified engineering`, `Research prototype`, `In development`, and `Planned`. **Delete the example until a matching achievement is real.** The initial `entries` list is intentionally empty because the original timeline is already embedded in `index.html`.

Commit the change to `main` (or have an authorized collaborator create a PR and approve it). GitHub Actions validates the data, builds the page, and deploys the new revision automatically. No need to download and re-upload the entire page.

### Update other text

Use GitHub's web editor on `index.html`. The design, benchmarks, links, and current content are in that HTML file. Changes to `index.html` also trigger the same deploy. Preserve the code at the bottom handling version checks and scroll restoration.

### What happens for existing visitors?

While the tab is visible, it checks a tiny `version.json` file every **60 seconds**, and again when the tab regains focus. When GitHub Pages serves a new build, it reloads the page, restores the reader's position relative to the same section or timeline card, and shows a dismissible **“Nevolra has been updated”** notice. The browser URL remains on the same site; a version query can appear temporarily for cache refresh. Scroll restoration is best-effort if the section someone was reading is deleted or completely rewritten. No unexpected reload occurs offline or if update checking fails. GitHub Pages/CDN and browser caching mean updates are usually prompt but not guaranteed to appear immediately after deploy.

### Local preview

- Double-click `index.html` in Chrome/Edge to see the embedded website and its original timeline. File-based preview does not load the separate JSON updates because browser security restrictions differ.
- To preview added JSON entries on a PC, run `python -m http.server 8000` from this folder, then open `http://localhost:8000`.
- To validate a deploy locally run `python scripts/build_site.py`, which writes a standalone `_site` output folder.

### Security and editorial policy

- Never paste private source code, credentials, internal paths, personal conversations, access control details, or unredacted test logs into this repository.
- Each public claim should distinguish **implemented**, **test-passed**, **installed**, **Owner-accepted**, and **still research**.
- The November 2026 Ollama inference numbers are not proof of Nevolra's full-system speed. RAC/Genesis are ongoing research with scientific qualification gaps; not claims of neural continual learning or general intelligence.
- Ko-fi contributions are voluntary sponsorship, not equity securities or guaranteed returns. Confirm support URLs before publishing.
- A public GitHub Pages website can be shared by anyone with the link. If truly restricted access becomes necessary, use a hosting provider with authentication rather than relying on noindex.