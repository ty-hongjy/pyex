# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 09:45:25 2017

@author: Administrator
"""

import numpy as np
from mayavi import mlab
 
#建立数据
t = np.linspace(0, 4 * np.pi, 20)
x = np.sin(2 * t)
y = np.cos(t)
z = np.cos(2 * t)
s = 2 + np.sin(t)
 
#对数据进行可视化
points = mlab.points3d(x, y, z, s, colormap="Reds", scale_factor=.25)
#mlab.show()
s=mlab.gcf()
source=s.children[0]
manager=source.children[0]
colors=manager.children[0]
#colors.scalar_lut_manager.lut_mode='Blues'
lut=points.module_manager.scalar_lut_manager.lut_mode='Blues'

#surface=colors.children[0]
#surface.actor.property.representation='wireframe'
#surface.actor.property.color=0.6
