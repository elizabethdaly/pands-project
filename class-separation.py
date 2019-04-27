# Elizabeth Daly
# HDip Data Analytics 2019 pands-project
# 
# class-separation.py
# Script to read in and analyse the iris data set
# How well separated are the species?
# ###########################################################

# Import Pandas data analysis library.
import pandas as pd

# Import matplotlib for 2D plotting.
import matplotlib.pyplot as plt

# Import Seaborn
import seaborn as sb

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

# ###########################################################
# Histogram of SepalLength for all species.
# There's only one legend, so I have to get the 3 species names into it in legend handle.
data.groupby('Name')['SepalLength'].hist(bins=10, alpha=0.5, stacked=True)
plt.title('SepalLength', fontsize=18)
plt.xlabel('cm', fontsize=16)
plt.ylabel('Count', fontsize=16)
plt.legend((species), loc='best', fontsize=12)
plt.savefig('Hist_SepalLength.jpeg')
plt.show()

# Histogram of SepalWidth for all species.
data.groupby('Name')['SepalWidth'].hist(bins=10, alpha=0.5, stacked=True)
plt.title('SepalWidth', fontsize=18)
plt.xlabel('cm', fontsize=16)
plt.ylabel('Count', fontsize=16)
plt.legend((species), loc='best', fontsize=12)
plt.savefig('Hist_SepalWidth.jpeg')
plt.show()

# Histogram of PetalLength for all species.
data.groupby('Name')['PetalLength'].hist(bins=10, alpha=0.5, stacked=True)
plt.title('PetalLength', fontsize=18)
plt.xlabel('cm', fontsize=16)
plt.ylabel('Count', fontsize=16)
plt.legend((species), loc='best', fontsize=12)
plt.savefig('Hist_PetalLength.jpeg')
plt.show()

# Histogram of PetalWidth for all species.
data.groupby('Name')['PetalWidth'].hist(bins=10, alpha=0.5, stacked=True)
plt.title('PetalWidth', fontsize=18)
plt.xlabel('cm', fontsize=16)
plt.ylabel('Count', fontsize=16)
plt.legend((species), loc='best', fontsize=12)
plt.savefig('Hist_PetalWidth.jpeg')
plt.show()

# ###########################################################
# Plot all four histograms in one figure using subplot.
# Edit legend for these small graphs.
# Leave out some x and y axes titles to avoid crowding.
plt.subplot(2,2,1)
data.groupby('Name')['SepalLength'].hist(bins=10, alpha=0.5, stacked=True)
plt.title('SepalLength', fontsize=12)
#plt.xlabel('cm', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.legend((species), loc='best', fontsize=10, fancybox=True, framealpha=0.5)

plt.subplot(2,2,2)
data.groupby('Name')['SepalWidth'].hist(bins=10, alpha=0.5, stacked=True)
plt.title('SepalWidth', fontsize=12)
#plt.xlabel('cm', fontsize=10)
#plt.ylabel('Count', fontsize=10)
plt.legend((species), loc='best', fontsize=10, fancybox=True, framealpha=0.5)

plt.subplot(2,2,3)
data.groupby('Name')['PetalLength'].hist(bins=10, alpha=0.5, stacked=True)
plt.title('PetalLength', fontsize=12)
plt.xlabel('cm', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.legend((species), loc='best', fontsize=10, fancybox=True, framealpha=0.5)

plt.subplot(2,2,4)
data.groupby('Name')['PetalWidth'].hist(bins=10, alpha=0.5, stacked=True)
plt.title('PetalWidth', fontsize=12)
plt.xlabel('cm', fontsize=10)
#plt.ylabel('Count', fontsize=10)
plt.legend((species), loc='best', fontsize=10, fancybox=True, framealpha=0.5)

# To avoid title and x axis labels overlapping in the subplot.
plt.tight_layout()

plt.savefig('Hist_4attributes.jpeg')
plt.show()

# ###########################################################
# Try Seaborn swarmplot as a cooler way to investigate species differences.

# Slightly modified from https://seaborn.pydata.org/examples/
# scatterplot_categorical.html?highlight=iris%20swarmplot
# style options are: darkgrid, whitegrid, dark, white, ticks
# palette options are: deep, muted, bright, pastel, dark, colorblind
sb.set(style="whitegrid", palette="pastel")


# "Melt" the dataset to "long-form" or "tidy" representation.
# Make "Name" the identifier variable and all other columns just measurements.
iris = pd.melt(data, "Name", var_name="measurement")

# Draw a categorical scatterplot to show each observation.
# Now plot measurements on y axis.
# Each "Name" has a different colour.
# Points are adjusted along categorical (x) axis so that they don't overlap. 
# Each sepcies is coloured as in histograms above for easy comparison.
sb.swarmplot(x="measurement", y="value", hue="Name", data=iris)
plt.savefig('SwarmPlot.jpeg')
plt.show()
