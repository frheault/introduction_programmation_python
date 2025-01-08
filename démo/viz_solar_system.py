"""
=======================
Animation du Système Solaire
=======================

Ce programme crée une animation du système solaire avec des sphères texturées.
On va simuler le mouvement des planètes en orbite autour du soleil.
"""

import itertools
import imageio.v2 as imageio
import numpy as np
import fury

from utils import flouter, effet_vortex, pixeliser, niveaux_de_gris, inverser_couleurs

# Créer une scène où tout sera affiché
scene = fury.window.Scene()

# Créer un panneau avec des boutons pause/démarrer
panel = fury.ui.Panel2D(size=(300, 100), color=(1, 1, 1), align="right")
panel.center = (400, 50)

pause_button = fury.ui.Button2D(
    icon_fnames=[("square", fury.data.read_viz_icons(fname="pause2.png"))]
)
start_button = fury.ui.Button2D(
    icon_fnames=[("square", fury.data.read_viz_icons(fname="play3.png"))]
)

# Ajouter les boutons au panneau
panel.add_element(pause_button, (0.25, 0.33))
panel.add_element(start_button, (0.66, 0.33))


# Informations sur chaque planète : texture, position, et taille
planets_data = [
    {"filename": "textures/8k_mercury.jpg",
     "position": 7,
     "earth_days": 58,
     "scale": (0.4, 0.4, 0.4)
     },
    {"filename": "textures/8k_venus_surface.jpg",
     "position": 9,
     "earth_days": 243,
     "scale": (0.6, 0.6, 0.6)
     },
    {"filename": "textures/1_earth_8k.jpg",
     "position": 11,
     "earth_days": 1,
     "scale": (0.4, 0.4, 0.4) # Essayer une terre plate avec (4, 4, 0.4) (D)
     },
    {"filename": "textures/8k_mars.jpg",
     "position": 13,
     "earth_days": 1,
     "scale": (0.8, 0.8, 0.8)
     },
    {"filename": "textures/colors.png", # À remplacer par une texture de Jupiter (B)
     "position": 16,
     "earth_days": 0.41,
     "scale": (2, 2, 2)
     },
    {"filename": "textures/8k_saturn.jpg",
     "position": 19,
     "earth_days": 0.45,
     "scale": (2, 2, 2)
     },
    {"filename": "textures/2k_uranus.jpg",
     "position": 22,
     "earth_days": 0.70,
     "scale": (1, 1, 1)
     },
    {"filename": "textures/blob.png", # À remplacer par une texture de Neptune (C)
     "position": 25,
     "earth_days": 0.70,
     "scale": (1, 1, 1)
     },
    {"filename":
     "textures/8k_sun.jpg",
     "position": 0,
     "earth_days": 27,
     "scale": (5, 5, 5)
     },
]

TIME_FACTOR = 1  # Essayer des valeurs entre 1 et 100 (A)
for planet in planets_data:
    planet["earth_days"] *= TIME_FACTOR


# Fonction pour initialiser une planète (l'ajouter à la scène avec texture, position et taille)
def init_planet(planet_data):
    # Lecture du fichier de texture
    planet_image = imageio.imread(planet_data["filename"])

    # Modification de la texture (FINAL)
    # planet_image = pixeliser(planet_image, taille_pixel=25)
    # planet_image = niveaux_de_gris(planet_image)
    # planet_image = inverser_couleurs(planet_image)

    # Créer un acteur pour la planète
    planet_actor = fury.actor.texture_on_sphere(planet_image)
    planet_actor.SetPosition(planet_data["position"], 0, 0)
    fury.utils.rotate(planet_actor, rotation=(90, 1, 0, 0))
    fury.utils.rotate(planet_actor, rotation=(180, 0, 0, 1))
    planet_actor.SetScale(planet_data["scale"])
    scene.add(planet_actor)

    return planet_actor

# Créer les planètes en fonction des données
planet_actor_list = list(map(init_planet, planets_data))

# Assigner chaque planète à une variable
mercury_actor = planet_actor_list[0]
venus_actor = planet_actor_list[1]
earth_actor = planet_actor_list[2]
mars_actor = planet_actor_list[3]
jupiter_actor = planet_actor_list[4]
saturn_actor = planet_actor_list[5]
uranus_actor = planet_actor_list[6]
neptune_actor = planet_actor_list[7]
sun_actor = planet_actor_list[8]


