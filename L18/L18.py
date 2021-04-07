#========================================#
# ESSC 4510 Tutorial 18 Python Script
# Name:
# Student ID:
# Sample Script made by Benjamin Loi
#========================================#

# Import Necessary Packages
#========================================#
import pandas as pd # Reading Table
import numpy as np # Processing Array
import matplotlib.pyplot as plt # Drawing Graph



#========================================#

# Ex 18.1
# Read the forecast data.
#========================================#
forecast = pd.read_csv("L18.csv", index_col=0, header=None)
# print(forecast)
yi = np.array(forecast.loc["Forecast probability yi"])
forecast_count = np.array(forecast.loc["Number of times forecast"])
n_occur = np.array(forecast.loc["Number of precipitation occurrences"])



#========================================#

# For yi = 0, 0.1, 0.2, 0.3, ..., 1.0 (11 values),
# there are 10 thresholds yt = 0.05, 0.15, ..., 0.95.
# The amount of "no" forecasts is the sum of forecast_count for all yi < yt, 
# while "yes" forecasts is the sum but for all yi > yt.
# Meanwhile the number of a = "hit" is the sum of n_occur for yi > yt,
# c = "miss" is the sum of n_occur for yi < yt.
# b = "False Alarm" is the amount of "yes" forecast minus a.
# Similarly, d = "Correct Negative" is the amount of "no" minus c.
# "Hit Rate" = a/(a+c), "False Alarm Rate" = b/(b+d).
# The function np.cumsum() can be very helpful.
# Reference: https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html.
#========================================#
yt = (yi[:-1] + yi[1:])/2
# Computing the Hit Rate.
c = np.cumsum(n_occur)[:-1]
a = np.sum(n_occur) - c
HR = a/np.sum(n_occur)
# Computing the False Alarm Rate in a way similar to above.



#========================================#

# Plot the ROC curve, where y is "Hit Rate" and x is "False Alarm".
# You are very experienced in plotting so you can do as you wish.
# The only remainder is to connect the point (0,0) and (1,1) when drawing the curve.
# You may also label the markers using the yt array.
#========================================#



#========================================#