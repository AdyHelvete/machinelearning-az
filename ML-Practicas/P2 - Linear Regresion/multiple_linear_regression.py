# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:28:22 2019
@author: adrian.perez
"""
# Regresión Linear Multiple

# Plantilla de Preprocesado 
#Como importar las librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importar el dataset
dataset = pd.read_csv("50_startups.csv")

X=dataset.iloc[:, :-1].values #EStablece las variables independientes
y=dataset.iloc[:, 4].values #establecer variable dependiente


#Codificar datos categoricos para el País en variables Dummy
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X=LabelEncoder()
X[:,3]=labelencoder_X.fit_transform(X[:,3])
onehotencoder=OneHotEncoder(categorical_features=[3])
X=onehotencoder.fit_transform(X).toarray()

#Evitar la trampa de las variables Dummy
X=X[:,1:]

#Dividir el dataset en conjuto de entrenamiento y conjunto de test
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.20,random_state=0)

#Ajustar el modelo de regresión lienal multiple con daots deTraining 
from sklearn.linear_model import LinearRegression
regression=LinearRegression()
regression.fit(X_train,y_train)

#Predicción de los resultados con el conjunto de testing

y_pred=regression.predict(X_test)

#construir modelo optimo de regrisiónm multiple utilizando la eliminación hacia atrs
import statsmodels.formula.api as sm
X=np.append(arr=np.ones((50,1)).astype(int),values=X,axis=1)
SL=0.05

X_opt=X[:,[0,1,2,3,4,5]]
regression_OLS=sm.OLS(endog=y,exog=X_opt).fit()
regression_OLS.summary()

X_opt=X[:,[0,1,3,4,5]]
regression_OLS=sm.OLS(endog=y,exog=X_opt).fit()
regression_OLS.summary()

X_opt=X[:,[0,3,4,5]]
regression_OLS=sm.OLS(endog=y,exog=X_opt).fit()
regression_OLS.summary()

X_opt=X[:,[0,3,5]]
regression_OLS=sm.OLS(endog=y,exog=X_opt).fit()
regression_OLS.summary()

X_opt=X[:,[0,3]]
regression_OLS=sm.OLS(endog=y,exog=X_opt).fit()
regression_OLS.summary()



