# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:17:22 2019

@author: adrian.perez
"""
#Como importar las librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importar el dataset
dataset = pd.read_csv("Mall_customers.csv")

X=dataset.iloc[:, [3,4]].values  #EStablece las variables independientes

#Metodo del codo para averiguar el número de clusters optimo
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init="k-means++",max_iter=300,n_init=10,random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
    
plt.plot(range(1,11),wcss)
plt.title("Metodo del codo")
plt.xlabel("Número de Clusters")
plt.plot("WCSS(k)")
plt.show()   

#Aplicar el método k-means para segmentar el data set
kmeans=KMeans(n_clusters=5,init="k-means++",max_iter=300,n_init=10,random_state=0)
y_kmeans=kmeans.fit_predict(X)

#Representación gráfica de los clusters
plt.scatter(X[y_kmeans==0,0],X[y_kmeans==0,1],s=100,c="red",label="Cluster 1")
plt.scatter(X[y_kmeans==1,0],X[y_kmeans==1,1],s=100,c="green",label="Cluster 2")
plt.scatter(X[y_kmeans==2,0],X[y_kmeans==2,1],s=100,c="blue",label="Cluster 3")
plt.scatter(X[y_kmeans==3,0],X[y_kmeans==3,1],s=100,c="cyan",label="Cluster 4")
plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1],s=100,c="magenta",label="Cluster 5")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c="yellow",label="Baricentros")
plt.title("Cluster de clientes")
plt.xlabel("Ingresos Anuales $")
plt.ylabel("Puntuación de Gastos")
plt.legend()
plt.show()