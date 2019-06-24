#regresión lineal multiple con eliminación hacia atras automático

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

backwardElimination <- function(x, sl) {
  numVars = length(x)
  for (i in c(1:numVars)){
    regressor = lm(formula = Profit ~ ., data = x)
    maxVar = max(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"])
    if (maxVar > sl){
      j = which(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"] == maxVar)
      x = x[, -j]
    }
    numVars = numVars - 1
  }
  y_pred=predict(regressor,newdata = testing_set)
  #Prediccion con test
  
  return(summary(regressor))

}

SL = 0.05
dataset = dataset[, c(1,2,3,4,5)]
backwardElimination(training_set, SL)




