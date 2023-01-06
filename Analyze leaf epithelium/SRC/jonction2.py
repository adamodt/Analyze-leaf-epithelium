import napari
import skimage.data
import skimage.filters
import numpy as np
from napari.types import LabelsData
from skimage.filters import threshold_otsu 
from skimage import morphology
from skimage.morphology import disk
from skimage.filters import median   
from skimage.morphology import skeletonize
import matplotlib.pyplot as plt
from skimage.morphology import square, cube 
import skimage.filters.rank as rank
from skimage import measure
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from skimage import color
from tifffile import imread
import matplotlib as plt
import glob
from skimage.morphology import disk, binary_erosion

def masque_jonction_puzzle(image_pathway):
    #import tifffile
    #open image
    img = imread(image_pathway)
    
    #image in black and white
    img_gray = color.rgb2gray(img)
    
    #median filter
    median_img = median(img_gray, disk(7)) 
    
    #treshold
    block_size = 115 
    local_threshold = skimage.filters.threshold_local(img_gray, block_size=block_size)
    mask_jonction = img_gray < local_threshold
    
    ##Remove noise
    mask1 = morphology.remove_small_objects(mask_jonction.astype(bool), 700)

    #Closing holes
    mask2 = morphology.remove_small_holes(mask1.astype(bool), 100)
    
    #Binary opening
    mask3 = morphology.binary_opening(mask2.astype(bool), morphology.disk(1))
    
    #skeleton
    skeleton = skeletonize(mask3)
    return(skeleton)

def masque_jonction_normale(image_pathway):
    #import tifffile
    #open image
    img = imread(image_pathway)
    
    #image in black and white
    img_gray = color.rgb2gray(img)
    
    #median filter
    median_img = median(img_gray, disk(7)) 
    
    #treshold
    block_size = 115 
    local_threshold = skimage.filters.threshold_local(img_gray, block_size=block_size)
    mask_jonction = img_gray < local_threshold
    
    ##Remove noise
    mask1 = morphology.remove_small_objects(mask_jonction.astype(bool), 800)

    #Closing holes
    mask2 = morphology.remove_small_holes(mask1.astype(bool), 400)
    
    #Binary opening
    mask3 = morphology.binary_opening(mask2.astype(bool), morphology.disk(1))
    
    #skeleton
    skeleton = skeletonize(mask3)
    return(skeleton)

def masque_jonction_puzzle_sombre(image_pathway):
    #import tifffile
    #open image
    img = imread(image_pathway)
    
    #image in black and white
    img_gray = color.rgb2gray(img)
    
    #median filter
    median_img = median(img_gray, disk(7)) 
    
    #treshold
    block_size = 115 
    local_threshold = skimage.filters.threshold_local(img_gray, block_size=block_size)
    mask_jonction = img_gray < local_threshold
    
    ##Remove noise
    mask1 = morphology.remove_small_objects(mask_jonction.astype(bool), 800)

    #Closing holes
    mask2 = morphology.remove_small_holes(mask1.astype(bool), 400)
    
    #Binary opening
    mask3 = morphology.binary_opening(mask2.astype(bool), morphology.disk(1))
    
    #skeleton
    skeleton = skeletonize(mask3)
    return(skeleton)

def masque_jonction_puzzle_veines(image_pathway):
    #import tifffile
    #open image
    img = imread(image_pathway)
    
    #image in black and white
    img_gray = color.rgb2gray(img)
    
    #median filter
    median_img = median(img_gray, disk(10)) 
    
    #treshold
    block_size = 115 
    local_threshold = skimage.filters.threshold_local(img_gray, block_size=block_size)
    mask_jonction = img_gray < local_threshold
    
    ##Remove noise
    mask1 = morphology.remove_small_objects(mask_jonction.astype(bool), 6000)
    
    #Erosion
    mask2 = binary_erosion(mask1, disk(5, dtype=bool))
    
    #Remove small objects
    mask3 = morphology.remove_small_objects(mask2.astype(bool), 6000)
    
    #skeleton
    skeleton = skeletonize(mask3)
    return(skeleton)

