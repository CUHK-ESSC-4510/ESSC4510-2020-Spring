#========================================#
# ESSC 4510 Tutorial 02 Python Script
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



#========================================#

# Ex 2.1
# Read HKO climate data using the same way as in Ex 1.1.
#========================================#



#========================================#

# Evaluate lag-k auto-correlation, 
# by extracting the earliest and latest n-k data as two arrays,
# and use scipy.stats.pearsonr(<>, <>)[0] with the arrays as arguments,
# since lag-k auto-correlation is essentially the correlation 
# between the earliest and latest n-k data.
# Use for loop to evaluate from k = 1 to 5
#========================================#
# for k in np.arange(1, 5+1):



#========================================#


# Ex 2.2
# Prepare a figure with 2x2 panels.
# With 3 variables, there will be 3C2 = 3 scatter plots.
#========================================#
n_var = 3
fig, axes = plt.subplots(n_var-1, n_var-1)
plt.show()



#========================================#

# Use <ax>.scatter(x,y) to produce a scatter plot on a particular subplot.
# Add legends, titles, axis labels for each subplot.
# Double for loops can be used to go through all the panels as shown below.
#========================================#
# for i in np.arange(n_var-1):
    # for j in np.arange(i+1):
        # print(i,j)
        # do something on axes[i,j] ...



#========================================#

# (optional) Remove the unused axes by <ax>.set_visible(False).
#========================================#



#========================================#

# Output the figure as .png format.
#========================================#
fig.savefig("Ex_2_2.png")



#========================================#

# Ex 2.3
# Reference: https://realpython.com/numpy-scipy-pandas-correlation-python/,
# and https://benalexkeen.com/correlation-in-python/.
# For Pearson correlation, np.corrcoef() is sufficient.
#========================================#




#========================================#

# For Spearman correlation, create a 3x3 array,
# and use double for loop to run all the combinations.
# At each iteration, fill in the array element,
# with corresponding Spearman correlation computed by scipy.stats.spearmanr(x,y)[0].
#========================================#
Spearman_corr = np.array([3,3])
# for i in np.arange(n_var):
    # for j in np.arange(n_var):
        # do something on column i and j from HKO data



#========================================#
