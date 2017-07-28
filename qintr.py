#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.QINTR
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np


def qintr(p, i):
    
    """
    Program calculates intrinsic axis ratios from the projected axis ratios
    and the inclination angle.
    
    INPUTS
      p : projected axis ratios
      i : inclination angle [must be in radians unless unit explictly given]
    """
    
    q = np.sqrt(p**2-np.cos(i)**2)/np.sin(i)
    
    return q
