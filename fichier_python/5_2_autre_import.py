#!/usr/bin/env python
# coding: utf-8

# ### Introduction aux Imports en Python
# 
# #### Qu'est-ce que `import` ?
# 
# L'instruction `import` en Python permet d'inclure des modules et des bibliothèques dans votre script. Ces modules peuvent être des fonctionnalités intégrées à Python, des bibliothèques tierces installées séparément, ou des modules définis par l'utilisateur.
# 
# #### Types d'Imports
# 
# 1. **Modules Intégrés (Built-in)**
#    - Python inclut un grand nombre de modules intégrés prêts à l'emploi, comme `math`, `datetime`, et `random`.
#    - Ces modules fournissent des fonctionnalités de base pour les calculs mathématiques, la manipulation de dates et d'heures, la génération de nombres aléatoires, etc.
# 
# 2. **Modules de la Bibliothèque Standard**
#    - En plus des modules intégrés, Python dispose d'une bibliothèque standard riche contenant des modules comme `os`, `sys`, `json`, et `re`.
#    - Ces modules offrent des fonctionnalités pour l'interaction avec le système d'exploitation, la gestion des arguments de ligne de commande, la manipulation de fichiers JSON, et les opérations sur les expressions régulières.
# 
# 3. **Modules Externes (Libraries Tierces)**
#    - Les bibliothèques tierces sont développées par la communauté et peuvent être installées via des gestionnaires de paquets comme `pip`.
#    - Exemples populaires : `numpy`, `pandas`, `scipy`, `matplotlib`.
# 
# #### Bonnes Pratiques
# 
# 1. **Importez seulement ce dont vous avez besoin**
#    - Évitez les imports globaux (`from module import *`) car ils polluent l'espace de noms et rendent le code moins lisible.
#    - Préférez importer des fonctions ou des classes spécifiques (`from module import fonction`).
# 
# 2. **Utilisez des alias pour les imports longs ou fréquents**
#    - Utilisez des alias pour simplifier les références aux modules (`import numpy as np`).
# 
# 3. **Organisez les imports en trois sections**
#    - Imports intégrés de Python.
#    - Imports de la bibliothèque standard.
#    - Imports de bibliothèques tierces.
#    - Séparez chaque section par une ligne vide pour améliorer la lisibilité.
# 
# 4. **Placez les imports en haut du fichier**
#    - Les imports doivent être placés au début du fichier pour être facilement trouvés et maintenus.

# ### Exemples de Différentes Façons d'Importer des Modules en Python
# 
# #### 1. Importer Tout le Module
# 
# **Syntaxe** : `import module_name`
# 
# **Description** : Cette méthode importe tout le module. Vous pouvez accéder aux fonctions et classes du module en utilisant le préfixe `module_name.`.
# 
# **Quand l'utiliser** :
# - Lorsque vous avez besoin d'utiliser plusieurs fonctions ou classes du module.
# - Pour éviter les conflits de noms avec des fonctions ou classes locales.
# 
# **Exemple** :
# 
# ```python
# import numpy
# 
# # Utilisation de fonctions de numpy
# array = numpy.array([1, 2, 3])
# print(numpy.mean(array))
# ```
# 
# #### 2. Importer des Fonctions ou Classes Spécifiques
# 
# **Syntaxe** : `from module_name import function_name, class_name`
# 
# **Description** : Cette méthode importe uniquement les fonctions ou classes spécifiées du module. Vous pouvez utiliser ces fonctions et classes directement sans le préfixe `module_name.`.
# 
# **Quand l'utiliser** :
# - Lorsque vous avez besoin d'utiliser seulement quelques fonctions ou classes du module.
# - Pour rendre le code plus concis.
# 
# **Exemple** :
# 
# ```python
# from numpy import array, mean
# 
# # Utilisation directe des fonctions importées
# array = array([1, 2, 3])
# print(mean(array))
# ```
# 
# #### 3. Importer Tout le Module avec un Alias
# 
# **Syntaxe** : `import module_name as alias`
# 
# **Description** : Cette méthode importe tout le module et lui attribue un alias. Vous pouvez accéder aux fonctions et classes du module en utilisant le préfixe `alias.`.
# 
# **Quand l'utiliser** :
# - Lorsque le nom du module est long ou redondant.
# - Pour améliorer la lisibilité du code.
# - Pratique courante pour les modules fréquemment utilisés, comme `numpy` avec l'alias `np`.
# 
# **Exemple** :
# 
# ```python
# import numpy as np
# 
# # Utilisation de fonctions de numpy avec un alias
# array = np.array([1, 2, 3])
# print(np.mean(array))
# ```

# 
# #### Cinq Bibliothèques Connues et Utiles
# 
# 1. **`numpy`**
#    - Utilisé pour le calcul scientifique et les opérations sur les tableaux multidimensionnels. Offre des fonctionnalités performantes pour les calculs numériques.
#    
# 2. **`pandas`**
#    - Fournit des structures de données et des outils d'analyse de données flexibles et puissants. Idéal pour la manipulation de données tabulaires et les analyses statistiques.
#    
# 3. **`matplotlib`**
#    - Bibliothèque de traçage pour créer des visualisations statiques, animées et interactives en Python. Utilisée pour la création de graphiques, de diagrammes et de figures.
# 
# 4. **`scipy`**
#    - Une bibliothèque qui s'appuie sur `numpy` pour fournir des routines et algorithmes avancés pour les mathématiques, la science et l'ingénierie. Elle offre des modules pour l'optimisation, l'intégration, l'interpolation, la transformation de Fourier, les fonctions spéciales, et plus encore. `scipy` est essentiel pour les calculs scientifiques et les analyses de données complexes.
# 
# 5. **Bibliothèque de Traitement d'Audio : `librosa`**
#    - `librosa` est une bibliothèque puissante pour l'analyse audio et la manipulation de signaux audio. Elle offre des fonctionnalités pour le chargement et la sauvegarde de fichiers audio, l'extraction de caractéristiques audio, la transformation de signaux audio, et la visualisation de données audio. `librosa` est largement utilisée dans les projets de traitement du signal audio et d'apprentissage automatique.
# 
# 6. **Bibliothèque de Traitement de Mesh : `trimesh`**
#    - `trimesh` est une bibliothèque pour le traitement des maillages 3D. Elle permet de lire, écrire, et manipuler des maillages en 3D, ainsi que d'effectuer des opérations géométriques, des analyses et des visualisations. `trimesh` est utile pour les applications en modélisation 3D, en ingénierie, et en réalité virtuelle/augmentée.
# 

# --------------------------------- #


# À faire : Importer la fonction min et max de la librarie Numpy et trouver le minimum de la liste suivante : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] et le maximum de la liste suivante : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste1 = [12, 2, 3, 4, 45, 6, 7, -8, 9, 10]

