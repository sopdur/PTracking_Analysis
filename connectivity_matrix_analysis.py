#!/usr/bin/env python
# coding: utf-8

import xarray as xr
import numpy as np

#Load data
ds = xr.open_dataset('./c.nc')
traj_list = np.arange(0,490000+1)

east_atl_count = []
central_atl_count = []
west_atl_count = []
csea_count = []
lon = []
lat = []

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

    #Particles that travel through the east equatorial Atlantic 
    for i, j in XY:
        if i in np.arange(-20,-4) and j in np.arange(0,16):
            east_array.append(1)
        else:
            east_array.append(0)
    
    #Particles that travel through the central equatorial Atlantic 
    for i, j in XY:
        if i in np.arange(-45,-19) and j in np.arange(0,16):
            central_array.append(1)
        else:
            central_array.append(0)
    
    #Particles that travel through the west equatorial Atlantic 
    for i, j in XY:
        if i in np.arange(-60,-44) and j in np.arange(0,16):
            west_array.append(1)
        else: 
            west_array.append(0)
    
    #Particles that travel thought the Caribbean Sea
    for i, j in XY: 
        if i in np.arange(-80,-64) and j in np.arange(10,21):
            csea_array.append.(1)
        else:
            csea_array.append(0)
    
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
    
    if lon[0] in np.arange(-45, -39) and lat[0] in np.arange(27, 31):
        sargasso_ne.append(1)
    else:
        sargasso_ne.append(0)
    
    if lon[0] in np.arange(-45, -39) and lat[0] in np.arange(25, 27):
        sargasso_se.append(1)
    else:
        sargasso_se.append(0)
        
    if lon[0] in np.arange(-50, -45) and lat[0] in np.arange(25, 27):
        sargasso_sw.append(1)
    else:
        sargasso_sw.append(0)
        
    if lon[0] in np.append(-50, -45) and lat[0] in np.arange(27, 31):
        sargasso_nw.append(1)
    else:
        sargasso_nw.append(0)

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
    

    
