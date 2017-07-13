# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 15:58:25 2017

@author: Administrator
"""

from tvtk.api import tvtk
from tvtkfunc import ivtk_scene,event_loop
 
s = tvtk.STLReader(file_name = "python.stl")
m = tvtk.PolyDataMapper(input_connection = s.output_port)
a = tvtk.Actor(mapper = m)
 
win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()