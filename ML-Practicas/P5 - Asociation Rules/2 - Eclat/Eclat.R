#Eclat

#preprocesado de datos
#install.packager("arules")
library(arules)

#importar dataset
dataset=read.csv("Market_Basket_Optimisation.csv",header = FALSE)
dataset=read.transactions("Market_Basket_Optimisation.csv",
                          sep=",",rm.duplicates = TRUE)

#Entrenar algoritmo Eclat

rules=eclat(dataset,parameter = list(support=0.003,minlen=2))

#Visualización

inspect(sort(rules,by='support')[1:10])
