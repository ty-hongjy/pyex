# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 11:52:05 2017

@author: hongjy
"""

import matplotlib.pyplot as plt
import numpy as np
 
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
 
a = np.arange(0.0, 5.0, 0.02)
 
plt.subplot(2,1,1)
plt.plot(a,f(a))
 
plt.subplot(2,1,2)
plt.plot(a, np.cos(np.pi*a), 'r--')
plt.savefig("test",dip=600)
plt.show()