# Data Preprocessing Template

dataFileName = 'Data.csv'

# Importing the dataset
dataset = read.csv(dataFileName)
#dataset = dataset[, 2:3]

# splitting the dataset into the training set and test set
# install.packages('caTools')
library(caTools)
set.seed(123)

split = sample.split(dataset$Purchased,
                     SplitRatio = 0.8) # need pass only dependent variable

trainingSet = subset(dataset, split==TRUE)
testSet = subset(dataset, split==FALSE)

# Feature Scaling 
# trainingSet[, 2:3] = scale(trainingSet[, 2:3])
# testSet[, 2:3] = scale(testSet[, 2:3])

