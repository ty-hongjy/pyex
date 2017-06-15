# -*- coding: utf-8 -*-
"""
Created on Wed May 31 16:58:47 2017

@author: hongjy
"""
import time
import pandas as pd
import numpy as np  
 
#from sklearn.cluster import KMeans

from sklearn.preprocessing import Imputer
from sklearn.cross_validation import train_test_split 
from sklearn.metrics import classification_report
   
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

ISOTIMEFORMAT='%Y-%m-%d %X' #add by me
_is_verify=False
#_is_verify=True
 
def load_datasets(filepaths):
#def load_datasets(filepaths, label_paths):
    print("start loading data:"+filepaths)
    print(time.strftime(ISOTIMEFORMAT,time.localtime(time.time()))) #add by me
    feature = np.ndarray(shape=(0,54))
    label = np.ndarray(shape=(0,1))
#    for file in feature_paths:
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
#    for file in label_paths:
#        df = pd.read_table(file, header=None)
#        label = np.concatenate((label, df))

    if len(df1.columns)==55:         
#    if type=='train':
        label = df1[54]
#        print(label.shape)
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
    x,y = load_datasets(trainfilePaths)
#    x_train,y_train = load_datasets(trainfilePaths)
#    x_train, x_, y_train, y_ = train_test_split(x_train, y_train, test_size = 0.0)
#step 1 take x and y as train_data and test_data
    if _is_verify:
        print('Step 1')
        x_train, x_test, y_train, y_test = \
            train_test_split(x, y, test_size=0.3, random_state=0)
    #    x_train, x_test, y_train, y_test = \
    #        cross_validation.train_test_split(x, y, test_size=0.3, random_state=0)
        print('Start knn training')
        knn = KNeighborsClassifier().fit(x_train, y_train)
        print('Training done')
        print(time.strftime(ISOTIMEFORMAT,time.localtime(time.time()))) 
    
        print('Start knn predict')
        answer_knn = knn.predict(x_test)
        print(len(answer_knn))
    #    pd.write_table(answer_knn,'module2.txt', delimiter=' ', na_values='?')
        print('Prediction done')
        print(time.strftime(ISOTIMEFORMAT,time.localtime(time.time())))
    #    return  None     
        
        print('Start DT training')
        dt = DecisionTreeClassifier().fit(x_train, y_train)
        print('Training done')
        answer_dt = dt.predict(x_test)
    #    pd.write_table(answer_dt,'module2.txt', delimiter=' ', na_values='?')
        print('Prediction done')
        print(time.strftime(ISOTIMEFORMAT,time.localtime(time.time())))
         
        print('Start Bayes training')
        gnb = GaussianNB().fit(x_train, y_train)
        print('Training done')
        answer_gnb = gnb.predict(x_test)
    #    pd.write_table(answer_gnb,'module3.txt', delimiter=' ', na_values='?')
        print('Prediction done')
        print(time.strftime(ISOTIMEFORMAT,time.localtime(time.time())))
          
        print('\n\nThe classification report for knn:')
        print(classification_report(y_test, answer_knn))
        print('\n\nThe classification report for DT:')
        print(classification_report(y_test, answer_dt))
        print('\n\nThe classification report for Bayes:')
        print(classification_report(y_test, answer_gnb))

#step 2 take x and y as train_data. independ  test_data as predict_data 
    print('Step 2')
    x_test = load_datasets(testfilePaths)
    print(len(x_test))
    x_train, x_, y_train, y_ = train_test_split(x, y, test_size = 0.0)
    print('Start knn training')
    knn = KNeighborsClassifier().fit(x_train, y_train)
    print('Training done')
    print(time.strftime(ISOTIMEFORMAT,time.localtime(time.time()))) 

    print('Start knn predict')
    answer_knn = knn.predict(x_test)
    print(len(answer_knn))
#    pd.write_table(answer_knn,'module2.txt', delimiter=' ', na_values='?')
    np.savetxt('module1.txt',answer_knn,fmt='%d', delimiter=',')
    print('Prediction done')
    print(time.strftime(ISOTIMEFORMAT,time.localtime(time.time())))
#    return  None     

    print('Start DT training')
    dt = DecisionTreeClassifier().fit(x_train, y_train)
    print('Training done')
    answer_dt = dt.predict(x_test)
#    pd.write_table(answer_dt,'module2.txt', delimiter=' ', na_values='?')
    print(len(answer_dt))
    np.savetxt('module2.txt',answer_dt,fmt='%d', delimiter=',')
    print('Prediction done')
    print(time.strftime(ISOTIMEFORMAT,time.localtime(time.time())))

    print('Start Bayes training')
    gnb = GaussianNB().fit(x_train, y_train)
    print('Training done')
    answer_gnb = gnb.predict(x_test)
    print(len(answer_gnb))
#    pd.write_table(answer_gnb,'module3.txt', delimiter=' ', na_values='?')
    np.savetxt('module3.txt',answer_gnb,fmt='%d', delimiter=',')
    print('Prediction done')
    print(time.strftime(ISOTIMEFORMAT,time.localtime(time.time())))

if __name__ == '__main__':
    main()