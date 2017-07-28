#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.INCL
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np
from astropy import units as u


def incl(p, q):
    
    """
    Program calculates implied inclination angle (in radians) from projected
    and intrinsic axis ratios.
    
    INPUTS
      p : projected axis ratios
      q : intrinsic axis ratios
    """
    
    if np.all(q==1.): i = np.pi/2.
    else:
        w = q!=1.
        ii = np.arccos(np.sqrt((p[w]**2-q[w]**2)/(1.-q[w]**2))).value
        i = ii.mean()
    
    return i*u.rad
