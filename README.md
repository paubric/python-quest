# Quest
This project is a quantitative series tool for one-liner data visualization through multiple plot types, by using the versatility of Numpy and Matplotlib.

![Figure](https://github.com/paubric/python-quest/blob/master/Figure_1.png)

## Introduction
Quest can perform common descriptive statistics operations and generate a scatter plot and a distribution plot, based on an input file which contains numbers delimited by whitespace. It can be used like this:
```
python3 main.py --file my_file.txt
```
In addition to the visualization, the program also outputs numerical values in the console.
```
Mean:			 6.0
Median:			 7.0
Mode:			 [5 7 9]
Linear Regression:	 0.2060606060606064 * x + 5.07272727272727
Correlation:		 0.2060606060606064
Range:			 9
Interquartile range:	 2
Variance:		 6.6
Standard deviation:	 2.569046515733026
```
## Features
### Scatter Plot
- Plots data
- Plots mean
- Plots median
- Plots regression line
### Distribution Plot
- Plots distribution
- Plots mode(s)
- Plots mean frequency
### Numerical
- Computes mean, median, mode, regression, range, interquintile range, variance, standard deviation, correlation

## TODO
- <s>Mean, median, mode</s>
- <s>Regression</s>
- <s>Range, IQR</s>
- <s>Variance, standard deviation, correlation</s>
