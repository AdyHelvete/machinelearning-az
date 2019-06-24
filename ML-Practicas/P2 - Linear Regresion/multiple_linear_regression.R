#regresión lineal multiple

dataset=read.csv('50_Startups.csv')
#dataset=dataset[,2:3]

#Vriable categorica a variables dummy (En R son factores)

dataset$State=factor(dataset$State,
                       levels=c("New York","California","Florida"),
                       labels=c(1,2,3))

#dividir los datos en conjuntos de entrenamiento y test
#install.packages("caTools")
library(caTools)
set.seed(123) #Semilla para aleatorios
split=sample.split(dataset$Profit,SplitRatio =0.8)

training_set=subset(dataset,split==TRUE)
testing_set=subset(dataset,split==FALSE)

# Escalado de valores
# training_set[,2:3]=scale(training_set[,2:3])
# testing_set[,2:3]=scale(testing_set[,2:3])

#Ajustar modelo de regresión Lineal Multiple con el Conjunto de Entrenamiento

# regression=lm(formula=Profit ~ R.D.Spend + Administration + Marketing.Spend + State,data=training_set)
regression=lm(formula=Profit ~ ., data=training_set)

# Predecir los resultados con el Conjunto de Test

y_pred=predict(regression,newdata = testing_set)

#Construir un modelo optimo con la eliminación hacia atrás
SL=0.05 #Nivel de significancia es arbitrario, lo normal es manejar 0.05

regression=lm(formula=Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
              data=dataset)
summary(regression)

#Borrado state por un P valor alto,mayor a 0.05
regression=lm(formula=Profit ~ R.D.Spend + Administration + Marketing.Spend,
              data=dataset)
summary(regression)

#Borrado Administration por un P valor alto,mayor a 0.05
regression=lm(formula=Profit ~ R.D.Spend + Marketing.Spend,
              data=dataset)
summary(regression)

#Borrado Marketing.Spend  por un P valor alto,mayor a 0.05 ( tene un valor de 0.6, que podemos utilizar y pasarlo por alto)
regression=lm(formula=Profit ~ R.D.Spend,
              data=dataset)
summary(regression)





