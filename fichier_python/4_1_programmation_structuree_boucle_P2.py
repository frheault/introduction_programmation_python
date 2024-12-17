#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


def section(text):
    print('\033[1m{}\033[0m'.format(text))


# ### Résumé des Boucles `while` vs `for` en Python
# 
# #### Boucles `while`
# 
# - **Concept** : La boucle `while` exécute un bloc de code tant qu'une condition spécifiée est vraie. La condition est évaluée avant chaque itération.
# - **Utilisation** : Utilisée lorsque le nombre d'itérations n'est pas connu à l'avance et dépend de la satisfaction d'une condition.
# - **Avantages** :
#   - Flexibilité : Peut être utilisée pour créer des boucles complexes avec des conditions dynamiques.
#   - Contrôle fin : Permet d'intégrer facilement des instructions de contrôle comme `break` pour arrêter la boucle et `continue` pour sauter à l'itération suivante.
# - **Inconvénients** :
#   - Risque de boucles infinies : Si la condition de terminaison n'est jamais satisfaite, la boucle peut devenir infinie.
#   - Moins lisible : Peut devenir difficile à lire et comprendre si les conditions sont complexes.
# 
# #### Boucles `for`
# 
# - **Concept** : La boucle `for` itère sur une séquence (comme une liste, un tuple, un dictionnaire, un set ou une chaîne de caractères) ou un objet itérable, exécutant un bloc de code pour chaque élément.
# - **Utilisation** : Utilisée lorsque le nombre d'itérations est connu à l'avance ou lorsqu'il s'agit d'itérer sur une collection d'éléments.
# - **Avantages** :
#   - Simplicité et lisibilité : Le code est généralement plus simple et plus lisible pour les itérations sur des séquences.
#   - Moins de risque de boucles infinies : Comme elle itère sur une séquence définie, il y a moins de risque de créer des boucles infinies.
#   - Compatibilité avec les collections : Optimisée pour les opérations sur les collections de données, avec des structures de contrôle intégrées pour chaque élément.
# - **Inconvénients** :
#   - Moins flexible : Moins adaptée pour les boucles où la condition de terminaison dépend de calculs ou de conditions dynamiques.
#   - Moins de contrôle : Moins de flexibilité pour intégrer des conditions dynamiques au sein de la boucle par rapport à `while`.
# 
# #### Comparaison et Choix
# 
# - **Quand utiliser `while`** :
#   - Lorsque le nombre d'itérations dépend d'une condition dynamique.
#   - Lorsque vous avez besoin de répéter une action jusqu'à ce qu'une certaine condition soit remplie.
#   - Pour des boucles complexes avec plusieurs conditions de terminaison.
# 
# - **Quand utiliser `for`** :
#   - Lorsque vous devez itérer sur une séquence d'éléments connue à l'avance.
#   - Pour des opérations simples et répétitives sur des collections de données.
#   - Lorsque la lisibilité et la simplicité du code sont prioritaires.
# 
# ### Conclusion
# 
# Les boucles `while` et `for` sont des outils essentiels en programmation, chacun ayant ses propres avantages et inconvénients. Les boucles `while` offrent plus de flexibilité pour les conditions dynamiques et les itérations non déterministes, tandis que les boucles `for` sont optimisées pour la simplicité et la lisibilité lors de l'itération sur des séquences. Choisir la bonne boucle dépend du contexte et des besoins spécifiques de votre programme.

# --------------------------------- #


section('Parcourir une liste d\'éléments')

fruits = ["pomme", "banane", "cerise"]
# Ici au lieu de créer une variable i pour parcourir la liste,
# on parcourt directement les éléments de la liste

for fruit in fruits:
    print(fruit) # Ne pas oublier l'indentation du bloc (comme if/else et while)

# Ici pour rester clair, on utilise le nom de la liste au pluriel
# pour indiquer qu'on parcourt une liste d'éléments.
# La variable fruit (singulier) contient un élément de la liste durant l'itération (bloc)


# --------------------------------- #


section('Utiliser range() pour itérer sur une série de nombres')

# Si on veut faire la somme de 1 à 5 avec un for (plutot qu'un while)
intervalle = [1, 2, 3, 4, 5]
somme = 0
for i in intervalle:
    somme += i
print(somme)

# Imaginer la longueur de la liste si on veut faire la somme de 1 à 1000 !
# On peut utiliser la fonction range() pour générer une série de nombres
somme = 0
for i in range(1,1000):
    somme += i
print(somme)


# --------------------------------- #


section('Parcourir les clés et valeurs d\'un dictionnaire')

info_etudiant = {
    "nom": "Alice",
    "âge": 23,
    "ville": "Montréal"
}
for cle, valeur in info_etudiant.items():
    print(f"{cle}: {valeur}")


# --------------------------------- #


section('Utilisation avancée avec une liste')

fruits = ["pomme", "banane", "cerise"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# On peut aussi utiliser la fonction enumerate() pour obtenir l'index et la valeur
# d'une liste en même temps

fruits = ["pomme", "banane", "cerise"]
couleurs = ["rouge", "jaune", "rouge"]

for index in range(len(fruits)):
    fruit = fruits[index]
    couleur = couleurs[index]
    print(f"Index {index}: {fruit} ({couleur})")

# On peut aussi utiliser la fonction range() pour obtenir l'index
# et la valeur de plusieurs listes en même temps


# --------------------------------- #


section('Utilisation avec une chaîne de caractères')

mot = "Python"
for index, lettre in enumerate(mot):
    print(f"Index {index}: {lettre}")

# Imaginer vouloir trouver la position de la lettre 'h' dans le mot 'Python'
position = mot.index('h')
print(f"La lettre 'h' est à la position {position}")

# On peut aussi utiliser la fonction enumerate() pour obtenir l'index et la valeur
# d'une chaîne de caractères en même temps
position = None
for index, lettre in enumerate(mot):
    if lettre == 'h':
        position = index
        break
print(f"La lettre 'h' est à la position {position}")

# Il y a plusieurs façons de faire la même chose en programmation !

