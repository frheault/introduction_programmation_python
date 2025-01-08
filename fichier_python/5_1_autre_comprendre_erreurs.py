#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


def section(text):
    print('\033[1m{}\033[0m'.format(text))


# ### Introduction aux Erreurs, Stack Traces et Débogage pour les Novices en Programmation
# 
# #### Erreurs en Programmation
# 
# Les erreurs, ou exceptions, sont des problèmes qui surviennent lors de l'exécution d'un programme. Elles peuvent être causées par des fautes de syntaxe, des erreurs logiques ou des problèmes imprévus, comme des valeurs inattendues ou des conditions non gérées. Comprendre et résoudre ces erreurs est une compétence essentielle pour tout programmeur.
# 
# #### Types d'Erreurs
# 
# 1. **Erreurs de Syntaxe** : 
#    - Causées par des violations des règles de la syntaxe du langage (par exemple, des parenthèses manquantes).
#    - Faciles à identifier car elles empêchent le code de s'exécuter.
#    
# 2. **Erreurs d'Exécution (Runtime Errors)** :
#    - Se produisent lorsque le programme s'exécute et que quelque chose de non prévu survient (par exemple, division par zéro).
#    - Plus difficiles à détecter avant l'exécution du code.
# 
# 3. **Erreurs Logiques** :
#    - Le programme s'exécute sans erreurs, mais le résultat n'est pas celui attendu.
#    - Causées par une logique incorrecte dans le code.
# 
# #### Comprendre les Stack Traces
# 
# Une stack trace est un rapport détaillé généré lorsque une erreur d'exécution se produit. Elle montre la séquence d'appels de fonctions qui ont conduit à l'erreur. Les éléments clés d'une stack trace incluent :
# 
# 1. **Le Message d'Erreur** : Indique le type d'erreur (par exemple, `TypeError`, `ValueError`) et une description de l'erreur.
# 2. **La Liste des Appels de Fonctions** : Montre chaque appel de fonction qui a conduit à l'erreur, en commençant par la plus récente. Chaque entrée inclut le fichier, le numéro de ligne, et le nom de la fonction.
# 
# #### Trucs pour Régler les Erreurs
# 
# 1. **Lire le Message d'Erreur** :
#    - Comprenez ce que le message d'erreur indique. Il fournit souvent des indices sur ce qui a mal tourné.
# 
# 2. **Analyser la Stack Trace** :
#    - Remontez la trace pour voir où l'erreur a commencé. Identifiez le fichier et la ligne de code responsables.
# 
# 3. **Reproduire l'Erreur** :
#    - Essayez de recréer l'erreur pour comprendre quelles conditions la déclenchent. Cela peut aider à isoler le problème.
# 
# 4. **Ajouter des Impressions (print) ou des Logs** :
#    - Utilisez des déclarations `print` ou des outils de journalisation pour afficher les valeurs des variables et le flux du programme. Cela peut aider à identifier où le code ne fonctionne pas comme prévu.
# 
# 5. **Simplifier le Code** :
#    - Réduisez le code à un exemple minimal qui reproduit l'erreur. Cela rend le débogage plus facile.

# #### 1. Erreur de Syntaxe : (SyntaxError)
# 
# **Exemple** : Oublier les deux-points après une déclaration de condition `if`.
# 
# ```python
# 
# if True # SyntaxError:
#     print("Réussi !")
# ```
# 
# ---
# 
# **Exemple** : Oublier les deux-points après une déclaration de fonction `def`.
# 
# ```python
# 
# 
# def saluer()
#     print("Bonjour")
# ```
# 
# ---
# 
# **Exemple** : Oublier les deux-points après une déclaration de boucle `for`.
# 
# ```python
# 
# for i in range(5)
#     print(i)
# ```

# --------------------------------- #


# À faire : Corriger les (3) erreurs ci-dessus


# #### 2. Erreur de Syntaxe () [] {}  "" '' (SyntaxError)
# 
# **Exemple** : Apostrophe incorrecte dans une chaîne de caractères.
# 
# ```python
# 
# texte = 'Ceci est une erreur"
# print(texte)
# ```
# 
# ---
# 
# **Exemple** : Parenthèses non fermés pour une fonction.
# 
# ```python
# 
# mot = "Sherbrooke"
# longeur = len(mot
# print(longueur)
# ```
# 
# ---
# 
# **Exemple** : Crochets non fermés pour une liste.
# 
# ```python
# 
# ma_liste = [1, 2, 3, 4, 5
# ```

# --------------------------------- #


# À faire : Corriger les (3) erreurs ci-dessus


