#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


def section(text):
    print('\033[1m{}\033[0m'.format(text))


# --------------------------------- #


section('Conditions pour des itérations')

# Les boucles while permettent d'exécuter un bloc de code tant qu'une condition spécifiée est vraie.
# Le bloc de code sera répété jusqu'à ce que la condition devienne fausse.

# Imprimez i tant que i est inférieur à 6:
i = 1
while i < 6:
    print(i)
    i += 1

# À faire: Utilisez une boucle while pour imprimer les valeurs de 1 à 50 pour des multiples de 5.


# --------------------------------- #


# Cette boucle sera infinie (elle ne s'arrêtera jamais), pourquoi ?
i = 1
while i < 6:
    print(i)


# --------------------------------- #


section('Le mot clé break')

# Faire une boucle sur le nombre de caractères d'une chaîne de caractères et arrêter la boucle si le caractère est un espace
texte = 'Hello, World!'
i = 0
while i < len(texte):
    if texte[i] == ' ':
        break
    print(texte[i])
    i += 1

# Le mot clé break va arrêter l'exécution de la boucle et sortir du bloc de code.


# --------------------------------- #


section('Le mot clé continue')

# Afficher les nombres non divisibles par 3
i = 0
while i < 12:
    i += 1
    if i % 3 == 0:
        continue
    print(i)

# Le mot clé continue va arrêter l'exécution du bloc de code actuel et passer à l'itération suivante.


# --------------------------------- #


# Typiquement, les boucles while sont utilisées lorsqu'on ne sait pas combien de fois la boucle doit être exécutée.
# On utilise souvent la variable de contrôle i pour compter le nombre d'itérations.

section('Boucle While pour Compter les Voyelles')

# À faire : Utilisez une boucle while pour compter le nombre de voyelles dans une chaîne de caractères
texte = "Python est amusant"
voyelles = "aeiouy"

i = 0 # Initialisation de la variable de contrôle
compteur = 0 # Initialisation du compteur

texte = text.lower()
while i < len(text):
    if text[i] in voyelles: # Est-ce que le caractère est une voyelle ?
        compteur += 1
    i += 1

print(f"Nombre de voyelles : {compteur}") # Affichage formaté


# --------------------------------- #


section('Calculer la Somme des Nombres Positifs')

# Initialiser la somme et demander la première entrée de l'utilisateur
somme = 0
valeur = int(input("Entrez un nombre (négatif pour arrêter) : "))
# Le mot clé input() permet de demander une entrée à l'utilisateur (retourne un str)
# La fonction int() permet de convertir la chaîne de caractères en un entier (cast)

# Utiliser une boucle while pour continuer à demander des nombres jusqu'à ce qu'un nombre négatif soit entré
while valeur >= 0:
    somme += valeur
    valeur = int(input("Entrez un nombre (négatif pour arrêter) : "))

# Afficher la somme des nombres positifs
print("La somme des nombres positifs est :", somme)

