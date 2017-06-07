# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 11:25:38 2017

@author: hongjy
"""

from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
 
f = '31省市居民家庭消费水平-city.txt'
 
#data = pd.read_csv(f, header=None, encoding='gb2312')
data = pd.read_csv(f, header=None)
 
km = KMeans(n_clusters=3)
 
data['label'] = km.fit_predict(data.ix[:,1:])
 
expenses = np.sum(km.cluster_centers_ , axis=1)
 
n=0
 
print( data[0][data.label==n])
 
print( expenses[n])