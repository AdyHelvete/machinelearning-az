# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:09:19 2019

@author: adrian.perez
"""

#Regresión polinomica

# Plantilla de Preprocesado 
#Como importar las librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importar el dataset
dataset = pd.read_csv("Position_salaries.csv")

X=dataset.iloc[:,1:2].values #EStablece las variables independientes
y=dataset.iloc[:, 2].values #establecer variable dependiente

#Dividir el dataset en conjuto de entrenamiento y conjunto de test
#En este caso no se dividen en sets  de test y training por que hay pocos datos

#from sklearn.model_selection import train_test_split
#X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=1/3,random_state=0)

#Escalado de vaiables
"""from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)"""
#Ajustar la regresion lineal con el dataset
from sklearn.linear_model import LinearRegression
lineal_reg=LinearRegression()
lineal_reg.fit(X,y)

# Ajustar regresión polinomica con el data set
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=5)
X_poly=poly_reg.fit_transform(X)
lin_reg_2=LinearRegression()
lin_reg_2.fit(X_poly,y)

#Visualizacion de los resultados del modelo lineal

plt.scatter(X,y,color="red")
plt.plot(X,lineal_reg.predict(X),color="blue")
plt.title("Modelo de regresion lineal")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo en $")
plt.show()

#visualizacipon de los resultados del  modelo polinómico
X_grid=np.arange(min(X),max(X),0.1) # Ajustar los valores de X para un mejro calidad en la grafica(unicamente)
X_grid=X_grid.reshape(len(X_grid),1)
plt.scatter(X,y,color="red")
#plt.plot(X,lin_reg_2.predict(X_poly),color="blue")
plt.plot(X_grid,lin_reg_2.predict(poly_reg.fit_transform(X_grid)),color="blue")
plt.title("Modelo de regresion polinomica")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo en $")
plt.show()


#Predicción de los modelos

lineal_reg.predict([[6.5]])

lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))






