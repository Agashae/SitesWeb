# Agashae OS — Portfolio

Portfolio personnel d'Agashae Premakumar, presente sous la forme d'un faux systeme d'exploitation ("bureau" avec icones, barre des taches, horloge). Le site regroupe qui je suis, mon CV, mes competences, mes coordonnees, et surtout **tous mes projets**.

## Pourquoi ce projet ?

Avant, chacun de mes projets (AgaMoon, Nexus, RedBull...) vivait dans son propre depot, sans lien entre eux et sans page pour les presenter. Pour quelqu'un qui regarde mon travail, il fallait fouiller plusieurs repos differents pour comprendre ce que j'ai fait.

Ce depot resout ca : c'est un **portfolio central** qui integre tous mes projets scolaires et personnels au meme endroit, avec une page d'accueil qui donne envie de cliquer et une navigation simple entre eux. L'objectif est d'avoir un seul lien a partager (a un employeur, une ecole, un recruteur) qui montre tout mon travail d'un coup, plutot que de dispatcher les gens sur plusieurs repos GitHub.

## Structure du depot

```
SitesWeb/
├── index.html          bureau (page d'accueil) avec les icones et la taskbar
├── apropos.html         qui je suis, parcours, experiences
├── projets.html         liste de mes projets, avec un lien vers chacun
├── competences.html      connaissances techniques, langues, modules ETML
├── contact.html          coordonnees, LinkedIn, GitHub
├── readme.html           version "site" de ce README, credits
├── CV_AgashaePremakumar.pdf
├── style.css / main.js
│
├── MoonWebsite/         projet : site sur la lune (HTML/CSS)
├── Nexus/               projet : site sur l'astronomie
└── RedBull/             projet : site dedie a l'univers Red Bull
```

Chaque dossier de projet (`MoonWebsite`, `Nexus`, `RedBull`) est un mini-site independant, accessible directement depuis la page **Projets** du portfolio.

## Technologies

- HTML / CSS / JavaScript vanilla (pas de framework)
- Police [Space Mono](https://fonts.google.com/specimen/Space+Mono) (Google Fonts)
- Icones [Phosphor Icons](https://phosphoricons.com/)

## Voir le site

En local : cloner le depot et ouvrir `index.html` dans un navigateur.

```bash
git clone https://github.com/Agashae/SitesWeb.git
cd SitesWeb
```

Puis ouvrir `index.html`.

## Auteur

**Agashae Premakumar** — Apprenti informaticien CFC, Exploitation & Infrastructure (ETML)

- [LinkedIn](https://www.linkedin.com/in/agashae-premakumar/)
- [GitHub](https://github.com/Agashae)
