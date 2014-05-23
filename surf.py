#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.SURF
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import exp


def surf( pmge, x, y ):
    
    """
    Calculates the surface density of an MGE at given (x',y').
    
    INPUTS
      pmge : projected MGE
      x    : projected x'
      y    : projected y'
    """
    
    surf = pmge.i * exp( -0.5 / pmge.s**2 * ( x**2 + y**2 / pmge.q**2 ) )
    surf = surf.sum()
    
    return surf
