# Elizabeth Daly
# HDip Data Analytics 2019 pands-project
# 
# Script to read in the iris data set.
#
# ###########################################################
#
# Import pandas data analysis library.
import pandas as pd

# Import matplotlib for 2D plotting.
import matplotlib.pyplot as plt

# Read the iris.csv file from this directory.
# The result is a pandas DataFrame
data = pd.read_csv('iris.csv')

# Look at various attributes of the data to get an idea of its structure.

# Print the first few lines.
print(data.head())

# What are the data types?
print(data.dtypes)


quit()

print(data.index)

# Find the column labels.
labels = data.columns
print(labels)
labels
print(len(labels))
print(labels[0])
quit()

# Separate out the columns according to their indices.
slen = data['SepalLength']
swid = data['SepalWidth']
plen = data['PetalLength']
pwid = data['PetalWidth']

print(slen)
# Plot them.
plt.hist(slen)
plt.show()

