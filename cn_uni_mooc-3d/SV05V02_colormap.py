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

#访问surf对象的LUT
#LUT是一个255X4 的数组，列向量表示RGBA，每个值得的范围是0~255
lut=surf.module_manager.scalar_lut_manager.lut.table.to_array()
#增加透明梯度，修改alpha通道
lut[:,-1]=np.linspace(0,255,256)
surf.module_manager.scalar_lut_manager.lut.table=lut
# 更新视图并显示出来
#mlab.show()

