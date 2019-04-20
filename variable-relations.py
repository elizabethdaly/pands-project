# Elizabeth Daly
# HDip Data Analytics 2019 pands-project
# 
# class-separation.py
# Script to read in and analyse the iris data set
# How are the variables related to each other?
# ###########################################################

# Import Pandas data analysis library.
import pandas as pd

# Import matplotlib for 2D plotting.
import matplotlib.pyplot as plt

# Import Seaborn
import seaborn as sb

# Read the iris.csv file from this directory.
data = pd.read_csv('iris.csv')

# ###########################################################
# Pandas scatter matrix to see how the variables are related - or not.

# Needed this to avoid a FutureWarning related to location of plotting module.
# Note that all species are plotted in same colour. 
from pandas.plotting import scatter_matrix
pd.plotting.scatter_matrix(data, alpha=0.8)
plt.savefig('ScatterMatrix_Pandas.jpeg')
plt.show()

# ###########################################################
# Seaborn scatter matrix via pairplot.
# Each "Name" has a different colours so species can be differentiated.
# Stick to the colour palette I've already used in histograms etc.
sb.set(style="ticks", palette="pastel")
sb.pairplot(data, hue="Name", diag_kind='hist')
plt.savefig('ScatterMatrix_Seaborn.jpeg')
plt.show()

# ###########################################################
# Try linear regression on some combinations of variables.
# Adapted from : https://seaborn.pydata.org/examples/multiple_regression.html?highlight=iris%20data%20set
# Example plots Sepal length on x, Sepal width on y. Check I get same plot before trying other variables.

# sb.set()
# # Plot sepal_width as a function of sepal_length
# g = sb.lmplot(x="SepalLength", y="SepalWidth", hue="Name", \
# truncate=True, height=5, data=data)
# # Use more informative axis labels than are provided by default
# g.set_axis_labels("Sepal length (mm)", "Sepal width (mm)")
# plt.show()

# Plot PetalLength as a function of PetalWidth
# Leave out hue="Name" as want to fit data from all species to same line.
sb.set(palette="muted")
g = sb.lmplot(x="PetalWidth", y="PetalLength", truncate=True, height=5, data=data)
plt.title('PetalLength vs PetalWidth', fontsize=12)
g.set_axis_labels("PetalWidth (mm)", "PetalLength (mm)")
plt.savefig('PetalLvW_Seaborn.jpeg')
plt.show()

# Plot PetalWidth as a function of PetalLength
g = sb.lmplot(x="PetalLength", y="PetalWidth", truncate=True, height=5, data=data)
plt.title('PetalWidth vs PetalLength', fontsize=12)
g.set_axis_labels("PetalLength (mm)", "PetalWidth (mm)")
plt.savefig('PetalWvL_Seaborn.jpeg')
plt.show()

# Do one with hue parameter set to show difference.
g = sb.lmplot(x="PetalLength", y="PetalWidth", hue="Name", truncate=True, height=5, data=data)
plt.title('PetalWidth vs PetalLength', fontsize=12)
g.set_axis_labels("PetalLength (mm)", "PetalWidth (mm)")
plt.savefig('Sep_PetalWvL_Seaborn.jpeg')
plt.show()

# ###########################################################

