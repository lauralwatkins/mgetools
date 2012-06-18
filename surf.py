#!/usr/bin/env python
# -----------------------------------------------------------------------------
# SURF
#   
#   Calculates the surface density of an MGE at given (x',y').
#   
#   INPUTS
#     pmge : projected MGE
#     x    : projected x'
#     y    : projected y'
#   
#   HISTORY
#     v1.0 : Laura L Watkins [lauralwatkins@gmail.com] - MPIA, 2012/03/14
# -----------------------------------------------------------------------------

from numpy import exp


def surf( mge, x, y ):
    
    surf = pmge.i * exp( -0.5 / pmge.s**2 * ( x**2 + y**2 / pmge.q**2 ) )
    surf = surf.sum()
    
    return surf
