# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 11:26:04 2017

@author: Administrator
"""

import numpy as np
from mayavi import mlab
#建立数据
x, y = np.mgrid[-10:10:200j, -10:10:200j]
z = 100 * np.sin(x * y) / (x * y)
# 对数据进行可视化
mlab.figure(bgcolor=(1, 1, 1))
surf = mlab.surf(z, colormap='cool')
# 更新视图并显示出来
#mlab.show()

