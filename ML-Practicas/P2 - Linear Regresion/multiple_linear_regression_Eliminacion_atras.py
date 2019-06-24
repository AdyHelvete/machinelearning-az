# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:28:22 2019
@author: adrian.perez
"""
# Regresión Linear Multiple Con Eliminación Hacia Atras utilizando P valores

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

#construir modelo optimo de regrisiónm multiple utilizando la eliminación hacia atrs
#import statsmodels.formula.api as sm
X=np.append(arr=np.ones((50,1)).astype(int),values=X,axis=1)

## Algoritmo de eliminación hacia atras Utilizando P valores

import statsmodels.formula.api as sm
def backwardElimination(x, sl):    
    numVars = len(x[0])    
    for i in range(0, numVars):        
        regressor_OLS = sm.OLS(y, x).fit()        
        maxVar = max(regressor_OLS.pvalues).astype(float)        
        if maxVar > sl:            
            for j in range(0, numVars - i):                
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):                    
                    x = np.delete(x, j, 1)    
    regressor_OLS.summary()    
    return x 
 
SL = 0.05
X_opt=X[:,[0,1,2,3,4,5]]
X_Modeled = backwardElimination(X_opt, SL)