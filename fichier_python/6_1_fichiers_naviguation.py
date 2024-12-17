#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


def section(text):
    print('\033[1m{}\033[0m'.format(text))


# ### Introduction à la Bibliothèque `os`, la Lecture et l'Écriture de Fichiers, et les Instructions `with` en Python
# 
# #### Bibliothèque `os`
# 
# La bibliothèque `os` en Python fournit une interface pour interagir avec le système d'exploitation. Elle permet de manipuler des fichiers et des répertoires, d'obtenir des informations sur le système, et d'exécuter des commandes du système d'exploitation.
# 
# **Utilisations courantes de `os`** :
# - **Gestion des Fichiers et Répertoires** : Créer, renommer, supprimer des fichiers et des dossiers.
# - **Navigation dans le Système de Fichiers** : Changer le répertoire de travail, lister les fichiers dans un répertoire.
# - **Informations Système** : Obtenir des informations sur le système d'exploitation, les variables d'environnement.

# --------------------------------- #


section('Naviguation simple')

import os

# Manipulation de chemin
path = "/home/User/"
filename = os.path.join(path, 'Desktop', 'file.txt')
print(filename)

basename = os.path.basename(filename)
dirname = os.path.dirname(filename)
basename, ext = os.path.splitext(basename)
print(dirname, basename, ext)
# Dans vos propres mots qu'est-ce que dirname, basename et ext?


# --------------------------------- #


section('Naviguation avancée')
print('WALK')
for root, dirs, files in os.walk("data/", topdown=False):
    for name in files:
        if os.path.splitext(name)[1] != '.png':
            print(os.path.join(root, name))
# À faire : Quand vous voyez le print(), allez voir le dossier data/
# Pouvez-vous décrire dans vos mots ce que ce morceau de code fait ?
        
print('\n---------------\n')

print('GLOB')
from glob import glob
for i, filename in enumerate(glob('data/*.png')):
    print(i, filename)
# À faire : Et maintenant, selon vous qu'est-ce que ce morceau de code fait


# #### Lecture et Écriture de Fichiers
# 
# Lire et écrire des fichiers sont des opérations de base en programmation, et Python rend ces tâches simples et efficaces.
# 
# **Lecture de fichiers** :
# - **Ouvrir un fichier en mode lecture** : Pour lire le contenu d'un fichier.
# - **Lire le contenu** : Utiliser des méthodes pour lire tout le fichier ou ligne par ligne.
# - **Fermer le fichier** : Fermer le fichier après la lecture pour libérer les ressources.
# 
# **Écriture de fichiers** :
# - **Ouvrir un fichier en mode écriture** : Pour écrire des données dans un fichier. Si le fichier n'existe pas, il sera créé.
# - **Écrire des données** : Utiliser des méthodes pour écrire des chaînes de caractères ou des données binaires dans le fichier.
# - **Fermer le fichier** : Fermer le fichier après l'écriture pour s'assurer que toutes les données sont correctement enregistrées.
# 
# #### Instructions `with`
# 
# Les instructions `with` simplifient la gestion des ressources comme les fichiers. Elles garantissent que les fichiers sont correctement fermés après leur utilisation, même si une erreur survient pendant l'exécution du bloc de code.
# 
# **Avantages des instructions `with`** :
# - **Simplicité et Lisibilité** : Le code est plus simple et plus lisible.
# - **Gestion Automatique des Ressources** : Les fichiers sont automatiquement fermés, ce qui évite les fuites de ressources.
# - **Gestion des Erreurs** : Assure que les ressources sont correctement libérées même en cas d'erreur.

