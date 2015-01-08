# -*- coding: utf-8 -*-
"""
Created on Fri Apr 04 13:45:42 2014

USAGE:
==============
import testNumpy2VTK
To create dataset for testing return a vtImagdata list and a vtkimagedata mask
testNumpy2VTK.testarray2VTKimage()

@ author (C) Cristina Gallego, University of Toronto, 2013
----------------------------------------------------------------------
"""

from convertNumpy import *
from display import *
from numpy import *

import os, os.path
import pickle
import dicom

from inputs_init import *
from vtk.util.numpy_support import vtk_to_numpy


### temporary use for testing
def testarray2VTKimage():
    convertImages = convertNumpy()
    mytest = convertImages.testconvertArray2vtkImage((20,20,10))
    
    print "\n Visualize volumes..."
    displaymytest = Display()
    myvolume = displaymytest.simpleVisualize(mytest, interact=True)
    
    return 
    
