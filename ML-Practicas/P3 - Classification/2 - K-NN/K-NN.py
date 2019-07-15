# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:48:45 2019

@author: adrian.perez
"""
# Clasificador KNN

#Preprocesado 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#importar el dataset
dataset = pd.read_csv("Social_Network_Ads.csv")

X=dataset.iloc[:,[2,3]].values #EStablece las variables independientes
y=dataset.iloc[:, 4].values #establecer variable dependiente

#Dividir el dataset en conjuto de entrenamiento y conjunto de test
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=0)

#Escalado de vaiables
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)

# Ajustar modelo de clasificacion en el conjunto de entrenamiento
#Crear modelo aqui
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,metric="minkowski",p=2)
classifier.fit(X_train,y_train)

#Predicción de los resultados del conjunto de Testing
y_pred=classifier.predict(X_test)

#Elaborando Matríz de Confusión
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

#Representación Gráfica de los resultados del algoritmo en el conjunto de entrenamiento
from matplotlib.colors import ListedColormap
X_set,y_set=X_train,y_train
X1,X2=np.meshgrid(np.arange(start=X_set[:,0].min()-1,stop=X_set[:,0].max()+1,step=0.01),
                  np.arange(start=X_set[:,1].min()-1,stop=X_set[:,1].max()+1,step=0.01))
plt.contourf(X1,X2, classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),
             alpha=0.75,cmap=ListedColormap(['red','green']))
plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j,0],X_set[y_set==j,1],
                c=ListedColormap(('red','green'))(i), label=j)
plt.title("Clasificador (Conjunto de Enternamiento)")
plt.xlabel("Edad")
plt.ylabel("Sueldo Estimado")
plt.legend()
plt.show()

#Representación Gráfica de los resultados del algoritmo en el conjunto de test
from matplotlib.colors import ListedColormap
X_set,y_set=X_test,y_test
X1,X2=np.meshgrid(np.arange(start=X_set[:,0].min()-1,stop=X_set[:,0].max()+1,step=0.01),
                  np.arange(start=X_set[:,1].min()-1,stop=X_set[:,1].max()+1,step=0.01))
plt.contourf(X1,X2, classifier.predict(np.array([X1.ravel(),X2.ravel()]).T).reshape(X1.shape),
             alpha=0.75,cmap=ListedColormap(['red','green']))
plt.xlim(X1.min(),X1.max())
plt.ylim(X2.min(),X2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j,0],X_set[y_set==j,1],
                c=ListedColormap(('red','green'))(i), label=j)
plt.title("Clasificador (Conjunto de Enternamiento)")
plt.xlabel("Edad")
plt.ylabel("Sueldo Estimado")
plt.legend()
plt.show()

