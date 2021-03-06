#Cluserin con K-MEans

#importar dataset
dataset=read.csv("Mall_Customers.csv")

#Seleccionar columnas de variables
X=dataset[,4:5]

#M�todo del Codo
set.seed(6)
wcss=vector()
for(i in 1:10){
  wcss[i]<-sum(kmeans(X,i)$withinss)
}

plot(1:10,wcss,type = 'b',main = "M�todo del codo",
     xlab="N�mero de clusters(k)",ylab="WCSS")

#Vemos que el codo m�s significativo en este caso est� en 5 clusters

#Aplicar el algoritmo de k-means con k �ptimo

set.seed(29)#Valor es irelevante, pero hay que poner uno
kmeans<-kmeans(X,4,iter.max = 300,nstart = 10)

#Visualizaci�n de los clusters 
install.packages("cluster")
library(cluster)
clusplot(X,
         kmeans$cluster,
         lines = 0,
         shade = TRUE,
         color=TRUE,
         label=1,
         plotchar = FALSE,
         span = TRUE,
         main = "Clustering de Clientes",
         xlab="Ingresos Anuales",
         ylab="Puntuaci�n (0-100)")
