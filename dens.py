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
      imge : intrinsic MGE
      r    : intrinsic R 
      z    : intrinsic z
    """
    
    cpts = np.array([ cpt["i"]*np.exp(-0.5/cpt["s"]**2*(r**2+(z/cpt["q"])**2))\
        for cpt in imge ])
    dens = np.sum(cpts, axis=0)
    
    return dens
