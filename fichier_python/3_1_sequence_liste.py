#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


def section(text):
    print('\033[1m{}\033[0m'.format(text))


# --------------------------------- #


section('Créer et Identifier une Liste')

# Créer une liste de nombres
ma_liste = [1, 2, 3, 4, 5]

# Utiliser type() pour vérifier le type de la variable
print("Type de ma_liste:", type(ma_liste))

# Utiliser len() pour obtenir la longueur de la liste
print("Longueur de ma_liste:", len(ma_liste))


# --------------------------------- #


section('Accéder aux Éléments d\'une Liste')

# Créer une liste de fruits
fruits = ["pomme", "banane", "cerise"]

# Accéder au premier élément
print("Premier fruit:", fruits[0])

# Accéder au deuxième élément
print("Deuxième fruit:", fruits[1])

# Accéder au dernier élément
print("Dernier fruit:", fruits[-1])


# --------------------------------- #


section('Utiliser if/else avec des Listes')

# Créer une liste de nombres
nombres = [5, 15, 25, 35, 45]

# Vérifier si le premier élément est supérieur à 10
if nombres[0] > 10:
    print("Le premier nombre est supérieur à 10")
else:
    print("Le premier nombre est inférieur ou égal à 10")


# --------------------------------- #


section('Utiliser une Boucle While pour Parcourir une Liste')

# Créer une liste de nombres
nombres = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# Initialiser un index
i = 0

# Utiliser une boucle while pour parcourir et imprimer chaque élément
while i < len(nombres):
    print("Nombre à l'index", i, ":", nombres[i])
    i += 1


# --------------------------------- #


section('Listes avec Différents Types d\'Éléments')

# Créer une liste avec des types différents
elements_mixes = [1, "Bonjour", 3.14, True, ["a", "b", "c"], 5, 10]

# Utiliser une boucle while pour parcourir et imprimer chaque élément et son type
i = 0
while i < len(elements_mixes):
    print(f"Élément à l'index {i}: {elements_mixes[i]} (type: {type(elements_mixes[i])})")
    if isinstance(elements_mixes[i], int) or isinstance(elements_mixes[i], float):
        print("  Est un nombre!")
    i += 1


# --------------------------------- #


section('Modifier les Éléments d\'une Liste avec une Boucle While')

# Créer une liste de nombres
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialiser un index
i = 0

# Utiliser une boucle while pour parcourir la liste
while i < len(nombres):
    if nombres[i] % 2 == 0:
        # Si le nombre est pair, mettre True
        nombres[i] = True
    else:
        # Si le nombre est impair, mettre False
        nombres[i] = False
    i += 1

# Imprimer la liste après modifications
print("Liste après modifications:", nombres)


# --------------------------------- #


section('Fonctions Utiles pour les Listes')

# Créer une liste d'exemple
ma_liste = [3, 6, 1, 9, 6, 3, 8, 6]

# Ajouter un élément à la fin de la liste
ma_liste.append(10)
print("Liste après append(10):", ma_liste)

# Supprimer et retourner le dernier élément de la liste
dernier_element = ma_liste.pop()
print("Dernier élément après pop():", dernier_element)
print("Liste après pop():", ma_liste)

# Supprimer la première occurrence d'un élément
ma_liste.remove(6)
print("Liste après remove(6):", ma_liste)

# Trouver l'index de la première occurrence d'un élément
index_de_3 = ma_liste.index(3)
print("Index de la première occurrence de 3:", index_de_3)

# Compter le nombre d'occurrences d'un élément
nombre_de_6 = ma_liste.count(6)
print("Nombre d'occurrences de 6:", nombre_de_6)

# Trier la liste en ordre croissant
ma_liste.sort()
print("Liste après sort():", ma_liste)

# Inverser l'ordre des éléments de la liste
ma_liste.reverse()
print("Liste après reverse():", ma_liste)

