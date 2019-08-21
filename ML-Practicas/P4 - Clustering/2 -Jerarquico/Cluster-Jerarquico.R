#Clustering Jerárquico

#importar dataset
dataset=read.csv("Mall_Customers.csv")

#Seleccionar columnas de variables
X=dataset[,4:5]

#Utilizar dendograma para encontrar el número optimo de clusters
dendogram=hclust(dist(X,method="euclidean"),
                 method = "ward.D")
plot(dendogram,
     main = "Método del dendograma",
     xlab="clientes del Centro Comercial",
     ylab="Distancia euclidea")


#Vemos que son 5 clusters para el caso

#Ajustar el clustering gerárquico

set.seed(29)#Valor es irelevante, pero hay que poner uno

hc=hclust(dist(X,method="euclidean"),
                 method = "ward.D")

y_hc=cutree(hc,k=5)

#Visualización de los clusters 
install.packages("cluster")
library(cluster)
clusplot(X,
         y_hc,
         lines = 0,
         shade = TRUE,
         color=TRUE,
         label=1,
         plotchar = FALSE,
         span = TRUE,
         main = "Clustering de Clientes",
         xlab="Ingresos Anuales",
         ylab="Puntuación (0-100)")

