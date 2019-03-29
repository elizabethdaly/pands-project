# Elizabeth Daly
# HDip Data Analytics 2019 pands-project
# 
# Script to read in the iris data set.
#
# ###########################################################
#
# Import Pandas data analysis library.
import pandas as pd

# Import matplotlib for 2D plotting.
import matplotlib.pyplot as plt

# Read the iris.csv file from this directory.
# The result is a DataFrame, the basic data format for Pandas.
data = pd.read_csv('iris.csv')

# Look at various attributes of the data to get an idea of its structure.
# ###########################################################

# Print the first few lines.
print(data.head())

# What are the data types of each columns?
print(data.dtypes)

# What is the number of rows, columns in the data set?
d_shape = data.shape
print("n rows = ", d_shape[0], ", n_cols = ", d_shape[1] )

# What are the row labels of the DataFrame?
print("Data index: ", data.index)

# What are the column labels of the DataFrame?
col_labels = data.columns
print("Data column labels: ", col_labels)

# Use decsribe() to get some basic statistics about each column of the data.
# It would probably make more sense to get this information for each species.
print(data[col_labels[0]].describe())
print(data[col_labels[1]].describe())
print(data[col_labels[2]].describe())
print(data[col_labels[3]].describe())
print(data[col_labels[4]].describe())

# Select each column according to its index.
# The result is a Series.
slen = data[col_labels[0]]      # col 1
swid = data[col_labels[1]]      # col 2
plen = data[col_labels[2]]      # col 3
pwid = data[col_labels[3]]      # col 4
species = data[col_labels[3]]   # col 4

# These are the column headings.
print("col1: ", col_labels[0])
print("col2: ", col_labels[1])
print("col3: ", col_labels[2])
print("col4: ", col_labels[3])
print("col5: ", col_labels[4])

# Try some plotting.
# want each column as a line
data[col_labels[0]].plot(kind='line')
plt.show()
quit()

plt.hist(slen)
plt.show()

