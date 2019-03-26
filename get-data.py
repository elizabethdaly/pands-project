# Script to read in iris data

import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file from this directory.
data = pd.read_csv('iris.csv')

# data.index

# Find the column labels.
labels = data.columns
print(labels)

# Separate out the columns according to their indices.
slen = data['SepalLength']
swid = data['SepalWidth']
plen = data['PetalLength']
pwid = data['PetalWidth']

print(slen)
# Plot them.
plt.hist(slen)
plt.show()