# Constante gravitationnelle G et autres constantes pour calculer les orbites
g_exponent = np.float_power(10, -11)
g_constant = 6.673 * g_exponent

m_exponent = 1073741824  # np.power(10, 30)
m_constant = 1.989 * m_exponent

miu = m_constant * g_constant

# Fonction pour calculer la période d'orbite d'une planète
def get_orbit_period(radius):
    return 2 * np.pi * np.sqrt(np.power(radius, 3) / miu)

# Fonction pour calculer la position orbitale d'une planète à un moment donné
def get_orbital_position(radius, time):
    orbit_period = get_orbit_period(radius)
    # Modifier le coefficient 1 pour changer la taille de l'orbite (E)
    x = 1 * radius * np.cos((-2 * np.pi * time) / orbit_period)
    y = 1 * radius * np.sin((-2 * np.pi * time) / orbit_period)
    return x, y

# Faire tourner les planètes autour de leur axe
def rotate_axial(actor, time, radius):
    axis = (0, radius, 0)
    angle = time * TIME_FACTOR / 100
    fury.utils.rotate(actor, rotation=(angle, axis[0], axis[1], axis[2]))
    return angle

# Placer la caméra pour bien voir les planètes
scene.set_camera(position=(-100, 60, 100))

# Créer un gestionnaire de scène (pour afficher l'animation)
showm = fury.window.ShowManager(scene=scene, size=(900, 768), reset_camera=True, order_transparent=True)
scene.add(panel)

# Utiliser un compteur pour gérer le temps
counter = itertools.count()

# Mettre à jour la position des planètes à chaque image
def update_planet_position(r_planet, planet_actor, cnt):
    pos_planet = get_orbital_position(r_planet, cnt)
    planet_actor.SetPosition(pos_planet[0], 0, pos_planet[1])
    return pos_planet

# Calculer l'orbite des planètes (chemin qu'elles suivent)
def calculate_path(r_planet, c):
    return [[get_orbital_position(r_planet, i)[0],
             0, get_orbital_position(r_planet, i)[1]]
        for i in range(c)]

# Rayon des planètes (distances par rapport au Soleil)
r_planets = [p_data["position"] for p_data in planets_data if "sun" not in p_data["filename"]]

# Acteurs des planètes
planet_actors = [mercury_actor, venus_actor, earth_actor, mars_actor,
                 jupiter_actor, saturn_actor, uranus_actor, neptune_actor]

# Données du Soleil
sun_data = {"actor": sun_actor,
            "position": planets_data[8]["position"],
            "earth_days": planets_data[8]["earth_days"]
            }

# Temps de rotation des planètes autour d'elles-mêmes (en jours terrestres)
r_times = [p_data["earth_days"] for p_data in planets_data]

# Calculer les chemins des planètes
planet_tracks = [calculate_path(rplanet, rplanet * 85) for rplanet in r_planets]

# Visualiser les orbites avec des lignes
orbit_actor = fury.actor.line(planet_tracks, colors=(1, 1, 1), linewidth=0.1)
scene.add(orbit_actor)

# Fonction qui sera appelée pour chaque image de l'animation
def timer_callback(_obj, _event):
    cnt = next(counter)
    showm.render()

    # Faire tourner le soleil
    rotate_axial(sun_actor, sun_data["earth_days"], 1)

    # Mettre à jour la position et la rotation des planètes
    for r_planet, p_actor, r_time in zip(r_planets, planet_actors, r_times):
        update_planet_position(r_planet, p_actor, cnt / TIME_FACTOR)
        rotate_axial(p_actor, r_time, r_planet)

    # Arrêter l'animation après 2000 images
    if cnt == 2000:
        showm.exit()

# Actions des boutons pour démarrer et arrêter l'animation
def start_animation(i_ren, _obj, _button):
    showm.add_timer_callback(True, 1, timer_callback)

def pause_animation(i_ren, _obj, _button):
    showm.destroy_timers()

start_button.on_left_mouse_button_clicked = start_animation
pause_button.on_left_mouse_button_clicked = pause_animation

# Lancer l'animation
showm.add_timer_callback(True, 1, timer_callback)
showm.start()
