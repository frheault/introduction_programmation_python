#!/usr/bin/env python
# coding: utf-8

# ### Bonnes Pratiques
# 
# - L'utilisation de `#` permet d'écrire un commentaire sur une ligne.
# - L'utilisation de `""" """` permet d'écrire un commentaire sur plusieurs lignes.
# - Les variables en minuscule, avec un `_` entre les mots (e.g. `sphere_radius`).
# - Les variables booléennes devraient commencer par `is_` (e.g. `is_cube`).
# - Les constantes devraient être en majuscule (e.g. `PI`).
# - Attention aux noms réservés (`int`, `list`, `tuple`, `type`, `len`, `print`, etc.).
# - Une opération de 'cast' devrait être vérifiée avant et après : `int(True)` ou `int('18.5')`.
# - Les opérateurs arithmétiques devraient avoir un espace de chaque côté (`+`, `-`, `*`, `/`, `//`, `%`, `**`).
# - Pareil pour les opérateurs logiques (`==`, `<`, `>`, `<=`, `>=`, `!=`).
# - Pareil pour les opérateurs d'affectation (`=`, `+=`, `-=`, `*=`, `/=`, `//=`, `**=`).
# ---
# 
# - **Nommez vos variables clairement** : Utilisez des noms de variables descriptifs pour que le code soit facile à comprendre (e.g. `nombre_de_etudiants`).
# - **Utilisez des commentaires** : Expliquez ce que fait chaque partie du code, surtout pour des concepts plus complexes.
# - **Tester souvent** : Exécutez votre code fréquemment pour détecter les erreurs tôt.
# - **Vérifiez les types de données** : Utilisez la fonction `type()` pour vérifier les types de vos variables et assurez-vous qu'ils sont corrects.
# - **Évitez les noms réservés** : Ne nommez pas vos variables avec des mots réservés comme `int`, `list`, ou `str`.

# ### Nombre à virgule flottante
# - Attention ces chiffres ont TOUJOURS une précision limitée
# - Ne jamais utilisé de == entre des _float_
# - Si le _float_ est en fait un _int_ les opérations seront exact
# - Utilisation d'un EPSILON est recommandé si le type est incertain
# - Python support float16, float32, float64, float128 (surtout avec numpy)
# 
# ### Ordre des opérations
# - Parenthèse en premier
# - De gauche à droite: *, /, //
# - De gauche à droite: +, -
# 
# Où se trouve le ** et le % dans l'ordre d'opération?
# 
# ---

# ### Conseils pour Lire et Comprendre du Code Inconnu
# 
# Même sans connaître les structures de contrôle comme `if/else` et les boucles, vous pouvez toujours appliquer quelques stratégies de base pour comprendre le code inconnu. Voici des conseils adaptés à votre niveau actuel :
# 
# 1. **Commencez par le Haut** :
#    - Lisez les commentaires et les descriptions au début du fichier. Ils donnent souvent une vue d'ensemble du code.
# 
# 2. **Identifiez les Variables** :
#    - Recherchez les déclarations de variables et essayez de comprendre ce qu'elles représentent. Notez les types de variables que vous connaissez (`int`, `float`, `bool`, `str`).
# 
# 3. **Suivez les Impressions (print)** :
#    - Les instructions `print` sont vos amies. Elles montrent ce que le programme essaie d'afficher. Regardez les valeurs imprimées pour comprendre ce que fait le code.
# 
# 4. **Cherchez les Opérations Simples** :
#    - Identifiez les opérations arithmétiques (`+`, `-`, `*`, `/`) et les comparaisons (`==`, `!=`, `>`, `<`). Comprenez comment elles manipulent les variables.
# 
# 5. **Utilisez des Commentaires** :
#    - Ajoutez des commentaires à côté des lignes de code pour expliquer ce que vous pensez qu'elles font. Cela vous aidera à structurer vos pensées.
# 
# ### Exemple Simple de Lecture de Code
# 
# Voici un exemple de code simple et comment le lire :
# 
# ```python
# # Déclarer des variables
# nombre1 = 10
# nombre2 = 20
# texte = "Le résultat est : "
# 
# # Faire une opération
# resultat = nombre1 + nombre2
# 
# # Imprimer le résultat
# print(texte, resultat)
# ```
# 
# #### Étapes pour Comprendre le Code
# 
# 1. **Lire les Variables** :
#    - `nombre1` et `nombre2` sont des entiers (`int`) avec des valeurs de 10 et 20.
#    - `texte` est une chaîne de caractères (`str`) qui contient "Le résultat est : ".
# 
# 2. **Identifier les Opérations** :
#    - `resultat` est une nouvelle variable qui stocke la somme de `nombre1` et `nombre2`. Le résultat sera 30.
# 
# 3. **Suivre les Impressions (print)** :
#    - `print(texte, resultat)` affichera "Le résultat est : 30".

# ### Autres Exemples Simples
# 
# #### Exemple 1 : Manipulation de Chaînes de Caractères
# ```python
# # Déclarer des variables de type chaîne
# prenom = "Alice"
# nom = "Dupont"
# 
# # Concatenation de chaînes
# nom_complet = prenom + " " + nom
# 
# # Imprimer le nom complet
# print("Nom complet :", nom_complet)
# ```
# 
# #### Exemple 2 : Utilisation de Booléens
# ```python
# # Déclarer des variables
# age = 20
# is_adulte = age >= 18  # Vérifie si l'âge est 18 ou plus
# 
# # Imprimer le résultat
# print("Est adulte :", is_adulte)
# ```
# 
# ### Conseils Généraux
# - **Notez les Valeurs** : Écrivez les valeurs des variables au fur et à mesure que vous lisez le code.
# - **Soyez Curieux** : Essayez de modifier des valeurs et de réexécuter le code pour voir ce qui change.
# - **Pratiquez Régulièrement** : Plus vous lirez et écrirez du code, plus cela deviendra naturel.
# 
# En suivant ces conseils et en pratiquant régulièrement, vous deviendrez plus à l'aise pour naviguer et comprendre du code inconnu.

# --------------------------------- #




