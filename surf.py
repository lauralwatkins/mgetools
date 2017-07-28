#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.SURF
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np


def surf(pmge, x, y):
    
    """
    Calculates the surface density of an MGE at given (x',y').
    
    INPUTS
      pmge : projected MGE, must be given as an astropy Table or QTable
      x    : projected x', should have the same units as MGE widths
      y    : projected y', should have the same units as MGE widths
    """
    
    try:
        x.to(pmge["s"].unit)
        y.to(pmge["s"].unit)
    except:
        print("MGE.SURF: cannot convert x and y units to MGE width units.")
        return np.nan
    
    cpts = np.array([ cpt["i"]*np.exp(-0.5/cpt["s"]**2 \
        *(x.to(pmge["s"].unit)**2+(y.to(pmge["s"].unit)/cpt["q"])**2)) \
        for cpt in pmge ])*pmge["i"].unit
    surf = np.sum(cpts, axis=0)
    
    return surf
