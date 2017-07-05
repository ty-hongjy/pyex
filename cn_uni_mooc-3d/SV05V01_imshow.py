# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 09:39:59 2017

@author: Administrator
"""

import numpy
from mayavi import mlab
 
s = numpy.random.random((10, 10))
img = mlab.imshow(s, colormap='gist_earth')
mlab.show()
