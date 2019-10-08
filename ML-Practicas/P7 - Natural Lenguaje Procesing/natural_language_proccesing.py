# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:57:23 2019

@author: adrian.perez
"""

#Natural Languaje Processing

#librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importar el dataset

dataset = pd.read_csv("Restaurant_Reviews.tsv",delimiter="\t",quoting=3)

#Limpieza de texto
import re
import nltk

nltk.download('stopwords') #Descarga de palabras irrelevantes
from nltk.corpus import stopwords #Stopwords para quitar palabras irrelevantes
from nltk.stem.porter import PorterStemmer #Sacar la raiz de la palabra sin conjugaciones,etc

corpus=[]
for i in range(0,1000):
         
       review=re.sub('[^a-zA-Z]',' ',dataset['Review'][i]) #"Dejar unicamente letras"
       review=review.lower() # "Pasar a minusculas"
       review=review.split() #dividir frases en vectores de palabras
       ps=PorterStemmer() 
       review=[ps.stem(word) for word in review if not word in set(stopwords.words('english'))] #trabajar la limpieza y transformacion para cada palabra
       review=' '.join(review)
       corpus.append(review)

#crear saco de palabras
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500) #se limita el maximo de palabras-columnas a 1500
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:,1].values #se elige la columna de valoración para 'y' en la correlacion


""" Se aplica el alogirmo de clasificacion naive Bayes"""
#Dividir el dataset en conjuto de entrenamiento y conjunto de test
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=0)
# Ajustar modelo de clasificacion en el conjunto de entrenamiento
#Crear modelo aqui
from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(X_train,y_train)
#Predicción de los resultados del conjunto de Testing
y_pred=classifier.predict(X_test)
#Elaborando Matríz de Confusión
from sklearn.metrics import confusion_matrix
cm_Bayes=confusion_matrix(y_test,y_pred)

""" SVM """
# Ajustar modelo de clasificacion en el conjunto de entrenamiento
#Crear modelo aqui
from sklearn.svm import SVC
classifier=SVC(kernel="linear",random_state=0)
classifier.fit(X_train,y_train)

#Predicción de los resultados del conjunto de Testing
y_pred=classifier.predict(X_test)

#Elaborando Matríz de Confusión
from sklearn.metrics import confusion_matrix
cm_SVM=confusion_matrix(y_test,y_pred)

""" Random Forest"""
from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier(n_estimators=50,criterion="entropy",random_state=0)
classifier.fit(X_train,y_train)
#Predicción de los resultados del conjunto de Testing
y_pred=classifier.predict(X_test)
#Elaborando Matríz de Confusión
from sklearn.metrics import confusion_matrix
cm_RandomForest=confusion_matrix(y_test,y_pred)

""" Kernel SVM"""
from sklearn.svm import SVC
classifier=SVC(kernel="rbf",random_state=0)
classifier.fit(X_train,y_train)

#Predicción de los resultados del conjunto de Testing
y_pred=classifier.predict(X_test)

#Elaborando Matríz de Confusión
from sklearn.metrics import confusion_matrix
cm_Kernel_SVM=confusion_matrix(y_test,y_pred)
