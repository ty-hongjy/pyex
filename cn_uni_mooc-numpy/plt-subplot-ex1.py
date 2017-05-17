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
plt.subplot(2,2,1)
#plt.figure(1)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',startangle=90)
plt.axis('equal')
#plt.show()

#import numpy as np
np.random.seed(0)
mu,sigma=0,1
a=np.random.normal(mu,sigma,size=1000)
#plt.figure(3)
plt.subplot(2,2,2)
plt.hist(a,30,normed=1,histtype='stepfilled')
#plt.show()


#plt.figure(4)
plt.subplot(2,2,4)
plt.plot(10*np.random.randn(1000),10*np.random.randn(1000),'ro')
plt.title('Simple Scatter')
plt.savefig("test",dip=600)
plt.show()
