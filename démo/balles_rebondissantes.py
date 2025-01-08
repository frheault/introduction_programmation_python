#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import deepcopy
from itertools import combinations
import random
import sys

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from scipy.spatial import cKDTree
from tqdm import tqdm

# Requiert des librairies pour exécuter: pip install matplotlib numpy scipy tqdm pyqt6
# pyqt6 est en python==3.12, pyqt5 pour python==3.11 et non-nécessaire pour python<=3.10

def on_close(event):
    exit()


def ajuster_chevauchement(balle1, balle2):
    """
    Gère la collision et l'ajustement du chevauchement entre deux balles.

    Parameters:
        balle1, balle2: Les objets Balle impliqués dans la collision.

    Returns:
        balle1, balle2: Les objets Balle après la collision et l'ajustement du chevauchement.
    """

    # Calcul de la distance entre les centres des deux balles
    distance = np.sqrt((balle1.x - balle2.x)**2 + (balle1.y - balle2.y)**2,
                       dtype=np.float64)

    # Détection de collision
    if distance < balle1.rayon + balle2.rayon:

        # Calcul du chevauchement
        chevauchement = distance - (balle1.rayon + balle2.rayon)

        # Calcul du vecteur unitaire (mouv_norm) entre les deux balles
        mouv_norm = np.array([balle1.x - balle2.x, balle1.y - balle2.y],
                             dtype=np.float64)
        mouv_norm /= np.linalg.norm(mouv_norm)

        # Pondération du déplacement par les rayons des balles
        ratio1 = balle2.rayon / (balle1.rayon + balle2.rayon)
        ratio2 = balle1.rayon / (balle1.rayon + balle2.rayon)

        # Ajustement des positions pour éviter le chevauchement
        balle1.x -= mouv_norm[0] * chevauchement * ratio1
        balle1.y -= mouv_norm[1] * chevauchement * ratio1
        balle2.x += mouv_norm[0] * chevauchement * ratio2
        balle2.y += mouv_norm[1] * chevauchement * ratio2

    return balle1, balle2


def ajuster_chevauchements_tous(balles):
    """
    Ajuste le chevauchement entre toutes les paires possibles de balles.

    Parameters:
        balles: Liste des objets Balle à ajuster.

    Returns:
        balles: Liste des objets Balle après ajustement du chevauchement.
    """

    # Générer toutes les combinaisons possibles de paires de balles
    comb_balles = list(combinations(balles, 2))

    # Mélanger les combinaisons pour simuler un ordre aléatoire de collision
    random.shuffle(comb_balles)

    # Appliquer la fonction d'ajustement du chevauchement à chaque paire de balles
    for balle1, balle2 in comb_balles:
        balle1, balle2 = ajuster_chevauchement(balle1, balle2)

    return balles


def gerer_collision_simple(balle1, balle2):
    """
    Gère la collision simple entre deux balles en échangeant simplement leurs vitesses.

    Parameters:
        balle1, balle2: Les objets Balle impliqués dans la collision.

    Returns:
        balle1, balle2: Les objets Balle après la collision.
    """

    # Calcul de la distance entre les deux balles
    distance = np.sqrt((balle1.x - balle2.x)**2 + (balle1.y - balle2.y)**2,
                       dtype=np.float64)

    # Vérification de la collision
    if distance < balle1.rayon + balle2.rayon:
        # Échange des vitesses des deux balles
        balle1.dx, balle1.dy, balle2.dx, balle2.dy = balle2.dx, balle2.dy, balle1.dx, balle1.dy

    return balle1, balle2


