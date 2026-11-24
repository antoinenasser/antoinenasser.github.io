# Aide-mémoire du site

Mon site perso, en ligne sur https://antoinenasser.github.io.
Il est construit avec [Jekyll](https://jekyllrb.com/) et le thème [al-folio](https://github.com/alshedivat/al-folio) (v1.2), et il est hébergé gratuitement par GitHub Pages.

Ce fichier est mon aide-mémoire : où est quoi, et comment faire les choses courantes. Le `README.md` est la vitrine publique du repo : le garder court.

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
| Les personnes encadrées (mentoring)      | `_data/mentoring.yml`                                           |
| Les couleurs des badges (JAMES, EGU, …)  | `_data/venues.yml`                                              |
| Les notes / how-tos                      | `_posts/nom-court/`, un dossier par note                        |
| Images, GIF, vidéos, figures d'une note  | dans le dossier de la note                                      |
| Les boutons de partage sous les notes    | `_data/share.yml`                                               |
| Le compteur de visites                   | `_config.yml`, `analytics:` (tableau de bord chez Cloudflare)   |
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
  abstract = {Le résumé, affiché par le bouton Abstract.},
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
| `abstract`          | bouton « Abstract »                                                                                      |
| `doi`, `arxiv`, `hal` | boutons DOI / arXiv / HAL                                                                              |
| `code`, `pdf`, `slides`, `poster`, `video`, `website`, `html` | boutons vers un lien, ou vers un fichier de `assets/pdf/` |
| `bibtex_show = {true}` | bouton « Bib » qui montre l'entrée BibTeX                                                             |
| `additional_info`   | texte ajouté après la référence (liens vers les données, par exemple)                                    |
| `tag`               | texte en gras à la fin de la ligne, par exemple `{Submitted to Journal of Computational Physics}`          |

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
  slides    = {mes_slides.pdf},
  tag       = {Invited talk}
}
```

- `slides = {mes_slides.pdf}` affiche un bouton vers `assets/pdf/mes_slides.pdf` (ou vers une adresse web).
- `tag` s'affiche en gras à la fin de la ligne. J'utilise `Invited talk`, `Invited seminar`, `Contributed presentation` et `Laboratory seminar`. Le PDF range les talks en deux sections selon que le tag commence par « Invited » ou non.
- Pas de travaux « en préparation » sur le site : un article y entre une fois soumis, avec `abbr = {Submitted}` et `journal = {Submitted to The Cryosphere}`. Quand son preprint est en ligne, ajouter le `doi`, passer le badge à `Preprint` (ou `arXiv`) et mettre la revue dans `tag`.

### Le mentoring

La liste sous les publications de l'accueil vient de `_data/mentoring.yml` : nom, institution, année, et en option `role` (« Master's internship, co-supervised », « informal guidance ») et `url`.

### La liste PDF des publications

`bin/publication_list.py` fabrique `assets/pdf/Antoine_Nasser_publications.pdf` à partir des deux fichiers `.bib`. C'est une liste simple, facile à copier-coller, liée en haut des pages Publications et Talks.

Il n'y a rien à faire : elle est refaite à chaque publication du site et à chaque lancement de `./bin/serve`. Le fichier n'est pas dans Git, il est généré.

### Une note ou un how-to

Chaque note a son propre dossier dans `_posts/`, avec tout ce qu'elle affiche. Exemple complet :

```text
_posts/article1-rice-paddies/
  2026-11-18-rice-paddies-from-space.md   ← la note
  assets/anim_vh_season.mp4               ← ses images, GIF, vidéos, figures HTML…
  assets/article1/fig_01.1.png
```

1. Créer un dossier `_posts/nom-court/` (nom libre) et y mettre la note `AAAA-MM-JJ-nom-court.md`. La date au début du nom est obligatoire : sans elle, Jekyll ignore le fichier.
2. Dans le fichier vide, taper `article` puis Tab pour l'en-tête. Changer le titre, la description, les tags, puis écrire. Le thème affiche déjà le titre et la date : ne pas les répéter en `# Titre` dans le texte.
3. Les fichiers du dossier s'appellent par leur chemin relatif, comme dans l'aperçu Markdown de VS Code : `![Carte des rizières](assets/carte.png)`.
4. La note apparaît dans l'onglet **Notes**, à l'adresse `/blog/AAAA/nom-court/`. Les fichiers du dossier sont publiés à côté d'elle, sauf les `.md` (on peut y garder des notes de travail).
5. L'annoncer dans la chronologie avec une news (voir plus haut).

