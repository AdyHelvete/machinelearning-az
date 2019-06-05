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


#Dividir el dataset en conjuto de entrenamiento y conjunto de test

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

#Escalado de vaiables
"""from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)"""