def gerer_collision_avancee(balle1, balle2):
    """
    Gère la collision avancée entre deux balles en utilisant la conservation du moment linéaire.

    Parameters:
        balle1, balle2: Les objets Balle impliqués dans la collision.

    Returns:
        balle1, balle2: Les objets Balle après la collision.
    """

    # Calcul de la distance entre les deux balles
    distance = np.sqrt((balle1.x - balle2.x)**2 +
                       (balle1.y - balle2.y)**2, dtype=np.float64)

    # Vérification de la collision
    if distance < balle1.rayon + balle2.rayon:

        # Calcul du vecteur unitaire entre les deux balles
        dx = balle1.x - balle2.x
        dy = balle1.y - balle2.y
        vecteur_unitaire = np.array([dx, dy]) / distance

        # Calcul des composantes de la vitesse selon ce vecteur
        vitesse1_initiale = balle1.dx * \
            vecteur_unitaire[0] + balle1.dy * vecteur_unitaire[1]
        vitesse2_initiale = balle2.dx * \
            vecteur_unitaire[0] + balle2.dy * vecteur_unitaire[1]

        # Mise à jour des vitesses en utilisant la conservation du moment linéaire
        vitesse1_finale = vitesse2_initiale
        vitesse2_finale = vitesse1_initiale

        # Mise à jour des composantes de la vitesse des balles
        balle1.dx = balle1.dx + \
            (vitesse1_finale - vitesse1_initiale) * vecteur_unitaire[0]
        balle1.dy = balle1.dy + \
            (vitesse1_finale - vitesse1_initiale) * vecteur_unitaire[1]
        balle2.dx = balle2.dx + \
            (vitesse2_finale - vitesse2_initiale) * vecteur_unitaire[0]
        balle2.dy = balle2.dy + \
            (vitesse2_finale - vitesse2_initiale) * vecteur_unitaire[1]

    return balle1, balle2


def gerer_collision_complexe(balle1, balle2, perte_energie=0.25):
    """
    Gère la collision complexe entre deux balles en tenant compte des lois de la physique
    et d'une perte d'énergie.

    Parameters:
        balle1, balle2: Les objets Balle impliqués dans la collision.
        perte_energie: Pourcentage d'énergie perdu lors de la collision (entre 0 et 1).

    Returns:
        balle1, balle2: Les objets Balle après la collision.
    """

    # Calcul de la distance entre les deux balles
    distance = np.sqrt((balle1.x - balle2.x)**2 + (balle1.y - balle2.y)**2,
                       dtype=np.float64)

    # Vérification de la collision
    if distance < balle1.rayon + balle2.rayon:

        # Calcul des masses en fonction des rayons (m = rho * r^3)
        m1 = balle1.rayon ** 3
        m2 = balle2.rayon ** 3

        # Calcul des vecteurs de vitesse initiaux
        v1 = np.array([balle1.dx, balle1.dy], dtype=np.float64)
        v2 = np.array([balle2.dx, balle2.dy], dtype=np.float64)

        # Calcul du vecteur normal n et du vecteur tangentiel t
        n = np.array([balle1.x - balle2.x, balle1.y - balle2.y],
                     dtype=np.float64)
        n = n / np.linalg.norm(n)
        t = np.array([-n[1], n[0]], dtype=np.float64)

        # Projection des vitesses sur les vecteurs n et t
        v1n = np.dot(v1, n)
        v1t = np.dot(v1, t)
        v2n = np.dot(v2, n)
        v2t = np.dot(v2, t)

        # Facteur d'énergie conservée
        facteur_energie = 1 - perte_energie

        # Mise à jour des composantes normales de la vitesse après collision
        v1n_f = (((m1 - m2) / (m1 + m2)) * v1n +
                 ((2 * m2) / (m1 + m2)) * v2n) * facteur_energie
        v2n_f = (((m2 - m1) / (m1 + m2)) * v2n +
                 ((2 * m1) / (m1 + m2)) * v1n) * facteur_energie

        # Les composantes tangentes de la vitesse restent inchangées
        v1t_f = v1t
        v2t_f = v2t

        # Combinaison des composantes pour obtenir les vitesses finales
        v1_f = v1n_f * n + v1t_f * t
        v2_f = v2n_f * n + v2t_f * t

        # Mise à jour des vitesses des balles
        balle1.dx, balle1.dy = v1_f[0], v1_f[1]
        balle2.dx, balle2.dy = v2_f[0], v2_f[1]

    return balle1, balle2


