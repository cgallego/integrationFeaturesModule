# -*- coding: utf-8 -*-
"""
Created on Tue Apr 01 10:47:40 2014

This script will load volumes, Load a lesion Segmentation (VOI), Visualize volumes
and then extract Dynamic, Morphology and Texture features from the VOI.

@ author (C) Cristina Gallego, University of Toronto, 2013
----------------------------------------------------------------------
"""

from convertNumpy import *
from display import *
from features_dynamic import *
from features_morphology import *
from features_texture import *
import pickle

###################################################### 

# Load the dictionary back from the pickle file.
print "\n Loading Data..."

pkl_file = open('npDICOMImages.p', 'rb')
npImagesandMask = pickle.load(pkl_file)
pkl_file.close()

# create convertor instance
convertor = convertNumpy()

# at this point proceed with all image data needed stored in npImagesandMask and mask data in meshlesion3D    
# Convert back to vtk objects for actual use
ImagedataVTK=[] 
for i in range(npImagesandMask['nvol']):
    vtkimage = convertor.convertDCEArray2vtkImage(npImagesandMask, i)
    ImagedataVTK.append( vtkimage )


print "\n Reload and visualize"
loadNumpyDisplay = Display()

# transform to dicom to get same coords for mask        
[t_ImagedataVTK, t_cube] = loadNumpyDisplay.dicomTransform(ImagedataVTK[0], npImagesandMask['image_pos_pat'], npImagesandMask['image_ori_pat'])

# creat VOI 3D mesh from binary mask
npmask = npImagesandMask['mask']
meshlesion3D = convertor.createMeshfromMask(npmask, t_ImagedataVTK, npImagesandMask)

#add segmentation
loadNumpyDisplay.addSegment(meshlesion3D)

# visualize image and mask   
loadNumpyDisplay.addSegment(meshlesion3D)
loadNumpyDisplay.visualize(ImagedataVTK, npImagesandMask['image_pos_pat'], npImagesandMask['image_ori_pat'], sub=True, postS=1, interact=True)

###### Extract Dynamic features
print "\n Extract Dynamic features..."
loadDynamic = Dynamic()
dynamicfeatures = loadDynamic.extractfeatures(ImagedataVTK, npImagesandMask, npImagesandMask['image_pos_pat'], npImagesandMask['image_ori_pat'], meshlesion3D)
print dynamicfeatures

###### Extract Morphology features
print "\n Extract Morphology features..."
loadMorphology = Morphology()
morphofeatures = loadMorphology.extractfeatures(ImagedataVTK, npImagesandMask['image_pos_pat'], npImagesandMask['image_ori_pat'], meshlesion3D)
print morphofeatures

###### Extract Texture features
print "\n Extract Texture features..."
loadTexture = Texture()
texturefeatures = loadTexture.extractfeatures(ImagedataVTK, npImagesandMask['image_pos_pat'], npImagesandMask['image_ori_pat'], loadMorphology.VOI_efect_diameter, loadMorphology.lesion_centroid)
print texturefeatures


    
    
    
    
    
    
        
        
    

