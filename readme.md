# Morpion à l'Africaine

Jeu de morpion à deux joueurs, développé en Python avec **tkinter**. Chaque joueur dispose de 3 pions qu'il place et déplace librement sur un plateau carré. Le premier qui aligne ses 3 pions gagne.

<!-- Ajouter ici une capture d'écran : ![Capture du jeu](capture.png) -->

## Fonctionnalités

- Menu principal : commencer, aide, quitter
- Saisie du nom des deux joueurs
- Choix de la couleur de chaque joueur
- Plateau 2D dessiné avec `Canvas` (carré, diagonales et médianes)
- Mise en surbrillance des positions libres lors de la sélection d'un pion
- Détection automatique de la victoire et réinitialisation de la partie
- Retour au menu depuis le plateau

## Règles du jeu

1. Le plateau est un carré avec ses deux diagonales et ses deux médianes. Il offre 9 positions : les 4 coins, les 4 milieux de côtés et le centre.
2. Deux joueurs s'affrontent. Chacun a 3 pions, placés au départ de part et d'autre du plateau.
3. À tour de rôle, un joueur sélectionne l'un de ses pions puis le place sur une position libre du plateau. Les pions se déplacent librement, sans contrainte de distance.
4. Le premier joueur qui aligne ses 3 pions sur un côté, une médiane ou une diagonale gagne la partie.

## Prérequis

- Python 3
- tkinter (inclus par défaut avec Python sous Windows et macOS)

Sous Linux (Debian/Ubuntu), si tkinter est absent :

```bash
sudo apt install python3-tk
```

Aucune autre dépendance n'est nécessaire.

## Lancer le jeu

```bash
git clone https://github.com/<ton-user>/<nom-du-repo>.git
cd <nom-du-repo>
python main.py
```

## Comment jouer

1. Cliquer sur **Commencer le jeu**, saisir le nom des deux joueurs, choisir les couleurs, puis cliquer sur **Valider**.
2. Cliquer sur l'un de vos pions : les positions libres s'affichent en rouge.
3. Cliquer près de la position voulue pour y placer le pion. Le tour passe à l'autre joueur.
4. Continuer jusqu'à ce qu'un joueur aligne ses 3 pions.

## Structure du projet

```
.
├── main.py      # code du jeu
└── README.md
```

## Évolutions prévues

- Version mobile (Flutter)
- Améliorations de l'interface

## Auteur

Arouna