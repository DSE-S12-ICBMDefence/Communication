import math
import numpy as np

def DistanceLatitude(width,altitude,latitude):
    Re =6378;
    #Number of orbits
    p = round(m.pi * Re / (2 * width))
    d = 2 * (Re + altitude) * np.cos(latitude) * np.sin(np.pi / (2 * p))
    return d, p