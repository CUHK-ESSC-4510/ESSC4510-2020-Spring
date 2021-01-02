#========================================#
# ESSC 4510 Tutorial 03 Python Script
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
import cartopy.crs as ccrs # Map Projection



#========================================#

# Ex 3.3
# Extract the pressure data from the given .nc file.
#========================================#
data = xr.open_dataset("slp_1948-2014.nc")
slp = data["slp"]
print(slp)
lat_array = data["lat"]
lon_array = data["lon"]



#========================================#

# Locate Darwin (Lat: -12.46, Lon: 130.84) from the data, 
# by manipulating whole array operation, np.abs(), <>.argmin(),
# to search the nearest lat/lon indices.
#========================================#
lat_Darwin = -12.46
lon_Darwin = 130.84
nearest_y = np.abs(lat_Darwin - lat_array).argmin()
print("Nearest y-index:", nearest_y)
# Repeat the same for longitude.



#========================================#

# Find the slp correlation between Darwin and every grid point,
# by using double for loop to fill in a NaN array,
# that has the same lat/lon extent as the slp array.
#========================================#
slp_corr = np.empty([len(lon_array), len(lat_array)]) 
# Notice that slp_corr has the shape (row = nlon) * (column = nlat).
# Make sure that all data are initially NaN to deal with potential problems during later calculation.
slp_corr[:] = np.nan
for i in np.arange(len(lon_array)):
    for j in np.arange(len(lat_array)):
        # Iterate over all grid points, slp[{"lon": i, "lat": j}]),
        # and compared against the Darwin slp at nearest_lat, nearest_lon.
        # Use scipy.stats.pearsonr(<>, <>)[0] to compute the correlation,
        # and assign the answer to the empty array slp_corr.



#========================================#
# Remark: it is possible to utilize vectorized functions only and avoid for loop.

# Prepare the map object for plotting.
#========================================#
fig = plt.figure()
# Mercator Projection
ax_map = fig.add_subplot(1,1,1, projection=ccrs.PlateCarree(central_longitude=0.0))
ax_map.coastlines()



#========================================#

# Draw the correlation contour plot by <>.contour(<lon>, <lat>, <values>)
#========================================#
ct = ax_map.contour(lon_array, lat_array, slp_corr.T, # T stands for transpose.
                    np.linspace(-1, 1, 11)) # the last argument indicates the contour intervals.
ax_map.clabel(ct)
plt.show()



#========================================#
# Remark: A discontinuity appears in the middle of the contour plot.
# This can be fixed by manually cycling the data,
# adding an extra longtitude of 360.0, copied from longtitude of 0.0.
# from cartopy.util import add_cyclic_point may help,
# Reference: https://scitools.org.uk/cartopy/docs/v0.15/cartopy/util/util.html

# Add legends, titles, axis labels.
#========================================#



#========================================#