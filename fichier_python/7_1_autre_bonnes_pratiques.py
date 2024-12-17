#!/usr/bin/env python
# coding: utf-8

# #### 1. Nommer les Variables
# 
# **Mauvaise Pratique** : Utiliser des noms de variables non descriptifs.
# 
# ```python
# # Mauvaise pratique
# x = 5
# y = 10
# z = x + y
# print(z)
# ```
# 
# **Bonne Pratique** : Utiliser des noms de variables descriptifs.
# 
# ```python
# # Bonne pratique
# nombre_de_pommes = 5
# nombre_de_bananes = 10
# total_fruits = nombre_de_pommes + nombre_de_bananes
# print(total_fruits)
# ```
# 
# ---
# 
# #### 2. Gestion des Fichiers
# 
# **Mauvaise Pratique** : Ne pas fermer les fichiers après utilisation.
# 
# ```python
# # Mauvaise pratique
# fichier = open('exemple.txt', 'r')
# contenu = fichier.read()
# print(contenu)
# 
# ---
# fichier.close()
# ```
# 
# **Bonne Pratique** : Utiliser les instructions `with` pour garantir la fermeture des fichiers.
# 
# ```python
# # Bonne pratique
# with open('exemple.txt', 'r') as fichier:
#     contenu = fichier.read()
#     print(contenu)
# ```
# 
# ---
# 
# #### 3. Boucles Inefficaces
# 
# **Mauvaise Pratique** : Utiliser des boucles inefficaces pour des tâches simples.
# 
# ```python
# # Mauvaise pratique
# nombres = [1, 2, 3, 4, 5]
# somme = 0
# for nombre in nombres:
#     somme += nombre
# print(somme)
# ```
# 
# **Bonne Pratique** : Utiliser des fonctions intégrées pour des opérations simples.
# 
# ```python
# # Bonne pratique
# nombres = [1, 2, 3, 4, 5]
# somme = sum(nombres)
# print(somme)
# ```
# 
# ---
# 
# #### 4. Gestion des Exceptions
# 
# **Mauvaise Pratique** : Ne pas gérer les exceptions.
# 
# ```python
# # Mauvaise pratique
# def diviser(a, b):
#     return a / b
# 
# print(diviser(10, 0))
# ```
# 
# **Bonne Pratique** : Gérer les exceptions pour éviter les erreurs d'exécution.
# 
# ```python
# # Bonne pratique
# def diviser(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Erreur : division par zero"
# 
# print(diviser(10, 0))
# ```
# 
# ---
# 
# #### 5. Répétition de Code
# 
# **Mauvaise Pratique** : Répéter du code identique à plusieurs endroits.
# 
# ```python
# # Mauvaise pratique
# def aire_carre(cote):
#     return cote * cote
# 
# def aire_rectangle(longueur, largeur):
#     return longueur * largeur
# 
# print(aire_carre(4))
# print(aire_rectangle(4, 5))
# ```
# 
# **Bonne Pratique** : Réutiliser le code en utilisant des fonctions.
# 
# ```python
# # Bonne pratique
# def aire_quadrilatere(longueur, largeur=None):
#     if largeur is None:
#         return longueur * longueur
#     return longueur * largeur
# 
# print(aire_quadrilatere(4))  # Pour un carré
# print(aire_quadrilatere(4, 5))  # Pour un rectangle
# ```
# 
# ---
# 
# #### 6. Commentaires
# 
# **Mauvaise Pratique** : Absence de commentaires ou commentaires inutiles.
# 
# ```python
# # Mauvaise pratique
# a = 5  # Déclare une variable a
# b = 10  # Déclare une variable b
# c = a + b  # Additionne a et b
# print(c)  # Affiche c
# ```
# 
# **Bonne Pratique** : Utiliser des commentaires utiles et pertinents.
# 
# ```python
# # Bonne pratique
# nombre_de_pommes = 5
# nombre_de_bananes = 10
# 
# # Calcule le total de fruits
# total_fruits = nombre_de_pommes + nombre_de_bananes
# print(total_fruits)
# ```
# 
# ---
# 
# #### 7. Hardcoding des Valeurs
# 
# **Mauvaise Pratique** : Utiliser des valeurs codées en dur dans le code.
# 
# ```python
# # Mauvaise pratique
# prix = 100
# taux_de_tva = 0.2
# prix_ttc = prix + (prix * taux_de_tva)
# print(prix_ttc)
# ```
# 
# **Bonne Pratique** : Utiliser des constantes pour les valeurs fixes.
# 
# ```python
# # Bonne pratique
# PRIX = 100
# TAUX_DE_TVA = 0.2
# prix_ttc = PRIX + (PRIX * TAUX_DE_TVA)
# print(prix_ttc)
# ```
# 
# ---
# 
# #### 8. Utilisation de Boucles Plutôt que des Compréhensions de Liste
# 
# **Mauvaise Pratique** : Utiliser des boucles pour créer des listes.
# 
# ```python
# # Mauvaise pratique
# carres = []
# for i in range(10):
#     carres.append(i * i)
# print(carres)
# ```
# 
# **Bonne Pratique** : Utiliser des compréhensions de liste pour créer des listes.
# 
# ```python
# # Bonne pratique
# carres = [i * i for i in range(10)]
# print(carres)
# ```
# 
# ---
# 
# #### 9. Ne Pas Vérifier les Types de Données
# 
# **Mauvaise Pratique** : Ne pas vérifier les types de données des entrées.
# 
# ```python
# # Mauvaise pratique
# def additionner(a, b):
#     return a + b
# 
# print(additionner("10", 5))
# ```
# 
# **Bonne Pratique** : Vérifier les types de données des entrées.
# 
# ```python
# # Bonne pratique
# def additionner(a, b):
#     if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
#         return "Erreur : les arguments doivent etre des nombres"
#     return a + b
# 
# print(additionner("10", 5))
# ```
