# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:09:19 2019
@author: adrian.perez
"""
#Modelo de soporte vectorial

#Preprocesado 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#importar el dataset
dataset = pd.read_csv("Position_salaries.csv")
X=dataset.iloc[:,1:2].values #EStablece las variables independientes
y=dataset.iloc[:, 2].values #establecer variable dependiente

#Dividir el dataset en conjuto de entrenamiento y conjunto de test
"""
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=1/3,random_state=0)
"""
#Escalado de vaiables
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
sc_y=StandardScaler()
X=sc_X.fit_transform(X)
y=sc_y.fit_transform(y.reshape(-1,1))


# Ajustar regresión con el data set
# Crear modelo de regression
from sklearn.svm import SVR
regression=SVR(kernel="rbf")
regression.fit(X,y)

#Predicción de los modelos de SVR

y_pred=regression.predict(sc_X.transform([[6.5]]))
#y_pred=regression.predict(X_test)

#aplicamos el escalado inverso
y_pred=sc_y.inverse_transform(y_pred)

#visualizacipon de los resultados del  modelo SVR

X_grid=np.arange(min(X),max(X),0.1) # Ajustar los valores de X para un mejro calidad en la grafica(unicamente)
X_grid=X_grid.reshape(len(X_grid),1)
plt.scatter(X,y,color="red")
#plt.plot(X,lin_reg_2.predict(X_poly),color="blue")
plt.plot(X_grid,regression.predict(X_grid),color="blue")
plt.title("Modelo de regresion SVR")
plt.xlabel("")
plt.ylabel("")
plt.show()

#revertimos es escalado para graficar los valores reales
X=sc_X.inverse_transform(X)
y=sc_y.inverse_transform(y)

X_grid=np.arange(min(X),max(X),0.1) # Ajustar los valores de X para un mejro calidad en la grafica(unicamente)
X_grid=X_grid.reshape(len(X_grid),1)
plt.scatter(X,y,color="red")
#plt.plot(X,lin_reg_2.predict(X_poly),color="blue")
#plt.plot(X_grid,regression.predict(X_grid),color="blue")
plt.title("Modelo de regresion SVR")
plt.xlabel("")
plt.ylabel("")
plt.show()
