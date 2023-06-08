# casino_python_tkinter

Casino Application


Description:

Ce projet est une application de casino permettant aux utilisateurs de jouer à différents jeux de hasard tels que la machine à sous et la roulette. L'application est implémentée en utilisant Python et la bibliothèque Tkinter pour l'interface graphique.

Fonctionnalités:

Jeu de machine à sous : Les utilisateurs peuvent jouer à la machine à sous en misant 1€ par tour. S'ils obtiennent trois symboles identiques, ils remportent 500€.
Jeu de roulette : Les utilisateurs peuvent jouer à la roulette en choisissant un numéro entre 0 et 49 et en misant une certaine somme d'argent. S'ils devinent correctement le numéro tiré, ils remportent trois fois la mise.

Structure du projet:

Le projet est organisé comme suit :

Le fichier main.py est le point d'entrée de l'application. Il initialise les objets nécessaires, tels que l'utilisateur et les jeux, et affiche le menu principal.
Le dossier jeux contient les différents jeux disponibles.
jeu.py est la classe de base Jeu qui définit les fonctionnalités communes à tous les jeux.
machineasous.py est la classe MachineASous qui hérite de Jeu et implémente le jeu de la machine à sous.
roulette.py est la classe Roulette qui hérite de Jeu et implémente le jeu de la roulette.
Le fichier user.py contient la classe User qui représente un utilisateur du casino. Il gère le nom d'utilisateur, le mot de passe et l'argent du joueur.

Prérequis:

Avant de pouvoir exécuter l'application, assurez-vous d'avoir les éléments suivants installés :

Python 3.x : https://www.python.org/downloads/

Instructions d'exécution:

Assurez-vous d'avoir Python installé sur votre machine.
Téléchargez ou clonez le projet sur votre ordinateur.
Ouvrez une invite de commande ou un terminal et accédez au répertoire du projet.
Exécutez la commande suivante pour lancer l'application :
css

python main.py
L'application du casino s'ouvrira et vous pourrez choisir parmi les différents jeux disponibles.
