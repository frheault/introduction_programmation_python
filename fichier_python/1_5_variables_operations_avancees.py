#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


def section(text):
    print('\033[1m{}\033[0m'.format(text))


# --------------------------------- #


section('Attention avec les nombres à virgule flottante')
import math as m

# Vous pouvez utiliser la notation scientifique
print(1.15e-3 == 0.00115)
print(12.5e4 == 125000)

RAYON_MM = 2.1e-3
EPSILON = 10e-6
surface_cm2 = 2 * RAYON_MM * m.pi / 100
print(surface_cm2)

print(0.1 + 0.2 - 0.3)
print(0.2 + 0.1, 0.2 - 0.1)


# --------------------------------- #


# À faire : Devinez le résultat ? True or False
# À faire : Afficher le résultat
résultat = 0.2 + 0.1 == 0.3

# La comparaison de 'float' n'est pas recommandé, utilisez plutot cette methode
# Au lieu de vérifier si les valeurs sont égales, regardez si leur soustraction sont proche de zéros
# print(abs((0.2 + 0.1) - 0.3) < EPSILON)

# Devinez le résultat ? True or False
# print(1e16 + 1 == 1e16)
# print(int(1e16) + 1 == 1e16)
# print(int(1e16) + 1.0 == 1e16)


# --------------------------------- #


section('Attention à l\'ordre des opérations')
a, b, c, d, e = 5, -6, 4, -1, 2
print(a - b + c // 2 + d * e)

# Lequel de ces opérations seront égales, quel sera le résultat ?
print(a - b + (c // 2) + d * e)
print(a - b + (c // 2) + (d * e))
print((a - b) + (c // 2) + (d * e))
print(((a - b) + (c // 2)) + (d * e))
print((((a - b) + (c // 2)) + (d * e)))


# --------------------------------- #


section("Convertir des Types de Données")

# Définir une chaîne de caractères représentant un nombre
str_nombre = "123"

# Convertir la chaîne en entier (parfois nommé casting / cast)
int_nombre = int(str_nombre)
print(f"Le nombre entier est: {int_nombre}")

# Convertir un nombre flottant en entier
float_nombre = 45.67
int_flottant = int(float_nombre)
print(f"Le nombre entier à partir du flottant est: {int_flottant}")

# Convertir un entier en chaîne (essayer de print() le résultat)
str_nombre = str(int_nombre)
# Convertir un int en float
float_nombre = float(int_nombre)
# Convertir un bool en float
float_nombre = float(True)

# Que sera le résultat ?
# print(str(True), str(False))
# print(int(True), int(False))
# print(float(17), float(0))





# --------------------------------- #


section("Calculer le Périmètre d'un Cercle")

import math # À venir plus tard

# Définir le rayon du cercle
rayon = 7

# Calculer le périmètre
perimetre = 2 * math.pi * rayon

# Afficher le périmètre
print(f"Le périmètre du cercle est: {perimetre}")


# --------------------------------- #


section("Vérifier si une Chaîne Contient un Mot")

# Définir une chaîne de caractères
phrase = "Python est génial"

# Vérifier si la chaîne contient le mot "génial"
contient_genial = "génial" in phrase
print(f"La phrase contient 'génial': {contient_genial}")

# Vérifier si la chaîne contient le mot "difficile"
contient_difficile = "difficile" in phrase
print(f"La phrase contient 'difficile': {contient_difficile}")


# --------------------------------- #


section("Comparer Deux Nombres")

# Définir deux nombres
a = 15
b = 20

# Comparer les nombres et afficher les résultats
print(f"{a} est plus grand que {b}: {a > b}")
print(f"{a} est plus petit que {b}: {a < b}")
print(f"{a} est égal à {b}: {a == b}")


# --------------------------------- #


section("Calcul de l'Aire d'un Rectangle")

# Définir les dimensions du rectangle
longueur = 10
largeur = 5

# Calculer l'aire
aire = longueur * largeur

# Afficher l'aire
print(f"L'aire du rectangle est: {aire}")


# --------------------------------- #


section("Utilisation de Fonctions et Variables Booléennes")

# Utiliser la fonction et afficher le résultat
nombre = 4
is_pair = nombre % 2 == 0
print(f"{nombre} est pair: {is_pair}")

# Tester avec un autre nombre
nombre = 7
is_pair = nombre % 2 == 0
print(f"{nombre} est pair: {is_pair}")


# --------------------------------- #




