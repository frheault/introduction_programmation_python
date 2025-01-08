#!/usr/bin/env python
# coding: utf-8

# --------------------------------- #


import os
import numpy as np 
import matplotlib.pyplot as plt
import nibabel as nib

from utils import split_name_with_nii, get_slice, get_nifti_data, get_nifti_header_info, summarize_intensities


# --------------------------------- #


np.set_printoptions(suppress=True)
# Naviguate in a folder recursively
for root, dirs, files in os.walk("data/bids/", topdown=False):
    for name in files:
        path = os.path.join(root, name)
        base, ext = split_name_with_nii(path)
        if ext in ['.nii', '.nii.gz']:
            print(path)
            curr_img = nib.load(path)
            curr_data = get_nifti_data(curr_img)
            if curr_data.ndim > 3:
                last_dim = curr_data.shape[-1]
                curr_data = curr_data[..., 0]
            else:
                last_dim = 0

            aff, dims, vox_sizes, vox_order = \
                get_nifti_header_info(curr_img)
            fig, axs = plt.subplots(1, 3, figsize=(9, 27))
            for i, axis in enumerate(['axial', 'coronal', 'sagittal']):
                curr_slice = get_slice(curr_data, axis)
                axs[i].imshow(curr_slice, cmap='gray')
            print(np.round(aff, 3))
            print(dims, np.round(vox_sizes, 3), vox_order, curr_data.dtype)
            print(summarize_intensities(curr_data))
            if last_dim:
                print('4D size: {}'.format(last_dim))
            plt.show()
            print('===============================')

