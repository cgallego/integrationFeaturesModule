Extract_Features Module:
Description:
Module that loads up data and segmented VOI to then extract dynamic morphological and texture features.

From a DICOM IMAGE folder for a StudyID/ExamID/SeriesID/LesionID:
===================================
1. Run script extract_features.py
will create a pickled structure with the required inputs for feature selection.

To interact or not with display, turn to False the interact parameter

From Pickle dictionary input:
===================================
1. Run script run_allfeatures.py
Loads pickle structure "npDICOMImages.p" with the above inputs.

Required inputs: Dictionary with:
dict_keys([
* 'im0', 	float64 array of pre-contrast volume
* 'im1', 	float64 array of post-contrast1 volume
* 'im2',	float64 array of post-contrast2 volume 
* 'im3', 	float64 array of post-contrast3 volume
* 'im4', 	float64 array of post-contrast4 volume
* 'mask', float64 array 3D volume of lesion segmentation, zeros in background, ones in foreground 

* 'ti0' 	dicom tag [0x0008,0x0032] for Volume Series im0
* 'ti1', 	dicom tag [0x0008,0x0032] for Volume Series im1
* 'ti2', 	dicom tag [0x0008,0x0032] for Volume Series im2
* 'ti3', 	dicom tag [0x0008,0x0032] for Volume Series im3
* 'ti4', 	dicom tag [0x0008,0x0032] for Volume Series im4
* 'image_ori_pat', 	dicom tag [0x0020,0x0037]
* 'image_pos_pat', 	dicom tag [0x0020,0x0032] from most-far-left slice
* 'spacing', tuple 3	[inplane, slice_thickness]
* 'dims',    tuple 3	[Volume extent]
* 'nvol',    int	Number of total dynamic volumes (e.g 5)
])

outputs:
====
* dynamicfeatures_contour: Pandas dataframe with dynamic features from contour pixels only
* dynamicfeatures_inside: Pandas dataframe with dynamic features from inside pixels (all pixels) 
* morphofeatures: Pandas dataframe with morphology features
* texturefeatures: Pandas dataframe with texture features
total: 77 features


USAGE:
=====
To run all features pipeline after having create "npDICOMImages.p" pickle file as detailed above, run script "run_allfeatures.py" found here: https://github.com/cgallego/integrationFeaturesModule/blob/master/run_allfeatures.py
