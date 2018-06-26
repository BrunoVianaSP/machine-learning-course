
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("Start program.") 


dataFileName = 'Salary_Data.csv'

# Importing the dataset
print("Importing dataset...")
dataset = pd.read_csv(dataFileName)

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
print("\n(IV) Features: " + str(X))
print("\n(DV) Dependent Variable: " + str(y))

# splitting the dataset into the training set and test set
from sklearn.cross_validation import train_test_split
xTrain, xTest, yTrain, yTest = train_test_split(X, y, 
                                                test_size = 1/3, 
                                                random_state = 0)


# Fitting Simple Linear Regression to the training set
from sklearn.linear_model import LinearRegression
# Create a Machine
regressor = LinearRegression()
# Machine is learning here
regressor.fit(xTrain, yTrain)


# Predicting the Test set results
yPred = regressor.predict(xTest)


# Visualising the Training set results
plt.scatter(xTrain, yTrain, color = 'red')
plt.plot(xTrain, regressor.predict(xTrain), color = 'blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()



# Visualising the Test set results
plt.scatter(xTest, yTest, color = 'red')
plt.plot(xTrain, regressor.predict(xTrain), color = 'blue')
plt.title('Salary vs Experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

