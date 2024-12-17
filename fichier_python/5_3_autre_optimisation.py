#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


def section(text):
    print('\033[1m{}\033[0m'.format(text))


# ### Introduction au Code Lent vs Rapide (Optimisation) pour les Très Novices
# 
# #### Qu'est-ce que le Code Lent et Rapide ?
# 
# - **Code Lent** : Le code lent prend plus de temps pour s'exécuter. Cela peut être dû à des algorithmes inefficaces, des structures de données inappropriées, ou des opérations répétitives inutiles.
# - **Code Rapide** : Le code rapide s'exécute plus rapidement, souvent en raison de l'utilisation de meilleures pratiques de programmation, de choix d'algorithmes efficaces, et d'optimisations de code.
# 
# #### Facteurs qui Rendent le Code Lent
# 
# 1. **Algorithmes Inefficaces** : L'utilisation d'algorithmes qui ont des complexités temporelles élevées (comme O(n^2) au lieu de O(n log n)) peut ralentir considérablement le code.
# 2. **Boucles Inutiles** : Répéter des opérations dans des boucles alors qu'elles pourraient être effectuées en dehors ou optimisées.
# 3. **Structures de Données Inappropriées** : Utiliser des structures de données qui ne sont pas adaptées aux besoins spécifiques peut entraîner des temps de traitement plus longs.
# 4. **Accès Fréquent aux Disques ou Réseaux** : Les opérations de lecture/écriture sur disque ou les appels réseau peuvent être très lents comparés aux opérations en mémoire.
# 5. **Fonctions Répétitives** : Appeler des fonctions coûteuses à répétition au lieu de stocker les résultats lorsque cela est possible.

# --------------------------------- #


section('Boucle Inefficace')
from time import time

def somme_lente(liste):
    somme = 0
    for element in liste:
        somme += element
    return somme

timer = time()
ma_liste = range(1000)
print(somme_lente(ma_liste),
      'Calculé en: {}ms'.format((time() - timer) * 1000))


def somme_rapide(liste):
    return sum(liste) # Il existe souvent des fonctions qui font le travail pour nous

timer = time()
ma_liste = range(1000)
print(somme_lente(ma_liste),
      'Calculé en: {}ms'.format((time() - timer) * 1000))

# Est-ce plus rapide ?


# --------------------------------- #


section('Recherche dans une Liste vs Set')

def element_present_lent(liste, element):
    return element in liste

ma_liste = [i for i in range(100000)]
timer = time()
print(element_present_lent(ma_liste, 9999),
      'Calculé en: {}ms'.format((time() - timer) * 1000))

def element_present_rapide(ensemble, element):
    return element in ensemble

mon_ensemble = {i for i in range(100000)}
timer = time()
print(element_present_rapide(mon_ensemble, 9999),
      'Calculé en: {}ms'.format((time() - timer) * 1000))

# À faire : Essayer de trouver l'élément 9, 99, 999, 9999, 99999
# Quel est le comportement, et pourquoi ?


# --------------------------------- #


section('Optimisation de calcul')

from time import time

# Fonction extrement simple testant 100% des chiffres
def is_prime_1(x):
    is_prime = True
    for i in range(2, x-1):
        if x % i == 0:
            is_prime = False
    return is_prime

# Fonction testant 100% des chiffres jusqu'à la racine carré
def is_prime_2(x):
    is_prime = True
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            is_prime = False
    return is_prime

# Fonction testant les chiffres jusqu'au premier contre-exemple
def is_prime_3(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x < 2:
        return False

    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

# À faire : Tester 65345941, pourquoi le #3 est maintenant plus lent ?
timer = time()
print(is_prime_1(65345940),
      'Calculé en: {}ms'.format((time() - timer) * 1000))

timer = time()
print(is_prime_2(65345940),
      'Calculé en: {}ms'.format((time() - timer) * 1000))

timer = time()
print(is_prime_3(65345940),
      'Calculé en: {}ms'.format((time() - timer) * 1000))


# --------------------------------- #


section('Fonction définie par les utilisateurs vs built-in')

import random
from time import time

# Génération des données
ages = [1, 12, 15, 18, 21, 25, 30, 36, 45, 54, 65, 75, 85, 90]
names = ['Dave', 'Mike', 'Steve', 'Kevin', 'Roger', 'Blanche',
         'Rose', 'Violette', 'Ginette', 'Sarah', 'Julie', 'Arthur',
         'Lucie', 'Marie']
wealth = [10000, -10000, 20000, -25000, 35000, -50000, 0, 0, 1000,
          -2500, 500000, 1900050, -156547, -6236987]

print(len(ages), len(names), len(wealth))
random.seed(0) #
random.shuffle(ages)
random.shuffle(names)
random.shuffle(wealth)
attributes = zip(ages, names, wealth)
# À faire : Pouvez-vous trouver (en ligne) ce que zip() fait

def sort_att(ma_liste, att=0, inverse=False):
    """
    ma_liste : séquence en entrée (type: liste)
    att : attribut sur lequel sera faite le triage
    inverse : Inverser le triage
    """
    ma_liste = list(ma_liste)
    
    # À faire : Êtes-vous capable de comprendre ce que ce code fait ?
    # En lisant une ligne à la fois, êtes-vous capable de suivre le déroulement ?
    ordered_lst = []
    while len(ordered_lst) < len(ma_liste):
        min_val = 9999999999
        min_pos = 0
        for pos, val in enumerate(ma_liste):
            if val[att] < min_val and val not in ordered_lst:
                min_pos = pos
                min_val = val[att]
        ordered_lst.append(ma_liste[min_pos])
    
    # Quel est le résultat de cette fonction ?
    return ordered_lst[::-1] if inverse else ordered_lst

# À faire : Essayer les paramètres optionels
timer = time()
resultat_1 = sort_att(attributes)
print(resultat_1)

# Il s'agit pas vraiment d'une optimisation du temps de calcul, mais de VOTRE temps
# Beaucoup de fonction existe déjà en Python, il faut vérifier ce qui existe déjà
# avant de re-faire une fonction complexe !
from operator import itemgetter
attributes = zip(ages, names, wealth)
timer = time()
resultat_2 = list(sorted(attributes, key=itemgetter(0), reverse=False))
print(resultat_2)

# À faire : Vérifier que resultat_1 et resultat_2 sont identique
# À faire : Comparer la vitesse d'exécution entre ma fonction et la fonction built-in

