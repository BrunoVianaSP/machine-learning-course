# Multiple Linear Regression
 
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("Start program.") 


dataFileName = '50_Startups.csv'

# Importing the dataset
print("Importing dataset...")
dataset = pd.read_csv(dataFileName)

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values
print("\nMatrix of Features: " + str(X))
print("\nDependent Variable: " + str(y))
print("\nFeatures with missig value:\n" + str(X))


# Encoding categorical data
categorialVarColumn = 3
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoderX = LabelEncoder()
X[:, categorialVarColumn] = labelEncoderX.fit_transform(X[:, categorialVarColumn])
print("\nIndependent V. Encoded Categorical Data Column:\n" + str(X))

oneHotEncoder = OneHotEncoder(categorical_features = [3])
X = oneHotEncoder.fit_transform(X).toarray()
print("\Independent V. Encoded Categorical Data to Dummy Variables:\n" + str(X))

# Avoiding the Dummy Variable Trap
X = X[:, 1:] # the libraries can do it for us

# splitting the dataset into the training set and test set
from sklearn.cross_validation import train_test_split
xTrain, xTest, yTrain, yTesT = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression for the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(xTrain, yTrain)

# Predicting the Test set results
yPred = regressor.predict(xTest)


# Building a optimal model using Backward Elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50, 1)).astype(int), 
              values=X, 
              axis=1)

# Only the features that are statitically significant
xOpt = X[:, [0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = xOpt).fit()
regressor_OLS.summary()

# Remove the highest p-value
xOpt = X[:, [0,1,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = xOpt).fit()
regressor_OLS.summary()

# Remove the highest p-value
xOpt = X[:, [0,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = xOpt).fit()
regressor_OLS.summary()

# Remove the highest p-value
xOpt = X[:, [0,3,5]]
regressor_OLS = sm.OLS(endog = y, exog = xOpt).fit()
regressor_OLS.summary()

# Remove the highest p-value
xOpt = X[:, [0,3]] # only de highest significant variable(R&D) for predicting profit 
regressor_OLS = sm.OLS(endog = y, exog = xOpt).fit()
regressor_OLS.summary()































