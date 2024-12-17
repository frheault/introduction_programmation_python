#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


# Ceci est utile simplement pour l'affichage, exécuter en premier
def section(text):
    print('\033[1m{}\033[0m'.format(text))


# --------------------------------- #


section('Instancier des chaines de caractères')
# Utiliser des guillemets simples pour instancier une chaîne de caractères
mon_texte1 = 'Bonjour'
print(mon_texte1)

# Utiliser des guillemets doubles pour instancier une chaîne de caractères
mon_texte2 = "Salut"
print(mon_texte2)

# Les guillemets doivent s'ouvrir et se fermer correctement
# Les deux exemples suivants sont corrects :
correct1 = 'Ceci est une chaîne de caractères'
correct2 = "Ceci est aussi une chaîne de caractères"

# Exemple incorrect - les guillemets ne correspondent pas
# incorrect = 'Ceci provoquera une erreur"


# --------------------------------- #


section("Manipuler des chaines de caractères")

# Créer plusieurs variables contenant des chaînes de caractères
partie1 = "Bonjour"
partie2 = "tout"
partie3 = "le monde"

# Les concaténer (les assembler) en une seule chaîne
phrase = partie1 + " " + partie2 + " " + partie3

# Afficher la phrase complète
print(phrase)

# print(a - b) # Cette ligne provoquera une erreur car l'opération de soustraction n'est pas supportée pour les strings


# --------------------------------- #


section("Obtenir des lettres en particulier")
mot = "Python"

# Accéder et afficher le premier caractère
print(mot[0])  # Affiche 'P'

# Accéder et afficher le troisième caractère
print(mot[2])  # Affiche 't'

# Afficher le dernier caractère
print(mot[-1])  # Affiche 'n'


# --------------------------------- #


section('Manipulation des chaines')
s = "Python est génial"

# La fonction len() permet d'obtenir la longueur de la chaîne
# On dit que le 'retour' de la fonction est la longueur de la chaîne et le type est int
print(type(s))
print(len(s))

# Accéder à un caractère spécifique
print(s[0]) # Premier caractère
print(s[-1]) # Dernier caractère

# Substring (sous-chaîne)
print(s[0:6]) # Les 6 premiers caractères
print(s[7:10]) # Les caractères de la position 7 à 9


# --------------------------------- #


section('Méthodes des chaines')
# Convertir en majuscule/minuscule
print(s.upper())
print(s.lower())

# Remplacer une partie de la chaîne
print(s.replace("génial", "super"))

# Trouver la position d'une sous-chaîne
print(s.find("est"))


# --------------------------------- #


section('Formatage des chaines')
nom = "Alice"
age = 30

# Utilisation de la méthode format
print("Je m'appelle {} et j'ai {} ans.".format(nom, age))

# Utilisation des f-strings (Python 3.6+) à favoriser
print(f"Je m'appelle {nom} et j'ai {age} ans.")


# --------------------------------- #


# Attention certaines opérations doivent être assignées à des variables
mot = "bonjour"
mot.upper()
print(mot)

# L'opération upper(), tout comme lower() ou replace(), doit être assignée à une variable
mot = mot.upper()
print(mot)


# --------------------------------- #


# À faire : Créez vos propres variables de type string et essayez les différentes méthodes et opérations présentées.
# Par exemple:
mon_texte = "Je suis en train d'apprendre Phyton"
typo = "Phyton"

mon_texte = mon_texte.replace(typo, "Python")
mon_texte = mon_texte.upper()

# Quel sera la valeur de mon_texte ?


# --------------------------------- #