# #### Exemple 1 : Lire Tout le Contenu d'un Fichier
# 
# ```python
# section('Lire Tout le Contenu d\'un Fichier')
# 
# # Ouvrir le fichier en mode lecture ('r') et lire tout le contenu
# with open('exemple.txt', 'r') as fichier:
#     contenu = fichier.read()
#     print(contenu)
# ```
# 
# #### Exemple 2 : Lire un Fichier Ligne par Ligne
# 
# ```python
# section('Lire un Fichier Ligne par Ligne')
# 
# # Ouvrir le fichier en mode lecture ('r') et lire ligne par ligne
# with open('exemple.txt', 'r') as fichier:
#     for ligne in fichier:
#         print(ligne, end='')  # end='' pour éviter d'ajouter des nouvelles lignes supplémentaires
# ```
# 
# #### Exemple 3 : Lire les Lignes d'un Fichier dans une Liste
# 
# ```python
# section('Lire les Lignes d\'un Fichier dans une Liste')
# 
# # Ouvrir le fichier en mode lecture ('r') et stocker les lignes dans une liste
# with open('exemple.txt', 'r') as fichier:
#     lignes = fichier.readlines()
#     print(lignes)
# ```
# 
# #### Exemple 4 : Lire une Quantité Spécifique de Caractères
# 
# ```python
# section('Lire une Quantité Spécifique de Caractères')
# 
# # Ouvrir le fichier en mode lecture ('r') et lire les 10 premiers caractères
# with open('exemple.txt', 'r') as fichier:
#     contenu = fichier.read(10)
#     print(contenu)
# ```

# ### Exemples de Code pour l'Écriture Simple de Fichiers en Python
# 
# #### Exemple 1 : Écrire du Texte dans un Fichier
# 
# ```python
# section('Écrire du Texte dans un Fichier')
# 
# # Ouvrir le fichier en mode écriture ('w') et écrire du texte
# with open('exemple.txt', 'w') as fichier:
#     fichier.write("Ceci est une ligne de texte.\n")
#     fichier.write("Ceci est une autre ligne de texte.\n")
# ```
# 
# #### Exemple 2 : Ajouter du Texte à la Fin d'un Fichier
# 
# ```python
# section('Ajouter du Texte à la Fin d\'un Fichier')
# 
# # Ouvrir le fichier en mode ajout ('a') et ajouter du texte
# with open('exemple.txt', 'a') as fichier:
#     fichier.write("Cette ligne est ajoutée à la fin du fichier.\n")
# ```
# 
# #### Exemple 3 : Écrire des Lignes de Texte à Partir d'une Liste
# 
# ```python
# section('Écrire des Lignes de Texte à Partir d\'une Liste')
# 
# # Liste de lignes à écrire dans le fichier
# lignes = [
#     "Première ligne.\n",
#     "Deuxième ligne.\n",
#     "Troisième ligne.\n"
# ]
# 
# # Ouvrir le fichier en mode écriture ('w') et écrire les lignes
# with open('exemple.txt', 'w') as fichier:
#     fichier.writelines(lignes)
# ```

# --------------------------------- #


# À faire : Voici un exercice résumant plusieurs concept
# 1) Lire le fichier data/mini_texte.txt
# 2) Déterminer la longueur totale du texte (nombre de caractère)
# 3) Trouver tout les mots ayant la lettre 'a'
# 4) Faire une liste de tout les mots de plus de 4 lettres


# --------------------------------- #


section('Lire un Fichier depuis le Disque')

import os
import random
from time import time

def lire_et_nettoyer(filename):
    """
    Lit un fichier et extrait une liste de mots, en supprimant les caractères indésirables.
    """
    with open(filename, 'r') as f:
        lignes = f.readlines()

    mots = []
    caracteres_a_supprimer = ['.', ',']

    for ligne in lignes:
        if ligne.strip() == '':  # Vérifie les lignes vides
            continue

        for caractere in caracteres_a_supprimer:
            ligne = ligne.replace(caractere, ' ')
        mots.extend(ligne.lower().split()) # Une ligne, plusieurs opération

    mots_nettoyes = []
    for mot in mots:
        if mot is not mot.isdigit(): # Que fait cette fonction
            mots_nettoyes.append(mot)
    return mots_nettoyes

liste_de_mots = lire_et_nettoyer(os.path.join('data', 'mid_texte.txt'))
print(liste_de_mots)

