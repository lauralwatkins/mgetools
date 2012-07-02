#!/usr/bin/env python
# -----------------------------------------------------------------------------
# INCL
#   
#   Program calculates implied inclination angle (in radians) from projected
#   and intrinsic axis ratios.
#   
#   INPUTS
#     p : projected axis ratios
#     q : intrinsic acis ratios
#   
#   HISTORY
#     v1.0 : Laura L Watkins [lauralwatkins@gmail.com] - MPIA, 2012/06/19
# -----------------------------------------------------------------------------

from numpy import arccos, rad2deg, sqrt


def incl( p, q, deg=False ):
    
    i = arccos( sqrt( ( p**2 - q**2 ) / ( 1. - q**2 ) ) )
    
    return i