#========================================#
# ESSC 4510 Tutorial 09 Python Script
# Name:
# Student ID:
# Sample Script made by Benjamin Loi
#========================================#

# Import Necessary Packages
#========================================#
import pandas as pd # Reading Table
import numpy as np # Processing Array
import scipy.stats # Computing Statistic
import matplotlib.pyplot as plt # Drawing Graph
import statsmodels.api as sm # Statistical Models



#========================================#

# Ex 9.1
# Store the June temperature and pressure as a Pandas table.
#========================================#
data_9 = pd.DataFrame({"Temp": [26.1, 24.5, 24.8, 24.5, 24.1, 24.3, 26.4, 24.9, 23.7, 23.5,
                    24.0, 24.1, 23.7, 24.3, 26.6, 24.6, 24.8, 24.4, 26.8, 25.2],
                    "Pres": [1009.5, 1010.9, 1010.7, 1011.2, 1011.9, 1011.2, 1009.3, 1011.1, 1012.0, 1011.4,
                    1010.9, 1011.5, 1011.0, 1011.2, 1009.9, 1012.5, 1011.1, 1011.8, 1009.3, 1010.6]})


                    
#========================================#

# Leave-one-out Cross Validation.
# Each time leaving one observation out,
# and regress with the remaining n-1 data.
# Repeat with n times.
# Use scipy.stats.linregress(), or statsmodels.api.OLS().
#========================================#
n = len(data_9)
temp = data_9["Temp"]
pres = data_9["Pres"]
# An array to store the prediction MSE for each iteration.
MSE_predict = np.zeros(n)
for i in np.arange(n):
    # Choose all entries except the one with index i.
    temp_leaveOne = np.delete(temp.values, i)
    pres_leaveOne = np.delete(pres.values, i)
    # Linear Regression with temp_leaveOne and pres_leaveOne.



    # Calculate the error between the prediction, and 
    # the true predictand for the left out entry.



#========================================#

# Plot the regression lines as required.
#========================================#



#========================================#

