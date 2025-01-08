#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


def section(text):
    print('\033[1m{}\033[0m'.format(text))


# ### Introduction aux Sets en Python
# 
# Les sets (ensembles) sont des collections non ordonnées d'éléments uniques. Ils sont utiles pour stocker des éléments sans doublons et pour effectuer des opérations mathématiques telles que l'union, l'intersection et la différence. Voici une courte introduction à leur utilité, leur création et leurs utilisations en Python.
# 
# #### Utilité des Sets
# 
# - **Éléments Uniques** : Les sets ne contiennent pas de doublons, ce qui est utile pour garantir l'unicité des éléments dans une collection.
# - **Opérations Mathématiques** : Les sets permettent d'effectuer des opérations telles que l'union, l'intersection et la différence, qui sont couramment utilisées en mathématiques et en traitement de données.
# - **Recherche Efficace** : La recherche d'éléments dans un set est généralement plus rapide que dans une liste en raison de la manière dont les sets sont implémentés.
# 
# #### Créer un Set
# 
# Les sets sont créés en utilisant des accolades `{}` ou la fonction `set()`.

# --------------------------------- #


section('Créer un Set')

# Créer un set avec des accolades
mon_set = {1, 2, 3, 4, 5}
print("Mon set:", mon_set)

# Créer un set en utilisant la fonction set()
mon_set_vide = set()
print("Set vide:", mon_set_vide)


# --------------------------------- #


section('Ajouter des Éléments à un Set')

mon_set = {1, 2, 3}
mon_set.add(4)
print("Set après ajout de 4:", mon_set)

# Ajouter un élément déjà présent n'aura pas d'effet (pas de doublons)
mon_set.add(2)
print("Set après ajout de 2 (déjà présent):", mon_set)


# --------------------------------- #


section('Vérifier la Présence d\'un Élément')

print(3 in mon_set)  # True
print(5 in mon_set)  # False


# --------------------------------- #


section('Supprimer des Éléments')

mon_set.remove(2)
print("Set après suppression de 2:", mon_set)

# Utiliser discard() pour éviter l'erreur si l'élément n'existe pas
mon_set.discard(10)  # Ne fait rien car 10 n'est pas dans le set
print("Set après tentative de suppression de 10:", mon_set)


# --------------------------------- #


section('Opération booléenne sur les Sets')

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union de Sets
union_set = set1 | set2
print("Union de set1 et set2:", union_set)

# Différence de Sets
difference_set = set1 - set2
print("Différence de set1 et set2:", difference_set)

# Intersection de Sets
intersection_set = set1 & set2
print("Intersection de set1 et set2:", intersection_set)



# --------------------------------- #