Pour préparer une note sans la mettre en ligne : ajouter `published: false` dans l'en-tête, et la voir avec `./bin/serve --unpublished`. Ne pas mettre les dossiers dans `_drafts/` : Jekyll y prend chaque fichier texte pour un brouillon.

Une image seule sur sa ligne devient une figure : largeur de la colonne, centrée, coins arrondis, zoom au clic, chargement différé. Sa légende est la ligne suivante, en italique :

```markdown
![Carte des rizières](assets/carte.png)
*Fig. 2. Les rizières de la zone d'étude.*
```

| Pour insérer…                          | Snippet VS Code | Remarque                                                                                      |
| -------------------------------------- | --------------- | --------------------------------------------------------------------------------------------- |
| une image ou un GIF                    | `image`         | fichier dans le dossier de la note                                                            |
| une vidéo                              | `video`         | MP4 dans le dossier de la note                                                                |
| une figure interactive                 | `plotly`        | en Python : `fig.write_html("figure.html", include_plotlyjs="cdn")`, dans le dossier de la note |
| un notebook + bouton Colab             | `notebook`      | dans `assets/jupyter/` ; exécuter le notebook avant le commit : la page montre les sorties enregistrées |
| une équation                           | `equation`      | LaTeX entre `$$ … $$`, aussi en ligne                                                         |

Le modèle `_drafts/article-template.md` montre le reste (notebook, équations, code). Pour le voir : `./bin/serve --drafts` puis http://localhost:4000/blog/2026/article-template/. Ses images sont rangées dans les dossiers communs (`assets/img/posts/`, `assets/plotly/`) et appelées par l'include `figure.liquid`. Cette façon de faire marche toujours, et c'est la seule qui fabrique des versions WebP allégées des images. Avec elle, deux fichiers ne doivent pas porter le même nom avec deux extensions (`carte.png` et `carte.gif`) : ils se marchent dessus.

Les widgets Python en direct (`ipywidgets`) ne peuvent pas tourner sur un site statique. On les remplace par une figure Plotly avec curseurs, ou par le bouton Colab qui ouvre le notebook pour le lecteur.

Pour une note qui renvoie vers un article publié ailleurs (Medium, un blog de labo…), ajouter `redirect: https://...` dans l'en-tête : le titre dans l'onglet Notes mènera directement au lien.

### Le partage des notes

Sous chaque note, une ligne « Share » : LinkedIn, X, Bluesky, e-mail, copier le lien, et sur téléphone le menu de partage du système. Aucun script tiers : ce sont de simples liens.

- Ajouter ou retirer un réseau : `_data/share.yml`.
- Masquer la ligne sur une note : `share: false` dans son en-tête.
- L'aperçu du lien (titre, description, image) quand on colle l'adresse dans LinkedIn, X, Slack… : le titre et la `description:` de l'en-tête, et l'image `og_image:`, un chemin relatif au dossier de la note comme pour les figures (`og_image: assets/article1/fig_01.2.png`). Une image carrée ou large, sans petit texte, rend le mieux. Sans `og_image:`, c'est la photo de profil (`og_image:` de `_config.yml`).
- LinkedIn garde un aperçu en mémoire plusieurs jours. Après un changement d'image ou de titre, coller l'adresse dans https://www.linkedin.com/post-inspector/ pour le rafraîchir.

### Les statistiques de visite

Le compteur est invisible pour les visiteurs : le site envoie chaque page vue à Cloudflare Web Analytics, et les chiffres ne se voient que dans mon tableau de bord Cloudflare. Pas de cookie, donc pas de bandeau de consentement. Les visiteurs qui ont un bloqueur de pubs ne sont pas comptés : les chiffres sont un minimum.

