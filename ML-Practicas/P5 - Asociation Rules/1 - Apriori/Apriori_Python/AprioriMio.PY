# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:38:07 2019

@author: adrian.perez
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importar el dataset
dataset = pd.read_csv("Market_Basket_Optimisation.csv",header=None)
transactions=[]

for i in range(0,7501):
       transactions.append([str(dataset.values[i,j]) for j in range(0,20)])


#entrenar algoritno de Apriori
from apyori import apriori
rules=apriori(transactions,min_support=0.003,min_confidence=.2, min_lift=3,min_length=2)  

results=list(rules)
results[4]