# -*- coding: utf-8 -*-
"""
Created on Wed May 31 16:58:47 2017

@author: hongjy
"""
import time
import pandas as pd
import numpy as np  

from sklearn.preprocessing import Imputer
from sklearn.cross_validation import train_test_split 
from sklearn.metrics import classification_report
   
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

ISOTIMEFORMAT='%Y-%m-%d %X' #add by me

def load_datasets(filepaths):
#def load_datasets(filepaths, label_paths):
    print("start loading data:"+filepaths)
    print(time.strftime(ISOTIMEFORMAT,time.localtime(time.time()))) #add by me
    feature = np.ndarray(shape=(0,54))
    label = np.ndarray(shape=(0,1))
    df1 = pd.read_table(filepaths, delimiter=' ', na_values='?', header=None)
    if len(df1.columns)==55:
        df=df1.drop(54,axis=1)
    else:
        df=df1
#    print(len(df.columns))
    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
    imp.fit(df)
    df = imp.transform(df)
    feature = np.concatenate((feature, df))
#    print(feature.shape) 

    if len(df1.columns)==55:         
        label = df1[54]
        print("end loaded data")
        print(time.strftime(ISOTIMEFORMAT,time.localtime(time.time()))) #add by me
        return feature, label
    else:
        print("end loaded data")
        print(time.strftime(ISOTIMEFORMAT,time.localtime(time.time()))) #add by me
        return feature

def main():
    ''' 数据路径 '''
    trainfilePaths = 'test_data\data_train.txt'
    testfilePaths = 'test_data\data_test.txt'
    ''' 读入数据  '''
    x_train,y_train = load_datasets(trainfilePaths)
    x_test = load_datasets(testfilePaths)
    x_train, x_, y_train, y_ = train_test_split(x_train, y_train, test_size = 0.0)

    print('Start knn training')
    knn = KNeighborsClassifier().fit(x_train, y_train)
    print('Training done')
    print(time.strftime(ISOTIMEFORMAT,time.localtime(time.time()))) #add by me

    print('Start knn predict')
    answer_knn = knn.predict(x_test)
    print(len(answer_knn))
    print('Prediction done')
    print(time.strftime(ISOTIMEFORMAT,time.localtime(time.time())))#add by me
    return  None     
    print('Start training DT')
    dt = DecisionTreeClassifier().fit(x_train, y_train)
    print('Training done')
    answer_dt = dt.predict(x_test)
    print(len(answer_dt))
    print('Prediction done')
    print(time.strftime(ISOTIMEFORMAT,time.localtime(time.time())))#add by me

    print('Start training Bayes')
    gnb = GaussianNB().fit(x_train, y_train)
    print('Training done')
    answer_gnb = gnb.predict(x_test)
    print(len(answer_gnb))
    print('Prediction done')
    print(time.strftime(ISOTIMEFORMAT,time.localtime(time.time())))#add by me
 
     
#    print('\n\nThe classification report for knn:')
#    print(classification_report(y_test, answer_knn))
#    print('\n\nThe classification report for DT:')
#    print(classification_report(y_test, answer_dt))
#    print('\n\nThe classification report for Bayes:')
#    print(classification_report(y_test, answer_gnb))
    
if __name__ == '__main__':
    main()    