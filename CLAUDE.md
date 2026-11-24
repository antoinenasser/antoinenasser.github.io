# CLAUDE.md

Personal site of Antoine Nasser (antoinenasser.github.io), built on the al-folio v1.2 Jekyll starter.
README.md is the short public description of the repo (English, points to the al-folio template); keep it sober.
CHEATSHEET.md (in French, for the owner) says where each piece of content lives; keep it in sync when adding features.
Publications: no "in preparation" works on the site; a paper enters once submitted (badge `Submitted`, journal `Submitted to <journal>`; when its preprint goes online, add the DOI and switch to the preprint badge with a `tag` naming the journal), and prefer the published version (title, author order) over preprint versions.

- `baseurl` is empty; the site is served at the root. The repo must stay named `antoinenasser.github.io`.
- Preview: `./bin/serve` (Homebrew ruby@3.3 + `.venv` for `jupyter nbconvert`, `pybtex`, `typst`). Build: same PATH, `bundle exec jekyll build`.
- Native gem builds need `SDKROOT=/Library/Developer/CommandLineTools/SDKs/MacOSX26.5.sdk` (the installed macOS 27 SDK breaks the linker); `bin/serve` sets it.
- Layouts, includes and Sass come from the `al_folio_core` gem (see `vendor/bundle/.../al_folio_core-*`). Prefer `_config.yml`, `_data/` and content files; only add local `_layouts/`, `_includes/` or `_sass/` overrides when config cannot express the change. Theme docs: `docs/`.
- Local additions: `_includes/profile_links.liquid` (link rows fed by `_data/links.yml`, groups `main` and `more`), `bin/publication_list.py` (plain PDF of papers.bib + talks.bib, generated in deploy.yml and bin/serve, gitignored), `.vscode/` snippets.
- Posts are folders: `_posts/<folder>/YYYY-MM-DD-slug.md` plus its files, linked by relative paths. `_plugins/post_folders.rb` publishes the folder's non-Markdown files next to the post's page, and gives a Markdown image that starts a paragraph the figure classes, zoom and lazy loading. One post per folder; work-in-progress folders use `published: false` (`_drafts/` would turn every text file into a draft). deploy.yml triggers on `_posts/**` and `_plugins/**`.
- Analytics: Cloudflare Web Analytics, token in `analytics.cloudflare` of `_config.yml` (cookieless, no consent banner). `bin/serve` adds `_config.dev.yml`, which turns every analytics provider off locally. `serve_og_meta` and `serve_schema_org` are on; a folder post's relative `og_image:` is resolved by `_plugins/post_folders.rb`. Keep `description:` in `_config.yml` as `>-`: a trailing newline breaks the Schema.org JSON. Search Console verification goes in `google_site_verification`.
- No CV page or CV PDF: the owner removed it on purpose (and purged it from Git history).
- Theme overrides: `_layouts/bib.liquid` (copy of the gem layout, "Abs" renamed "Abstract", white text on badges without a venue url), `_layouts/about.liquid` (adds the mentoring section from `_data/mentoring.yml`) and `_layouts/post.liquid` (adds `_includes/share_links.liquid` on posts, networks in `_data/share.yml`, `share: false` hides it). `_includes/hook/bib.liquid` appends the bib `tag` field in bold. Re-copy the layouts from the gem after a theme upgrade.
- Bib comments must not contain `@` or backticks (the BibTeX lexer chokes). Write "von" particles as `{de Lavergne}, Casimir`.
- GIFs in `figure.liquid` need `avoid_scaling=true`; files sharing a base name (`x.png`, `x.gif`) collide in the generated webp.
- Deploy: push to `main` runs `.github/workflows/deploy.yml`, which publishes to the `gh-pages` branch (Pages source). The `gh` token lacks the `workflow` scope, so pushes go over SSH.
