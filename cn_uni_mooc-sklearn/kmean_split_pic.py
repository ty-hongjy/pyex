# -*- coding: utf-8 -*-
"""
Created on Thu May 25 16:12:54 2017

@author: hongjy
"""

import numpy as np
import PIL.Image as image
from sklearn.cluster import KMeans
 
def loadData(filePath):
    f = open(filePath,'rb')
    data = []
    img = image.open(f)
    m,n = img.size
    for i in range(m):
        for j in range(n):
            x,y,z = img.getpixel((i,j))
            data.append([x/256.0,y/256.0,z/256.0])
    f.close()
    return np.mat(data),m,n
 
imgData,row,col = loadData('bull.jpg')
label = KMeans(n_clusters=4).fit_predict(imgData)
label = label.reshape([row,col])

pic_new = image.new("L", (row, col))
for i in range(row):
    for j in range(col):
        pic_new.putpixel((i,j), int(256/(label[i][j]+1)))
pic_new.save("result-bull-4.jpg", "JPEG")
