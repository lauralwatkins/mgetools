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
      pmge : projected MGE
      x    : projected x'
      y    : projected y'
    """
    
    cpts = np.array([ cpt["i"]*np.exp(-0.5/cpt["s"]**2*(x**2+(y/cpt["q"])**2))\
        for cpt in pmge ])
    surf = np.sum(cpts, axis=0)
    
    return surf
