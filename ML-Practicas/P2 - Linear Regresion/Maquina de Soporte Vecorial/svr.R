#Plantilla de Regresión

dataset=read.csv('Position_Salaries.csv')
dataset=dataset[,2:3] #Solo ocupamos las columnas 2 y 3

#dividir los datos en conjuntos de entrenamiento y test
#install.packages("caTools")
library(caTools)
#set.seed(123) #Semilla para aleatorios

#Dividir en data set de entrenamiento y test
#En este caso no se dividen porque hay pocos datos

# split=sample.split(dataset$Salary,SplitRatio =2/3)
# training_set=subset(dataset,split==TRUE)
# testing_set=subset(dataset,split==FALSE)

# Escalado de valores
# training_set[,2:3]=scale(training_set[,2:3])
# testing_set[,2:3]=scale(testing_set[,2:3])

#Ajustar Modelo re Regresión con el Conunto de datos

#install.packages("e1071") #Libreria para modelos SVR
regression=svm(formula=Salary ~., 
               data = dataset,
               type="eps-regression",
               kernel="radial")

#Predicción de resultados de la regresión
y_pred=predict(regression,newdata = data.frame(Level=6.5))



#Visualización  del modelo con regresion
#install.packages("ggplot2")
library(ggplot2)

#x_grid=seq(min(dataset$Level),max(dataset$Level),0.1) #Suavisando la curva graficando más valores

ggplot()+
  geom_point(aes(x=dataset$Level,y=dataset$Salary),
             color="red")+
  geom_line(aes(x=dataset$Level,y=predict(regression,newdata = data.frame(Level=dataset$Level))),
            color="blue")+
  ggtitle("Predicción (Modelo de regresión SVR)")+
  xlab("Etiqueta Eje X")+
  ylab("Etiqueta Eje Y")
