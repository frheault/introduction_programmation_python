#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


def section(text):
    print('\033[1m{}\033[0m'.format(text))


# ### Les Dictionnaires en Python
# 
# #### Concept
# 
# Les dictionnaires sont des structures de données en Python qui stockent des paires clé-valeur. Chaque élément d'un dictionnaire est constitué d'une clé unique associée à une valeur. Les clés peuvent être de n'importe quel type immuable (comme des chaînes de caractères, des nombres, ou des tuples), tandis que les valeurs peuvent être de n'importe quel type. Les dictionnaires sont définis à l'aide des accolades `{}`.
# 
# #### Utilisation
# 
# Les dictionnaires sont particulièrement utiles pour les situations où vous devez associer des éléments entre eux, par exemple pour stocker des informations sur des étudiants (nom, âge, cours), des produits (nom, prix, quantité), ou tout autre ensemble de données où chaque élément peut être identifié de manière unique par une clé. Ils permettent une recherche rapide et une gestion efficace des données.
# 
# #### Avantages
# 
# 1. **Accès Rapide** : Les dictionnaires offrent un accès rapide aux valeurs en utilisant les clés. La recherche, l'insertion et la suppression d'éléments sont généralement très rapides grâce à l'implémentation sous-jacente basée sur des tables de hachage.
# 
# 2. **Flexibilité** : Les valeurs dans un dictionnaire peuvent être de n'importe quel type, y compris des listes, des tuples, ou même d'autres dictionnaires, ce qui permet de créer des structures de données complexes.
# 
# 3. **Clarté du Code** : En utilisant des paires clé-valeur, les dictionnaires rendent le code plus lisible et facile à comprendre, car les clés décrivent clairement le rôle des valeurs associées.
# 

# --------------------------------- #


section('Création d\'un Dictionnaire')

# Créer un dictionnaire vide
mon_dictionnaire = {}

# Créer un dictionnaire avec des paires clé-valeur
info_etudiant = {
    "nom": "Alice",
    "âge": 23,
    "cours": ["Math", "Physique", "Informatique"]
}

print("Dictionnaire:", info_etudiant)

# Quel est la différence entre la création d'un set et d'un dictionnaire?


# --------------------------------- #


section('Ajouter et Modifier des Paires Clé-Valeur')

# Ajouter une nouvelle paire clé-valeur
info_etudiant["ville"] = "Montréal"
print("Après ajout:", info_etudiant)

# Modifier une valeur existante
info_etudiant["âge"] = 24
print("Après modification:", info_etudiant)


# --------------------------------- #


section('Méthodes Utiles : items(), keys(), values()')

# Obtenir les paires clé-valeur
items = info_etudiant.items()
print("Paires clé-valeur:", items)

# Obtenir les clés
cles = info_etudiant.keys()
print("Clés:", cles)

# Obtenir les valeurs
valeurs = info_etudiant.values()
print("Valeurs:", valeurs)


# --------------------------------- #


section('Vérifier la Présence d\'une Clé')

# Vérifier si une clé existe dans le dictionnaire
if "nom" in info_etudiant:
    print("La clé 'nom' existe dans le dictionnaire")

if "adresse" not in info_etudiant:
    print("La clé 'adresse' n'existe pas dans le dictionnaire")

# Utiliser la méthode get() pour éviter une erreur si la clé n'existe pas
adresse = info_etudiant.get("adresse")
print("Adresse:", adresse)

# À faire: Essayer d'accéder à une clé qui n'existe pas sans utiliser get()


# --------------------------------- #


section('Fonctions Utiles pour les Dictionnaires')

dictionnaire = {"nom": "Alice", "âge": 23}
mise_a_jour = {"âge": 24, "ville": "Montréal"}
dictionnaire.update(mise_a_jour)
print(dictionnaire)  # {'nom': 'Alice', 'âge': 24, 'ville': 'Montréal'}

dictionnaire = {"nom": "Alice", "âge": 23}
# Supprimer une clé existante
age = dictionnaire.pop("âge")
print(age)  # 23
print(dictionnaire)  # {'nom': 'Alice'}
# Que ce passe-t-il dans cette opération?

# Supprimer une clé inexistante avec une valeur par défaut
ville = dictionnaire.pop("ville", "Non disponible")
print(ville)  # Non disponible

dictionnaire = {"nom": "Alice", "âge": 23}
mise_a_jour = {"âge": 24, "ville": "Montréal"}
dictionnaire.update(mise_a_jour)
print(dictionnaire)  # {'nom': 'Alice', 'âge': 24, 'ville': 'Montréal'}

# Que se passe-t-il si on utilise la méthode update() avec un dictionnaire vide?
# Et avec un dictionnaire ayant des clés différentes?

