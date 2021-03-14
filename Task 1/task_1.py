# -*- coding: utf-8 -*-
"""Task 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EQh7SSKco3Ok6z8kXbXGYv_exkv48Gy-

#**Problem Statement:-** 
### Predict the percentage of an student based on the no. of study hours.

# Importing libraries
"""

import numpy as np                        # NumPy is a Python library used for working with arrays.
import pandas as pd                       # Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.     
import matplotlib.pyplot as plt           # Library used for Visualization

"""# Importing dataset"""

url="https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv"
dataset=pd.read_csv(url)

"""### This is how our dataset looks like."""

dataset

"""### Sample 10 rows from our dataset"""

dataset.sample(10)

dataset.info()

dataset.describe()

"""### Dividing our data into "Attributes" input and "Labels" output."""

x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

"""# Splitting the dataset

### Splitting our data into Training and Test set so that we can train our model with training set and then test it with our test set.
"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=177013)

"""# Training Simple Linear Regression on Training set

### Applying LinearRegression algorithm on training set to train the model.
"""

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)

"""# Predicting test set results

### Predicting results with test set
"""

pred=lr.predict(x_test)

hrs=9.25
res=lr.predict([[hrs]])
res

"""### Predicting Results with any value of your choice."""

print("Number of Hours=>{}".format(hrs))
print("Score predicted by model=>{:.2f}".format(res[0]))

"""# Visualising Training set results"""

plt.scatter(x_train,y_train,color='blue')
plt.plot(x_train,lr.predict(x_train),color='red')
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.title("Hours Vs Scores")
plt.show()

"""# Visualizing Test set results"""

plt.scatter(x_test,y_test,color='blue')
plt.plot(x_train,lr.predict(x_train),color='red')
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.title("Hours Vs Scores")
plt.show()
