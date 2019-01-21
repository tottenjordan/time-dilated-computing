# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 17:18:56 2019

@author: jtotten
"""
import math

# satellite aging for a non-rotating satellite and earth

r_sat_meters = 26.6e6
r_earth_meters = 6.371e6

# earths mass in terms of meters
M_earth_meters = 0.004435

#rot = ((-r_sat_meters+2*M_earth_meters)*((r_earth_meters)/(r_sat_meters*(-r_earth_meters+2*M_earth_meters))))^0.5

x = -r_sat_meters + 2*M_earth_meters
y = r_earth_meters
z = r_sat_meters*(-r_earth_meters + 2*M_earth_meters)
t = y/z
r = x*t

# the ratio of satellite time to earth time
rot = math.sqrt(r)
rot

# seconds in an earth day
earth_secs = 8.64e4
sat_secs = rot*earth_secs
satellite_age = sat_secs - earth_secs
satellite_age

# the satellite ages 4.574e-5 more seconds a day than earth