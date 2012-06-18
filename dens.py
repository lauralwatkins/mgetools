#!/usr/bin/env python
# -----------------------------------------------------------------------------
# DENS
#   
#   Calculates the volume density of an MGE at given (R,z).
#   
#   INPUTS
#     imge : intrinsic MGE
#     r    : intrinsic R 
#     z    : intrinsic z
#   
#   HISTORY
#     v1.0 : Laura L Watkins [lauralwatkins@gmail.com] - MPIA, 2012/03/14
# -----------------------------------------------------------------------------

def dens( imge, r, z ):
    
    dens = imge.i * np.exp( -0.5 / imge.s**2 * ( r**2 + z**2 / imge.q**2 ) )
    dens = dens.sum()
    
    return dens
