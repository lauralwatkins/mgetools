#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.QPROJ
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import cos, sin, sqrt


def qproj( q, i ):
    
    """
    Program calculates projected axis ratios from the intrinsic axis ratios
    and the inclination angle.
    
    INPUTS
      q : intrinsic acis ratios
      i : inclination angle [radians]
    """
    
    p = sqrt( q**2 * sin(i)**2 + cos(i)**2 )
    
    return p
