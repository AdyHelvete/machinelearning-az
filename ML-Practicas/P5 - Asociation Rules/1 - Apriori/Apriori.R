#Plantilla de Reglas de Asosicación - Apriori

#Preprocesado de Datos

#importar dataset
#dataset=read.csv("Market_Basket_Optimisation.csv",header = FALSE)
dataset=read.csv("Clientes.csv")

#install.packages("arules")
library(arules)

dataset=read.transactions("Clientes.csv",
                          sep=",",rm.duplicates = TRUE)

summary(dataset)
itemFrequencyPlot(dataset,topN=30)

#Entrenar algoritmo Apriori

rules=apriori(dataset,parameter = list(support=0.001,confidence=0.2))

#Visualización

inspect(sort(rules,by='lift')[1:10])
