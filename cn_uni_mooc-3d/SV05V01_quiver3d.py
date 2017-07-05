# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 09:46:53 2017

@author: Administrator
"""

import numpy as np
from mayavi import mlab
 
x, y, z = np.mgrid[-2:3, -2:3, -2:3]
r = np.sqrt(x ** 2 + y ** 2 + z ** 4)
u = y * np.sin(r)/(r + 0.001)
v = -x * np.sin(r)/(r+0.001)
w = np.zeros_like(z)
 
obj = mlab.quiver3d(x, y, z, u, v, w, line_width=3, scale_factor=1)
mlab.show()