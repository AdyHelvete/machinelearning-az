#Natural Lengual Processing

# importar el dataset
dataset_original=read.delim("Restaurant_Reviews.tsv",quote = '',stringsAsFactors = FALSE)

#Limpieza de datos
#install.packages("tm")
#install.packages("SnowballC")

library(tm)
library(SnowballC)
corpus=VCorpus(VectorSource(dataset_original$Review))
corpus=tm_map(corpus,content_transformer(tolower))

#Consultar el primer elemento del corpus
#as.character(corpus[[1]])

#Limpieza de los textos
corpus=tm_map(corpus,removeNumbers)
corpus=tm_map(corpus,removePunctuation)
corpus=tm_map(corpus,removeWords,stopwords(kind = "en"))
corpus=tm_map(corpus,stemDocument)
corpus=tm_map(corpus,stripWhitespace)

#Creación de matriz dispersa (Bag of Words)
dtm=DocumentTermMatrix(corpus)
dtm=removeSparseTerms(dtm,0.999)


dataset=as.data.frame(as.matrix(dtm))
dataset$Liked=dataset_original$Liked

# En algunos casos (BAyes,random forest, descicion tree) Codificar la variable de clasificación como factor
dataset$Liked=factor(dataset$Liked,
                         levels=c(0,1))

#dividir los datos en conjuntos de entrenamiento y test
#install.packages("caTools")
library(caTools)
set.seed(123) #Semilla para aleatorios
split=sample.split(dataset$Liked,SplitRatio =0.80)

training_set=subset(dataset,split==TRUE)
testing_set=subset(dataset,split==FALSE)

#Ajustar el clasificador Random Forest con el conjunto de entrenamiento

#Aqui
#install.packages("randomForest")
library(randomForest)

classifier=randomForest(x=training_set[,-692],
                        y=training_set$Liked, 
                        ntree = 11)

#predicción de los resultados con el conjunto de testing
y_pred=predict(classifier,newdata = testing_set[,-692],
               type="class")


#Crear matriz de confusión
cm=table(testing_set[,692],y_pred)