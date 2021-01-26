#========================================#
# ESSC 4510 Tutorial 07 Python Script
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

# Ex 7.1
# Store the June temperature and pressure as a Pandas table.
#========================================#
data_7 = pd.DataFrame({"Temp": [26.1, 24.5, 24.8, 24.5, 24.1, 24.3, 26.4, 24.9, 23.7, 23.5,
                    24.0, 24.1, 23.7, 24.3, 26.6, 24.6, 24.8, 24.4, 26.8, 25.2],
                    "Pres": [1009.5, 1010.9, 1010.7, 1011.2, 1011.9, 1011.2, 1009.3, 1011.1, 1012.0, 1011.4,
                    1010.9, 1011.5, 1011.0, 1011.2, 1009.9, 1012.5, 1011.1, 1011.8, 1009.3, 1010.6]})
print(data_7)



#========================================#

# Carry out Linear Regression on the data, and compute R^2.
# There are many packages providing functions for that, such as 
# scipy.stats.linregress() and sklearn.linear_model.LinearRegression().
# For statistical purpose, please use statsmodels.api.OLS(),
# as it provides a summary for many important quantities,
# answers for some parts can be easily read from.
# Reference: https://datatofish.com/statsmodels-linear-regression/.
# s_e^2 can be checked via <model>.mse_resid,
# or using .summary2() instead and check the scale entry.
# The whole documentation can be viewed at 
# https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.RegressionResults.html#statsmodels.regression.linear_model.RegressionResults.
# Extract the required values from the instance, no hard coding is allowed!
#========================================#
Y = data_7["Temp"]
X = sm.add_constant(data_7["Pres"]) # Adding the intercept term.



#========================================#

# Evaluate the prediction variance for x_0 = 1013 mb,
# as well as for a nearby range like 1005 - 1015 mb.
# and check the probability and prediction interval, by
# scipy.stats.norm.cdf() and scipy.stats.norm.ppf().
#========================================#
p = np.arange(1005, 1015, 0.05)



#========================================#

# Plot the regression function and the 95% prediction interval.
# I think you have been familiar with plotting,
# so I won't write any outline from now.
#========================================#



#========================================#
