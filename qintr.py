#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.QINTR
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import cos, sin, sqrt


def qintr( p, i ):
    
    """
    Program calculates intrinsic axis ratios from the projected axis ratios
    and the inclination angle.
    
    INPUTS
      p : projected axis ratios
      i : inclination angle [radians]
    """
    
    q = sqrt( p**2 - cos(i)**2 ) / sin(i)
    
    return q
