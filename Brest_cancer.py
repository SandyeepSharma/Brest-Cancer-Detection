#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 13:10:17 2019

@author: sandeep
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense



data = pd.read_csv(r'/home/sandeep/disk_C/csv_file/Brest_cancer/data.csv')
 
pd.set_option("display.max_columns",30)
data.head(5)
data.describe()
data.info()

np.random.seed(42)
data.drop('Unnamed: 32', axis=1 , inplace = True)
data.drop('id', axis=1 , inplace = True)
data['diagnosis'].unique()
data.isnull().sum()
data.diagnosis.replace(['M','B'] ,[0,1] , inplace = True)
data.columns

X = data.iloc[:,1:]
y= data.iloc[:,[1]]

X-train ,X_test , y_train ,y_test = 

def base():
    model = Sequential()
    model.add(10, input =30 , activation = 'relu' , kernel_initializer = 'normal')
    model.add(1 , activation = 'relu' , kernel_initializer = 'sigmoid')
    
    model.compile(loss = 'binary_crossentropy' , optimizer = 'adam' , metrices = ['accuracy'])
    return model
