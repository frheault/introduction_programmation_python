#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


def section(text):
    print('\033[1m{}\033[0m'.format(text))


# --------------------------------- #


section('Utilisation de if in avec les Chaînes de Caractères')

# Vérifier si un caractère ou une sous-chaîne est présent dans une chaîne
phrase = "Python est amusant"
if "Python" in phrase:
    print("La chaîne contient 'Python'")
if "amusant" in phrase:
    print("La chaîne contient 'amusant'")


# --------------------------------- #


section('Utilisation de while avec les Chaînes de Caractères')

# Parcourir une chaîne de caractères avec une boucle while
texte = "Bonjour"
i = 0
while i < len(texte):
    print(texte[i])
    i += 1


# --------------------------------- #


section('Fonctions Utiles pour les Chaînes de Caractères')

texte = "Python est génial. Python est facile à apprendre."

# Utiliser len() pour obtenir la longueur de la chaîne
print("Longueur de la chaîne:", len(texte))

# Utiliser find() pour trouver la position de la première occurrence d'une sous-chaîne
position = texte.find("génial")
print("Position de 'génial':", position)

# Utiliser count() pour compter le nombre d'occurrences d'une sous-chaîne
occurrences = texte.count("Python")
print("Nombre d'occurrences de 'Python':", occurrences)

# Utiliser upper() et lower() pour changer la casse
print("En majuscules:", texte.upper())
print("En minuscules:", texte.lower())

# Utiliser replace() pour remplacer une sous-chaîne par une autre
nouveau_texte = texte.replace("génial", "super")
print("Texte modifié:", nouveau_texte)

# Utiliser split() pour diviser la chaîne en une liste de mots
mots = texte.split()
print("Liste des mots:", mots)

# Utiliser split() avec un délimiteur personnalisé pour diviser la chaîne
mots = texte.split(".")
print("Liste des mots (délimité par '.'):", mots)

# Utiliser join() pour joindre une liste de mots en une chaîne
chaine_join = " ".join(mots)
print("Chaîne jointe:", chaine_join)

# On peut aussi utiliser join() avec un délimiteur personnalisé pour joindre les mots
chaine_join = "-".join(mots)
print("Chaîne jointe (délimité par '-':", chaine_join)

# À faire : Trouver la position du mot "de" dans la phrase suivante
phrase = "Python est un langage de programmation populaire à Sherbrooke"

