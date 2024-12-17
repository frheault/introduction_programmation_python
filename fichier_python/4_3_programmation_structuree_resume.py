#!/usr/bin/env python
# coding: utf-8

# ### Résumé de la Programmation Structurée en Python
# 
# La programmation structurée est un paradigme de programmation qui utilise des structures de contrôle claires et définies pour organiser le code. En Python, cela inclut les conditions (`if/else`), les boucles (`while`, `for`), les fonctions, et l'indentation pour structurer les blocs de code. Voici un résumé concis des principaux éléments de la programmation structurée.
# 
# ---
# 
# #### Conditions (if/else)
# 
# - **if** : Permet d'exécuter un bloc de code si une condition est vraie.
# - **else** : Exécute un bloc de code alternatif si la condition `if` est fausse.
# - **elif** : Permet de vérifier plusieurs conditions, en ajoutant des alternatives entre `if` et `else`.
# 
# ---
# 
# #### Boucles (while, for)
# 
# - **while** : Exécute un bloc de code tant qu'une condition est vraie. Utilisée lorsque le nombre d'itérations n'est pas connu à l'avance.
# - **for** : Itère sur une séquence (comme une liste, un tuple ou une chaîne) et exécute un bloc de code pour chaque élément. Utilisée lorsque le nombre d'itérations est connu à l'avance ou pour parcourir des collections d'éléments.
# 
# ---
# 
# #### Fonctions
# 
# - **Définition** : Utilise le mot-clé `def`, suivi du nom de la fonction et des paramètres entre parenthèses. Le corps de la fonction est indenté.
# - **Paramètres** : Les fonctions peuvent prendre des paramètres pour passer des données.
# - **Retour de Valeur** : Utilise le mot-clé `return` pour renvoyer une valeur.
# - **Utilisation** : Les fonctions permettent de réutiliser le code, de le modulariser et de le rendre plus lisible.
# 
# ---
# 
# #### Indentation et Blocs de Code
# 
# - **Indentation** : En Python, l'indentation est essentielle pour délimiter les blocs de code. Chaque bloc de code à l'intérieur des conditions, des boucles, et des fonctions doit être indenté de manière cohérente.
# - **Blocs de Code** : Un bloc de code est un groupe de déclarations qui sont exécutées ensemble. L'indentation indique quels codes font partie du même bloc.
# 
# ---
# 
# #### Portée des Variables (Variable Scope)
# 
# - **Portée Locale** : Les variables déclarées à l'intérieur d'une fonction sont locales à cette fonction et ne peuvent pas être accédées en dehors de celle-ci.
# - **Portée Globale** : Les variables déclarées en dehors de toutes les fonctions sont globales et peuvent être accédées de n'importe où dans le code.
# - **Variable Shadowing** : Une variable locale peut avoir le même nom qu'une variable globale, mais elles seront traitées comme des variables distinctes. La variable locale masque la variable globale dans son scope.
# 
# ---
# 
# ### Conclusion
# 
# La programmation structurée en Python repose sur l'utilisation de structures de contrôle claires et bien définies. Les conditions permettent de prendre des décisions, les boucles permettent de répéter des actions, et les fonctions permettent de structurer et de réutiliser le code. L'indentation et la portée des variables sont essentielles pour maintenir la clarté et l'organisation du code. En suivant ces principes, les développeurs peuvent écrire des programmes Python efficaces, lisibles et maintenables.
