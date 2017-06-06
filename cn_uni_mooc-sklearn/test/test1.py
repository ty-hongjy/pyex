# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 11:05:05 2017

@author: hongjy
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 24 13:53:31 2017

@author: hongjy
"""

import numpy as np
from sklearn.cluster import KMeans

if __name__ == '__main__':
    data= ((3,1), (3,2), (4,1), (4,2), (1,3), (1,4), (2,3), (2,4))
    km = KMeans(n_clusters=2)
    label = km.fit_predict(data)
    print(label)
    print(km.cluster_centers_)

    expenses = np.sum(km.cluster_centers_,axis=1)
    print(expenses)
