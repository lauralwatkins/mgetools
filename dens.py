#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.DENS
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np


def dens(imge, r, z):
    
    """
    Calculates the volume density of an MGE at given (R,z).
    
    INPUTS
      imge : intrinsic MGE, must be given as an astropy Table or QTable
      r    : intrinsic R, should have the same units as MGE widths
      z    : intrinsic z, should have the same units as MGE widths
    """
    
    try:
        r.to(imge["s"].unit)
        z.to(imge["s"].unit)
    except:
        print("MGE.SURF: cannot convert r and z units to MGE width units.")
        return np.nan
    
    cpts = np.array([ cpt["i"]*np.exp(-0.5/cpt["s"]**2 \
        *(r.to(imge["s"].unit)**2+(z.to(imge["s"].unit)/cpt["q"])**2)) \
        for cpt in imge ])*imge["i"].unit
    dens = np.sum(cpts, axis=0)
    
    return dens
