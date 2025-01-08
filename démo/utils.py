#!/usr/bin/env python

import os
import numpy as np 
import nibabel as nib
from scipy.ndimage import convolve
from skimage.transform import swirl

axis_enum = {'sagittal':0, 'coronal':1,'axial':2}

def split_name_with_nii(filename):
    base, ext = os.path.splitext(filename)

    if ext == ".gz":
        # Test if we have a .nii additional extension
        tmp_base, extra_ext = os.path.splitext(base)

        if extra_ext == ".nii":
            ext = extra_ext + ext
            base = tmp_base

    return base, ext


def get_slice(volume_3d, axis_name, indice=None):
    # Personal preference for orientation (nose up for axial, nose left for sagittal, nose first for coronal)
    # Operation done in 2D, still very fast and easier to understand
    if axis_name == 'sagittal':
        if indice is None:
            indice = volume_3d.shape[0] // 2
        slice_2d = np.rot90(volume_3d[indice,:,:])
    elif axis_name == 'coronal':
        if indice is None:
            indice = volume_3d.shape[1] // 2
        slice_2d = np.rot90(np.flip(volume_3d, axis=1)[:,indice,:])
    elif axis_name == 'axial':
        if indice is None:
            indice = volume_3d.shape[2] // 2
        slice_2d = np.rot90(np.flip(volume_3d, axis=2)[:,:,indice])
    else:
        raise ValueError('{0} is not a valid axis name'.format(axis))

    return slice_2d


def get_nifti_data(img):
    return np.asanyarray(img.dataobj)


def get_nifti_header_info(img):
    header = img.header
    affine = header.get_best_affine()
    dimensions = header['dim'][1:4]
    voxel_sizes = header['pixdim'][1:4]

    if not affine[0:3, 0:3].any():
        raise ValueError(
            'Invalid affine, contains only zeros.'
            'Cannot determine voxel order from transformation')
    voxel_order = ''.join(nib.aff2axcodes(affine))
    return affine, dimensions, voxel_sizes, voxel_order


def summarize_intensities(data):
    total_voxel = np.prod(data.shape)
    non_zeros = np.count_nonzero(data)
    mean = np.mean(data[data > 0])
    std = np.std(data[data > 0])
    median = np.percentile(data[data > 0], 50)
    iqr = np.percentile(data[data > 0], 75) - \
        np.percentile(data[data > 0], 25)
    max_val = np.max(data[data > 0])
    min_val = np.min(data[data > 0])
    return total_voxel, non_zeros, \
            round(mean, 3), round(std, 3), \
            round(median, 3), round(iqr, 3), \
            round(max_val, 3), round(min_val, 3)


def generate_square(shape, corner, size):
    data = np.zeros(shape)
    x_min = int(corner[0])
    y_min = int(corner[1])
    x_max = int(x_min + size[0])
    y_max = int(y_min + size[1])
    data[x_min:x_max, y_min:y_max] = 1

    return data


def flouter(image, taille_noyau=5):
    """
    Applique un effet de flou simple en moyennant les pixels voisins.
    
    Paramètres :
        image (np.ndarray) : Tableau d'image d'entrée.
        taille_noyau (int) : Taille du noyau de moyennage.
        
    Retour :
        np.ndarray : Image floutée.
    """
    noyau = np.ones((taille_noyau, taille_noyau)) / (taille_noyau ** 2)
    image_floutee = np.zeros_like(image)
    
    # Appliquer le flou sur chaque canal (R, G, B)
    for i in range(3):
        image_floutee[:, :, i] = convolve(image[:, :, i], noyau)
    
    return image_floutee.astype(np.uint8)

def effet_vortex(image, intensité=20, rayon=5000):
    """
    Applique un effet de distorsion en tourbillon à l'image.
    
    Paramètres :
        image (np.ndarray) : Tableau d'image d'entrée.
        intensité (float) : Intensité du tourbillon.
        rayon (int) : Rayon de l'effet de tourbillon depuis le centre.
        
    Retour :
        np.ndarray : Image avec l'effet de tourbillon.
    """
    image_vortex = swirl(image, strength=intensité, radius=rayon, mode='wrap')
    
    return (image_vortex * 255).astype(np.uint8)

def pixeliser(image, taille_pixel=25):
    """
    Réduit la résolution de l'image en la pixelisant.
    
    Paramètres :
        image (np.ndarray) : Tableau d'image d'entrée.
        taille_pixel (int) : Taille des blocs de pixels. Valeur plus grande = plus de pixelisation.
        
    Retour :
        np.ndarray : Image pixelisée.
    """
    # Obtenir la forme originale de l'image
    h, w, c = image.shape
    
    # Redimensionner en plus petites dimensions avec un facteur taille_pixel
    image_reduite = image[::taille_pixel, ::taille_pixel]
    
    # Répéter pour revenir à la taille d'origine
    image_pixelisee = np.repeat(np.repeat(image_reduite, taille_pixel, axis=0), taille_pixel, axis=1)
    
    return image_pixelisee[:h, :w, :c]

def niveaux_de_gris(image):
    """
    Convertit l'image en niveaux de gris en moyennant les valeurs RGB.
    
    Paramètres :
        image (np.ndarray) : Tableau d'image d'entrée.
        
    Retour :
        np.ndarray : Image en niveaux de gris.
    """
    # Convertir l'image en niveaux de gris en moyennant les canaux RGB
    image_gris = np.mean(image, axis=2, keepdims=True)
    
    # Répliquer les valeurs de niveaux de gris sur 3 canaux pour compatibilité avec d'autres fonctions
    image_gris = np.repeat(image_gris, 3, axis=2)
    
    return image_gris.astype(np.uint8)

def inverser_couleurs(image):
    """
    Inverse les couleurs de l'image.
    
    Paramètres :
        image (np.ndarray) : Tableau d'image d'entrée.
        
    Retour :
        np.ndarray : Image avec couleurs inversées.
    """
    return 255 - image