def masque_jonction_normal_veines(image_pathway):
    #import tifffile
    #open image
    img = imread(image_pathway)
    
    #image in black and white
    img_gray = color.rgb2gray(img)
    
    #median filter
    median_img = median(img_gray, disk(10)) 
    
    #treshold
    block_size = 115 
    local_threshold = skimage.filters.threshold_local(median_img, block_size=block_size)
    mask_jonction1 = median_img < local_threshold
    
    #Binary opening
    mask1 = morphology.binary_dilation(mask_jonction1.astype(bool), morphology.disk(5))
    
    
    #Closing holes
    mask2 = morphology.remove_small_holes(mask1.astype(bool), 800)
    
    #Remove small objects
    mask3 = morphology.remove_small_objects(mask2.astype(bool), 3000)
    
    
    #skeleton
    skeleton = skeletonize(mask3)
    return(skeleton)


def masque_jonction_stomates(image_pathway):
    #import tifffile
    #open image
    img = imread(image_pathway)
    
    #image in black and white
    img_gray = color.rgb2gray(img)
    
    #median filter
    median_img = median(img_gray, disk(7)) 
    
    #treshold
    block_size = 115 
    local_threshold = skimage.filters.threshold_local(median_img, block_size=block_size)
    mask_jonction1 = median_img < local_threshold
    
     #Remove noise
    mask1 = morphology.remove_small_objects(mask_jonction1.astype(bool), 900) 
    #Closing holes
    mask2 = morphology.remove_small_holes(mask1.astype(bool), 1200) 
    #Binary opening
    mask3 = morphology.binary_opening(mask2.astype(bool), morphology.disk(2))    
    
    #skeleton
    skeleton = skeletonize(mask3)
    return(skeleton)

def masque_rondes_veines(image_pathway):
    #import tifffile
    #open image
    img = imread(image_pathway)
    
    #image in black and white
    img_gray = color.rgb2gray(img)
    
    #median filter
    median_img = median(img_gray, disk(10)) 
    
    #treshold
    block_size = 115 
    local_threshold = skimage.filters.threshold_local(median_img, block_size=block_size)
    mask_jonction1 = median_img < local_threshold
    
     #Remove noise
    mask1 = morphology.remove_small_objects(mask_jonction1.astype(bool), 1000) 
    #Closing holes
    mask2 = morphology.remove_small_holes(mask1.astype(bool), 700) 
    #Binary opening
    mask3 = morphology.binary_opening(mask2.astype(bool), morphology.disk(2))    
    
    #skeleton
    skeleton = skeletonize(mask3)
    return(skeleton)

def jonctions_totales(skeleton):
    
    #get the neighbouring pixel
    img = skeleton.astype("uint8")
    img2 = rank.sum(img, square(2))

    #transform all junctions with 1 and non junction with 0
    mask_corrected = img2.copy()
    mask_corrected[img2 > 2] = 1
    mask_corrected[img2 <= 2] = 0

    #label all jonctions 
    labelled = skimage.morphology.label(mask_corrected)

    #get the number of total junctions
    props = measure.regionprops_table(
        labelled,
        properties=['label',"centroid"] 
        )
    df_junction = pd.DataFrame(props)
    total_junction = len(df_junction["label"])
    
    return(df_junction)

def jonctions_non_triangulaires (df_junction) :
     #creating a list with all the centroids coordinates:
    centroids = np.array([list(df_junction["centroid-0"]),list(df_junction["centroid-1"])]).T

    #find nearest neighbors :
    X = centroids
    nbrs = NearestNeighbors(n_neighbors=2, algorithm="ball_tree").fit(X)
    distances, indices = nbrs.kneighbors(X)

    #determine non triangular junctions:
    j4 = np.unique(indices[distances[:, 1] < 5])

    #get the centroid coordinates of non triangular junctions:
    df_j4 = df_junction[df_junction["label"].isin(j4)]
    return(df_j4)