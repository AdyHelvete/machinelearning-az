# -*- coding: utf-8 -*-
"""Created on Mon Jun 10 13:11:58 2019
@author: adrian.perez
"""
#Regresión linear simple

# Plantilla de Preprocesado 
#Como importar las librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importar el dataset
dataset = pd.read_csv("Salary_Data.csv")

X=dataset.iloc[:, :-1].values #EStablece las variables independientes
y=dataset.iloc[:, 1].values #establecer variable dependiente

#Dividir el dataset en conjuto de entrenamiento y conjunto de test
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=1/3,random_state=0)

#Escalado de vaiables
"""from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)"""

#crear modelo de regresión lineal siempre con conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression=LinearRegression()
regression.fit(X_train,y_train)

#Predecir el conjunto de test
y_pred= regression.predict(X_test)

#visualizar los resultados de entrenamiento
plt.scatter(X_train,y_train,color="red")
plt.plot(X_train,regression.predict(X_train),color="blue")
plt.title("Sueldo vs Años de experiencia(Conjunto de Entremaniento)")
plt.xlabel("Añis de experiencia")
plt.ylabel("Sueldo en $")
plt.show()

#visualizar los resultados de test
plt.scatter(X_test,y_test,color="red")
plt.plot(X_train,regression.predict(X_train),color="blue")
plt.title("Sueldo vs Años de experiencia(Conjunto de Prueba)")
plt.xlabel("Añis de experiencia")
plt.ylabel("Sueldo en $")
plt.show()