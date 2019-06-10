#regresión lineal Simple

dataset=read.csv('Salary_Data.csv')
#dataset=dataset[,2:3]

#dividir los datos en conjuntos de entrenamiento y test
#install.packages("caTools")
library(caTools)
set.seed(123) #Semilla para aleatorios
split=sample.split(dataset$Salary,SplitRatio =2/3)

training_set=subset(dataset,split==TRUE)
testing_set=subset(dataset,split==FALSE)

# Escalado de valores
# training_set[,2:3]=scale(training_set[,2:3])
# testing_set[,2:3]=scale(testing_set[,2:3])

#Ajustar el modelo de regresión lineal simple con datos de entrenamiento
regressor=lm(formula=Salary ~ YearsExperience,
             data=training_set)
#Conocer detalles del modelo P-valor, R-Cuadrada
#Summary(regressor) 
#Predecir resultados con el conjunto de test
y_pred=predict(regressor,newdata = testing_set)

#Visualización de datos en el conjunto de entrenamiento
#install.packages("ggplot2")
library(ggplot2)
ggplot() +
  geom_point(aes(x=training_set$YearsExperience,y=training_set$Salary),
             colour="red") +
  geom_line(aes(x=training_set$YearsExperience,
                y=predict(regressor,newdata = training_set)),
            colour="blue") +
  ggtitle("Sueldo vs Años de Experiencia (Entrenamiento)")+
  xlab("Años de experiencia")+
  ylab("Sueldo($)")

#Visualización de datos de prueba
ggplot() +
  geom_point(aes(x=testing_set$YearsExperience,y=testing_set$Salary),
             colour="red") +
  geom_line(aes(x=training_set$YearsExperience,
                y=predict(regressor,newdata = training_set)),
            colour="blue") +
  ggtitle("Sueldo vs Años de Experiencia (Test)")+
  xlab("Años de experiencia")+
  ylab("Sueldo($)")


