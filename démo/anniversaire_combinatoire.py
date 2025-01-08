
from collections import Counter
import os
import random


def generer_population(nb_individus, jours=365):
    """
    Génère une population avec des anniversaires aléatoires.
    """
    return [random.randint(1, jours) for _ in range(nb_individus)]


def compter_partages(population):
    """
    Compte combien de fois chaque jour est partagé et classe les résultats.
    """
    compte_jours = Counter(population)
    partages = Counter(compte_jours.values())
    return partages


def simuler_partages(nb_simulations, nb_individus, jours=365):
    """
    Simule plusieurs groupes et calcule les probabilités de partage.
    """
    cumul_partages = Counter()

    for _ in range(nb_simulations):
        population = generer_population(nb_individus, jours)
        partages = compter_partages(population)
        # Ajouter uniquement les partages supérieurs à 1 individu
        for partage, _ in partages.items():
            if partage > 1:
                cumul_partages[partage] += 1

    return cumul_partages


def calculer_probabilites(cumul_partages, nb_simulations):
    """
    Calcule les probabilités en pourcentage pour chaque type de partage.
    """
    probabilites = {}
    total = 0
    for partage, count in cumul_partages.items():
        probabilites[partage] = (count / nb_simulations) * 100
        total += count

    return probabilites


def afficher_probabilites(probabilites):
    """
    Affiche les probabilités sous forme de tableau textuel.
    """
    print("Probabilités de partage d'anniversaires :")
    print("-" * 43)
    print(f"| {'Nb individus':<15} | {'Probabilité (%)':<20} |")
    print("-" * 43)
    for partage, prob in sorted(probabilites.items()):
        print(f"| {partage:<15} | {prob:<20.3f} |")
    print("-" * 43)


def generer_code():
    """
    Génère un code unique à partir du chemin du fichier.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    choix_aleatoire = random.randint(0, 9)
    valeur_aleatoire = random.randint(0, 9)
    majuscule = bool(random.getrandbits(1))

    code = alphabet[choix_aleatoire]
    code = code.upper() if majuscule else code
    check = str(20 - (valeur_aleatoire + choix_aleatoire)).zfill(2)
    code_p1 = f"{code}{alphabet[-(choix_aleatoire+1)]}{code.swapcase()}"
    code_p2 = f"{valeur_aleatoire}{choix_aleatoire}{check}"
    return f"{code_p1}_{code_p2}" if majuscule else f"{code_p1}-{code_p2}"


# Transforme le CWD en un entier (somme des codes ASCII)
random.seed(0)

INFO = """
Saviez-vous que la probabilité que deux personnes partagent une date
d'anniversaire dans une salle remplie de personnes est hautement non intuitive ?

Dans une salle de seulement 23 personnes, il y a 50% de chance que 2 personnes
partagent une date d'anniversaire.

Ce petit programme permet de simuler 10 000 fois une population et de vérifier
le pourcentage de partage d'anniversaire.

(Essayez avec la valeur 23 pour voir que la probabilité que 2 personnes partagent
un anniversaire dépasse tout juste 50%)
"""
print(INFO)

# Paramètres
NB_SIMULATIONS = 10000
NB_INDIVIDUS = input("Nombre d'individus dans vos simulations : ")
try:
    NB_INDIVIDUS = int(NB_INDIVIDUS)
except ValueError:
    print("Veuillez entrer un nombre entier valide.")
    exit(1)

# Étapes principales
cumul_partages = simuler_partages(NB_SIMULATIONS, NB_INDIVIDUS)
probabilites = calculer_probabilites(cumul_partages, NB_SIMULATIONS)
afficher_probabilites(probabilites)

cwd = os.getcwd()
seed = sum(ord(char) for char in cwd)
random.seed(0)
print(f"\nCode de soumission : {generer_code()}")
