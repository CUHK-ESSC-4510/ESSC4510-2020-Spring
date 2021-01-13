#========================================#
# ESSC 4510 Tutorial 04 Python Script
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

# Ex 4.2
# Get the temperature and rainfall data from the given .nc file.
# The data are the same as Tutorial 3.
#========================================#
data_4 = xr.open_dataset("temp_precip_city_China_July_1998-2015.nc")
prec_BJ, prec_WH, prec_HK = data_4["prec_BJ"], data_4["prec_WH"], data_4["prec_HK"]
temp_BJ, temp_WH, temp_HK = data_4["temp_BJ"], data_4["temp_WH"], data_4["temp_HK"]



#========================================#

# Evaluate the mean and standard deviation of the data,
# by np.mean(), np.std().
#========================================#



#========================================#

# Part (a)
#================================================================================#
# START OF FUNCTION
#================================================================================#
def hist_and_fit(time_series, var_name, mean, std):
    """
        A plotting function to produce the required graph.
        Apply this function for all the six sets of data.
        time_series: the precipitation or temperature time series.
        var_name: the name of the variable.
        mean: the mean of the data.
        std: the standard deviation of the data.
    """

    # Create an empty figure.
    #========================================#
    fig = plt.figure()
    ax = fig.add_subplot()



    #========================================#

    # Plot the histogram by plt.hist().
    # You may want to scale y-axis to fraction,
    # by setting density = True.
    # Since we read the data into an xarray Dataset,
    # we need to convert it into an numpy array,
    # by np.array() to avoid bugs.
    #========================================#



    #========================================#

    # Compute the fitted parameters for Gaussian and Gamma distribution,
    # by matching the mean and standard deviation of the actual data.
    #========================================#
    # Fitting Gaussian Distribution.
    mu = mean
    sigma = std
    # Derive the relation for Gamma distribution.



    #========================================#

    # Plot the fitted distribution by stats.norm.pdf() and stats.gamma.pdf().
    # For the Gamma one, please read the documentation carefully
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gamma.html.
    #========================================#
    x = np.linspace(0, 100, 101) # Sampling points, adjust the numbers yourself.
    # Mapping the corresponding Gaussian pdf from x.
    y_gaussian = scipy.stats.norm.pdf(x, mu, sigma)
    # Plot the fitted Gaussian pdf.
    ax.plot(x, y_gaussian)
    # Repeat the similar procedure for Gamma distribution.



    #========================================#

    # Add legends, titles, axis labels, as well as 
    # the values of the fitted parameters, either
    # in a textbox, using ax.text(), or simply in the legends.
    # https://matplotlib.org/3.1.1/gallery/recipes/placing_text_boxes.html
    #========================================#



    #========================================#

    # Output the figure as .png format.
    #========================================#
    fig.savefig("Ex_4_2a_" + var_name + ".png")



    #========================================#

#================================================================================#
# END OF FUNCTION
#================================================================================#

# Call the function hist_and_fit() for all the six cases.
#========================================#



#========================================#

# Part (b)
#================================================================================#
# START OF FUNCTION
#================================================================================#
def QQ_plot(time_series, var_name, mean, std, fit="Gaussian"):
    """
        A function drawing the QQ plot.
        Apply this function when suitable.
        The first 4 paramters are the same for hist_and_fit.
        fit: fitting Gaussian or Gamma, default is Gaussian.
    """

    # Create an empty figure.
    #========================================#
    fig = plt.figure()
    ax = fig.add_subplot()



    #========================================#

    # Extract the 1st-99th percentiles from the observation,
    # by np.percentile(<data>, <percentiles>).
    #========================================#
    per_obs = np.percentile(time_series, np.arange(1,100))



    #========================================#

    # Compute the 1st-99th percentiles from the fitted distribuition,
    # either for Gaussian or Gamma.
    #========================================#
    if fit == "Gaussian":
        # Fitting parameters.
        mu = mean
        sigma = std
        # Convert the percentiles, or ranks,
        # to cumulative probabilities by formula like Tukey.
        rank = np.arange(1,100)
        prob_fit = (rank - 1/3) / (100 + 1/3)
        # Compute the inverse of CDF to obtain the theoretical percentiles.
        per_fit = scipy.stats.norm.ppf(prob_fit, mu, sigma)
    elif fit == "Gamma":
        # Similar applies for Gamma distribution.
        pass



    #========================================#

    # Draw the diagonal.
    #========================================#
    diag = np.linspace(0, 100, 101) # Adjust the numbers yourself.
    ax.plot(diag, diag)



    #========================================#

    # Draw the scatter plot from both observed and fitted percentiles,
    # by ax.scatter(<fit>, <obs>).
    #========================================#



    #========================================#

    # Add legends, titles, axis labels.
    #========================================#



    #========================================#

    # Output the figure as .png format.
    #========================================#
    fig.savefig("Ex_4_2b_" + var_name + ".png")



    #========================================#

#================================================================================#
# END OF FUNCTION
#================================================================================#

# Call the function QQ_plot() for all the six cases.
#========================================#



#========================================#

# Ex 4.3
#================================================================================#
# START OF FUNCTION
#================================================================================#

def lag_corr(temp, prec, city_name, k):
    """
        Calculate the lagged correlation between two sets of data.
        temp: temperature time series,
        prec: rainfall time series,
        city_name: self-explanatory,
        k: time lag.
    """

    # Evaluate lag-k correlation, 
    # by extracting the earliest n-k data from the first time series,
    # and the latest n-k data from the second time series.
    # Use scipy.stats.pearsonr()[0] to obtain the number.
    #========================================#



    #========================================#

    # Output the correlation by return(<value>).
    #========================================#



    #========================================#

#================================================================================#
# END OF FUNCTION
#================================================================================#

# Use the function lag_corr() to calculate from k = -4 to 4.
#========================================#



#========================================#

# Plot the scatter plot for the case with largest r_k.
#========================================#



#========================================#