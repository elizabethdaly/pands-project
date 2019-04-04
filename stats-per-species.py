# turn this into a function later

# ###########################################################
# All below is in main file, will need to just pass dataframe to fun I think.
# Import Pandas data analysis library.
import pandas as pd

# Import matplotlib for 2D plotting.
import matplotlib.pyplot as plt

# Import Numpy
import numpy as np

# Read the iris.csv file from this directory.
data = pd.read_csv('iris.csv')
# print(data.head())

d_shape = data.shape
print("n rows = ", d_shape[0], ", n_cols = ", d_shape[1] )

# What are the column labels of the DataFrame?
col_labels = data.columns
print("Data column labels: ", col_labels)

# ###########################################################
# Create 3 dataframes, each corresponding to a single species.
setosa = data.loc[data['Name'] == "Iris-setosa"]
versicolor = data.loc[data['Name'] == "Iris-versicolor"]
virginica = data.loc[data['Name'] == "Iris-virginica"]

# Check them.
print("size=", setosa.shape)
print(setosa.head())
print("size=", versicolor.shape)
print(versicolor.head())
print("size=", virginica.shape)
print(virginica.head())
