# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 11:34:08 2017

@author: hongjy
"""

from sklearn.cluster import DBSCAN
import pandas as pd
from sklearn import metrics

f=u'学生月上网时间分布-TestData.txt'
data = pd.read_csv(f,header=None)
starttime = pd.to_datetime(data[4]).apply(lambda x:x.hour).reshape(-1,1)
DB = DBSCAN(eps=0.01,min_samples=20).fit(starttime)
labels = DB.labels_
raito = len(labels[labels[:]==-1])*1.0/len(labels)
n_clusters_ = len(set(labels)-{-1})
silhouette = metrics.silhouette_score(starttime, labels)