# CLAUDE.md

Personal site of Antoine Nasser (antoinenasser.github.io), built on the al-folio v1.2 Jekyll starter.
See README.md for where each piece of content lives.

- `baseurl` is empty; the site is served at the root.
- Preview: `./bin/serve` (Homebrew ruby@3.3 + `.venv` for `jupyter nbconvert`). Build: same PATH, `bundle exec jekyll build`.
- Native gem builds need `SDKROOT=/Library/Developer/CommandLineTools/SDKs/MacOSX26.5.sdk` (the installed macOS 27 SDK breaks the linker); `bin/serve` sets it.
- Layouts, includes and Sass come from the `al_folio_core` gem (see `vendor/bundle/.../al_folio_core-*`). Prefer `_config.yml`, `_data/` and content files; only add local `_layouts/`, `_includes/` or `_sass/` overrides when config cannot express the change. Theme docs: `docs/`.
- Bib comments must not contain `@` or backticks (the BibTeX lexer chokes). Write "von" particles as `{de Lavergne}, Casimir`.
