#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


def section(text):
    print('\033[1m{}\033[0m'.format(text))


# --------------------------------- #


section('Introduction aux Conditions IF')
valeur = -120

# Utiliser une condition IF pour vérifier si la valeur est divisible par 12
if valeur % 12 != 0:
    print('Not divisible by 12')

# Le mot clé if permet d'ensuite évaluer une condition, suivi d'un : pour terminer la ligne
# Une indentation / tabulation / 4 espaces permet de définir un bloc qui sera optionellement executé si la condition est vrai


# --------------------------------- #


a = -10

if a < 0:
    a *= -1
    a += 3
a += 2

# À faire : quelle sera la valeur final de a ? Faite un print() pour confirmer
# À faire : essayer de changer la valeur de a à 10, quelle sera la valeur finale de a ?


# --------------------------------- #


section('Conditions IF/ELSE')

valeur = -120

# Utiliser une condition IF/ELSE pour vérifier si la valeur est divisible par 10
if valeur % 10:
    print('Not Divisible by 10')
else:
    print('Divisible by 10')


# --------------------------------- #


section('Conditions IF/ELIF/ELSE')

# Utiliser une condition IF/ELIF/ELSE pour catégoriser la valeur
if valeur > 100: # Condition tester en premier
    print('Big Number!')
elif valeur < 1: # Si la première condition est fausse, test celle-ci
    print('Small Number...')
else: # Si la condition ci-dessus (elif) est fausse, le bloc suivant est executé
    print('Medium Number.')

valeur = -120

if valeur < 0: # La première condition est vrai, donc ce bloc s'exécute
    print(f'{valeur} est negatif') 
elif valeur % 12 == 0: # Ce bloc ne sera donc pas executé
    print(f'{valeur} est divisible par 12')


# --------------------------------- #


section('Exemple Avancé')

# Déclarer deux variables
num_1, num_2 = -18, -10

# Vérifier si une ou les deux variables sont négatives
if num_1 < 0 or num_2 < 0:
    print('One is Negative!')
elif num_1 < 0 and num_2 < 0:
    print('Both are Negative!')
# Pourquoi ce code ne fonctionne-t-il pas comme prévu ?


# --------------------------------- #




