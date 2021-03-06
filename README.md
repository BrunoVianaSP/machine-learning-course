# Machine Learning A-Z - Hands On with Python and Learning
Tutorial based on https://www.udemy.com/machinelearning/learn/v4/overview

## Section 1 - Introduction

### Applications of Machine Learning

**Image Recognition**  
**Game Body Recognition like Kinect**  
**Virtual Reality headset**  
**Voice Recognition**  
**Robots**  
**Advertisement delivery**  
**Recomender Systems**  
**Earth climates monitoring**  
**Neuroscience improvements**  
**Territories exploration**  

These are basic applications of Machine Learning used in our real life.  


## Installing Python and Anaconda (Mac & Windows)

**Go to:** https://anaconda.org/anaconda/python just download for your O.S and follow the instructions for installing it. It's just a very basic installation. There is no weird configuration.  

**After installation:** open the Spyder IDE go to view > toolbars > Variable explorer; Object inspector. These are the toolbars we're going to need. 


## Installing R and R Studio (Mac & Windows)

### Install R

**Go to:** https://cran.r-project.org/ download R for you O.S install it then you'll have the R language installed in your machine.  

### Install R Studio

**Go to:** https://www.rstudio.com/ select the right one for your O.S just install it and you're ready.


## Section 2 - Data Preprocessing

Here you can have more https://www.geeksforgeeks.org/data-preprocessing-machine-learning-python/

### Importing the libraries
Here are the libraries we're gonna need most part of the course.

**Python** 

*import numpy as np*: includes the mathematic tools needed. [NumPy](http://www.numpy.org/)  
*import matplotlib.pyplot as plt*: for ploting some charts. [MatplotLib](https://matplotlib.org/api/pyplot_api.html)  
*import pandas as pd*: for manage datasets. [Pandas](https://pandas.pydata.org/)  
 
This is enough to import the libraries above in a .py file running on Spyder IDE. Just run the code to see the successful importing.

**R**   
*For this section there's no need of library import in R*


### Importing the dataset  

We need to import and separate the dataset in two different matrices, one of *Features* (Independent variables) and another of Dependent variables.  

**Explanation**  


| Country  | Age | Salary | Purchased |
| ---------| --- | ------ | --------- |
| France   | 44  | 72000  | no        |
| Spain    | 27  | 48000  | yes       |
| Germany  | 30  | 54000  | no        |
| Spain    | 38  | 61000  | no        |
| Germany  | 40  |        | yes       |
| France   | 35  | 58000  | yes       |
| Spain    |     | 52000  | no        |
| France   | 48  | 79000  | yes       |
| Germany  | 50  | 83000  | no        |
| France   | 37  | 67000  | yes       |


```
In my case I have a dataset of 10 observations (ten rows) for these columns: Country, Age, Salary, Purchased   
Independent variables: Country, Age, Salary   
Dependent variables: Purchased  

```
**Python**  
dataset = pd.read_csv('FileName.csv');  
X = dataset.iloc[:, :-1].values //Features (Independent variables)  
y = dataset.iloc[:, 3].values   // (Dependent variables)  

**R**  
dataset = read.csv('Data.csv') // there is no need matrix separation in R. Much simpler than Python.  


### Missing Data
In this part of the course we're going to learn a simple way to deal with *Missing Data* by taking the **mean** of the column that have the missing data and fill the rows with this problem.


**Python**  
from sklearn.preprocessing import Imputer [SKLearn Imputer](http://scikit-learn.org/stable/modules/preprocessing.html#preprocessing)
imputer = Imputer(missing_values='NaN', strategy="mean", axis=0)
imputer = imputer.fit(X[:, 1:3]) # fit part missing data of X to imputer
X[:, 1:3] = imputer.transform(X[:, 1:3]) # replace X dataset with fixed columns 

Some explanations: 
    By putting NaN as the first parameter of Imputer we're telling the class that we are replacing the missing values filled as nan by Python.
    

**R**  

dataset$Age = ifelse(is.na(dataset$Age), 
                     ave(dataset$Age, FUN=function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN=function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary)


Some explanations: 
    In R you just need to write a conditional on the column you with take care of missing values. This is much more easier to understand than Python. 
    


**After missing values handling using the mean for both columns Age and Salary**

| Country  | Age | Salary | Purchased |
| ---------| --- | ------ | --------- |
| France   | 44  | 72000  | no        |
| Spain    | 27  | 48000  | yes       |
| Germany  | 30  | 54000  | no        |
| Spain    | 38  | 61000  | no        |
| Germany  | 40  |**63777**| yes      |
| France   | 35  | 58000  | yes       |
| Spain    |**38**| 52000 | no        |
| France   | 48  | 79000  | yes       |
| Germany  | 50  | 83000  | no        |
| France   | 37  | 67000  | yes       |



### Categorical Data

### Spliting Dataset into Training and Test sets

### Feature Scaling





