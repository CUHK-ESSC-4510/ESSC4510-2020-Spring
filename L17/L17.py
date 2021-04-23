#========================================#
# ESSC 4510 Tutorial 17 Python Script
# Name:
# Student ID:
# Sample Script made by Benjamin Loi
#========================================#

# Import Necessary Packages
#========================================#
import numpy as np # Processing Array
import scipy.stats # Computing Statistic
import scipy.linalg # Linear Algebra
import matplotlib.pyplot as plt # Drawing Graph


#========================================#

# Ex 17.1
# Precipitation Data for Canandaigua in 1987 Jan.
# Make a new array to indicate the days with rainfall,
# by boolean comparison.
#========================================#
C_prep = np.array( [0.00, 0.04, 0.84, 0.00, 0.00, 
                    0.00, 0.02, 0.05, 0.01, 0.09,
                    0.18, 0.04, 0.04, 0.00, 0.06,
                    0.03, 0.04, 0.00, 0.00, 0.33,
                    0.02, 0.01, 0.33, 0.08, 0.00,
                    0.00, 0.00, 0.00, 0.01, 0.01,
                    0.13])
# C_israin = 



#========================================#

# Find out the conditional probabilities
# for a rainy/non-rainy day to be followed by
# another rainy/non-rainy day.
# E.g. P(rainy tomorrow|rainy today)
# = no. of rainy -> rainy / (no. of rainy -> rainy + non-rainy)
# the function np.logical_and() and np.sum() may be needed.
#========================================#
# P_rtr = 
# P_rtnr = 
# P_nrtr = 
# P_nrtnr = 

# Organize the probability into a matrix 
# to represent the Markov Chain.
# P_MC = np.array([[P_nrtnr, P_rtnr], [P_nrtr, P_rtr]])



#========================================#

# Perform a Chi-square Test using the function
# scipy.stats.chi2_contingency(),
# Notice that we need the real frequencies, 
# not only the conditional probabilities.
# Reference: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html.
#========================================#



#========================================#

# The stationary probability is simply found
# from the eigenvector for the Markov Chain 
# that corresponds to the eigenvalue of 1.
# Simply use scipy.linalg.eig() on the matrix.
# Documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.eig.html.
# Remember to scale the eigenvector so that 
# the sum of entries along column equals to 1.
# You may also use the formula taught in class.
#========================================#



#========================================#

# The theoretical lag-1 autocorrelation of the Markov Chain,
# will be P(rainy tomorrow|rainy today) - P(rainy tomorrow|non-rainy today).
# Extending the logics for lag-k autocorrelation, 
# we can look at the k-th power of the Markov Chain matrix,
# and perform the subtraction between the elements at the same position.
# Notice matrix multiplication is done by dot product,
# done by np.dot() in Python.
#========================================#



#========================================#

# The required probability for a 3 days wet streak,
# is simply the product of P(2nd wet|1st wet) * P(3rd wet|2nd wet).
# What are they?
#========================================#



#========================================#