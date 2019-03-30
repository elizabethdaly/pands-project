# pands-project
## Elizabeth Daly
### January-April 2019
### HDip Data Analytics 2019 Programming and Scripting Project

Git-hub repository at:
https://github.com/elizabethdaly/pands-project.git

# The Fisher Iris Data Set

## Introduction
Sir Ronald Fisher (1890-1962) was a British statistician and biologist who is best known for his work in the application of statistics to the design of scientific experiments. Following undergraduate study in mathematics at the University of Cambridge, he remained there for postgraduate work in physics, including the theory of errors. He continued his research in statistics over the next few years while working in various jobs - insurance company ststistician and teacher. In 1919 he became the statistician at the Rothamsted Experimental Station in Hertfordshire,where he had access to huge amounts of agricultural data. Here, he developed and applied statistical methods to the design of plant breeding experiments in order to get maximum useful information from the experiments while minimizing time, effort, and money. He held academic positions at University College London and Cambridge University before retiring to Australia, where he died in 1962. During his career he published many articles and books on various topics in statistics and genetics, including the method of maximum likelihood estimation and the analysis of variance.

Fisher introduced the iris flower data set and the linear discriminent analysis (LDA) in a 1936 publication. LDA is a method to reduce the number of dimensions in data sets in order to perform pattern classification or machine learning. As the MathWorks reference below states, if one has a data set containing observations with measurements on many variables and their known classes, could this data be used to determne which class measurements from new  observations are most likely to belong to? It seems to be a popular data set for demonstrating how to perform classification and for providing training sets in machine learning (see Wolfram reference below).  

### Description of the data set
Fisher's (or Anderson's) iris data set gives the measurements in centimetres of the variables sepal length, sepal width, petal length, and petal width (in that order) for 50 flowers from each of three species of iris. The species are _Iris setosa_, _Iris versicolor_, and _Iris virginica_. The data set consists of 150 rows or observations (50 samples from each species) by five columns. The first four columns contain the samples/measurements and the fifth contains the species name (or class). I obtained the data set as a csv file from GitHub as detailed below.

## Analysis
The Python script **get-data.py** reads the csv file containing the data set and does some basic analysis. I import the modules I need for data analysis and plotting: Pandas, NumPy and matplotlib. The csv file is then read into a DataFrame - the basic data format for Pandas. Each row of a DataFrame represents a sample of data, with each column containing a different variable; the format is therefore compatible with the Iris Data Set we are investigating for this project. I use various **Pandas** functions as follows:
* .head() to look at the first few lines.
* .dtypes to find the data types of each column.
* .shape to find the (number of rows, number of columns) in the dataframe.
* .columns to find the labels of each column.
* .describe() to generate some descriptive statistics for each column of numeric data. The output of describe() is another dataframe.

The head of the file looks like:

SepalLength | SepalWidth | PetalLength | PetalWidth | Name
------------|------------|-------------|------------|-----
5.1 | 3.5 | 1.4 | 0.2 | Iris-setosa
4.9 | 3.0 | 1.4 | 0.2 | Iris-setosa
4.7 | 3.2 | 1.3 | 0.2 | Iris-setosa
4.6 | 3.1 | 1.5 | 0.2 | Iris-setosa
5.0 | 3.6 | 1.4 | 0.2 | Iris-setosa

The column labels are SepalLength, SepalWidth, PetalLength, and PetalWidth all of type float64. The fifth column label is Name of type object (or string); it holds the name of the species. The dataframe size is 150 rows x 5 columns.

The descriptive statistics are as follows:

SepalLength | SepalWidth | PetalLength | PetalWidth | Name
------------|------------|-------------|------------|-----
count | 150.000000 |150.000000 | 150.000000 | 150.000000
mean | 5.843333 | 3.054000 | 3.758667 | 1.198667
std | 0.828066 | 0.433594 | 1.764420 | 0.763161
min | 4.300000 | 2.000000 | 1.000000 | 0.100000
25% | 5.100000 | 2.800000 | 1.600000 | 0.300000
50% | 5.800000 | 3.000000 | 4.350000 | 1.300000
75% | 6.400000 | 3.300000 | 5.100000 | 1.800000
max | 7.900000 | 4.400000 | 6.900000 | 2.500000

I then plot the data columns as seperate data series on a single plot using **matplotlib**. I'll explain the commands here the first time I use them.
* plt.xlim() to set x axis range.
* plt.xticks() to place tick marks on x axis according to a **NumPy** .arange() command.
* plt.gca() keeps track of the axes so that the columns can be plotted on the same graph.
* plt.title(), plt.ylabel(), and plt.xlabel() set up the graph titles and x and y axes labels.
* plt.legend() to add a legend and place it in 'best' location.
* plt.grid() to add gridlines.
* plt.davefig() to save the figure.
* plt.show() to display it.



## Conclusion

**References**
1. Sir Ronald Fisher: https://www.britannica.com/biography/Ronald-Aylmer-Fisher 
2. Sir Ronald Fisher: https://study.com/academy/lesson/sir-ronald-fisher-biography-contributions-to-statistics.html
3. Linear Discriminant Analysis: https://sebastianraschka.com/Articles/2014_python_lda.html
4. MathWorks: https://uk.mathworks.com/help/stats/examples/classification.html
5. Wolfram Data Repository: https://datarepository.wolframcloud.com/resources/Sample-Data-Fishers-Irises
6. Iris data set: https://github.com/pandas-dev/pandas/blob/master/pandas/tests/data/iris.csv
7. pandas Python data analysis library: https://pandas.pydata.org/
8. matplotlib Python 2D plotting library: https://matplotlib.org/
9. Pandas DataFrames: https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/
10. Plotting examples: http://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot

