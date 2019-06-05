#Plantilla para el preprocesado de datos
#importar el dataset

dataset=read.csv('Data.csv')
#dataset=dataset[,2:3]

#dividir los datos en conjuntos de entrenamiento y test
#install.packages("caTools")
library(caTools)
set.seed(123) #Semilla para aleatorios
split=sample.split(dataset$Purchased,SplitRatio =0.8)

training_set=subset(dataset,split==TRUE)
testing_set=subset(dataset,split==FALSE)

# Escalado de valores
# training_set[,2:3]=scale(training_set[,2:3])
# testing_set[,2:3]=scale(testing_set[,2:3])