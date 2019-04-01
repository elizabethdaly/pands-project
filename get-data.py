# Elizabeth Daly
# HDip Data Analytics 2019 pands-project
# 
# Script to read in & analyse the iris data set.
#
# ###########################################################
#
# Import Pandas data analysis library.
import pandas as pd

# Import matplotlib for 2D plotting.
import matplotlib.pyplot as plt

# Import Numpy
import numpy as np

# Read the iris.csv file from this directory.
# The result is a DataFrame, the basic data format for Pandas.
data = pd.read_csv('iris.csv')

# ###########################################################
# Look at various attributes of the data to get an idea of its structure.

# Print the first few lines.
print(data.head())

# What are the data types of each column?
print(data.dtypes)

# What is the number of rows, columns in the data set?
d_shape = data.shape
print("n rows = ", d_shape[0], ", n_cols = ", d_shape[1] )

# What are the row labels of the DataFrame?
print("Data index: ", data.index)

# What are the column labels of the DataFrame?
col_labels = data.columns
print("Data column labels: ", col_labels)

# ###########################################################
# Try some plotting. I want each column as a line.

# Keep track of axes so they can be used again.
ax = plt.gca()

# Plot each column of the data set as a different colour.
data[col_labels[0]].plot(kind='line', y= 'SepalLength', ax=ax)
data[col_labels[1]].plot(kind='line', y= 'SepalWidth', color='green', ax=ax)
data[col_labels[2]].plot(kind='line', y= 'PetalLength', color='red', ax=ax)
data[col_labels[3]].plot(kind='line', y= 'PetalWidth', color='yellow', ax=ax)

# Set x range. 
plt.xlim(0, 150)

# Set the x tick marks.
x = np.arange(0, 150, 25)
plt.xticks(x)

# Graph, x-axis, and y-axis titles.
plt.title("Overview of the Iris Data Set", fontsize=18)
plt.ylabel('cm', fontsize=16)
plt.xlabel('sample', fontsize=16)

# Graph legend and grid
plt.legend(loc='best', fontsize=10)
plt.grid()

# Save the figure.
# plt.savefig('Overview.jpeg')

plt.show()

# ###########################################################
# Use describe() to get some basic statistics about each column.
# It would make more sense to get this information for each species,
# but I'll start with this.

# print(data[col_labels[0]].describe())
# print(data[col_labels[1]].describe())
# print(data[col_labels[2]].describe())
# print(data[col_labels[3]].describe())
# print(data[col_labels[4]].describe())

# Or do all the numeric columns together, the output is another dataframe.
data_summary = data.describe()
print(data_summary)

# Plot these summary statistics.
# Almost ok except I don't want count
# data_summary.plot.bar()

# This omits count by selecting all but first row of summary dataframe.
data_summary.iloc[1:7,0:3].plot.bar()
plt.show()

quit()
data_summary.plot(kind='bar', y= 'SepalLength')
plt.show()

quit()
# Select each column according to its index.
# The result is a Series.
slen = data[col_labels[0]]      # col 1
swid = data[col_labels[1]]      # col 2
plen = data[col_labels[2]]      # col 3
pwid = data[col_labels[3]]      # col 4
species = data[col_labels[3]]   # col 5

# These are the column headings.
print("col1: ", col_labels[0])
print("col2: ", col_labels[1])
print("col3: ", col_labels[2])
print("col4: ", col_labels[3])
print("col5: ", col_labels[4])


# ###########################################################
# Start looking at statistics per species.
#ax1 = plt.gca()
data.groupby('Name')['SepalLength'].mean().plot(kind='bar')
#data.groupby('Name')['SepalLength'].std().plot(kind='bar', ax=ax1)
plt.show()

