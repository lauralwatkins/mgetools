#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.INCL
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import arccos, pi, rad2deg, sqrt


def incl( p, q ):
    
    """
    Program calculates implied inclination angle (in radians) from projected
    and intrinsic axis ratios.
    
    INPUTS
      p : projected axis ratios
      q : intrinsic axis ratios
    """
    
    if q == 1.: i = pi / 2.
    else: i = arccos( sqrt( ( p**2 - q**2 ) / ( 1. - q**2 ) ) )
    
    return i
