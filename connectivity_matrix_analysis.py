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


    

    