Mise en route (une fois) :

1. Créer un compte gratuit sur https://dash.cloudflare.com/sign-up (pas besoin d'y mettre le domaine).
2. Dans le tableau de bord, ouvrir **Web Analytics**, puis **Add a site**, et saisir `antoinenasser.github.io`. Le message « This hostname does not belong to any website on your Cloudflare account. You will need to install a JS Snippet » est normal : le site n'est pas hébergé chez Cloudflare, il envoie les visites par un petit script, que le thème ajoute lui-même à partir du token. Valider.
3. Cloudflare montre un bout de code avec `"token": "…"`. Copier ce token (32 caractères) dans `_config.yml`, à la ligne `cloudflare:` sous `analytics:`, puis commit et push.

Ensuite : **Web Analytics** → le site. On y voit les visites et pages vues par jour, les pages les plus lues (filtrer sur `/blog/` pour les notes), d'où viennent les visiteurs (LinkedIn, Google…), leur pays et leur appareil.

`./bin/serve` coupe le compteur (`_config.dev.yml`) : l'aperçu local ne compte pas comme une visite. Mes propres visites du site en ligne, elles, comptent.

### Être trouvé sur Google et Bing

Le site est ouvert aux moteurs de recherche : `robots.txt` autorise tout, et `sitemap.xml` (fabriqué à chaque construction) leur donne la liste des pages. Chaque page dit aussi aux moteurs qui je suis (Schema.org, avec mes profils ORCID, Scholar, GitHub et LinkedIn de `_data/socials.yml`). Il reste à se déclarer, une fois :

