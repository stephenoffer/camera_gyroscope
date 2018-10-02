#!/bin/env/python
# -*- encoding: utf-8 -*-
"""
===============================================================================
Configuration Variables
===============================================================================
author=gndctrl2mjrtm
-------------------------------------------------------------------------------
"""


#===============================================================================
# Camera Variables
#===============================================================================
# The horizontal range of view in angles
CAMERA_HORIZONTAL_RANGE = 40

# The vertical range of view in angles
CAMERA_VERTICAL_RANGE   = 40

#===============================================================================
# Gyroscope Variables
#===============================================================================
#-------------------------------------------------------------------------------
# Size of the template frame <2D list [20,20] - 
#                             max template size depends on camera>
# Larger template = greater accuracy, slower
# Smaller template = less accuracy, faster
TEMPLATE_SIZE			= [200,200]
#-------------------------------------------------------------------------------

#===============================================================================
# Run Variables
#===============================================================================
# Display the template and original frame in demo
DISPLAY					= False
