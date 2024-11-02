# -*- coding: utf-8 -*-
"""Diabetes classification

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GPyvOI4VFtUdJIdYznrWYgRwQb92tXRl
"""

from __future__ import division
from google.colab import drive
drive.mount('/content/gdrive/')



# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

df = pd.read_csv("/content/gdrive/MyDrive/Classification -Diabetes/diabetes2.csv")

df

df.head()

df.info()

df.shape

pd.isnull(df).sum()

df.describe()

x = df.drop('Outcome', axis = 1)
y = df['Outcome']

"""we remove outcome columns in x and we assign it to the y variable

# ***StandardScaler Normalization (Scaling)***
"""

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

ds = scaler.fit_transform(x)

data = pd.DataFrame(ds, columns = x.columns)
data.head()

"""Pair Plot is a matrix of graphs that enables the visualization of the relationship between each pair of variables in a dataset."""

sns.pairplot(df,hue = 'Outcome')

"""hue : name of variable in our data which we want to know relationship between

1.   List item
2.   List item

all data and Outcome ('Outcome' columns)
"""

sns.heatmap(df.corr(),annot=True)

plt.hist(df.Outcome, bins = 3)

plt.hist(df.Age, bins = 10)
plt.xlabel('Age')
plt.ylabel('Number of People')

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(data,y,test_size = 0.30,random_state = 10)

x.shape, y.shape

print('x_train: ', x_train.shape)
print('x_test: ', x_test.shape)
print('y_train: ', y_train.shape)
print('y_test: ', y_test.shape)

print('################### X_TRAİN ####################')
x_train.info()
print('################### X_TEST ####################')
x_test.info()
print('################### Y_TRAİN ####################')
y_train.info()
print('################### Y_TEST ####################')
y_test.info()

"""#Model Selection¶

#  **KNN**

The K-Nearest Neighbors (KNN) algorithm is a popular machine learning technique used for classification and regression tasks. KNN is best suited for datasets that have a small number of input features and a large number of data points
"""

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=9)

knn.fit(x_train,y_train)

prediction = knn.predict(x_test)
prediction

knn.score(x_test,y_test)*100

"""# Decision Tree

A decision tree is a non-parametric supervised learning algorithm, which is utilized for both classification and regression tasks. It has a hierarchical, tree structure, which consists of a root node, branches, internal nodes and leaf nodes.
"""

from sklearn.tree import DecisionTreeClassifier

Decision_model = DecisionTreeClassifier()
Decision_model = Decision_model.fit(x_train,y_train)
y_pred = Decision_model.predict(x_test)
y_pred

from sklearn import metrics
print("Accuracy:",metrics.accuracy_score(y_test, y_pred)*100)

"""

# **Logestic regression**





"""

from sklearn.linear_model import LogisticRegression

model=LogisticRegression()
model.fit(x_train,y_train)

pred=model.predict(x_train)
minimum=min(len(y_test),len(pred))
pred=pred[:minimum]
y_test=y_test[:minimum]
print(pred.shape)
print(y_test.shape)

from sklearn.metrics import accuracy_score,confusion_matrix

print(accuracy_score(y_test,pred))
print('')
print(confusion_matrix(y_test,pred))

from sklearn.metrics import ConfusionMatrixDisplay
cm=confusion_matrix(y_test,pred)

dis=ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=['Postive','Negative'])
dis.plot()
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test,pred))