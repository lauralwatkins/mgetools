#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.DENS
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import exp


def dens( imge, r, z ):
    
    """
    Calculates the volume density of an MGE at given (R,z).
    
    INPUTS
      imge : intrinsic MGE
      r    : intrinsic R 
      z    : intrinsic z
    """
    
    dens = imge.i * exp( -0.5 / imge.s**2 * ( r**2 + z**2 / imge.q**2 ) )
    dens = dens.sum()
    
    return dens
