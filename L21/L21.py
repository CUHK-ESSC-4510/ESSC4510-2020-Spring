#========================================#
# ESSC 4510 Tutorial 21 Python Script
# Name:
# Student ID:
# Sample Script made by Benjamin Loi
#========================================#

# Import Necessary Packages
#========================================#
import numpy as np # Processing Array
import xarray as xr # Reading .nc File
import matplotlib.pyplot as plt # Drawing Graph
import cartopy.crs as ccrs # Map Projection for Plotting
import sklearn.decomposition # Statistical Decomposition Methods



#========================================#

# Ex 21.2
# Read the SST data.
# Generate new arrays to store the coordinates.
#========================================#
SST_data = xr.open_dataset("HadISST_sst.nc")
time_array = SST_data["time"]
lat_array = SST_data["latitude"]
lon_array = SST_data["longitude"]
SST = SST_data["sst"]



#========================================#

# Since the data contain land grid points that have NaN values,
# we need to identify them and fill them with a gabbage value.
# To avoid interfering with other valid grid points,
# the entire time series for land grid points with NaN values,
# are set to all zeros (or other values like -999), 
# by using <DataArray>.where(), whose usage can be seen from
# http://xarray.pydata.org/en/stable/generated/xarray.DataArray.where.html.
# Additionally, we want to filter away the icy polar regions, 
# that also have gabbage negative values, by
# forcing all negative entries to be zeros too.
#========================================#
# Identify any grids that contains NaN.
NaN_grids = xr.ufuncs.isnan(SST)
# If a particular lat/lon location has at least one NaN,
# then it is flagged and masked.
land_mask = (NaN_grids.sum(dim="time") != 0)
# Another mask for the Frozen, that
# you can do it by emulating what is written above.



# Setting all masked data points to be zero by where().
# SST_masked = #####



#========================================#


# Remove the climatology from the time series to extract the anomalies.
# By using groupby functionality, where the documentation can be seen from
# http://xarray.pydata.org/en/stable/groupby.html.
# Subsequently, detrend the anomaly time series by removing the mean and linear trend.
# We can use <Dataset>.polyfit(dim="time", deg=1) 
# to apply linear regression for each grid in time.
# and use xarray.polyval(<time_array>, <coeffs>.polyfit_coefficients),
# where <coeffs> are the outputs from polyfit,
# to recover the linear fit for every grid.
# Finally, we simply subtract the linear fit from the time series.
# Reference: https://xarray.pydata.org/en/stable/generated/xarray.Dataset.polyfit.html,
# and http://xarray.pydata.org/en/stable/generated/xarray.polyval.html.
#========================================#
# SST_climatology = SST_masked.groupby("time.month").mean("time")
# SST_anomaly = SST_masked.groupby("time.month") - SST_climatology
# SST_linear_coeffs = SST_anomaly.polyfit(dim="time", deg=1)
# SST_linear_fit = xr.polyval(time_array, SST_linear_coeffs.polyfit_coefficients)
# SST_anomaly_detrend = SST_anomaly - SST_linear_fit



#========================================#


# Apply the PCA model from scikit-learn.
# First we need to reshape the anomaly data into 2D array,
# to facilitate this, we retrieve the order of coordinate axes,
# and shuffle the raw numpy array extracted from using .values
# so that the dimensions are in the order of (time, lat, lon),
# with <SST_array>.transpose(). Actually it is already in that order, 
# but we should still do this to allow greater flexibility.
# Finally do <SST_array>.reshape(len(time_array), -1)
# so that it becomes the form that can be used in the PCA functionality.
# Reference: https://numpy.org/doc/stable/reference/generated/numpy.transpose.html,
# and https://numpy.org/doc/stable/reference/generated/numpy.reshape.html.
#========================================#
# SST_dims = SST_anomaly_detrend.dims
# time_axis = SST_dims.index("time")
# lat_axis = SST_dims.index("latitude")
# lon_axis = SST_dims.index("longitude")



#========================================#

# Call the PCA functionality from sklearn.
# Fit the restructured SST array into the model.
# Reference: https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html,
# as well as https://stackabuse.com/implementing-pca-in-python-with-scikit-learn/.
# Useful attributes and methods from the PCA model are
# <PCA_model>.components_ which get the required eigenvector,
# that can be reshaped to find the loading pattern.
# and <PCA_model>.transform(<SST_array>), which can find 
# the evolution of the principal component index in time.
#========================================#
PCA_model = sklearn.decomposition.PCA(n_components=1) # Only look at the first principal components.
# PCA_model.fit()
# PCA_eigenv = PCA_model.components_[0]
# loading_pattern = PCA_eigenv.reshape(#####)



#========================================#

# Plot the EOF on a world map.
# The same familar way as before, but with an extra argument
# for the contourf function (..., transform=ccrs.PlateCarree()).
# Also graph the time-series for the first principal component.
#========================================#
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()




#========================================#