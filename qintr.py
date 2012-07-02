#!/usr/bin/env python
# -----------------------------------------------------------------------------
# QINTR
#   
#   Program calculates intrinsic axis ratios from the projected axis ratios
#   and the inclination angle.
#   
#   INPUTS
#     p : projected acis ratios
#     i : inclination angle [radians]
#   
#   HISTORY
#     v1.0 : Laura L Watkins [lauralwatkins@gmail.com] - MPIA, 2012/06/19
# -----------------------------------------------------------------------------

from numpy import cos, sin, sqrt


def qintr( p, i ):
    
    q = sqrt( p**2 - cos(i)**2 ) / sin(i)
    
    return q
