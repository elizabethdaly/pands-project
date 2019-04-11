# Elizabeth Daly
# HDip Data Analytics 2019 pands-project
# 
# class-separation.py
# Script to read in and analyse the iris data set
#
# ###########################################################

# Import Pandas data analysis library.
import pandas as pd

# Import matplotlib for 2D plotting.
import matplotlib.pyplot as plt

# Read the iris.csv file from this directory.
data = pd.read_csv('iris.csv')
# print(data.head())

d_shape = data.shape
print("n rows = ", d_shape[0], ", n_cols = ", d_shape[1] )

# What are the column labels of the DataFrame?
col_labels = data.columns
print("Data column labels: ", col_labels)

# List the unique values in data['Name'] column i.ie species.
# Need these for histogram legend.
species = data.Name.unique()
print("The three species are: ", species)

# Histogram of SepalLength for all species 
# There's only one legend, so I have to get the 3 species names into it in legend handle.
data.groupby('Name')['SepalLength'].hist(bins=10, alpha=0.5, stacked=True)
plt.title('SepalLength', fontsize=18)
plt.xlabel('cm', fontsize=16)
plt.ylabel('Count', fontsize=16)
plt.legend((species), loc='best', fontsize=12)
plt.savefig('Hist_SepalLength.jpeg')
plt.show()

# Histogram of SepalWidth for all species 
data.groupby('Name')['SepalWidth'].hist(bins=10, alpha=0.5, stacked=True)
plt.title('SepalWidth', fontsize=18)
plt.xlabel('cm', fontsize=16)
plt.ylabel('Count', fontsize=16)
plt.legend((species), loc='best', fontsize=12)
plt.savefig('Hist_SepalWidth.jpeg')
plt.show()

# Histogram of PetalLength for all species 
data.groupby('Name')['PetalLength'].hist(bins=10, alpha=0.5, stacked=True)
plt.title('PetalLength', fontsize=18)
plt.xlabel('cm', fontsize=16)
plt.ylabel('Count', fontsize=16)
plt.legend((species), loc='best', fontsize=12)
plt.savefig('Hist_PetalLength.jpeg')
plt.show()

# Histogram of PetalWidth for all species 
data.groupby('Name')['PetalWidth'].hist(bins=10, alpha=0.5, stacked=True)
plt.title('PetalWidth', fontsize=18)
plt.xlabel('cm', fontsize=16)
plt.ylabel('Count', fontsize=16)
plt.legend((species), loc='best', fontsize=12)
plt.savefig('Hist_PetalWidth.jpeg')
plt.show()


# scatter matrix?
data.plot.scatter(x='SepalLength', y='SepalWidth')
plt.show()