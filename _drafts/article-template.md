---
layout: post
title: Article template
date: 2026-11-16
description: A starting point for articles, with an image, a GIF, an interactive figure and a notebook.
tags: how-to
categories: notes
related_posts: false
toc:
  sidebar: left
---

This is the template for articles and how-tos. To write a new one, give it its own folder in `_posts/`, with its files:

```text
_posts/short-title/
  YYYY-MM-DD-short-title.md   <- the article, at /blog/YYYY/short-title/
  map.png                     <- its images, GIFs, videos, HTML figures
```

1. Copy the header above (title, date, description, tags) into the article and change it.
2. Point to the folder's files with relative paths: `![A map](map.png)`, the caption in italics on the next line.
   An image alone on its line is shown like a figure (column width, zoom on click).
3. `published: false` in the header keeps it offline; preview it with `./bin/serve --unpublished`.

`_posts/article1-rice-paddies/` is a full example.
The examples below use the shared folders under `assets/` instead, which still work.
Files in `_drafts/` (like this one) are only shown locally, with `./bin/serve --drafts`.

## Text and links

Normal Markdown: **bold**, _italic_, [a link](https://antoinenasser.github.io), lists, tables, footnotes[^1].

[^1]: A footnote.

## An image

{% include figure.liquid path="assets/img/posts/advection-final.png" class="img-fluid rounded z-depth-1" zoomable=true caption="A static figure. Click to zoom." %}

## A GIF

GIFs need `avoid_scaling=true`, otherwise they are shown as a still image.

{% include figure.liquid path="assets/img/posts/advection.gif" class="img-fluid rounded z-depth-1" avoid_scaling=true caption="A GIF made with matplotlib in the notebook below." %}

A video works the same way:
`{% raw %}{% include video.liquid path="assets/img/posts/my_movie.mp4" class="img-fluid rounded z-depth-1" controls=true autoplay=true loop=true %}{% endraw %}`

## An interactive figure from Python

A static site cannot run Python, so live `ipywidgets` do not work here.
Instead, build the figure with sliders in Python (Plotly), save it with `fig.write_html("assets/plotly/name.html", include_plotlyjs="cdn")` and embed the file:

<iframe src="{{ '/assets/plotly/advection.html' | relative_url }}" title="Upwind advection for several Courant numbers" width="100%" height="460" style="border: none;" loading="lazy"></iframe>

## A Jupyter notebook

Put the notebook in `assets/jupyter/` and run it before committing: the page shows the outputs saved in the file.
The button opens it in Google Colab, where readers can run it, widgets included.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/antoinenasser/antoinenasser.github.io/blob/main/assets/jupyter/advection-demo.ipynb)

{::nomarkdown}
{% assign jupyter_path = "assets/jupyter/advection-demo.ipynb" | relative_url %}
{% capture notebook_exists %}{% file_exists assets/jupyter/advection-demo.ipynb %}{% endcapture %}
{% if notebook_exists == "true" %}
{% jupyter_notebook jupyter_path %}
{% else %}

<p>Notebook not found.</p>
{% endif %}
{:/nomarkdown}

## Math

Inline $$u \cdot \nabla q$$ or displayed:

$$
\partial_t q + \nabla \cdot (\mathbf{u}\, q) = 0
$$

## Code

```python
q = q - courant * (q - np.roll(q, 1))
```

## Announcing it

Add a line to the timeline on the landing page with a file in `_news/`, for example `_news/2026-11-16-article.md`:

```markdown
---
layout: post
date: 2026-11-16
inline: true
related_posts: false
---

New article: [Article template](/blog/2026/article-template/)
```
