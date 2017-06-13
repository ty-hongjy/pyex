# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 17:09:04 2017

@author: hongjy
"""

import numpy as np
from sklearn.linear_model import Ridge
from sklearn import cross_validation
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

def main():
#    data = np.genfromtxt('岭回归归_noheader.csv', delimiter=',')
#    plt.plot(data[:,5])
#    plt.show()
#    x = data[:,:5]
#    y = data[:,5]
#    poly = PolynomialFeatures(6)

    data = np.genfromtxt('岭回归.csv',delimiter=',',skip_header=1,usecols=(1,2,3,4,5))#使用numpy方法读取数据,skip_header:跳过前n行
    plt.plot(data[:,4])
    plt.show()
    x = data[:,:4]
    y = data[:,4]
    poly = PolynomialFeatures(5)

    x = poly.fit_transform(x)
    
    train_x, test_x, train_y, test_y = \
    cross_validation.train_test_split(x, y, 
    test_size=0.3, random_state=0)#将数据分为训练集和测试集，test_size表示测试集的比例，random_state表示随机数种子
    
    #创建回归器，并进行训练                       
    clf = Ridge(alpha=1.0, fit_intercept=True)
    clf.fit(train_x, train_y)#对回归器进行训练
    score = clf.score(test_x, test_y)#利用测试集计算回归曲线的拟合优度
    #拟合优度：评价拟合的好坏，最大为1，无最小值。
    print('score:',score)
       
   #绘制拟合曲线
    start = 200
    end = 300
    y_pre = clf.predict(x)
    time = np.arange(start, end)
    plt.plot(time, y[start:end],'b', label="real")
    plt.plot(time, y_pre[start:end],'r', label="predict")
    plt.legend(loc="upper left")
    plt.show()
 
if __name__ == '__main__':
    main()