# 
# #### 3. Erreur de Type (TypeError)
# 
# **Exemple** : Essayer d'ajouter une chaîne de caractères à un nombre.
# 
# ```python
# 
# nombre = 5
# texte = "Le nombre est: "
# print(texte + nombre)  # TypeError: can only concatenate str (not "int") to str
# ```
# 
# ---
# 
# **Exemple** : Utiliser `input()` sans caster en `float` ou `int`.
# 
# ```python
# 
# valeur = input("Entrez un nombre : ")
# resultat = valeur ** 2
# print(resultat)
# ```
# 
# ---
# 
# **Exemple** : Essayer de convertir une chaîne de caractères non numérique en nombre.
# 
# ```python
# 
# texte = "dix"
# nombre = int(texte)  # ValueError: invalid literal for int() with base 10: 'dix'
# print(nombre)
# ```

# --------------------------------- #


# À faire : Corriger les (3) erreurs ci-dessus


# #### 4. Erreur de Nom (NameError)
# 
# **Exemple** : Utiliser une variable qui n'a pas été définie.
# 
# ```python
# 
# print(variable_inexistante)  # NameError: name 'variable_inexistante' is not defined
# ```
# 
# ---
# 
# **Exemple** : Utiliser une fonction qui n'a pas été définie.
# 
# ```python
# 
# print(addition(17, 3))  # NameError: name 'est_impair' is not defined
# ```
# 

# --------------------------------- #


# À faire : Corriger les (2) erreur ci-dessus


# 
# #### 5. Erreur d'Index (IndexError)
# 
# **Exemple** : Essayer d'accéder à un index qui est hors de la portée de la liste.
# 
# ```python
# 
# ma_liste = [1, 2, 3]
# print(ma_liste[5])  # IndexError: list index out of range
# # Attendu : Accéder au dernier élément
# ```

# --------------------------------- #


# À faire : Corriger l'erreur ci-dessus


# 
# #### 6. Erreur de Clé (KeyError)
# 
# **Exemple** : Essayer d'accéder à une clé qui n'existe pas dans un dictionnaire.
# 
# ```python
# 
# mon_dictionnaire = {"nom": "Alice"}
# print(mon_dictionnaire["Nom"])  # KeyError: 'Nom'
# ```

# --------------------------------- #


# À faire : Corriger l'erreur ci-dessus


# 
# #### 7. Boucle Infinie
# 
# **Exemple** : Oublier d'incrémenter une variable de contrôle dans une boucle `while`.
# 
# ```python
# 
# i = 0
# while i < 5:
#     print(i)
# ```

# --------------------------------- #


# À faire : Corriger l'erreur ci-dessus


# #### 8. Erreur d'Indentation
# 
# **Exemple** : Mauvaise indentation dans une fonction.
# 
# ```python
# 
# def saluer():
# print("Bonjour")
# 
# saluer()
# ```
# 
# ---
# 
# **Exemple** : Mauvaise indentation dans une boucle `while`.
# 
# ```python
# 
# i = 0
# while i < 5:
# print(i)
#     i += 1
# ```
# 
# ---
# 
# **Exemple** : Mauvaise indentation dans un bloc `if/else`.
# 
# ```python
# 
# x = 10
# if x > 5:
# print("x est supérieur à 5")
# else:
# print("x est inférieur ou égal à 5")
# ```
# 

# --------------------------------- #


# À faire : Corriger les (3) erreurs ci-dessus


# #### 9. Erreur Logique
# 
# **Exemple** : Utiliser une mauvaise condition dans une boucle `for`.
# 
# ```python
# 
# somme = 0
# nombres = [1, 2, 3, 4, 5, -1, 10]
# # Attendu : Si le nombre durant l'itération est négatif, terminer la boucle
# for nombre in nombres:
#     somme += nombre
#     if somme < 0:
#         break
# 
# print("La somme est:", somme)  # La somme devrait être: 15
# ```
# 

# --------------------------------- #


# À faire : Corriger l'erreur ci-dessus


# 
# #### 10. Utilisation Incorrecte de `in` avec des Strings
# 
# **Exemple** : Vérifier une sous-chaîne dans une liste de chaînes, au lieu de vérifier chaque élément.
# 
# ```python
# 
# # Chercher si "on" est présent dans l'une des 3 chaines
# mots = ["bonjour", "salut", "hello"]
# if "on" in mots:
#     print("Sous-chaîne trouvée")
# else:
#     print("Sous-chaîne non trouvée")
# # Attendu : "on" est présent dans "bONjour"
# ```

# --------------------------------- #


# À faire : Corriger l'erreur ci-dessus


# 
