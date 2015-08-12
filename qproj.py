#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.QPROJ
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np


def qproj(q, i):
    
    """
    Program calculates projected axis ratios from the intrinsic axis ratios
    and the inclination angle.
    
    INPUTS
      q : intrinsic acis ratios
      i : inclination angle [radians]
    """
    
    p = np.sqrt(q**2*np.sin(i)**2+np.cos(i)**2)
    
    return p
