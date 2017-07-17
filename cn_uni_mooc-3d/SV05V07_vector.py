# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 21:01:10 2017

@author: Administrator
"""
import numpy as np
from mayavi import mlab
from mayavi.tools import pipeline

_MODE_='normal'
#_MODE_='mask'
#_MODE_='flow'
#_MODE_='iso'
#_MODE_='cut'
#_MODE_='comp'

x, y, z = np.mgrid[0:1:20j, 0:1:20j, 0:1:20j]
u = np.sin(np.pi*x) * np.cos(np.pi*z)
v = -2*np.sin(np.pi*y) * np.cos(2*np.pi*z)
w = np.cos(np.pi*x)*np.sin(np.pi*z) + np.cos(np.pi*y)*np.sin(2*np.pi*z)

print("ok")
src=mlab.pipeline.vector_field(u,v,w)

if _MODE_=='mask':
    mlab.pipeline.vectors(src,mask_points=10,scale_factor=2.0) 
#    mlab.quiver3d(u,v,w)
elif _MODE_=='cut':
    mlab.pipeline.vector_cut_plane(src,mask_points=10,scale_factor=2.0) 

elif _MODE_=='iso':
    magnitude=mlab.pipeline.extract_vector_norm(src) 
    mlab.pipeline.iso_surface(magnitude,contours=[2.0,0.5])
    mlab.outline()

elif _MODE_=='flow':
    mlab.flow(u,v,w,seed_scale=1,seed_resolution=5,
              integration_direction='both')
    mlab.outline()

elif _MODE_=='comp':
    pass
else:
    mlab.quiver3d(u,v,w)
    mlab.outline()

mlab.show()
