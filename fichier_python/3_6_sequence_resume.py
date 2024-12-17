#!/usr/bin/env python
# coding: utf-8

# ### Résumé des Séquences Itérables en Python
# 
# Les séquences itérables en Python sont des collections d'éléments ordonnées qui permettent de parcourir les éléments un par un. Les principales séquences itérables en Python sont les listes, les tuples, les sets, et les dictionnaires. Chacune a ses caractéristiques et ses usages spécifiques. Voici un résumé de leurs différences et des situations appropriées pour les utiliser.
# 
# ---
# 
# #### Listes
# 
# - **Caractéristiques** : 
#   - Mutables (leurs éléments peuvent être modifiés après la création).
#   - Ordonnées (les éléments ont un ordre défini et peuvent être accédés par leur index).
#   - Permettent les éléments en double.
# - **Utilisation Appropriée** :
#   - Lorsque vous avez besoin d'une collection de données modifiable.
#   - Pour stocker des éléments en double.
#   - Pour accéder rapidement aux éléments par leur index.
# - **Situations Non Appropriées** :
#   - Lorsque l'immuabilité est nécessaire.
#   - Pour des recherches extrêmement rapides, où un set pourrait être plus approprié.
# 
# ---
# 
# #### Tuples
# 
# - **Caractéristiques** :
#   - Immutables (leurs éléments ne peuvent pas être modifiés après la création).
#   - Ordonnés (les éléments ont un ordre défini et peuvent être accédés par leur index).
#   - Permettent les éléments en double.
# - **Utilisation Appropriée** :
#   - Lorsque vous avez besoin d'une collection de données non modifiable.
#   - Pour les données constantes qui ne doivent pas être changées.
#   - Lorsque vous voulez utiliser des tuples comme clés dans un dictionnaire (les clés doivent être immuables).
# - **Situations Non Appropriées** :
#   - Lorsque vous avez besoin de modifier les éléments après la création.
#   - Pour des collections de données très dynamiques.
# 
# ---
# 
# #### Sets
# 
# - **Caractéristiques** :
#   - Mutables (leurs éléments peuvent être modifiés après la création), mais leurs éléments doivent être immuables.
#   - Non ordonnés (les éléments n'ont pas d'ordre défini et ne peuvent pas être accédés par leur index).
#   - Ne permettent pas les éléments en double (chaque élément est unique).
# - **Utilisation Appropriée** :
#   - Lorsque vous avez besoin d'une collection d'éléments uniques.
#   - Pour les opérations mathématiques comme l'union, l'intersection et la différence.
#   - Pour des recherches rapides d'existence d'éléments.
# - **Situations Non Appropriées** :
#   - Lorsque l'ordre des éléments est important.
#   - Pour des collections où des éléments en double sont nécessaires.
# 
# ---
# 
# #### Dictionnaires
# 
# - **Caractéristiques** :
#   - Mutables (leurs paires clé-valeur peuvent être modifiées après la création).
#   - Non ordonnés jusqu'à Python 3.7 (à partir de Python 3.7, les dictionnaires maintiennent l'ordre d'insertion des éléments).
#   - Ne permettent pas les clés en double (chaque clé est unique, mais les valeurs peuvent être dupliquées).
#   - Permettent des accès rapides aux valeurs via les clés.
# - **Utilisation Appropriée** :
#   - Lorsque vous avez besoin d'associer des paires clé-valeur.
#   - Pour des recherches rapides basées sur les clés.
#   - Pour structurer des données de manière plus complexe, comme des configurations ou des enregistrements.
# - **Situations Non Appropriées** :
#   - Lorsque vous avez seulement besoin d'une simple liste de valeurs sans clé associée.
#   - Pour des collections de données où des clés en double sont nécessaires.
# 
# ---
# 
# ### Conclusion
# 
# Choisir la bonne séquence itérable dépend de la nature des données et des opérations que vous devez effectuer sur elles. Les listes sont flexibles et polyvalentes pour la plupart des besoins généraux. Les tuples sont parfaits pour les collections de données immuables. Les sets sont optimaux pour les collections d'éléments uniques et les opérations mathématiques. Les dictionnaires sont idéaux pour les paires clé-valeur et les recherches rapides. Comprendre ces caractéristiques vous permet de choisir la structure de données la plus appropriée pour chaque situation.

# --------------------------------- #


# Les séquences itérables en Python (listes, tuples, sets, str, peuvent être converties
# les unes en les autres en utilisant les fonctions de conversion intégrées.
#  Voici comment effectuer ces conversions

# Liste d'exemple
ma_liste = ["a", "b", "c", "d", "e", "e", "d", "c", "b", "a"]

# Vers Tuple
mon_tuple = tuple(ma_liste)
print("Liste vers Tuple:", mon_tuple)

# Vers Set
mon_set = set(ma_liste)
print("Liste vers Set:", mon_set)

# Combien de "a" sont dans la liste et dans le set ? Pourquoi ?

# Vers Chaîne
ma_chaine = ' '.join(ma_liste)
print("Liste vers Chaîne:", ma_chaine)


# --------------------------------- #


# Tuple d'exemple
mon_tuple = (1, 2, 3, 4)

# Vers Liste
ma_liste = list(mon_tuple)
print("Tuple vers Liste:", ma_liste)

# Vers Set
mon_set = set(mon_tuple)
print("Tuple vers Set:", mon_set)

# Vers Chaîne
# ma_chaine = ' '.join(mon_tuple) # Ne fonctionne pas, pourquoi ?
ma_chaine = ' '.join(map(str, mon_tuple))
print("Tuple vers Chaîne:", ma_chaine)

# Map permet d'appliquer une fonction à chaque élément d'une séquence (magie de Python)
# On verra peut-être cela plus tard


# --------------------------------- #


# Chaîne d'exemple
ma_chaine = "1234"

# Vers Liste
ma_liste = list(ma_chaine)
print("Chaîne vers Liste:", ma_liste)

# Vers Tuple
mon_tuple = tuple(ma_chaine)
print("Chaîne vers Tuple:", mon_tuple)

# Vers Set
mon_set = set(ma_chaine)
print("Chaîne vers Set:", mon_set)

# À faire : convertir un set en liste, tuple et chaîne de caractères

