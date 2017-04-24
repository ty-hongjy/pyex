# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

labels='Frogs','Dogs','Hogs','Logs'
sizes=[15,30,45,30]
explode=[0,0.05,0,0]

plt.figure()
p1=plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',startangle=90)
plt.axis('equal')

np.random.seed(0)
mu,sigma=0,1
a=np.random.normal(mu,sigma,size=1000)
plt.figure()
p2=plt.hist(a,30,normed=1,histtype='stepfilled')

plt.figure(num=3,figsize=(8,6))
p3=plt.plot(10*np.random.randn(1000),10*np.random.randn(1000),'ro')
print(p3)
plt.title('Simple Scatter')
#plt.show()

plt.figure()
plt.subplot(2,2,1)
p1
plt.subplot(2,2,2)
p2
plt.subplot(2,2,4)
p3
#plt.show()
