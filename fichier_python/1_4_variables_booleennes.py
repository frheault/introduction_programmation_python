#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


# Ceci est utile simplement pour l'affichage, exécuter en premier
def section(text):
    print('\033[1m{}\033[0m'.format(text))


# --------------------------------- #


section("Créer une variable booléenne")

# Créer une variable contenant une valeur booléenne (True ou False)
mon_bool = True

# Afficher le contenu de la variable
print(mon_bool)
print(type(mon_bool))


# --------------------------------- #


section("Opérations de base")
# Créer des variables booléennes
a = True
b = False

# AND logique
print(a and b)  # Résultat : False

# OR logique
print(a or b)   # Résultat : True

# NOT logique
print(not a)    # Résultat : False
print(not b)    # Résultat : True

# Combinaisons d'opérateurs logiques
print((a and b) or (not b))  # Résultat : True


# --------------------------------- #


section("Comparer des entiers (ou des nombres réels")
# Créer des variables pour les comparaisons
x = 10
y = 5

# Plus grand que
print(x > y)   # Résultat : True

# Plus petit que
print(x < y)   # Résultat : False

# Égal à
print(x == y)  # Résultat : False

# Différent de
print(x != y)  # Résultat : True

# Plus grand ou égal à
print(x >= y)  # Résultat : True

# Plus petit ou égal à
print(x <= y)  # Résultat : False


# --------------------------------- #


# À faire : Créez vos propres variables booléennes et essayez les différentes opérations logiques et comparaisons.
# Par exemple :
# a = (10 >= 5)
# b = (5 < 3)
# print(a and b)
# print(a or b)
# print(not a)
# print((a and b) or (not b))


# --------------------------------- #


section("Comparer des chaines de caractères")
texte1 = "Bonjour"
texte2 = "Python"
texte3 = "Bonjour"

# Comparer les chaînes de caractères
print(texte1 == texte2)  # Résultat : False (Bonjour n'est pas égal à Python)
print(texte1 == texte3)  # Résultat : True (Bonjour est égal à Bonjour)

# Utiliser les comparaisons dans des expressions logiques
print(texte1 != texte2)  # Résultat : True (Bonjour est différent de Python)
print(texte1 != texte3)  # Résultat : False (Bonjour n'est pas différent de Bonjour)

# Comparer les chaînes selon l'ordre lexicographique (ordre alphabétique)
print(texte1 > texte2)  # Résultat : False (Bonjour vient avant Python)
print(texte1 < texte2)  # Résultat : True (Bonjour vient avant Python)

# Combiner des comparaisons avec des opérateurs logiques
print((texte1 == texte3) and (texte2 != texte3))  # Résultat : True (les deux conditions sont vraies)
print((texte1 == texte2) or (texte1 == texte3))  # Résultat : True (au moins une des conditions est vraie)


# --------------------------------- #


# À faire : Créez vos propres chaînes de caractères et essayez les différentes comparaisons et combinaisons logiques.
# Par exemple :
# string1 = "Hello"
# string2 = "World"
# string3 = "Hello"

# print(string1 == string2)
# print(string1 != string2)
# print(string1 == string3)
# print((string1 == string2) or (string1 == string3))
# print((string1 != string2) and (string1 == string3))

