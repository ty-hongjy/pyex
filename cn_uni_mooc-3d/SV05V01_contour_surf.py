# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:51:17 2017

@author: Administrator
"""

import numpy as np
from mayavi import mlab
 
def f(x, y):
    return np.sin(x - y)+np.cos(x + y)
 
x, y = np.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
con_s = mlab.contour_surf(x, y, f)
mlab.show()