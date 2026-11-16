# antoinenasser.github.io

Personal academic website of Antoine Nasser, built with [Jekyll](https://jekyllrb.com/) and the [al-folio](https://github.com/alshedivat/al-folio) theme (v1.2), hosted on GitHub Pages.

## Where things live

| What                               | File                                                                    |
| ---------------------------------- | ----------------------------------------------------------------------- |
| Bio, subtitle, photo caption       | `_pages/about.md`                                                       |
| Photo                              | `assets/img/prof_pic.jpg` (replace the file, keep the name)             |
| Links under the bio                | `_data/links.yml` (GitHub, Google Scholar, LinkedIn, ...)               |
| Timeline on the landing page       | `_news/` (one small Markdown file per item, see below)                  |
| Articles / how-tos                 | `_posts/` (start from `_drafts/article-template.md`)                    |
| Images and GIFs for articles       | `assets/img/posts/`                                                     |
| Interactive figures (Plotly HTML)  | `assets/plotly/`                                                        |
| Notebooks embedded in articles     | `assets/jupyter/`                                                       |
| Publications                       | `_bibliography/papers.bib`                                              |
| Landing-page "selected" papers     | `selected = {true}` in `papers.bib`                                     |
| Publication image / GIF / MP4      | `assets/img/publication_preview/` + `preview = {file.gif}` in the entry |
| Talks                              | `_bibliography/talks.bib`                                               |
| CV page (and the generated PDF)    | `_data/cv.yml`                                                          |
| Publication badge colors           | `_data/venues.yml`                                                      |
| Profile IDs for search engines     | `_data/socials.yml`                                                     |
| Site name, tabs, features          | `_config.yml`                                                           |

Tabs: a page in `_pages/` appears in the top bar when its header has `nav: true`; `nav_order` sets the order.
The blog tab is hidden (`nav: false` in `_pages/blog.md`) until there are posts.

## Add an item to the timeline

Create `_news/YYYY-MM-DD-anything.md`. The text can link to an article of this site or to any external page:

```markdown
---
layout: post
date: 2026-11-16
inline: true
related_posts: false
---

New article: [How I make ocean GIFs](/blog/2026/ocean-gifs/), or a [link elsewhere](https://example.org).
```

## Write an article

1. Copy `_drafts/article-template.md` to `_posts/YYYY-MM-DD-short-title.md` (it shows how to add images, GIFs, a Plotly figure, a notebook and math).
2. Preview it with `./bin/serve`; it is published at `/blog/YYYY/short-title/` when you push.
3. For the first article, set `nav: true` in `_pages/blog.md` to show the blog tab.

## Preview locally

```bash
./bin/serve            # http://localhost:4000, reloads on save
./bin/serve --drafts   # also shows posts in _drafts/
```

`bin/serve` uses Homebrew's Ruby 3.3 and the project's `.venv` (for Jupyter notebook rendering).
First-time setup on a new machine:

```bash
brew install ruby@3.3 imagemagick
python3 -m venv .venv && .venv/bin/pip install nbconvert
./bin/serve
```

Changes to `_config.yml` need a restart of `bin/serve`.

## Publish

Push to `main`. The `Deploy site` GitHub Action builds the site into the `gh-pages` branch
(Settings → Pages → Source: "Deploy from a branch", branch `gh-pages`).
The `Render a CV` action regenerates the PDF CV whenever `_data/cv.yml` changes.

## Theme docs

The al-folio documentation is in `docs/` (start with `docs/CUSTOMIZE.md`).
