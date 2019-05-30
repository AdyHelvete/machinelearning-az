# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:49:12 2019

@author: adrian.perez
"""
# Plantilla de Preprocesado 

#Como importar las librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importar el dataset
dataset = pd.read_csv("Data.csv")

X=dataset.iloc[:, :-1].values #EStablece las variables independientes
y=dataset.iloc[:, 3].values #establecer variable dependiente

#Tratamientos de los nan / NA
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values="NaN",strategy="mean",axis=0)
imputer=imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])

#Codificar datos categoricos
from sklearn.preprocessing import LabelEncoder
labelencoder_X=LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])
