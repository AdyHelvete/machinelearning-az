# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 17:03:03 2019

@author: adrian.perez
"""

#Muestreo de Thompson

#Importar las librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#cargar datasest
dataset=pd.read_csv("Ads_CTR_Optimisation.csv")

"""
#implementacion de selección aleatoria
import random
N=10000
d=10
ads_selected=[]
total_reward=0
for n in range(0,N):
       ad=random.randrange(d)
       ads_selected.append(ad)
       reward=dataset.values[n,ad]
       total_reward=total_reward + reward

#Visualizar el resultado, con histograma de frecuencias
plt.hist(ads_selected)
plt.title("Histograma de selección de anuncios")
plt.xlabel("Anuncio")
plt.ylabel("Número de veces que se visualizó")
plt.show()
"""

#Algoritmo de Muestreo de Thompson
import random
N=10000
d=10
number_of_rewards_1= [0]*d
number_of_rewards_0= [0]*d

ads_selected=[]
total_reward=0

for n in range(0,N):
       ad = 0
       max_random = 0       
       
       for i in range(0,d):
              random_beta=random.betavariate(number_of_rewards_1[i]+1, number_of_rewards_0[i]+1)
              
              if random_beta > max_random:
                     max_ramdom=random_beta
                     ad=i
       
       ads_selected.append(ad)
       reward=dataset.values[n,ad]
       
       if reward==1:
              number_of_rewards_1[ad]=number_of_rewards_1[ad]+1
       else:
             number_of_rewards_0[ad]=number_of_rewards_0[ad]+1 
             
       total_reward=total_reward+reward                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         

#histograma de resultados
plt.hist(ads_selected)
plt.title("Histograma de selección de anuncios")
plt.xlabel("Anuncio")
plt.ylabel("Número de veces que se visualizó")
plt.show()