class Balle:
    def __init__(self, x, y, dx, dy, rayon=0.1, couleur='b'):
        """Initialisation d'une balle."""
        self.x = np.float64(x)
        self.y = np.float64(y)
        self.dx = np.float64(dx)
        self.dy = np.float64(dy)
        self.rayon = rayon
        self.couleur = couleur

    def mettre_a_jour_position(self, x_limites, y_limites, balles,
                               methode_collision, taille_max):
        """Mise à jour de la position de la balle."""
        self.x += self.dx
        self.y += self.dy

        # Gestion des collisions avec les murs
        if self.x <= x_limites[0] + self.rayon or self.x >= x_limites[1] - self.rayon:
            self.dx = -self.dx
            self.x += self.dx
        if self.y <= y_limites[0] + self.rayon or self.y >= y_limites[1] - self.rayon:
            self.dy = -self.dy
            self.y += self.dy

        if methode_collision not in ['simple', 'avancée', 'complexe']:
            return

        positions = [[balle.x, balle.y] for balle in balles]
        kdtree = cKDTree(positions)
        balles_proches = []
        for i in kdtree.query_ball_point([self.x, self.y], r=2*taille_max):
            balles_proches.append(balles[i])
        balles = balles_proches

        # Vérification des collisions entre balles (si activé)
        for balle in balles:
            if balle == self:
                continue
            if methode_collision == 'simple':
                self, balle = gerer_collision_simple(self, balle)
                self, balle = ajuster_chevauchement(self, balle)
            if methode_collision == 'avancée':
                self, balle = gerer_collision_avancee(self, balle)
                self, balle = ajuster_chevauchement(self, balle)
            if methode_collision == 'complexe':
                self, balle = gerer_collision_complexe(self, balle)
                self, balle = ajuster_chevauchement(self, balle)


def initialiser_balles(nombre_balles, x_limites, _, vitesse_max,
                       taille_min, taille_max, couleurs_possibles):
    """
    Initialise un ensemble de balles avec des propriétés aléatoires, en évitant les chevauchements initiaux.
    """
    np.random.seed(0)
    x_bordures, y_bordures = x_limites[0] + \
        taille_max, x_limites[1] - taille_max

    balles = []
    while len(balles) != nombre_balles:
        balle = Balle(np.random.uniform(x_bordures, y_bordures),
                      np.random.uniform(x_bordures, y_bordures),
                      np.random.uniform(-vitesse_max, vitesse_max),
                      np.random.uniform(-vitesse_max, vitesse_max),
                      max(taille_min, np.random.normal(
                          taille_max/4, taille_max/3)),
                      np.random.choice(couleurs_possibles))

        # Vérifier si la nouvelle balle chevauche avec une balle existante
        chevauche = False
        for autre_balle in balles:
            distance = np.sqrt((balle.x - autre_balle.x) ** 2 + (balle.y - autre_balle.y)**2,
                               dtype=np.float64)
            if distance < balle.rayon + autre_balle.rayon:
                chevauche = True
                break

        # Ajouter la balle à la liste si elle ne chevauche pas
        if not chevauche:
            balles.append(balle)

    return ajuster_chevauchements_tous(balles)


def animer(frame, balles, x_limites, y_limites):
    """Fonction pour animer les balles."""
    plt.clf()
    plt.xlim(x_limites)
    plt.ylim(y_limites)
    for balle in balles[frame]:
        cercle = plt.Circle((balle.x, balle.y),
                            balle.rayon, color=balle.couleur)
        plt.gca().add_patch(cercle)


