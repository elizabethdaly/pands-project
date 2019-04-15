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

# Pairplot
sb.set(style="ticks")
sb.pairplot(data, hue="Name")
plt.show()
