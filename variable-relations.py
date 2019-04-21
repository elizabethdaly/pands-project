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

# Import Numpy
import numpy as np

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
#plt.savefig('PetalWvL_Seaborn.jpeg')
plt.show()

# Do one with hue parameter set to show difference.
g = sb.lmplot(x="PetalLength", y="PetalWidth", hue="Name", truncate=True, height=5, data=data)
plt.title('PetalWidth vs PetalLength fn(species)', fontsize=12)
g.set_axis_labels("PetalLength (mm)", "PetalWidth (mm)")
plt.savefig('Sep_PetalWvL_Seaborn.jpeg')
plt.show()

# ###########################################################
# Try some LSQ fitting using the statsmodels package.
# model=OLS, method=fit OLS=Ordinary Least Squares
# model = sm.OLS(y, X)

#import statsmodels.api as sm
import statsmodels.api as sm

# Ordinary least squares regression: y = m*x
model_Simple = sm.OLS(data['PetalWidth'], data['PetalLength']).fit()
print("Fit pars: ", model_Simple.params)
print("R2 : ", model_Simple.rsquared)
print(model_Simple.summary())

# Add a constant term to OLS fit: y = m*x + c
model = sm.OLS(data['PetalWidth'], sm.add_constant(data['PetalLength'])).fit()
print("Fit pars: ", model.params)
print("R2: ", model.rsquared)
print("Fit summary: ", model.summary())

# Calculate best fit line using the fitting parameters, for a range of integar x values.
xmax = np.ceil((max(data['PetalLength'])))
x = np.arange(0, xmax + 1, 1)
PW_fitSimple = x * model_Simple.params.PetalLength
PW_fit = x * model.params.PetalLength + model.params.const

# Plot the data and fit together.
plt.plot(data['PetalLength'], data['PetalWidth'], 'bo')
plt.plot(x, PW_fitSimple, 'g-')
plt.plot(x, PW_fit, 'r')
plt.xticks(x)
plt.grid(b=True, which='major', axis='both')
plt.title("OLS fit Petal Width vs Length", fontsize=18)
plt.ylabel('Petal Width (cm)', fontsize=16)
plt.xlabel('Petal Length (cm)', fontsize=16)
plt.legend(('Data', 'Simple fit', 'Fit'))

# Save the figure.
plt.savefig('OLSfit_PWvL.jpeg')
plt.show()


