#!/usr/bin/env python
# coding: utf-8

import xarray as xr
import numpy as np

from collections import namedtuple

# Named tuple to create a custome type for the areas
Area = namedtuple("Area", "lonMin lonMax latMin latMax")

EAST_EQUATORIAL_ATLANTIC_AREA = Area(-20, -4, 0, 16)
CENTRAL_EQUATORIAL_ATLANTIC_AREA = Area(-45, -19, 0, 16)
WEST_EQUATORIAL_ATLANTIC_AREA = Area(-60, -44, 0, 16)
CARIBBEAN_SEA_AREA = Area(-80, -64, 10, 21)

SARGASSO_NE_AREA = Area(-45, -39, 27, 31)
SARGASSO_SE_AREA = Area(-45, -39, 25, 27)
SARGASSO_SW_AREA = Area(-50, -45, 25, 27)
SARGASSO_NW_AREA = Area(-50, -45, 27, 31)

def inAreaBinary(i, j, area):
    # using int() on booleans converts true to 1 and false to 0
    # also used checked if the value was between the areas rather than in the range, not certain if this is quicker bust should save memory
    return int(area.lonMin <= i <= area.lonMax and j in area.latMin <= j <= area.latMax) 

#Load data
ds = xr.open_dataset('./c.nc')
traj_list = np.arange(0,490000+1)

east_atl_count = []
central_atl_count = []
west_atl_count = []
csea_count = []

#For each particle find if it enters the lat lon box at each timestep
for index in traj_list:
    east_array = []
    central_array = []
    west_array = []
    csea_array = []
    particle = ds.sel(traj=index)
    lon = particle['lon'].values
    lat = particle['lat'].values 
    XY = list(zip(lon,lat))

    for i, j in XY:
        # Placed all of these in the same for loop so the same values aren't looped over 4 times
        east_array.append(inAreaBinary(i, j, EAST_EQUATORIAL_ATLANTIC_AREA)) 
        central_array.append(inAreaBinary(i, j, CENTRAL_EQUATORIAL_ATLANTIC_AREA))
        west_array.append(inAreaBinary(i, j, WEST_EQUATORIAL_ATLANTIC_AREA))
        csea_array.append(inAreaBinary(i, j, CARIBBEAN_SEA_AREA))
    
    #Get logical array for each particle (at each time step) for the 4 boundary boxes
    east_atl_count.append(east_array)
    central_atl_count.append(central_array)
    west_atl_count.append(west_array)
    csea_count.append(csea_array)

#Find if initial position is within determined grid boxes of the Sargasso Sea (North East, SE, SW, & NW)
for index in traj_list:
    sargasso_ne = []
    sargasso_se = []
    sargasso_sw = []
    sargasso_nw = []
    particle = ds.sel(traj=index)
    lon = particle['lon'].values
    lat = particle['lat'].values 
    XY = list(zip(lon,lat))  

    sargasso_ne.append(inAreaBinary(lon[0], lat[0], SARGASSO_NE_AREA)) 
    sargasso_se.append(inAreaBinary(lon[0], lat[0], SARGASSO_SE_AREA)) 
    sargasso_sw.append(inAreaBinary(lon[0], lat[0], SARGASSO_SW_AREA)) 
    sargasso_nw.append(inAreaBinary(lon[0], lat[0], SARGASSO_NW_AREA)) 

#Find if a particle starts and ends in each source-destination
print('Creating connectivity matrices')
ne_to_east_atl = sargasse_ne * east_atl_count
ne_to_central = sargasso_ne * central_atl_count
ne_to_west = sargasso_ne * west_atl_count
ne_to_csea = sargasso_ne * csea_count 

se_to_east_atl = sargasse_se * east_atl_count
se_to_central = sargasso_se * central_atl_count
se_to_west = sargasso_se * west_atl_count
se_to_csea = sargasso_se * csea_count

sw_to_east_atl = sargasse_sw * east_atl_count
sw_to_central = sargasso_sw * central_atl_count
sw_to_west = sargasso_sw * west_atl_count
sw_to_csea = sargasso_sw * csea_count 

nw_to_east_atl = sargasse_sw * east_atl_count
nw_to_central = sargasso_sw * central_atl_count
nw_to_west = sargasso_sw * west_atl_count
nw_to_csea = sargasso_sw * csea_count 
