# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:57:29 2017

@author: Administrator
"""

from tvtk.api import tvtk
import numpy as np
 
x = np.array([0,3,9,15])
y = np.array([0,1,5])
z = np.array([0,2,3])
r = tvtk.RectilinearGrid()
r.x_coordinates = x
r.y_coordinates = y
r.z_coordinates = z
r.dimensions = len(x),len(y),len(z)