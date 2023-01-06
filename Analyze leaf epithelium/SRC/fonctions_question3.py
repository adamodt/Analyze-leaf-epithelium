#!/usr/bin/env python
# coding: utf-8

# ## Fonctions

# In[2]:


import napari
import tifffile
from tifffile import imread
import matplotlib as plt
import numpy as np
from skimage import measure
import pandas as pd
import glob
import skimage
from skimage import data
from skimage import morphology
from skimage.morphology import disk
from skimage.filters import median  
import skimage.filters as filters
from skimage import color
from skimage import restoration
from skimage.filters import threshold_otsu


# ### Rondes + veines

# In[6]:


def segmentation_rondes_veines(image_pathway) :
    # read image as numpy array
    img = imread(image_pathway)
    
    img_gray = color.rgb2gray(img)
    
    #Median filter      
    median_img = median(img_gray, disk(10))  

    #Threshold
    block_size = 151

    local_threshold = filters.threshold_local(median_img, block_size=block_size)
    mask = median_img > local_threshold
    
    #Remove noise
    mask1 = morphology.remove_small_objects(mask.astype(bool), 800) #Valeur ajustable selon l'image
    #Closing holes
    mask2 = morphology.remove_small_holes(mask1.astype(bool), 5000) #Valeur ajustable selon l'image
    #Binary opening
    mask3 = morphology.binary_opening(mask2.astype(bool), morphology.disk(6)) #Valeur ajustable selon l'image

    labelled = skimage.morphology.label(mask3)
    return labelled


# ### Stomates

# In[3]:


def segmentation_stomates(image_pathway) :
    # read image as numpy array
    img = imread(image_pathway)
    
    img_gray = color.rgb2gray(img)
    
    #Median filter      
    median_img = median(img_gray, disk(7))  

    #Threshold
    block_size = 35

    local_threshold = filters.threshold_local(median_img, block_size=block_size)
    mask = median_img > local_threshold
    
    #Remove noise
    mask1 = morphology.remove_small_objects(mask.astype(bool), 900) #Valeur ajustable selon l'image
    #Closing holes
    mask2 = morphology.remove_small_holes(mask1.astype(bool), 1200) #Valeur ajustable selon l'image
    #Binary opening
    mask3 = morphology.binary_opening(mask2.astype(bool), morphology.disk(6)) #Valeur ajustable selon l'image
    
    labelled = skimage.morphology.label(mask3)
    return labelled


# ### Normales

# In[4]:


def segmentation_normal(image_pathway) :
    # read image as numpy array
    img = imread(image_pathway)
    
    img_gray = color.rgb2gray(img)
   
    #Median filter      
    median_img = median(img_gray, disk(7))

    #Threshold
    block_size = 151

    local_threshold = filters.threshold_local(median_img, block_size=block_size)
    mask = median_img > local_threshold

    #Remove noise
    mask1 = morphology.remove_small_objects(mask.astype(bool), 400) #Valeur ajustable selon l'image
    #Closing holes
    mask2 = morphology.remove_small_holes(mask1.astype(bool), 900) #Valeur ajustable selon l'image
    #Binary opening
    mask3 = morphology.binary_opening(mask2.astype(bool), morphology.disk(6)) #Valeur ajustable selon l'image

    labelled = skimage.morphology.label(mask3)
    return labelled


# ### Normales + veines

# In[5]:


def segmentation_normal_veines(image_pathway) :
    # read image as numpy array
    img = imread(image_pathway)
    
    img_gray = color.rgb2gray(img)
    
    #Median filter      
    median_img = median(img_gray, disk(10))

    #Threshold
    block_size = 151

    local_threshold = filters.threshold_local(median_img, block_size=block_size)
    mask = median_img > local_threshold

    #Remove noise
    mask1 = morphology.binary_dilation(mask.astype(bool), morphology.disk(5))
    mask2 = morphology.remove_small_holes(mask1.astype(bool), 800)
    mask3 = morphology.binary_opening(mask2.astype(bool), morphology.disk(11))

    labelled = skimage.morphology.label(mask3)
    return labelled


# ### Puzzle

# In[6]:


def segmentation_puzzle(image_pathway) :
    # read image as numpy array
    img = imread(image_pathway)
    
    img_gray = color.rgb2gray(img)
  
    #Median filter      
    median_img = median(img_gray, disk(7))

    #Threshold
    block_size = 115

    local_threshold = filters.threshold_local(median_img, block_size=block_size)
    mask = median_img > local_threshold

    #Remove noise
    mask1 = morphology.remove_small_objects(mask.astype(bool), 700) #Valeur ajustable selon l'image
    #Closing holes
    mask2 = morphology.remove_small_holes(mask1.astype(bool), 100) #Valeur ajustable selon l'image
    #Binary opening
    mask3 = morphology.binary_opening(mask2.astype(bool), morphology.disk(8)) #Valeur ajustable selon l'image

    labelled = skimage.morphology.label(mask3)
    return labelled


# ### Puzzle + Veines

# In[7]:


def segmentation_puzzle_veines(image_pathway) :
    # read image as numpy array
    img = imread(image_pathway)
    
    img_gray = color.rgb2gray(img)
    
    #Median filter      
    median_img = median(img_gray, disk(10))

    #Threshold
    block_size = 171

    local_threshold = filters.threshold_local(median_img, block_size=block_size)
    mask = median_img > local_threshold

    #Remove noise
    mask1 = morphology.remove_small_objects(mask.astype(bool), 800) #Valeur ajustable selon l'image
    #Closing holes
    mask2 = morphology.remove_small_holes(mask1.astype(bool), 800) #Valeur ajustable selon l'image
    #Binary opening
    mask3 = morphology.binary_opening(mask2.astype(bool), morphology.disk(2)) #Valeur ajustable selon l'image
    
    labelled = skimage.morphology.label(mask3)
    return labelled


# ### Puzzle sombre

# In[8]:


def segmentation_puzzle_sombre(image_pathway) :
    # read image as numpy array
    img = imread(image_pathway)
    
    img_gray = color.rgb2gray(img)
    
    #Median filter      
    median_img = median(img_gray, disk(7))
    #viewer.add_image(median_img)

    #Threshold
    block_size = 301

    local_threshold = filters.threshold_local(median_img, block_size=block_size)
    mask = median_img > local_threshold
    
    #Remove noise
    mask1 = morphology.remove_small_holes(mask.astype(bool), 2000)
    mask2 = morphology.binary_dilation(mask1.astype(bool), morphology.disk(3))
    mask3 = morphology.remove_small_holes(mask2.astype(bool), 2000)
    mask4 = morphology.binary_opening(mask3.astype(bool), morphology.disk(4))
    mask5 = morphology.remove_small_objects(mask4.astype(bool), 2000)
    
    labelled = skimage.morphology.label(mask5)
    return labelled


# ### Convex hull perimeter

# In[9]:


def convex_perimeter(labelled):
        convex_mask = morphology.convex_hull_image(labelled)
        convex_perimeter = measure.perimeter(convex_mask)
        return convex_perimeter


# ### Lobeyness

# In[10]:


def lobeyness (labelled):
    props = measure.regionprops_table(
        labelled,
        properties=('label','area','perimeter'),
        extra_properties=(convex_perimeter,))

    df = pd.DataFrame(props)
    df = df.assign(lobeyness = df['perimeter']/df['convex_perimeter'])
    return df

