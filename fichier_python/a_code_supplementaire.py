#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


def section(text):
    print('\033[1m{}\033[0m'.format(text))


# ---
# ### Fonctions
# - Opération _atomique_ utilisant des entrées et des sorties (optional)
# - Simplifie la lisibilité du code en réutilisant des morceaux
# - Certaines sont _built-in_ d'autres _user-defined_ et d'autres _imported_
# - Les fonctions ont un large spectre de robustesse (_warning_, _error_, ```_return None```)
# - Toujours vérifier si une fonction existe avant d'essayer de le faire soit même
# 
# ---

# --------------------------------- #


section('built-in functions')

## Built-in functions (Integer, Float)
a = -10
b = 12.5

print(float(a), int(b), min(a,b), max(a,b), abs(a))

## Built-in functions (String)
text = 'All we have to ___ {0} what to do with the time that {0} given to {1}'.format('is', 'us')
text = text.replace('___', 'decide')
# text = text.replace(' ', '-')
text = text.split(' ')
text = '-'.join(text)
print(text)

## Built-in function (Other) + iterator
var = range(10)
print(var, list(var)) # What is the difference?
##
var_1 = ('1896', '1900', '1904')
var_2 = ('Athen', 'Paris', 'St-Louis')
var = zip(var_1, var_2)
print(var, list(var)) # What is the difference?


# --------------------------------- #


section('Imports)')

import random
import math
import itertools

## Random number generator (RNG): What is it?
# random.seed(0) 
print(random.randint(0,100), random.randint(0,100))
tmp_list = [0, 1, 2, 3, 4]
random.shuffle(tmp_list) # In-place
print(tmp_list)

print(math.ceil(1.2), math.floor(1.2))
print(math.pow(4, 2), math.sqrt(16))

str_list = [['a', 'b', 'c', 'd'], ['1', '2', '3', '4']]
var = itertools.chain(*str_list)
print(var, list(var))  # What is the difference?

var = itertools.combinations(str_list[0], r=2)
print(list(var))

var = itertools.product(str_list[0], str_list[0])
print(list(var))


# ---
# 
# ### Bonnes pratiques
# - Ordonner ses _imports_ en ordre alphabétique
# - Éviter les noms _built-in_
# - Séparer les librairies _built-in_ et externe
# - Ne pas utiliser ```from numpy import *```
# - Utiliser les raccourcis communs ```import numpy as np```
# - Si une opération vous apparait très simple et courante, vérifier si une librairie existe
# 
# Par exemple:
# ```from numpy.linalg import norm```
# - A function is a small chunk of code that performs a specific tasks, an algorithm. (norm)
# - A module is basically a bunch of related code saved in a file with the extension ```.py``` (linalg)
# - a Python packages are basically a directory of a collection of modules. (linalg vs numpy, voir GitHub)
# - while a package is a collection of modules, a library is a collection of packages (numpy)
# 
# https://learnpython.com/blog/python-modules-packages-libraries-frameworks/
# 
# ---

# ---
# 
# ### Bonnes pratiques
# - Lors d'opération de I/O toujours vérifier si les fichiers existent avant de commencer
# - Vérifier si le fichier est vide ou non
# - Toujours utiliser un _with statement_
# - Lors d'itération sur des données inconnues, faire attention au premier et dernier éléments
# - Éviter la conversion en liste si possible (iterator)
# - Si une entrée est fourni par l'utilisateur, toujours vous assurez de la conformité des données (type, longeur, dimension, etc.)
# - Ne pas continuer l'exécution si les entrées sont invalides
# - Écrire des avertissements et des erreurs faciles à comprendre
# - Documenter les fonctions, les scripts et le code en général (comme si un inconnu allait devoir le lire)
# 
# ---

# --------------------------------- #


section('Others patterns in Python')

## List Comprehensions
my_even_list = [i for i in range(10) if i % 2 == 0]
print(my_even_list)

## Unpacking
def get_info(id):
    info_dict = {1902: ('Francois', '1991')}
    return info_dict[id]

name, birthdate = get_info(1902)
print(name, birthdate)

## Merge dictionnaries
dict1 = { 'a': 1, 'b': 2 }
dict2 = { 'b': 3, 'c': 4 }

merged = { **dict1, **dict2 } # Python < 3.9
merged = dict1 | dict2 # Python >= 3.9 only
print(merged)

## Use keys, values and items for dictionnaries
print(merged.values(), merged.keys())
for key, value in merged.items():
    print(key, value)

## Using the Pythonic way
l1 = ['a', 'b', 'c', 'd', 'e']
l2 = ['A', 'B', 'C', 'D', 'E']
# Bad
for i in range(len(l1)):
    print(l1[i], l2[i])
print('_')
# Very Bad
for i in range(len(l1)):
    print(l1[len(l1)-i-1], l2[len(l1)-i-1])
print('_')
# Medium
l1, l2 = l1[::-1], l2[::-1]
for tup in zip(l1, l2):
    print(tup[0], tup[1])
print('_')
# Good
for str1, str2 in zip(reversed(l1), reversed(l2)):
    print(str1, str2)
    
## Using Map (part of  the pythonic way)
def capitalize(s):
    return s.upper()
    
mylist = list(map(capitalize, ['sentence', 'fragment']))
print(mylist)

list_of_ints = list(map(int, "1234567"))
print(list_of_ints)

## Understand the power of Python built-in function
def de_capitalize(s):
    return s.lower()
test = 'My first cat was my favorite cat in my opinion'.split()
print(max(set(map(de_capitalize, test)), key = test.count))

## Understand the power of Python built-in librairies
from collections import Counter
print(Counter("aaaaabbbbcccccddz"))

## Dont name variable if you don't need it
for i, _ in enumerate(test):
    print(i)
    
## Multi-line print
s1 = """Multi line strings can be put
        between triple quotes. It's not ideal
        when formatting your code though"""

print (s1)
# Multi line strings can be put
#         between triple quotes. It's not ideal
#         when formatting your code though
        
s2 = ("You can also concatenate multiple\n"
        "strings this way, but you'll have to\n"
        "explicitly put in the newlines")

print(s2)

## Use one-liner for ternary operator For conditional assignment
text = 'Sucess!' if len(test) == 10 else 'Failed!'
print(text)

## Chaining conditions
x = 20
if 5 <= x < 15:
    print('Case A')
elif 15 <= x < 25:
    print('Case B')
else:
    print('Case C')


# --------------------------------- #




