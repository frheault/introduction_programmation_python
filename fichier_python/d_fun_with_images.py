#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


import imageio.v2 as iio
import numpy as np
import os

# Load the image and declare functions
input_filename = 'data/man_computer_smiling.jpg'
ori_img = iio.imread(input_filename)

def save_anim(data_list, filename, fps=30):
    _, ext = os.path.splitext(filename)
    if ext not in ['.gif', '.mp4']:
        raise ValueError('Datatype {} not supported!'.format(ext))
    iio.mimsave(filename, data_list, fps=fps)
    
def generate_anim(data, func, tot_frame=100):
    anim = []
    for i in range(tot_frame):
        anim.append((func(data, (i, tot_frame))))
    return anim


# --------------------------------- #


# Function that will roll around one axis
def roll(data, iter_tuple):
    i = (data.shape[0] // iter_tuple[1]) * iter_tuple[0]
    return np.roll(data, i, axis=0)

data_list = generate_anim(ori_img, roll, tot_frame=ori_img.shape[0])
save_anim(data_list, 'roll.gif', fps=30)


# --------------------------------- #


from PIL import Image

# Using a libary to resample down and then up an image (pixelate/blur)
def pixelate(data, iter_tuple):
    i = iter_tuple[0] // (iter_tuple[1] // 10)
    x = data.shape[0] // (i+1)
    y = data.shape[1] // (i+1)
    
    tmp = Image.fromarray(data)
    down = tmp.resize((y,x), Image.NEAREST)
    up = down.resize((data.shape[1], data.shape[0]), Image.NEAREST)
    return np.array(up).astype(np.uint8)

data_list = generate_anim(ori_img, pixelate, tot_frame=100)
save_anim(data_list, 'pixelate.gif', fps=25)


# --------------------------------- #


# From a list of images, generate a GIF
filenames = sorted(os.listdir('data/frames/'))
data_list = []
for filename in filenames:
    curr_frame = iio.imread(os.path.join('data/frames/',
                                        filename))
    data_list.append(curr_frame)
save_anim(data_list, 'goku.gif', fps=15)


# --------------------------------- #




