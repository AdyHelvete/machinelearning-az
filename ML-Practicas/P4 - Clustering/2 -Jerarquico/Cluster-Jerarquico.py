# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:56:33 2019

@author: adrian.perez
"""

#Clustering Gerárquico

#Como importar las librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importar el dataset
dataset = pd.read_csv("Mall_customers.csv")

X=dataset.iloc[:,[3,4]].values

#Utilizar método de dendograma para encontrar el número optimo de clusters
import scipy.cluster.hierarchy as sch
dendograma=sch.dendrogram(sch.linkage(X,method="ward"))
plt.title("Dendograma")
plt.xlabel("Clientes")
plt.ylabel("Distancia Euclidea")
plt.show()

#ajustar el clustering jerárquico a nuestros datos
from sklearn.cluster import AgglomerativeClustering
hc=AgglomerativeClustering(n_clusters=5,affinity="euclidean",linkage="ward")
y_hc=hc.fit_predict(X)

#Representación gráfica de los clusters
plt.scatter(X[y_hc==0,0],X[y_hc==0,1],s=100,c="red",label="Cluster 1")
plt.scatter(X[y_hc==1,0],X[y_hc==1,1],s=100,c="green",label="Cluster 2")
plt.scatter(X[y_hc==2,0],X[y_hc==2,1],s=100,c="blue",label="Cluster 3")
plt.scatter(X[y_hc==3,0],X[y_hc==3,1],s=100,c="cyan",label="Cluster 4")
plt.scatter(X[y_hc==4,0],X[y_hc==4,1],s=100,c="magenta",label="Cluster 5")
#plt.scatter(hc.cluster_centers_[:,0],hc.cluster_centers_[:,1],s=300,c="yellow",label="Baricentros")
plt.title("Cluster de clientes")
plt.xlabel("Ingresos Anuales $")
plt.ylabel("Puntuación de Gastos")
plt.legend()
plt.show()