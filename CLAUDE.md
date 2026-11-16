# CLAUDE.md

Personal site of Antoine Nasser (antoinenasser.github.io), built on the al-folio v1.2 Jekyll starter.
README.md (in French, for the owner) says where each piece of content lives; keep it in sync when adding features.

- `baseurl` is empty; the site is served at the root. The repo must stay named `antoinenasser.github.io`.
- Preview: `./bin/serve` (Homebrew ruby@3.3 + `.venv` for `jupyter nbconvert`, `pybtex`, `typst`). Build: same PATH, `bundle exec jekyll build`.
- Native gem builds need `SDKROOT=/Library/Developer/CommandLineTools/SDKs/MacOSX26.5.sdk` (the installed macOS 27 SDK breaks the linker); `bin/serve` sets it.
- Layouts, includes and Sass come from the `al_folio_core` gem (see `vendor/bundle/.../al_folio_core-*`). Prefer `_config.yml`, `_data/` and content files; only add local `_layouts/`, `_includes/` or `_sass/` overrides when config cannot express the change. Theme docs: `docs/`.
- Local additions: `_includes/profile_links.liquid` (link rows fed by `_data/links.yml`, groups `main` and `more`), `bin/publication_list.py` (plain PDF of papers.bib + talks.bib, generated in deploy.yml and bin/serve, gitignored), `.vscode/` snippets.
- No CV page or CV PDF: the owner removed it on purpose (and purged it from Git history).
- Theme overrides: `_layouts/bib.liquid` (copy of the gem layout, "Abs" renamed "Abstract") and `_layouts/about.liquid` (adds the mentoring section from `_data/mentoring.yml`). `_includes/hook/bib.liquid` appends the bib `tag` field in bold. Re-copy the layouts from the gem after a theme upgrade.
- Bib comments must not contain `@` or backticks (the BibTeX lexer chokes). Write "von" particles as `{de Lavergne}, Casimir`.
- GIFs in `figure.liquid` need `avoid_scaling=true`; files sharing a base name (`x.png`, `x.gif`) collide in the generated webp.
- Deploy: push to `main` runs `.github/workflows/deploy.yml`, which publishes to the `gh-pages` branch (Pages source). The `gh` token lacks the `workflow` scope, so pushes go over SSH.
