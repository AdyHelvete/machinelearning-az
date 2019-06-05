# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:18:10 2019

@author: adrian.perez
"""
# Plantilla de Preprocesado - Datos Categoricos
#Como importar las librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importar el dataset
dataset = pd.read_csv("Data.csv")

X=dataset.iloc[:, :-1].values #EStablece las variables independientes
y=dataset.iloc[:, 3].values #establecer variable dependiente

#Codificar datos categoricos para el País
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X=LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])
onehotencoder=OneHotEncoder(categorical_features=[0])
X=onehotencoder.fit_transform(X).toarray()

#Codificar datos categoricos para la variable dependiente Yes/No en 1/0

labelencoder_Y=LabelEncoder()
y=labelencoder_Y.fit_transform(y)
