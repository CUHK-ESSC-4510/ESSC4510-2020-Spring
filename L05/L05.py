#========================================#
# ESSC 4510 Tutorial 05 Python Script
# Name:
# Student ID:
# Sample Script made by Benjamin Loi
#========================================#

# Import Necessary Packages
#========================================#
import pandas as pd # Reading Table
import numpy as np # Processing Array
import scipy.stats # Computing Statistic
import xarray as xr # Reading .nc File
import matplotlib.pyplot as plt # Drawing Graph



#========================================#

# Ex 5.1
# June Temperature of Non-El Nino and El Nino years.
#========================================#
# Non-El Nino
temp_El = np.array([26.1, 24.8, 26.4, 26.6, 26.8])
n_years_El = len(temp_El)
# El Nino
temp_nEl = np.array([24.5, 24.5, 24.1, 24.3, 24.9, 23.7, 23.5, 
                    24.0, 24.1, 23.7, 24.3, 24.6, 24.8, 24.4, 25.2])
n_years_nEl = len(temp_nEl)



#========================================#

# Evaluate the combined variance for the sample means,
# which is (s_1^2/n_1 + s_2^2/n_2).
#========================================#



#========================================#

# Compute the p-value by scipy.stats.ttest_ind(<data1>, <data2>).
# Reference: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html.
# The argument "equal_var" should be set to a suitable boolean value.
# The second output is the required p-value.
#========================================#



#========================================#

# Calculate the 95% confidence interval for the t-test.
# The null hypothesis has a mean of zero for Delta x = x_1 - x_2.
# Plugging the combined std computed above,
# and ddof = min(n_1, n_2) - 1 into,
# the function scipy.stats.t.interval(0.95, <ddof>, 0, <pooled std>).
# Reference: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html.
#========================================#



#========================================#

# Ex 5.2
# (Important) Please state clearly in your pdf, 
# which test, (a) or (b), is a paired test.
# This is important in deciding the form of t-test used.

# Get the temperature data from the given .nc file.
# The data are the same as Tutorial 3 and 4.
#========================================#
data_5 = xr.open_dataset("temp_precip_city_China_July_1998-2015.nc")



#========================================#

# Select the appropriate data.
# For extracting data from specific time period,
# please take a look at the sample script for tutorial 3.
#========================================#



#========================================#

# Use scipy.stats.ttest_ind() for two independent samples,
# and scipy.stats.ttest_rel() for the paired test,
# to retrieve the p-value, in a way similar to the last part.
#========================================#



#========================================#

# Ex 5.3
# Download and read the HKO rainfall data.
# Remember to upload the related dataset in submission.
#========================================#



#========================================#

# Evaluate the mean and standard deviation of the data,
# by np.mean(), np.std(), or otherwise.
#========================================#



#========================================#

# Fitting Gaussian and Gamma distribution into the data,
# by comparing the parameters like in Tutorial 4.
#========================================#



#========================================#

# Create an empty figure.
#========================================#



#========================================#

# Plot the histogram, by plt/ax.hist() 
# and the two fitted distribution,
# by scipy.stats.norm.pdf() and scipy.stats.gamma.pdf(),
# then plt/ax.plot()
# just like in Tutorial 4.
# To facilitate the Chi-square fitting,
# it is better to save the output returned from calling hist(),
# which is the frequency and range of each bin.
# This can be done like hist_freq = plt.hist()
# Documentation: https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.hist.html.
#========================================#



#========================================#

# We have the observed bin frequency from plt.hist().
# Now we want to compute the expected frequency
# of the two fitted distributions.
# This can be done by extracting the probability within
# the range of each bin, by
# scipy.stats.norm.cdf(<upper limit>) - scipy.stats.norm.cdf(<lower limit>),
# with appropriate parameters for the mean and std.
# Reference: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html.
# Similar for Gamma distribution.

# Notice that they are vectorized functions, which
# take an array and output another array.
# So we can utilize whole array operations, and
# need not to use for loops, which are acceptable anyways.
#========================================#



#========================================#

# Carry out the Chi-square goodness of fit test,
# by scipy.stats.chisquare(<f_obs>, <f_exp>, <ddof>).
# Degree of freedom is no. of bins − no. of parameters fit − 1.
# no. of parameters fit are two in both cases.
# Documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html.
#========================================#



#========================================#
