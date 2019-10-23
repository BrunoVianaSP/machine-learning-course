
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("Start program.") 


# Importing the dataset
print("Importing dataset...")
dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values
print("\nFeatures: " + str(X))
print("\nDependent Variable: " + str(y))

print("\nFeatures with missig value:\n" + str(X))

# taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy="mean", axis=0)
imputer = imputer.fit(X[:, 1:3]) # fit X to imputer
X[:, 1:3] = imputer.transform(X[:, 1:3]) # replace X dataset with fixed columns
print("\nFeatures without missig value:\n" + str(X))

# encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoderX = LabelEncoder()
X[:, 0] = labelEncoderX.fit_transform(X[:, 0])
print("\nIndependent V. Encoded Categorical Data Column:\n" + str(X))

oneHotEncoder = OneHotEncoder(categorical_features = [0])
X = oneHotEncoder.fit_transform(X).toarray()
print("\Independent V. Encoded Categorical Data to Dummy Variables:\n" + str(X))

labelEncoderY = LabelEncoder()
y = labelEncoderY.fit_transform(y)
print("\nDependent V. Encoded Categorical Data to Dummy Variables:\n" + str(y))


# splitting the dataset into the training set and test set
from sklearn.cross_validation import train_test_split
xTrain, xTest, yTrain, yTesT = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
scX = StandardScaler()
xTrain = scX.fit_transform(xTrain)
xTest = scX.transform(xTest)

# Splitting the dataset into the Training set and Test set
#from sklearn.cross_validation import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""
