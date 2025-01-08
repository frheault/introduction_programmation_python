#!/usr/bin/env python
# coding: utf-8

# # Comment naviguer ?
# Chaque cellule contient soit du texte, soit du code. Il est toujours important d'exécuter les cellules dans l'ordre. Pour se faire, cliquer sur la première contenant du code plus bas et cliquer sur le symbole 'Play' (triangle) pour exécuter la cellule.
# 
# Je vous suggère d'exécuter les cellules les unes après les autres, et de modifier le code lorsqu'un commentaire indique qu'il est important de modifier le code pour mieux comprendre.
# 
# La fonction **print** est crucial pour afficher des résultats, je vais l'expliquer en détails plus tard. Pour l'instant voyez **les utilisations de la fonction **print** comme une façon de voir le résultat d'un calcul pour faciliter le suivi des opérations. Une autre fonction est utile pour l'apprentissage, **type** permet de connaitre la représentation interne d'une variable (à venir)

# --------------------------------- #


# Ceci est utile simplement pour l'affichage, exécuter en premier
def section(text):
    print('\033[1m{}\033[0m'.format(text))

section('Test Affichage')
print('Ceci est un test !')


# --------------------------------- #


section('Opérations de base')
# En python les lignes commencant par # seront des commentaires (simple texte, pas réellement du code
# En Python toute les opérations de base d'une calculatrice sont possibles 
print(10 + 4)
print(10 - 4)
print(10 * 4)
print(10 ** 4) # Exposant
print(10 / 4)
print(10 // 4) # Division entière
print(10 % 4) # Modulo (reste d'une division entière


# --------------------------------- #


section('Variables')
# L'opérateur = permet de créer une nouvelle variable qui sera réutilisable (initialiser, instancier, déclarer) 
x = 10
y = 4

# On peut afficher plus d'une variable à la fois avec la fonction print()
print(x, y)

# On peut aussi voir la représentation interne de la variable avec la fonction type()
print(type(x), type(y))
# On voit que les variables x et y sont des 'int' pour integer (entier)

# À faire: Changer les valeurs de x et y pour des valeurs de votre choix


# --------------------------------- #


section('Opérations de base avec des variables')

# On peut utiliser les variables pour faires des opérations, comme avec une calculatrice
print(x + y)
print(x - y)
print(x * y)
print(x ** y)
print(x / y)
print(x // y)
print(x % y)


# --------------------------------- #


# Les types des variables n'est pas toujours le même que le résultat d'une opération les utilisants
# Ici je crée une nouvelle variable (z) et je lui assigne une valeur suivant une opération simple
z = (2 * x) + y
print(z, type(z))

# Ici, en réutilisant z je vais remplacer sa valeur par une nouvelle (overwrite)
z = (2 * x) / y
print(z, type(z))

# Comme vous le voyez 24 est un entier et 5.0 est un 'float' pour floating point (nombre à virgule flottante, réel)


# --------------------------------- #


section('Suivre les valeurs des variables')
# Attention les valeurs des variables peuvent évoluer (un peu comme réutiliser z dans le bloc précédent)

ma_variable = 17
print(ma_variable)

# Je peux réutiliser une variable pour faire un calcul et remplacer sa valeur antérieur
ma_variable = ma_variable - 1
print(ma_variable)

# En python, la ligne suivante permet de remplacer une variable de façon concise
ma_variable -= 1 # identifique à : ma_variable = ma_variable - 1
print(ma_variable)

# À faire : Essayer les opérateurs +=, -=, *=, /= ou **=


# --------------------------------- #


# Il est toujours important d'être capable de suivre les valeurs de nos variables

a = 1
b = 5

a += 1
b -= 1
c = (a ** b) - 10.0

# À faire : Tentez de deviner les valeurs finales de a, b, c
# À faire : Utiliser la fonction print() pour afficher les valeurs de a, b, c
# À faire : Utiliser la fonction print() et type() pour déterminer si c sera un entier ou un nombre réel

