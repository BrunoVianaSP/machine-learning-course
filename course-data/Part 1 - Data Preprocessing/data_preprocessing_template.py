
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("Start program.") 


dataFileName = 'Data.csv'

# Importing the dataset
print("Importing dataset...")
dataset = pd.read_csv(dataFileName)

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values
print("\nFeatures: " + str(X))
print("\nDependent Variable: " + str(y))

print("\nFeatures with missig value:\n" + str(X))

# splitting the dataset into the training set and test set
from sklearn.cross_validation import train_test_split
xTrain, xTest, yTrain, yTesT = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""
from sklearn.preprocessing import StandardScaler
scX = StandardScaler()
xTrain = scX.fit_transform(xTrain)
xTest = scX.transform(xTest)
"""
