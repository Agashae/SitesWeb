# Agashae OS — Portfolio

Le but est de créer un portfolio personnel, de le présenter  sous la forme d'un faux systeme d'exploitation avec un bureau, des icones, une barre des tâches et même l'heure.
Le site regroupe qui je suis, mon CV, mes competences, mes coordonnees, et surtout tous mes projets.

## Pourquoi ce projet ?

Avant, chacun de mes projets (AgaMoon, Nexus, RedBull...) était dans son propre depot, sans lien entre eux et sans page pour les presenter. Pour quelqu'un qui regarde mon travail, il fallait fouiller plusieurs repos differents pour comprendre ce que j'ai fait.

Ce depot resout ça : il centralise tous mes projets scolaires et personnels au même endroit, avec une page d'accueil qui donne envie de cliquer et une navigation simple entre eux. 
L'objectif est d'avoir un seul lien à partager (à un employeur, une école, un recruteur) qui montre tout mon travail d'un coup.

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

- HTML / CSS / JavaScript (pas de framework)


## Voir le site

En local : cloner le depot et ouvrir `index.html` dans un navigateur.

```bash
git clone https://github.com/Agashae/SitesWeb.git
cd SitesWeb
```

Puis ouvrir `index.html`.

## Auteur

**Agashae Premakumar** — Apprenti informaticien CFC, Exploitation & Infrastructure (ETML)
Claude pour l'aide à l'optimisation des codes, structuration des dossiers et correction générales

- [LinkedIn](https://www.linkedin.com/in/agashae-premakumar/)
- [GitHub](https://github.com/Agashae)
