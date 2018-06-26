# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Data.csv')

# Taking care of missing data
dataset$Age = ifelse(is.na(dataset$Age), 
                     ave(dataset$Age, FUN=function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN=function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)


# Encoding categorical data
# variables as factor
dataset$Country = factor(dataset$Country, 
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1, 2, 3))

dataset$Purchased = factor(dataset$Purchased, 
                           levels = c('Yes', 'No'),
                           labels = c(0, 1))


# splitting the dataset into the training set and test set
install.packages('caTools')
library(caTools)
set.seed(123)

split = sample.split(dataset$Purchased,
                     SplitRatio = 0.8) # need pass only dependent variable

trainingSet = subset(dataset, split==TRUE)
testSet = subset(dataset, split==FALSE)

# Feature Scaling 
trainingSet[, 2:3] = scale(trainingSet[, 2:3])
testSet[, 2:3] = scale(testSet[, 2:3])
