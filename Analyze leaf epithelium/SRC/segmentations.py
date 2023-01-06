from tifffile import imread
import napari
from skimage import restoration
from skimage import color
import skimage.filters as filters
import pandas as pd
from skimage.measure import label, regionprops, regionprops_table
from skimage.morphology import disk, label
from skimage import morphology
from skimage.feature import peak_local_max
from skimage.morphology import convex_hull_image
from skimage.segmentation import watershed
from scipy import ndimage as ndi
import numpy as np
from skimage import data             #source : https://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.median
from skimage.filters import median
import pandas as pd
import skimage
import glob


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


def segmentation_stomates(image_pathway) :
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


def segmentation_normal(image_pathway) :
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


def segmentation_normal_veines(image_pathway) :
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


def segmentation_puzzle(image_pathway) :
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


def segmentation_puzzle_veins(image_pathway) :
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


def segmentation_puzzle_sombre(image_pathway) :
    # read image as numpy array
    img = imread(image_pathway)
    
    img_gray = color.rgb2gray(img)
    
    #Median filter      
    median_img = median(img_gray, disk(7))

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


def counting() :
    # each colony correspond to a unique value
    # get individual unique value
    unique_values = np.unique(labelled)
    # get the number of unique value
    nb_cells = len(unique_values)  
    
    return nb_cells