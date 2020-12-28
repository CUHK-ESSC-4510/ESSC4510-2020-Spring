#========================================#
# ESSC 4510 Tutorial 01 Python Script
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

# Copy the whole rows of HKO rainfall data from 2001 to 2020, 
# and paste into an Excel spreadsheet, (important) saved as a .csv file.

# Ex 1.1
# Read the .csv file into a table using pandas.
#========================================#
HKO_data_rainfall = pd.read_csv("test.csv", # Replace the file name appropriately
                        names=["Year","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]) # Define the header names
print(HKO_data_rainfall)



#========================================#

# Select July rainfall data for the required years.
#========================================#
years = HKO_data_rainfall["Year"]
required_years = np.logical_and(2004 <= years, years <= 2008) # Replace the numbers with suitable years
rainfall_Jul = HKO_data_rainfall["Jul"]
rainfall_Jul_period = rainfall_Jul[required_years]
print(rainfall_Jul_period)



#========================================#


# Compute the median and mean,
# by using the functions np.mean(<>), np.median(<>), or
# the methods <>.mean(), <>.median() on Pandas table.
#========================================#



#========================================#

# Ex 1.2
# Copy and modify the first part of Ex 1.1 accordingly to process pressure data.

# Calculate the median, upper and lower quantiles first,
# by using np.median(<>), np.percentile(<>, <25/75>) (or np.quantile(<>, <0.25/0.75>)),
# or <>.median(), <>.quantile(<0.25/0.75>) on Pandas table.
#========================================#



#========================================#

# Subsequently calculate the IQR - Inter-quantile Range,
# and MAD - Median Absolute Deviation.
# np.abs() is useful for computing MAD.
#========================================#



#========================================#

# Standard deviation is simply obtained by
# np.std(<>, ddof=1), where ddof=1 indicates the sample standard deviation,
# by default ddof=0 which refers to the population standard deviation.
# Alternatively, apply <>.std() on Pandas table, note that however
# by default ddof=1 so the output is already the sample standard deviation.
#========================================#



#========================================#

# Ex 1.3
# Create an empty figure.
#========================================#
fig = plt.figure()
ax = fig.add_subplot()



#========================================#

# Sort the data by using np.sort(<>) and store the result in another variable.

# Prepare the cumulative probabilities using one of the formula provided in the slide.
# Example: Tukey, Weibull.
#========================================#
n_years = 5 # No. of years, please modify accordingly.
cumul_prob = ((np.arange(n_years)+1)-0.5)/n_years # Here Hazen formula is used. 
# (important) Please use other formula by changing the expression.



#========================================#

# Plot the CFD - Cumulative Frequency Distribution by using plt.step(<sorted values>, <cumulative probabilities>).
# Usage: https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.step.html
#========================================#



#========================================#

# Plot the histogram on the same figure by plt.hist().
# Usage: https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.hist.html
#========================================#



#========================================#

# (important) You need to add legends, titles, axis labels,
# as well as tweak some parameters in the plotting function to refine the plots.
#========================================#



#========================================#

# Output the figure as .png format.
#========================================#
fig.savefig("Ex_1_3.png")



#========================================#