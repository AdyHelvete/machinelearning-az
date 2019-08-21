#Clasificador con Arboles de Decisión

#importar dataset
dataset=read.csv("Social_Network_Ads.csv")

#Seleccionar columnas de variables
dataset=dataset[,3:5]

# En algunos casos (BAyes) Codificar la variable de clasificación como factor
dataset$Purchased=factor(dataset$Purchased,
                    levels=c(0,1))

#dividir los datos en conjuntos de entrenamiento y test
#install.packages("caTools")
library(caTools)
set.seed(123) #Semilla para aleatorios
split=sample.split(dataset$Purchased,SplitRatio =0.75)

training_set=subset(dataset,split==TRUE)
testing_set=subset(dataset,split==FALSE)

# Escalado de valores no aplica para Arboles de Desición
#training_set[,1:2]=scale(training_set[,1:2])
#testing_set[,1:2]=scale(testing_set[,1:2])

#Ajustar el clasificador con el conjunto de entrenamiento

#Aqui
#install.packages("rpart")
library(rpart)
classifier=rpart(formula = Purchased ~ .,
                 data=training_set)

#predicción de los resultados con el conjunto de testing
y_pred=predict(classifier,newdata = testing_set[,-3],
               type="class")


#Crear matriz de confusión
cm=table(testing_set[,3],y_pred)

#Visualización del conjunto de entrenamiento
#install.packages("ElementStatLearn")
library(ElementStatLearn)
set=training_set
X1=seq(min(set[,1])-1,max(set[,1])+1, by=1)
X2=seq(min(set[,2])-1,max(set[,2])+1, by=400)
grid_set=expand.grid(X1,X2)
colnames(grid_set)=c("Age","EstimatedSalary")
y_grid=predict(classifier,newdata = grid_set,type="class")
plot(set[,-3],
     main="Clasificación Arbol de decisión (Conjunto de training)",
     xlab = "Edad",ylab = "Sueldo estimado",
     xlim = range(X1),ylim = range(X2)
)
contour(X1,X2,matrix(as.numeric(y_grid),length(X1),length(X2)),add=TRUE)
points(grid_set,pch='.',col=ifelse(y_grid==1,'springgreen3','tomato'))
points(set,pch=21,bg=ifelse(set[,3]==1,'green4','red3'))

#Visualización del conjunto de prueba
set=testing_set
X1=seq(min(set[,1])-1,max(set[,1])+1, by=1)
X2=seq(min(set[,2])-1,max(set[,2])+1, by=500)
grid_set=expand.grid(X1,X2)
colnames(grid_set)=c("Age","EstimatedSalary")
y_grid=predict(classifier,newdata = grid_set,type="class")
plot(set[,-3],
     main="Clasificación Arbol de decisión (Conjunto de testing)",
     xlab = "Edad",ylab = "Sueldo estimado",
     xlim = range(X1),ylim = range(X2)
)
contour(X1,X2,matrix(as.numeric(y_grid),length(X1),length(X2)),add=TRUE)
points(grid_set,pch='.',col=ifelse(y_grid==1,'springgreen3','tomato'))
points(set,pch=21,bg=ifelse(set[,3]==1,'green4','red3'))

#REpresentación del árbol de decisión
plot(classifier)
text(classifier)