def main():
    """Fonction principale pour exécuter le code."""
    # Paramètres modifiables
    nombre_balles = 20
    facteur_temps = 50
    x_limites = [0, 1]
    y_limites = [0, 1]
    taille_min = 0.02
    taille_max = 0.1
    vitesse_max = 0.01 / facteur_temps
    couleurs_possibles = ['b', 'g', 'r', 'c', 'm', 'y', 'k',
                          'orange', 'purple', 'pink', 'brown', 'grey']

    methode_collision = sys.argv[1] if len(sys.argv) > 1 else None

    # Initialisation
    # Scénario 1: Collision frontale entre deux balles de rayon et de vitesse égaux.
    # Les deux balles se dirigent l'une vers l'autre sur l'axe des x à une vitesse de 0.001.
    balle1_1 = Balle(0.2, 0.5, 0.001, 0, 0.05, 'r')
    balle1_2 = Balle(0.8, 0.5, -0.001, 0, 0.05, 'g')

    # Scénario 2: Collision frontale entre deux balles de rayon différent mais de vitesse égale.
    # Les deux balles se dirigent l'une vers l'autre sur l'axe des x à une vitesse de 0.001. L'une a un rayon de 0.05, l'autre de 0.07.
    balle2_1 = Balle(0.2, 0.5, 0.001, 0, 0.05, 'r')
    balle2_2 = Balle(0.8, 0.5, -0.001, 0, 0.07, 'g')

    # Scénario 3: Collision frontale entre deux balles de rayon égal mais de vitesse différente.
    # Les deux balles se dirigent l'une vers l'autre sur l'axe des x à des vitesses de 0.001 et -0.002.
    balle3_1 = Balle(0.2, 0.5, 0.001, 0, 0.05, 'r')
    balle3_2 = Balle(0.8, 0.5, -0.002, 0, 0.05, 'g')

    # Scénario 4: Collision diagonale entre deux balles de rayon et de vitesse égaux.
    # Les deux balles se dirigent l'une vers l'autre en diagonale à une vitesse de 0.001 sur les axes x et y.
    balle4_1 = Balle(0.2, 0.2, 0.0002, 0.0002, 0.05, 'r')
    balle4_2 = Balle(0.8, 0.8, -0.0002, -0.0002, 0.05, 'g')

    # Scénario 5: Collision frontale entre deux balles de rayon et de vitesse égaux, avec un petit décalage sur l'axe des y.
    # Les deux balles se dirigent l'une vers l'autre sur l'axe des x à une vitesse de 0.0002, avec un décalage de 0.05 sur l'axe des y.
    balle5_1 = Balle(0.2, 0.5, 0.0002, 0, 0.05, 'r')
    balle5_2 = Balle(0.8, 0.6, -0.0002, 0, 0.1, 'g')

    # Scénario 4: Collision diagonale entre deux balles de rayon différent et de vitesse égaux.
    # Les deux balles se dirigent l'une vers l'autre en diagonale à une vitesse de 0.001 sur les axes x et y.
    balle6_1 = Balle(0.2, 0.2, 0.00005, 0.00005, 0.1, 'r')
    balle6_2 = Balle(0.8, 0.8, -0.00005, -0.00005, 0.05, 'g')

    # Scénario 7: Une balle immobile (comme une boule de billard) est frappée par une autre balle en mouvement.
    balle7_1 = Balle(0.2, 0.5, 0, 0, 0.05, 'r')  # Balle immobile
    balle7_2 = Balle(0.8, 0.5, -0.001, 0, 0.05, 'g')  # Balle en mouvement

    # Scénario 8: Effet de fronde gravitationnelle.
    # Une très petite balle est catapultée à une vitesse élevée après avoir frappé une très grande balle.
    balle8_1 = Balle(0.20, 0.5, 0.002, 0, 0.01, 'r')  # Petite balle
    balle8_2 = Balle(0.8, 0.5, -0.00005, 0, 0.1, 'g')  # Grande balle

    # Regroupement des scénarios dans une liste
    scenarios = [[balle1_1, balle1_2],
                 [balle2_1, balle2_2],
                 [balle3_1, balle3_2],
                 [balle4_1, balle4_2],
                 [balle5_1, balle5_2],
                 [balle6_1, balle6_2],
                 [balle7_1, balle7_2],
                 [balle8_1, balle8_2]]
    #balles = scenarios[4]
    balles = initialiser_balles(nombre_balles, x_limites, y_limites,
                                 vitesse_max, taille_min, taille_max,
                                 couleurs_possibles)

    # Précalcul des positions pour toutes les frames
    frames = 250 * facteur_temps
    positions_pre_calculees = []
    for i in tqdm(range(frames), desc="Génération des frames"):
        positions_pre_calculees.append(deepcopy(balles))
        if methode_collision in ['simple', 'avancée', 'complexe']:
            random.shuffle(balles)
        for balle in balles:
            balle.mettre_a_jour_position(x_limites, y_limites, balles,
                                         methode_collision, taille_max)

        if methode_collision in ['simple', 'avancée', 'complexe']:
            balles = ajuster_chevauchements_tous(balles)

    # Création de l'animation
    fig, ax = plt.subplots()
    ani = animation.FuncAnimation(fig, animer, frames=frames//facteur_temps,
                                  fargs=(positions_pre_calculees[::facteur_temps],
                                         x_limites, y_limites), interval=0)

    print("Rendu de l'animation")
    fig.canvas.mpl_connect('close_event', on_close)
    plt.show()


if __name__ == "__main__":
    main()
