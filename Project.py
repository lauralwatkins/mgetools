#!/usr/bin/env python

import numpy as np
from astropy import units as u


def Project(imge, inclination=None, distance=None, angular_unit=None):
    
    """
    Projects an MGE given an inclination value.
    
    If flattened, an inclination angle is also required, defined such that 0
    deg is face-on is 90 deg is edge-on.
    
    INPUTS
      imge : intrinsic MGE, must be given as an astropy QTable
    
    OPTIONAL KEYWORDS
      inclination : inclination [requires units, default None]
      distance : distance to object, only used if angular_unit also given
         [requires units, default None]
      angular_unit : angular units for projected Gaussian widths, if desired,
        only used if distance also given [default None]
    """
    
    # initialise projected MGE by copying intrinsic MGE
    pmge = imge.copy()
    
    # convert to turn volume density into surface density
    pmge["i"] *= np.sqrt(2*np.pi)*pmge["s"]
    
    # check to see if flattening is given and the MGE is flattened
    if "q" in imge.colnames and np.any(imge["q"]!=1):
        
        # fail if no inclination is given
        if inclination is None:
            print("MGE.PROJECT: Your MGE is flattened. Please provide an"\
                +" inclination.")
            return
        
        # convert flattening
        pmge["q"] = np.sqrt((imge["q"]*np.sin(inclination))**2 \
            + np.cos(inclination)**2)
        
        # adjust density for flattening
        pmge["i"] *= imge["q"]/pmge["q"]
    
    if distance is not None and angular_unit is not None:
        
        # convert units of widths from physical to angular
        pmge["s"] = (pmge["s"]*u.rad/distance).to(angular_unit)
    
    # fail if only one of distance of angular_unit are given
    elif (distance is not None and angular_unit is None) \
        or (angular_unit is not None and distance is None):
        print("MGE.PROJECT: Both distance and angular_unit are required if"\
            +" you wish to convert the projected Gaussian widths from"\
            +" physical to angular units.")
        return
    
    return pmge
