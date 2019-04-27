# Elizabeth Daly
# HDip Data Analytics 2019 pands-project
# 
# stats-per-species.py
# Script to read in and analyse the iris data set / species.
# Look at the statistics for each species.
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
species = data.Name.unique()
print("The three species are: ", species)

# ###########################################################
# Create 3 dataframes, each corresponding to a single species.
# Select rows based on species names using .loc[]
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

# Summary statistics for Iris-setosa.
setosa_summary = setosa.describe()
print("Iris-setosa")
print(setosa_summary)

# Bar plot with some of the statistics referenced by name.
setosa_summary.loc[['mean', 'std', '50%']].plot.bar()
plt.title("Summary statistics: Setosa", fontsize=18)
plt.ylabel('cm', fontsize=16)
plt.grid()
plt.savefig('SetosaStats.jpeg')
plt.show()

# Summary statistics for Iris-versicolor.
versicolor_summary = versicolor.describe()
print("Iris-versicolor")
print(versicolor_summary)

# Bar plot with some of the statistics referenced by name.
versicolor_summary.loc[['mean', 'std', '50%']].plot.bar()
plt.title("Summary statistics: Versicolor", fontsize=18)
plt.ylabel('cm', fontsize=16)
plt.grid()
plt.savefig('VersicolorStats.jpeg')
plt.show()

# Summary statistics for Iris-virginica.
virginica_summary = virginica.describe()
print("Iris-virginica")
print(virginica_summary)

# Bar plot with some of the statistics referenced by name.
virginica_summary.loc[['mean', 'std', '50%']].plot.bar()
plt.title("Summary statistics: Virginica", fontsize=18)
plt.ylabel('cm', fontsize=16)
plt.grid()
plt.savefig('VirginicaStats.jpeg')
plt.show()

# ###########################################################
# Can also look at some statistics per species using Pandas groupby()
# on the full data set, i.e. no need to create seperate DataFrames for each species.

# Mean
print(data.groupby('Name')['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'].mean())

# Standard deviation
print(data.groupby('Name')['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'].std())

# Bar chart of mean values for each species. 
# Use rot keyword in plot() to align x-tick labels nicely.
data.groupby('Name')['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'].mean(). \
plot(kind='bar',rot='horizontal')
plt.title('Mean variable values', fontsize=18)
plt.ylabel('cm', fontsize=16)
plt.grid()
plt.legend(loc='best', fontsize=12)
plt.savefig('Mean_species.jpeg')
plt.show()

# Bar chart of std values for each species. 
data.groupby('Name')['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'].std(). \
plot(kind='bar', rot='horizontal')
plt.title('Standard deviation of variable values', fontsize=18)
plt.ylabel('cm', fontsize=16)
plt.grid()
plt.legend(loc='best', fontsize=12)
plt.savefig('Std_species.jpeg')
plt.show()

# ###########################################################
# Or, I could do almost all of above visually using Matplotlib 
# box and whisker plot:
# The box extends from the lower to upper quartile values of the data.
# There is a a line at the median. 
# The whiskers extend from the box to show the range of the data. 
# Outlying points are those past the end of the whiskers.

# Setosa
# plt.subplot(3,1,1)
setosa.boxplot()
plt.title("Iris-Setosa", fontsize=18)
plt.ylabel('cm', fontsize=16)
plt.savefig('Setosa_boxplot.jpeg')
plt.show()

# Versicolor
# plt.subplot(3,1,2)
versicolor.boxplot()
plt.title("Iris-Versicolor", fontsize=18)
plt.ylabel('cm', fontsize=16)
plt.savefig('Versicolor_boxplot.jpeg')
plt.show()

# Virginica
# plt.subplot(3,1,3)
virginica.boxplot()
plt.title("Iris-Virginica", fontsize=18)
plt.ylabel('cm', fontsize=16)
plt.savefig('Virginica_boxplot.jpeg')
plt.show()