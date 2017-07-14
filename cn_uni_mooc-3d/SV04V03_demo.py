#,-*-,coding:,utf-8,-*-
"""
Created,on,Wed,Jun,28,17:13:20,2017

@author:,Administrator
"""

from numpy import pi, sin, cos, mgrid
from mayavi import mlab
 
#建立数据
dphi, dtheta = pi/250.0, pi/250.0
[phi,theta] = mgrid[0:pi+dphi*1.5:dphi,0:2*pi+dtheta*1.5:dtheta]
m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
x = r*sin(phi)*cos(theta)
y = r*cos(phi)
z = r*sin(phi)*sin(theta)
 
#对该数据进行三维可视化
s = mlab.mesh(x, y, z)
#mlab.show()

s=mlab.gcf()
print(s.scene.background)
source=s.children[0]
print(repr(source))
print(repr(source.name))

print(repr(source.data.points))
print(repr(source.data.point_data.scalars))
print(source.name)

manager=source.children[0]
colors=manager.children[0]
colors.scalar_lut_manager.lut_mode='Blues'
colors.scalar_lut_manager.show_legend=True

surface=colors.children[0]
surface.actor.property.representation='wireframe'
surface.actor.property.opacity=0.6


