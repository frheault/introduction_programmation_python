#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


def section(text):
    print('\033[1m{}\033[0m'.format(text))


# --------------------------------- #


import numpy as np
import matplotlib.pyplot as plt


# --------------------------------- #


section('Basic manipulations')
print('1D Array')
array = np.array([0.5,1.5,2.5,3.5,4.5, 5.5, 6.5, 7.5, 8.5, 9.5])
print('Simplest initialization', array)
print('Attribue', array.shape, array.dtype)

array = np.array([0.5,1.5,2.5,3.5,4.5, 5.5, 6.5, 7.5, 8.5, 9.5],
                 dtype=np.int16)
print('Changing data type', array)
print('Attribue', array.shape, array.dtype)

print('Indexing', array[4], array[5])
print('Slicing 1', array[4:7], array[:3], array[7:])
print('Slicing 2', array[-1], array[:5:-1], array[1::2])


# --------------------------------- #


section('Basic operation')
array = np.ones((10,))
print('ones', array)
array[0:5] = 0.5
print('modified', array)
array = array*3 + 7
print('multiply', array)

print('random', np.random.random((5,)))
print('arange', np.arange(5))
print('arange', np.linspace(10, 25, 4))


# --------------------------------- #


section('Plotting 1D data')

x = np.arange(100)
y = np.arange(100)
plt.plot(x,y)
plt.plot(x,(0.1*y)**2)
plt.plot(x, np.log((y+1)**3))
plt.show()

y = np.linspace(-2*np.pi, 2*np.pi, 100)
plt.plot(x,np.sin(y))
plt.plot(x,np.cos(y))
plt.show()


# --------------------------------- #


section('2D manipulations')
print('2D Array')
array = np.array([[1,2,3], [4,5,6], [7,8,9]])
print('Initialization')
print(array)

print('Attribue', array.shape, array.dtype)
print('Indexing', array[2, :], array[:, 2])


# --------------------------------- #


section('2D operations')
identity = np.eye(3)*2

print('identity (2x)')
print(identity)

array_1 = np.arange(1,4)
array_2 = np.array([2,2,2])
print('array_1', array_1)
print('array_2', array_2)

print(np.dot(array, identity), array_1*array_2,
      np.all(np.equal(np.dot(array, identity), array_1*array_2)))


# --------------------------------- #


section('Plotting 2D data')
fig, axs = plt.subplots(1, 2, figsize=(15, 8))
axs[0].imshow(np.eye(10))
axs[1].imshow(np.random.random((10,10)))
plt.show()


# --------------------------------- #


section('Contrast')
# Matplotlib automatically determines the contrast based on MIN/MAX
from mpl_toolkits.axes_grid1 import make_axes_locatable
fig, axs = plt.subplots(1, 5, figsize=(20, 4))
array = np.random.random((10,10))
for i, ax in enumerate(axs):
    array[6,8] += 1*i
    print(i, 'min', np.min(array), 'max', np.max(array), 'avg', np.average(array), 'std', np.std(array))
    im = ax.imshow(array)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im, cax=cax, orientation='vertical')
    
fig.tight_layout()
plt.show()


# --------------------------------- #


section('Masking')
from mpl_toolkits.axes_grid1 import make_axes_locatable
fig, axs = plt.subplots(1, 5, figsize=(20, 4))
array = np.random.random((5, 10,10))
array[0, :, 5] = 0
array[1, 4, :] = 0
array[2, 2:7, 2:5] = 0
array[3, :, :] = np.tril(array[3, :, :])
array[4, :, :] = np.triu(array[4, :, :])
for i, ax in enumerate(axs):
    im = ax.imshow(array[i])
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im, cax=cax, orientation='vertical')
    
fig.tight_layout()
plt.show()


# --------------------------------- #


section('Thresholding')
from mpl_toolkits.axes_grid1 import make_axes_locatable
fig, axs = plt.subplots(1, 5, figsize=(20, 4))
array = np.random.random((10,10))

for i, ax in enumerate(axs):
    tmp = array.copy()
    tmp[array > 0.2*(i+1)] = 0
    im = ax.imshow(tmp, vmin=0, vmax=1)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    fig.colorbar(im, cax=cax, orientation='vertical')
    
fig.tight_layout()
plt.show()


# --------------------------------- #




