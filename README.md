# Nevolra — Public Website

**Live website:** https://activemvp.github.io/nevolra-public-site/

This is the public, share-safe Nevolra development overview. The website is static, without a visitor editing interface, analytics service, or external scripts. It contains no private Nevolra architecture or development source.

## How to publish an update (owner only)

1. Open [data/updates.json](data/updates.json) on GitHub and choose the pencil (Edit).
2. Add a public-safe progress item with a unique lowercase `id`, a `YYYY-MM-DD` date, a `title`, a factual `body`, and one of these statuses: `Verified engineering`, `Research prototype`, `In development`, `Planned`.
3. Select **Commit changes** to `main` after reviewing the exact wording. The website builds and publishes automatically from [the GitHub Actions workflow](.github/workflows/pages.yml).
4. For changes to the main story, edit [index.html](index.html) instead.

Example (not an actual achievement; do not publish it as fact):
```json
{
  "entries": [
    {
      "id": "2026-11-20-example",
      "date": "2026-11-20",
      "title": "Example progress update",
      "body": "Replace this with an independently supported update.",
      "status": "In development"
    }
  ]
}
```
Keep existing entries when adding new ones. **Never publish unreleased controls, exact private paths, access credentials, unpublished source code or personal chat history.** A public repository exposes its entire commit history, including deleted material.

## Visitor update behavior

The website checks `version.json` approximately every 60 seconds when the browser tab is visible and again when focus returns. Following a successful deployment, it reloads automatically, attempts to restore the reader's original section and vertical offset, and shows a dismissible "Nevolra has been updated" notice. Scroll restoration is best-effort when content is removed or substantially rearranged. A CDN or network connection may delay updates; automatic reloads do not occur while offline.

## Permissions and public access

Only `ActiveMVP` and accounts or GitHub Apps explicitly granted repository **write** access can publish. General visitors may read, share or propose changes by pull request but cannot publish them. Review [repository access settings](https://github.com/ActiveMVP/nevolra-public-site/settings/access) before granting collaborators. The website and its public repository are readable by anyone; `noindex` is not a security measure.

## Maintenance

- Deployment workflow: `.github/workflows/pages.yml`
- Source page: `index.html`
- Progress updates: `data/updates.json`
- Build and schema checks: `scripts/build_site.py`
- Live status: [GitHub Actions](https://github.com/ActiveMVP/nevolra-public-site/actions)

The November 2026 raw Ollama benchmarks do not establish full Nevolra system performance. RAC/Genesis experiments remain research with scientific qualification gaps. Support contributions are voluntary, not equity or a guarantee of a financial return.
