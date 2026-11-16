---
layout: about
title: About
permalink: /
subtitle: Ocean modelling · Numerical methods · Machine learning for climate models

profile:
  align: right
  image: prof_pic.jpg # replace assets/img/prof_pic.jpg with your own photo (same file name)
  image_circular: false # crops the image to make it circular

selected_papers: true # lists the papers marked `selected = {true}` in _bibliography/papers.bib
mentoring: true # lists the people in _data/mentoring.yml under the selected publications
social: false # the visible links are the two rows around the bio, edited in _data/links.yml

announcements:
  enabled: true # the timeline of items in the `_news` folder, newest first
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false # set to true once you publish posts / how-tos in `_posts`
  scrollable: true
  # limit: 3
---

<!-- Bio: edit the paragraphs below. The links above and under it come from _data/links.yml. -->

{% include profile_links.liquid group="main" %}

I am a physical oceanographer working on the **numerics of ocean general circulation models**: how the discrete equations we solve on a computer represent coastlines, topography and ice-shelf cavities, and, more recently, how **machine learning** can produce numerical schemes that remain stable and generalize beyond their training data.

I am currently a Postdoctoral Research Associate in the [Atmospheric and Oceanic Sciences program](https://aos.princeton.edu/) at Princeton University, where I work with Alistair Adcroft on data-driven discretizations for climate models.

I did my PhD (2019–2023) at Sorbonne Université, between [LOCEAN](https://www.locean.ipsl.fr/) in Paris and [Inria / Laboratoire Jean Kuntzmann](https://team.inria.fr/airsea/) in Grenoble, under the supervision of Gurvan Madec, Laurent Debreu and Casimir de Lavergne. My thesis, [_Advancing the representation of flows along topography in z-coordinate ocean models_](https://theses.hal.science/tel-04399405), studied the spurious drag created by staircase-like coastlines and introduced Brinkman volume penalization to smooth topography and ice-shelf cavities in the NEMO ocean model.

{% include profile_links.liquid group="more" %}
