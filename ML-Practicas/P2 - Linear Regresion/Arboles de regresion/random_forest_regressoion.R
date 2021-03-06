#RAndom Forest Regression

dataset=read.csv('Position_Salaries.csv')
dataset=dataset[,2:3] #Solo ocupamos las columnas 2 y 3

#dividir los datos en conjuntos de entrenamiento y test
#install.packages("caTools")
#library(caTools)
#set.seed(123) #Semilla para aleatorios

#Dividir en data set de entrenamiento y test
#En este caso no se dividen porque hay pocos datos

# split=sample.split(dataset$Salary,SplitRatio =2/3)
# training_set=subset(dataset,split==TRUE)
# testing_set=subset(dataset,split==FALSE)

# Escalado de valores
# training_set[,2:3]=scale(training_set[,2:3])
# testing_set[,2:3]=scale(testing_set[,2:3])

#Ajustar Modelo de predicci�n Random Forest Regression con el Conunto de datos
#install.packages("randomForest")
library(randomForest)

set.seed(1234) #Semilla para aleatorios

regression=randomForest(x=dataset[1],
                        y=dataset$Salary,
                        ntree = 500)

#Predicci�n de resultados de la regresi�n
y_pred=predict(regression,newdata = data.frame(Level=6.5))



#Visualizaci�n  del modelo con regresion
#install.packages("ggplot2")
library(ggplot2)

x_grid=seq(min(dataset$Level),max(dataset$Level),0.01) #Suavisando la curva graficando m�s valores

ggplot()+
  geom_point(aes(x=dataset$Level,y=dataset$Salary),
             color="red")+
  geom_line(aes(x=x_grid,y=predict(regression,newdata = data.frame(Level=x_grid))),
            color="blue")+
  ggtitle("Predicci�n (Modelo de regresi�n)")+
  xlab("Etiqueta Eje X")+
  ylab("Etiqueta Eje Y")



