# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 21:00:06 2017

@author: Administrator
"""

import numpy as np
from mayavi import mlab
from mayavi.tools import pipeline

#_IS_AXES="Z"
_IS_AXES="XY"

x, y, z = np.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
s = np.sin(x*y*z)/(x*y*z)
 
src = mlab.pipeline.scalar_field(s)
if _IS_AXES=="Z":
    mlab.pipeline.iso_surface(src, contours=[s.min()+0.1*s.ptp(), ], opacity=0.1)
    mlab.pipeline.iso_surface(src, contours=[s.max()-0.1*s.ptp(), ])
    mlab.pipeline.image_plane_widget(src,
                                plane_orientation='z_axes',
                                slice_index=10,
                            )
else:
    mlab.pipeline.image_plane_widget(src,plane_orientation='x_axes',slice_index=10)
    mlab.pipeline.image_plane_widget(src,plane_orientation='y_axes',slice_index=10)
    mlab.outline()

mlab.show()