#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


def section(text):
    print('\033[1m{}\033[0m'.format(text))


# ### Les Fonctions en Python
# 
# #### Écriture des Fonctions
# 
# Les fonctions en Python sont définies en utilisant le mot-clé `def`, suivi du nom de la fonction, des parenthèses `()`, et d'un deux-points `:`. Le corps de la fonction est ensuite écrit en utilisant une indentation. Les fonctions peuvent prendre des paramètres et retourner des valeurs.
# 
# 1. **Définition de la Fonction** : Utilisez le mot-clé `def`.
# 2. **Nom de la Fonction** : Choisissez un nom descriptif pour la fonction.
# 3. **Paramètres** : Placez les paramètres entre parenthèses après le nom de la fonction.
# 4. **Deux-points** : Ajoutez un deux-points `:` après les parenthèses.
# 5. **Indentation** : Indentez le corps de la fonction pour indiquer le bloc de code qu'elle contient.
# 6. **Retour de Valeur** : Utilisez le mot-clé `return` pour retourner une valeur depuis la fonction (facultatif).
# 
# #### Utilisation des Fonctions
# 
# Les fonctions sont utilisées pour encapsuler des blocs de code réutilisables. Elles permettent de structurer le code de manière modulaire, rendant le code plus lisible et plus facile à maintenir. Voici quelques utilisations courantes des fonctions :
# 
# 1. **Réutilisabilité** : Les fonctions permettent de réutiliser le même bloc de code plusieurs fois sans avoir à le réécrire.
# 2. **Modularité** : Les fonctions aident à diviser un programme en morceaux plus petits et plus gérables.
# 3. **Lisibilité** : Les fonctions avec des noms descriptifs rendent le code plus lisible en indiquant clairement ce que chaque partie du code fait.
# 4. **Maintenance** : En regroupant le code dans des fonctions, il devient plus facile de localiser et de corriger les erreurs ou de mettre à jour le code.
# 
# #### Avantages des Fonctions
# 
# 1. **Abstraction** : Les fonctions permettent de masquer la complexité des opérations et de se concentrer sur un niveau d'abstraction plus élevé.
# 2. **Réduction de la Redondance** : En utilisant des fonctions, vous évitez de répéter le même code à plusieurs endroits dans votre programme.
# 3. **Facilité de Test** : Les fonctions isolent des morceaux de code, ce qui les rend plus faciles à tester et à déboguer individuellement.
# 4. **Encapsulation** : Les fonctions permettent d'encapsuler la logique et les données, ce qui améliore la clarté et l'organisation du code.
# 
# ### Structure d'une Fonction en Python
# 
# - **Définition** : La déclaration d'une fonction commence par le mot-clé `def`, suivi du nom de la fonction et de la liste des paramètres entre parenthèses.
# - **Paramètres** : Les paramètres sont des variables qui permettent de passer des données à la fonction. Les paramètres peuvent être optionnels ou obligatoires.
# - **Corps de la Fonction** : Le corps de la fonction est indente, et contient le code à exécuter lorsque la fonction est appelée.
# - **Retour de Valeur** : La fonction peut retourner une valeur en utilisant le mot-clé `return`. Si aucune valeur n'est retournée, la fonction retourne `None` par défaut.
# 
# ### Conclusion
# 
# Les fonctions sont un élément fondamental de la programmation en Python, offrant des avantages significatifs en termes de réutilisabilité, de modularité, de lisibilité et de maintenance du code. En encapsulant des blocs de code dans des fonctions, vous pouvez écrire des programmes plus clairs, plus organisés et plus faciles à gérer.

# --------------------------------- #


section('Fonction sans Paramètre')

def saluer():
    """
    Affiche un message de salutation.
    """
    print("Bonjour tout le monde !")

# Appel de la fonction
saluer()


# --------------------------------- #


section('Fonction avec Paramètres')

def additionner(a, b):
    """
    Retourne la somme de deux nombres.
    """
    return a + b

# Appel de la fonction avec des arguments
resultat = additionner(5, 3)
print("La somme est:", resultat)


# --------------------------------- #


section('Fonction et scope des variables')

def afficher():
    # Variable locale
    message = "Bonjour tout le monde !" # La variable message n'existe qu'à l'intérieur de la fonction
    print('in', message)

# Appel de la fonction
message = "Hello World !" # La variable message existe en dehors de la fonction
afficher()
print('out', message)

# Des variables de même nom peuvent exister en dehors et à l'intérieur d'une 
# fonction sans interférer l'une avec l'autre.


# --------------------------------- #


def exposant(x, n):
    """
    Retourne x à la puissance n.
    """
    # Variable locale
    resultat = x ** n
    return resultat

# x, n existe en dehors et à l'intérieur de la fonction sans interférer l'une avec l'autre.
x, n = 10, 3
resultat = exposant(2, 3)
print("Le résultat est:", resultat)

# x, n existe en dehors et à l'intérieur de la fonction, mais ici on réutilise les variables x, n
# dans l'appel de la fonction.
resultat = exposant(x, n)
print("Le résultat est:", resultat)

# Les noms de variables utilisés dans une fonction n'ont pas besoin d'être les 
# mêmes que ceux utilisés en dehors de la fonction.
a, b = 5, 2
resultat = exposant(a, b)
print("Le résultat est:", resultat)


# --------------------------------- #


section('Fonction avec Paramètres Optionnels')

def saluer_personne(nom="inconnu"):
    """
    Affiche un message de salutation pour une personne.
    """
    print(f"Bonjour, {nom} !")

# Appel de la fonction avec et sans argument
saluer_personne("Alice")
saluer_personne()


# --------------------------------- #


section('Fonction Utilisant une Liste')

def somme_liste(liste):
    """
    Retourne la somme des éléments d'une liste.
    """
    somme = 0
    for element in liste:
        somme += element
    return somme

# Appel de la fonction avec une liste
nombres = [1, 2, 3, 4, 5]
somme = somme_liste(nombres)
print("La somme des éléments de la liste est:", somme)


# --------------------------------- #


section('Lire du code avec des fonctions, boucle et if/else')

print('---')
def est_pair(n):
    """
    Retourne True si n est pair, False sinon.
    """
    print(f"Vérification de {n}...")
    if n % 2 == 0:
        print(f"{n} est pair.")
    else:
        print(f"{n} est impair.")
    print('===')

print('+++')

# Appel de la fonction
for val in (289, 578, 127.3, 1000.0):
    est_pair(val)
    print('***')
print('///')

# Les fonctions permettent de rendre le code plus lisible et plus facile à comprendre.
# Elles permettent également de réutiliser du code sans avoir à le réécrire.

# Mais il est important de savoir comment lire et dans quel ordre le code est exécuté.


