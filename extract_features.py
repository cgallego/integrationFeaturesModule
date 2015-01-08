# -*- coding: utf-8 -*-
"""
Created on Tue Apr 01 10:47:40 2014

This script will load volumes, Load a lesion Segmentation (VOI), Visualize volumes
and then extract Dynamic, Morphology and Texture features from the VOI.

@ author (C) Cristina Gallego, University of Toronto, 2013
----------------------------------------------------------------------
"""

from convertNumpy import *
from inputs_init import *
from display import *
from features_dynamic import *
from features_morphology import *
from features_texture import *

###################################################### 

# Load the dictionary back from the pickle file.
print "\n Loading Data..."

#To create dataset for testing return a vtImagdata list and a vtkimagedata mask
convertImages = convertNumpy()
[series_path, phases_series] = convertImages.testVTK2pOutputfile()

############################## 
# Convert npImagesandMask to list of vtkImageData 
npImagesandMask = convertImages.npDICOMImages

# at this point proceed with all image data needed stored in npImagesandMask and mask data in meshlesion3D    
print "\n Reload and visualize"
loadNumpyDisplay = Display()

# Convert back to vtk objects for actual use
ImagedataVTK=[] 
for i in range(npImagesandMask['nvol']):
    vtkimage = convertImages.convertDCEArray2vtkImage(npImagesandMask, i)
    ImagedataVTK.append( vtkimage )


# transform to dicom to get same coords for mask        
[t_ImagedataVTK, t_cube] = loadNumpyDisplay.dicomTransform(ImagedataVTK[0], npImagesandMask['image_pos_pat'], npImagesandMask['image_ori_pat'])
loadNumpyDisplay.visualize(ImagedataVTK, npImagesandMask['image_pos_pat'], npImagesandMask['image_ori_pat'], sub=True, postS=1, interact=False)

# creat VOI 3D mesh from binary mask
npmask = npImagesandMask['mask']
meshlesion3D = convertImages.createMeshfromMask(npmask, t_ImagedataVTK, npImagesandMask)

#add segmentation
lesion3D_mesh = loadNumpyDisplay.addSegment(meshlesion3D, [0,1,0], interact=True)

###### Extract Dynamic features
print "\n Extract Dynamic features... from contour"
loadDynamic = Dynamic()
dynamicfeatures_contour = loadDynamic.extractfeatures_contour(ImagedataVTK, npImagesandMask['image_pos_pat'], npImagesandMask['image_ori_pat'], series_path, phases_series, meshlesion3D)
print dynamicfeatures_contour

print "\n Extract Dynamic features... from all/inside pixels"
loadDynamic = Dynamic()
dynamicfeatures_inside = loadDynamic.extractfeatures_inside(ImagedataVTK, npImagesandMask['image_pos_pat'], npImagesandMask['image_ori_pat'], series_path, phases_series, meshlesion3D)
print dynamicfeatures_inside

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



    
    
    
    
    
    
    
    
    
    
    
        
        
    