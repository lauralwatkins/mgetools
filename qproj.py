#!/usr/bin/env python
# -----------------------------------------------------------------------------
# QPROJ
#   
#   Program calculates projected axis ratios from the intrinsic axis ratios
#   and the inclination angle.
#   
#   INPUTS
#     q : intrinsic acis ratios
#     i : inclination angle [radians]
#   
#   HISTORY
#     v1.0 : Laura L Watkins [lauralwatkins@gmail.com] - MPIA, 2012/06/19
# -----------------------------------------------------------------------------

from numpy import cos, sin, sqrt


def qproj( q, i ):
    
    p = sqrt( q**2 * sin(i)**2 + cos(i)**2 )
    
    return p
