import math
import numpy as np


####Inputs#####
#width [km]
#altitude [km]
#latitude [rad]

def DistanceLatitude(width,altitude,latitude):
    Re =6378;
    #Number of orbits
    p = round(np.pi * Re / width)
    #Distance in km
    d = 2 * (Re + altitude) * np.cos(latitude) * np.sin(np.pi / (2 * p))
    return d, p
