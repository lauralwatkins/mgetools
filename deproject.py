#!/usr/bin/env python

import numpy as np
from astropy import units as u


def Deproject(pmge, inclination=None, distance=None):
    
    """
    Deprojects an MGE.
    
    If flattened, an inclination angle is also required, defined such that 0
    deg is face-on is 90 deg is edge-on.
    
    If the projected widths are given in angular units, a distance is required
    to convert the resulting volume density and widths to physical units.
    
    INPUTS
      pmge : projected MGE, must be given as an astropy QTable
    
    OPTIONAL KEYWORDS
      inclination : inclination [requires units, default None]
      distance : distance to object [requires units, default None]
    """
    
    # initialise intrinsic MGE by copying projected MGE
    imge = pmge.copy()
    
    # base units of surface density and their powers
    bases = np.array(pmge["i"].unit.bases)
    powers = np.array(pmge["i"].unit.powers)
    
    # length unit for area
    length_unit = bases[powers==-2][0]

    # check to see if projected MGE widths are angles
    if pmge["s"].unit.physical_type is "angle":
        
        # need distance to convert to physical units, so fail if not given
        if distance is None:
            print("MGE.DEPROJECT: Distance required to convert widths from "\
                +"angular units to physical units.")
            return
        
        else:
            # convert to length units used in surface density
            imge["s"] = (pmge["s"]*distance/u.rad).to(length_unit)
    
    # adjustment to turn surface density into volume density
    imge["i"] /= imge["s"]*np.sqrt(2*np.pi)
    
    # check to see if flattening is given and the MGE is flattened
    if "q" in pmge.colnames and np.any(pmge["q"]!=1):
        
        # fail if no inclination is given
        if inclination is None:
            print("MGE.DEPROJECT: Your MGE is flattened. Please provide an"\
                +" inclination.")
            return
        
        # fail if inclination is too low (as this gives negative flattenings)
        imge["q"] = pmge["q"]**2 - np.cos(inclination)**2
        if np.any(imge["q"] <= 0):
            print("MGE.DEPROJECT: Inclination too low q < 0.")
            return
        
        # fail if any components are extremely flattened
        imge["q"] = np.sqrt(imge["q"]) / np.sin(inclination)
        if np.any(imge["q"] < 0.05):
            print("MGE.DEPROJECT: q < 0.05 components.")
            return
        
        # adjust density for flattening
        imge["i"] *= pmge["q"]/imge["q"]
    
    return imge
