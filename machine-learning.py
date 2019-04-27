# Elizabeth Daly
# HDip Data Analytics 2019 pands-project
# 
# machine-learning.py
# Script to read in and analyse the iris data set
# Try some machine learning using Linear Discriminant Analysis
# ###########################################################

# Code taken from: https://scikit-learn.org/stable/auto_examples/
# decomposition/plot_pca_vs_lda.html#sphx-glr-auto-examples-decomposition-plot-pca-vs-lda-py
# Explanation here: http://sebastianraschka.com/Articles/2014_python_lda.html#lda-via-scikit-learn


# Import Pandas data analysis library.
import pandas as pd

# Import matplotlib for 2D plotting.
import matplotlib.pyplot as plt

# Import Numpy
import numpy as np

# Import Seaborn
import seaborn as sb

# Import scikit-learn
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# ###########################################################
iris = datasets.load_iris()

# X is the 2D numpy array containing variable values.
X = iris.data

# y is the 1D numpy array of species names as integers (0,1,2) rather than strings.
y = iris.target

print("Training data X has ", X.ndim, "dimensions and shape ", X.shape)
print("target values y has ", y.ndim, "dimensions and shape ", y.shape)

target_names = iris.target_names
print("target_names: ", target_names)

lda = LinearDiscriminantAnalysis(n_components=2) 
X_r2 = lda.fit(X, y).transform(X)
print("LDA 2 components has ", X_r2.ndim, "dimensions and shape ", X_r2.shape)

# ###########################################################
plt.figure()
colors = ['blue', 'orange', 'green']
# Plot each column of X_r2 while keeping track of the species.
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], alpha=.5, color=color, label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.grid()
plt.title('LDA of Iris dataset (n_components=2)')
plt.xlabel('LD1')
plt.ylabel('LD2')
plt.savefig('LDA_iris.jpeg')
plt.show()

# ###########################################################
# Try the same thing with n_components=1 in lda

lda1 = LinearDiscriminantAnalysis(n_components=1)
X_r1 = lda1.fit(X, y).transform(X)
print("LDA 1 component has ", X_r1.ndim, "dimensions and shape ", X_r1.shape)

plt.figure()
colors = ['blue', 'orange', 'green']

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.plot(X_r1[y == i], alpha=.5, marker='o', linestyle='None', color=color, label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.grid()
plt.title('LDA of Iris dataset (n_components=1)')
plt.xlabel('Data point')
plt.ylabel('LD1')
plt.savefig('LDA(1cmpt)_iris.jpeg')
plt.show()

