# antoinenasser.github.io

Mon site perso, en ligne sur https://antoinenasser.github.io.
Il est construit avec [Jekyll](https://jekyllrb.com/) et le thème [al-folio](https://github.com/alshedivat/al-folio) (v1.2), et il est hébergé gratuitement par GitHub Pages.

Ce guide est un aide-mémoire : où est quoi, et comment faire les choses courantes.

---

## 1. Le cycle de travail

1. Ouvrir le dossier dans VS Code.
2. Lancer l'aperçu local dans le terminal :

   ```bash
   ./bin/serve            # http://localhost:4000, se recharge à chaque sauvegarde
   ./bin/serve --drafts   # montre aussi les brouillons de _drafts/
   ```

3. Modifier les fichiers, regarder le résultat dans le navigateur.
4. Publier :

   ```bash
   git add -A
   git commit -m "Ce que j'ai changé"
   git push
   ```

   Le site en ligne est à jour 2 à 3 minutes plus tard. La construction se suit dans l'onglet **Actions** du repo sur GitHub. Si une étape est rouge, le message d'erreur y est.

Pour une petite correction sans ordinateur configuré : sur la page du repo GitHub, appuyer sur la touche `.` ouvre un VS Code dans le navigateur. On modifie, puis on fait un commit depuis l'icône de gauche « Source Control ».

---

## 2. Où est quoi

| Je veux changer…                         | Fichier                                                         |
| ---------------------------------------- | --------------------------------------------------------------- |
| La bio, le sous-titre sous mon nom       | `_pages/about.md`                                               |
| La photo                                 | `assets/img/prof_pic.jpg` (remplacer le fichier, garder le nom) |
| Les boutons de liens (LinkedIn, …)       | `_data/links.yml`                                               |
| La chronologie de news                   | `_news/` (un petit fichier par news)                            |
| Les publications                         | `_bibliography/papers.bib`                                      |
| Les talks et posters                     | `_bibliography/talks.bib`                                       |
| Les couleurs des badges (JAMES, EGU, …)  | `_data/venues.yml`                                              |
| Les notes / how-tos                      | `_posts/` (modèle : `_drafts/article-template.md`)              |
| Images, GIF, vidéos des notes            | `assets/img/posts/`                                             |
| Figures interactives (Plotly)            | `assets/plotly/`                                                |
| Notebooks Jupyter                        | `assets/jupyter/`                                               |
| Les onglets et le texte des pages        | `_pages/`                                                       |
| Nom du site, options générales           | `_config.yml` (redémarrer `./bin/serve` après une modification) |

---

## 3. Recettes

### La bio et la photo

- La bio est le texte sous la deuxième ligne `---` de `_pages/about.md`. C'est du Markdown : `**gras**`, `_italique_`, `[texte](https://lien)`.
- Le sous-titre sous mon nom est la ligne `subtitle:` en haut du même fichier.
- La photo : remplacer `assets/img/prof_pic.jpg`. Pour une photo ronde : `image_circular: true`.

### Les boutons de liens

Dans `_data/links.yml`, il y a deux groupes :

- `main` : les boutons au-dessus de la bio (LinkedIn, GitHub, Google Scholar) ;
- `more` : les petits liens sous la bio (ORCID, code BVP).

Pour ajouter un lien, copier un bloc de trois lignes dans le bon groupe :

```yaml
  - name: Bluesky
    url: https://bsky.app/profile/...
    icon: fa-brands fa-bluesky
```

Les icônes viennent de [Font Awesome](https://fontawesome.com/search?ic=free) (`fa-brands fa-…`, `fa-solid fa-…`) ou de [Academicons](https://jpswalsh.github.io/academicons/) (`ai ai-…`).

### Une news dans la chronologie

Créer un fichier `_news/AAAA-MM-JJ-un-nom.md`. Dans VS Code, taper `news` puis Tab remplit tout.

```markdown
---
layout: post
date: 2026-11-16
inline: true
related_posts: false
---

New article: [How I make ocean GIFs](/blog/2026/ocean-gifs/), or a [link elsewhere](https://example.org).
```

Les liens peuvent pointer vers une note du site (`/blog/AAAA/nom/`) ou vers n'importe quelle page externe. Les emojis s'écrivent `:ocean:`.

### Une publication

Ajouter une entrée BibTeX dans `_bibliography/papers.bib`. L'ordre dans le fichier n'a pas d'importance : la page trie par date.

```bibtex
@article{nasser2027exemple,
  abbr     = {JAMES},
  title    = {Titre de l'article},
  author   = {Nasser, Antoine-Alexis and Adcroft, Alistair},
  journal  = {Journal of Advances in Modeling Earth Systems},
  volume   = {19},
  number   = {1},
  pages    = {e2027MS000000},
  year     = {2027},
  month    = {jan},
  doi      = {10.1029/2027MS000000},
  code     = {https://github.com/antoinenasser/mon-code},
  abstract = {Le résumé, affiché par le bouton Abs.},
  preview  = {mon_image.gif},
  selected = {true},
  bibtex_show = {true}
}
```

Les champs utiles, tous optionnels sauf titre, auteurs et année :

| Champ               | Effet                                                                                                    |
| ------------------- | -------------------------------------------------------------------------------------------------------- |
| `abbr`              | badge coloré à gauche ; sa couleur et son lien se règlent dans `_data/venues.yml`                        |
| `selected = {true}` | affiche la publication sur la page d'accueil                                                             |
| `preview`           | image, GIF ou MP4 à côté du titre, rangé dans `assets/img/publication_preview/`                          |
| `abstract`          | bouton « Abs »                                                                                           |
| `doi`, `arxiv`, `hal` | boutons DOI / arXiv / HAL                                                                              |
| `code`, `pdf`, `slides`, `poster`, `video`, `website`, `html` | boutons vers un lien, ou vers un fichier de `assets/pdf/` |
| `bibtex_show = {true}` | bouton « Bib » qui montre l'entrée BibTeX                                                             |
| `additional_info`   | texte ajouté après la référence (liens vers les données, par exemple)                                    |

Deux pièges du lecteur BibTeX :

- pas de `@` ni d'accent grave (`` ` ``) dans les lignes de commentaire qui commencent par `%` ;
- les noms à particule s'écrivent entre accolades : `{de Lavergne}, Casimir`.

Mon nom est souligné automatiquement s'il est écrit `Nasser, Antoine-Alexis` ou `Nasser, Antoine`. Pour mettre un lien sur le nom d'un co-auteur, voir `_data/coauthors.yml`.

### Un talk ou un poster

Même principe dans `_bibliography/talks.bib`, avec le type `@inproceedings` :

```bibtex
@inproceedings{nasser2027egu,
  abbr      = {EGU},
  title     = {Titre du talk},
  author    = {Nasser, Antoine-Alexis and Adcroft, Alistair},
  booktitle = {EGU General Assembly 2027},
  location  = {Vienna, Austria},
  year      = {2027},
  month     = {apr},
  doi       = {10.5194/egusphere-egu27-0000},
  slides    = {mes_slides.pdf}
}
```

`slides = {mes_slides.pdf}` affiche un bouton vers `assets/pdf/mes_slides.pdf`.

### La liste PDF des publications

`bin/publication_list.py` fabrique `assets/pdf/Antoine_Nasser_publications.pdf` à partir des deux fichiers `.bib`. C'est une liste simple, facile à copier-coller, liée en haut des pages Publications et Talks.

Il n'y a rien à faire : elle est refaite à chaque publication du site et à chaque lancement de `./bin/serve`. Le fichier n'est pas dans Git, il est généré.

### Une note ou un how-to

1. Copier `_drafts/article-template.md` dans `_posts/AAAA-MM-JJ-nom-court.md`. Ou créer le fichier et taper `article` puis Tab.
2. Changer le titre, la date, la description, puis écrire.
3. La note apparaît dans l'onglet **Notes**, à l'adresse `/blog/AAAA/nom-court/`.
4. L'annoncer dans la chronologie avec une news (voir plus haut).

Le modèle montre tout ce qu'on peut insérer. Pour le voir : `./bin/serve --drafts` puis http://localhost:4000/blog/2026/article-template/

| Pour insérer…                          | Snippet VS Code | Remarque                                                                                      |
| -------------------------------------- | --------------- | --------------------------------------------------------------------------------------------- |
| une image                              | `image`         | fichier dans `assets/img/posts/`                                                              |
| un GIF                                 | `gif`           | garder `avoid_scaling=true`, sinon le GIF devient une image fixe                              |
| une vidéo                              | `video`         | MP4 dans `assets/img/posts/`                                                                  |
| une figure interactive                 | `plotly`        | en Python : `fig.write_html("assets/plotly/nom.html", include_plotlyjs="cdn")`                |
| un notebook + bouton Colab             | `notebook`      | exécuter le notebook avant le commit : la page montre les sorties enregistrées                |
| une équation                           | `equation`      | LaTeX entre `$$ … $$`, aussi en ligne                                                         |

Les widgets Python en direct (`ipywidgets`) ne peuvent pas tourner sur un site statique. On les remplace par une figure Plotly avec curseurs, ou par le bouton Colab qui ouvre le notebook pour le lecteur.

Deux fichiers ne doivent pas porter le même nom avec deux extensions (`carte.png` et `carte.gif`) : ils se marchent dessus.

Pour une note qui renvoie vers un article publié ailleurs (Medium, un blog de labo…), ajouter `redirect: https://...` dans l'en-tête : le titre dans l'onglet Notes mènera directement au lien.

### Une nouvelle page ou un nouvel onglet

Créer `_pages/nom.md` :

```markdown
---
layout: page
title: Side quests
permalink: /side-quests/
description: Une phrase sous le titre.
nav: true
nav_order: 4
---

Le contenu en Markdown.
```

`nav: true` ajoute l'onglet. `nav_order` règle sa position (Publications = 1, Talks = 2, Notes = 3). Avec `nav: false`, la page existe mais n'est accessible que par un lien.

---

## 4. Options et apparence

Dans `_config.yml` (redémarrer `./bin/serve` après) :

| Option                    | Effet                                                                 |
| ------------------------- | --------------------------------------------------------------------- |
| `title`, `first_name`, `last_name`, `description` | nom du site et texte pour les moteurs de recherche |
| `max_width`               | largeur de la page (930px actuellement)                               |
| `enable_darkmode`         | bouton mode sombre                                                    |
| `search_enabled`          | recherche (raccourci ⌘K)                                              |
| `enable_math`             | équations LaTeX                                                       |
| `enable_medium_zoom`      | zoom au clic sur les images                                           |
| `enable_progressbar`      | barre de progression en haut des pages longues                        |
| `max_author_limit`        | nombre d'auteurs affichés avant « and N more authors »                |
| `giscus`                  | commentaires sous les notes (via GitHub Discussions)                  |
| `blog_name`, `blog_description` | titre et sous-titre de l'onglet Notes                           |

Dans `_pages/about.md` : `selected_papers` (publications sur l'accueil), `announcements` (la chronologie, `limit:` pour n'en montrer que N), `latest_posts` (les dernières notes sur l'accueil).

**La couleur d'accent** (magenta en mode clair, cyan en mode sombre) vient du thème. La changer demande deux petits fichiers de surcharge dans `_sass/`, voir « Changing theme color » dans `docs/CUSTOMIZE.md`.

---

## 5. VS Code

En ouvrant le dossier, VS Code propose d'installer les extensions recommandées (`.vscode/extensions.json`) :

- **Front Matter CMS** : un tableau de bord dans VS Code pour lister, créer et prévisualiser notes et news (optionnel) ;
- **Markdown All in One** : raccourcis et aperçu Markdown ;
- **Shopify Liquid** : coloration des balises `{% … %}` ;
- **YAML**, **Python**, **Jupyter**.

Les snippets du site (`.vscode/site.code-snippets`) : dans un fichier `.md`, taper `news`, `article`, `image`, `gif`, `video`, `plotly`, `notebook` ou `equation`, puis Tab.

---

## 6. Si quelque chose ne marche pas

| Symptôme                                         | Piste                                                                                       |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| Le site en ligne ne change pas                   | onglet **Actions** du repo : la construction a peut-être échoué, le message est dans le log |
| `Lexer: unexpected token` dans le terminal       | un `@` ou un accent grave dans un commentaire `%` d'un fichier `.bib`                       |
| Un nom d'auteur mal coupé                        | mettre la particule entre accolades : `{de Lavergne}, Casimir`                              |
| Un GIF reste figé                                | ajouter `avoid_scaling=true` à l'include                                                    |
| Une modification de `_config.yml` n'apparaît pas | arrêter (Ctrl+C) et relancer `./bin/serve`                                                  |
| Le PDF des publications n'est pas à jour en local | relancer `./bin/serve`                                                                     |
| `./bin/serve` échoue sur l'installation des gems | voir l'encadré ci-dessous                                                                   |

Installation sur un nouveau Mac :

```bash
brew install ruby@3.3 imagemagick
python3 -m venv .venv && .venv/bin/pip install nbconvert pybtex typst
./bin/serve
```

`bin/serve` utilise le Ruby 3.3 de Homebrew et le Python de `.venv`. Il force aussi le SDK macOS 26.5 : le SDK macOS 27 installé avec les Command Line Tools casse la compilation des gems.

---

## 7. Comment le site est fabriqué

- **Le thème** : al-folio fournit la mise en page, les listes de publications, la chronologie, les notes, la recherche et le mode sombre. Ses fichiers sont dans des gems Ruby (`al_folio_core`, …), pas dans ce dossier. On ne les modifie pas : on règle `_config.yml`, `_data/` et les pages.
- **Ajouts propres à ce site** :
  - `_includes/profile_links.liquid`, les boutons de liens ;
  - `bin/publication_list.py`, la liste PDF ;
  - `_drafts/article-template.md` et le notebook `assets/jupyter/advection-demo.ipynb`, qui fabrique le GIF et la figure interactive du modèle ;
  - `.vscode/`, les réglages et snippets.
- **La publication** : chaque `git push` sur `main` lance `.github/workflows/deploy.yml`. Il construit le site et le dépose sur la branche `gh-pages`, que GitHub Pages sert à l'adresse du site. Ne jamais modifier `gh-pages` à la main.
- **Le nom du repo** doit rester `antoinenasser.github.io` : c'est ce nom qui donne l'adresse du site.
- **La documentation complète du thème** est dans `docs/`. Commencer par `docs/CUSTOMIZE.md`.
- **La démo officielle d'al-folio**, https://alshedivat.github.io/al-folio/, sert de galerie d'idées : notes avec onglets, diagrammes, graphiques, pseudo-code, page de projets en cartes, page de repos GitHub, etc. Le code de chaque exemple est dans https://github.com/alshedivat/al-folio, dossier `_posts/`.
