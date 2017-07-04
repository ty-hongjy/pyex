# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:46:09 2017

@author: Administrator
"""

import numpy
from mayavi import mlab

x, y, z = numpy.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]
scalars = x * x + y * y + z * z
obj = mlab.contour3d(scalars, contours=8, transparent=True)
mlab.show()