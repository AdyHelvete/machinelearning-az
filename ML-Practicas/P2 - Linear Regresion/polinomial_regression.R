# Regresón Polinómica

dataset=read.csv('Position_salaries.csv')
dataset=dataset[,2:3] #Solo ocupamos las columnas 2 y 3

#dividir los datos en conjuntos de entrenamiento y test
#install.packages("caTools")
library(caTools)
set.seed(123) #Semilla para aleatorios

#Dividir en data set de entrenamiento y test
#En este caso no se dividen porque hay pocos datos

# split=sample.split(dataset$Salary,SplitRatio =2/3)
# training_set=subset(dataset,split==TRUE)
# testing_set=subset(dataset,split==FALSE)

#Tampoco hay proceso de escalado

#Ajustar Modelo re Regresión Lineal con el Conunto de datos

lin_reg=lm(formula = Salary ~.,
           data = dataset)

#Ajustar Modelo de Regresión Polinómica con el Conjunto de datos
dataset$Level2=dataset$Level^2 #Creamos columna de los cuadrados de la variable independiente
dataset$Level3=dataset$Level^3 #Creamos columna con el cubo de la variable independiente
dataset$Level5=dataset$Level^5 
poly_reg=lm(formula = Salary ~.,
            data = dataset)

#Visualización del modelo lineal
#install.packages("ggplot2")
#library(ggplot2)
ggplot()+
  geom_point(aes(x=dataset$Level,y=dataset$Salary),
             color="red")+
  geom_line(aes(x=dataset$Level,y=predict(lin_reg,newdata = dataset)),
            color="blue")+
  ggtitle("Predicción lineal del sueldo en función del nivel del empleado")+
  xlab("Nivel del empleado")+
  ylab("Sueldo $")


#Visualización del modelo polinómico
dataset$predict=predict(poly_reg,newdata = dataset)

ggplot()+
  geom_point(aes(x=dataset$Level,y=dataset$Salary),
             color="red")+
  geom_line(aes(x=dataset$Level,y=predict(poly_reg,newdata = dataset)),
            color="blue")+
  ggtitle("Predicción polinómica del sueldo en función del nivel del empleado")+
  xlab("Nivel del empleado")+
  ylab("Sueldo $") + 
  geom_text(aes(x=dataset$Level,y=predict(poly_reg,newdata = dataset),label=dataset$predict),hjust=0, vjust=0)

#Predicción de resultados con Regresión Lineal
y_pred=predict(lin_reg,newdata = data.frame(Level=6.5))

#Predicción de resultados con Regresión Polinómica
y_pred_poly=predict(poly_reg,newdata = data.frame(Level=6.5,
                                             Level2=6.5^2,
                                             Level3=6.5^3,
                                             Level5=6.5^5))
