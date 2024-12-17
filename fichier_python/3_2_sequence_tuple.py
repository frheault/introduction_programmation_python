#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


def section(text):
    print('\033[1m{}\033[0m'.format(text))


# ### Introduction aux Séquences (Itérables) : Listes vs Tuples en Python
# 
# Les listes et les tuples sont deux types de séquences en Python. Ils partagent de nombreuses similitudes, mais il existe des différences importantes entre eux. Voici des exemples concrets pour introduire les tuples, en comparant avec les listes.
# 
# #### Différences Clés
# 
# - **Listes** : Mutables (peuvent être modifiées), définies avec des crochets `[ ]`.
# - **Tuples** : Immutables (ne peuvent pas être modifiés après leur création), définis avec des parenthèses `( )`.
# 

# --------------------------------- #


section('Créer et Identifier une Liste et un Tuple')

# Créer une liste de nombres
ma_liste = [1, 2, 3, 4, 5]
# Créer un tuple de nombres
mon_tuple = (1, 2, 3, 4, 5)

# Utiliser type() pour vérifier le type de la variable
print("Type de ma_liste:", type(ma_liste))
print("Type de mon_tuple:", type(mon_tuple))

# Utiliser len() pour obtenir la longueur de la liste et du tuple
print("Longueur de ma_liste:", len(ma_liste))
print("Longueur de mon_tuple:", len(mon_tuple))


# --------------------------------- #


section('Accéder aux Éléments d\'une Liste et d\'un Tuple')

# Créer une liste de fruits
fruits_liste = ["pomme", "banane", "cerise"]
# Créer un tuple de fruits
fruits_tuple = ("pomme", "banane", "cerise")

# Accéder au premier élément
print("Premier fruit (liste):", fruits_liste[0])
print("Premier fruit (tuple):", fruits_tuple[0])

# Accéder au dernier élément
print("Dernier fruit (liste):", fruits_liste[-1])
print("Dernier fruit (tuple):", fruits_tuple[-1])


# --------------------------------- #


section('Utiliser une Boucle While pour Parcourir une Liste et un Tuple')

nombres_tuple = (10, 20, 30, 40, 50)

# Initialiser l'index
i = 0

# Utiliser une boucle while pour parcourir et imprimer chaque élément du tuple
print("Éléments du tuple:")
while i < len(nombres_tuple):
    print("Nombre à l'index", i, ":", nombres_tuple[i])
    i += 1

# Est-ce qu'il y a une différence entre une liste et un tuple lorsqu'on les parcourt avec une boucle while?


# --------------------------------- #


section('Ajouter des Éléments à une Liste et Tentative avec un Tuple')

# Créer une liste vide
ma_liste = []

# Ajouter des éléments à la liste
ma_liste.append(10)
ma_liste.append(20)
ma_liste.append(30)

# Imprimer la liste après les ajouts
print("Liste après ajouts:", ma_liste)

# Créer un tuple
mon_tuple = (10, 20, 30)

# Tenter d'ajouter un élément au tuple (ceci provoquera une erreur)
# Utiliser try/except pour gérer l'erreur (Sera expliquer dans un prochain cours)
try:
    mon_tuple.append(40)
except AttributeError as e:
    print("Erreur:", e)


# --------------------------------- #


section('Immutabilité des Tuples')

# Créer un tuple de nombres
nombres_tuple = (1, 2, 3, 4, 5)

# Tentative de modifier un élément du tuple (ceci provoquera une erreur)
try:
    nombres_tuple[1] = 10
except TypeError as e:
    print("Erreur:", e)


# --------------------------------- #


section('Fonctions Utiles pour les Tuples')

# Créer un tuple d'exemple
mon_tuple = (3, 6, 1, 9, 6, 3, 8, 6)

# Trouver l'index de la première occurrence d'un élément
index_de_3 = mon_tuple.index(3)
print("Index de la première occurrence de 3 dans le tuple:", index_de_3)

# Compter le nombre d'occurrences d'un élément
nombre_de_6 = mon_tuple.count(6)
print("Nombre d'occurrences de 6 dans le tuple:", nombre_de_6)

# Concaténation de tuples
autre_tuple = (10, 11)
nouveau_tuple = mon_tuple + autre_tuple
print("Tuple après concaténation:", nouveau_tuple)

# Déballage de tuple
a, b, c, d, e, f, g, h = mon_tuple
print("Déballage du tuple:", a, b, c, d, e, f, g, h)