1. **Google Search Console** : https://search.google.com/search-console, **Ajouter une propriété**, choisir **Préfixe de l'URL** (pas « Domaine », impossible sur github.io) et saisir `https://antoinenasser.github.io/`.
2. Validation : c'est fait par le fichier `google38cace6aebe80061.html` à la racine du repo (méthode **Fichier HTML**). Ne pas le supprimer, sinon Google perd la preuve que le site est à moi. L'autre méthode, **Balise HTML**, passerait par la ligne `google_site_verification:` de `_config.yml`.
3. Dans Search Console : **Sitemaps**, saisir `sitemap.xml`, **Envoyer**. Puis **Inspection de l'URL** sur la page d'accueil et **Demander une indexation**.
4. **Bing Webmaster Tools** (https://www.bing.com/webmasters) : se connecter et choisir **Importer depuis Google Search Console**, sans autre code. Bing alimente aussi DuckDuckGo, Ecosia et Yahoo.

Compter quelques jours à quelques semaines avant d'apparaître. Search Console montre ensuite les recherches qui mènent au site et les pages indexées.

Ce qui aide le plus à sortir sur « Antoine Nasser » : des liens vers le site depuis mes profils (LinkedIn → coordonnées → site web, profil GitHub, Google Scholar → page d'accueil, ORCID → sites web).

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
| `analytics`               | le compteur de visites (voir « Les statistiques de visite »)          |
| `serve_og_meta`, `og_image` | l'aperçu des liens partagés, et son image par défaut                |
| `google_site_verification` | le code de Google Search Console (voir « Être trouvé sur Google et Bing ») |

Dans `_pages/about.md` : `selected_papers` (publications sur l'accueil), `announcements` (la chronologie, `limit:` pour n'en montrer que N), `latest_posts` (les dernières notes sur l'accueil).

**La couleur d'accent** (magenta en mode clair, cyan en mode sombre) vient du thème. La changer demande deux petits fichiers de surcharge dans `_sass/`, voir « Changing theme color » dans `docs/CUSTOMIZE.md`.

---

## 5. VS Code

En ouvrant le dossier, VS Code propose d'installer les extensions recommandées (`.vscode/extensions.json`) :

- **Front Matter CMS** : un tableau de bord dans VS Code pour lister, créer et prévisualiser notes et news (optionnel) ;
- **Markdown All in One** : raccourcis et aperçu Markdown ;
- **Shopify Liquid** : coloration des balises `{% … %}` ;
- **YAML**, **Python**, **Jupyter**.

Les snippets du site (`.vscode/site.code-snippets`) : dans un fichier `.md`, taper `news`, `article`, `image`, `video`, `plotly`, `notebook` ou `equation`, puis Tab.

---

## 6. Si quelque chose ne marche pas

| Symptôme                                         | Piste                                                                                       |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| Le site en ligne ne change pas                   | onglet **Actions** du repo : la construction a peut-être échoué, le message est dans le log |
| `Lexer: unexpected token` dans le terminal       | un `@` ou un accent grave dans un commentaire `%` d'un fichier `.bib`                       |
| Un nom d'auteur mal coupé                        | mettre la particule entre accolades : `{de Lavergne}, Casimir`                              |
| Une note n'apparaît pas                          | nom de fichier sans date `AAAA-MM-JJ-`, date dans le futur, ou `published: false`           |
| Une image d'une note ne s'affiche pas            | chemin relatif au dossier de la note, sans `/` au début ; majuscules et minuscules comptent en ligne |
| Un GIF reste figé                                | ajouter `avoid_scaling=true` à l'include `figure.liquid`                                     |
| Une modification de `_config.yml` n'apparaît pas | arrêter (Ctrl+C) et relancer `./bin/serve`                                                  |
| En local, les images des notes manquent toutes   | `./bin/serve` tournait déjà quand `_plugins/` a changé : l'arrêter (Ctrl+C) et le relancer  |
| Le PDF des publications n'est pas à jour en local | relancer `./bin/serve`                                                                     |
| Le tableau de bord Cloudflare reste vide         | le token est-il dans `_config.yml` et poussé ? Les visites locales ne comptent pas ; un bloqueur de pubs cache aussi mes propres visites |
| L'aperçu LinkedIn montre l'ancienne image        | https://www.linkedin.com/post-inspector/ pour le rafraîchir                                 |
| Search Console refuse la validation             | la construction est-elle finie (onglet **Actions**) ? Le code est-il dans `google_site_verification:`, sans guillemets ni balise autour ? |
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
  - `_includes/hook/bib.liquid`, qui affiche le `tag` en gras ;
  - `_layouts/bib.liquid`, `_layouts/about.liquid` et `_layouts/post.liquid`, copies des fichiers du thème avec de petites modifications (« Abstract » au lieu de « Abs » et le texte blanc des badges sans lien, la section mentoring, la ligne de partage) ; après une mise à jour du thème, les recopier depuis la gem et refaire la modification ;
  - `_includes/share_links.liquid`, la ligne de partage sous les notes (réseaux dans `_data/share.yml`) ;
  - `_config.dev.yml`, lu en plus de `_config.yml` par `./bin/serve` seulement, pour couper le compteur de visites en local ;
  - `_includes/mentoring.liquid`, la liste de mentoring ;
  - `_plugins/post_folders.rb`, les notes en dossier : il publie les fichiers du dossier à côté de la note, donne aux images seules sur leur ligne l'allure des figures du thème, et accepte un `og_image:` relatif ;
  - `bin/publication_list.py`, la liste PDF ;
  - `_drafts/article-template.md` et le notebook `assets/jupyter/advection-demo.ipynb`, qui fabrique le GIF et la figure interactive du modèle ;
  - `.vscode/`, les réglages et snippets ;
  - ce fichier, et un `README.md` court qui renvoie au template d'origine.
- **La publication** : chaque `git push` sur `main` lance `.github/workflows/deploy.yml`. Il construit le site et le dépose sur la branche `gh-pages`, que GitHub Pages sert à l'adresse du site. Ne jamais modifier `gh-pages` à la main.
- **Le nom du repo** doit rester `antoinenasser.github.io` : c'est ce nom qui donne l'adresse du site.
- **La documentation complète du thème** est dans `docs/`. Commencer par `docs/CUSTOMIZE.md`.
- **La démo officielle d'al-folio**, https://alshedivat.github.io/al-folio/, sert de galerie d'idées : notes avec onglets, diagrammes, graphiques, pseudo-code, page de projets en cartes, page de repos GitHub, etc. Le code de chaque exemple est dans https://github.com/alshedivat/al-folio, dossier `_posts/`.
