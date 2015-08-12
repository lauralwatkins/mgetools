#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.INCL
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np


def incl(p, q):
    
    """
    Program calculates implied inclination angle (in radians) from projected
    and intrinsic axis ratios.
    
    INPUTS
      p : projected axis ratios
      q : intrinsic axis ratios
    """
    
    if q==1.: i = np.pi/2.
    else: i = np.arccos(np.sqrt((p**2-q**2)/(1.-q**2)))
    
    return i
