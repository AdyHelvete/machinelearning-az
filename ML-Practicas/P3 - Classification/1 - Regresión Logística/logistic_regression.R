#Regresión Ligistica

#importar dataset
dataset=read.csv("Social_Network_Ads.csv")

#Seleccionar columnas de variables
dataset=dataset[,3:5]

#dividir los datos en conjuntos de entrenamiento y test
#install.packages("caTools")
library(caTools)
set.seed(123) #Semilla para aleatorios
split=sample.split(dataset$Purchased,SplitRatio =0.75)

training_set=subset(dataset,split==TRUE)
testing_set=subset(dataset,split==FALSE)

# Escalado de valores
training_set[,1:2]=scale(training_set[,1:2])
testing_set[,1:2]=scale(testing_set[,1:2])

#Ajustar modelo de regresión logistica con el conjunto de entrenamiento

classifier=glm(formula = Purchased ~.,
               data = training_set,
               family = binomial)