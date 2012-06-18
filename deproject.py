#!/usr/bin/env python
# -----------------------------------------------------------------------------
# DEPROJECT
#   
#   Deprojects an MGE given an inclination value.
#   
#   INPUTS
#     pmge : projected MGE
#     incl : inclination [radians]
#   
#   HISTORY
#     v1.0 : Laura L Watkins [lauralwatkins@gmail.com] - MPIA, 2012/03/14
# -----------------------------------------------------------------------------

from numpy import cos, pi, recarray, sin, size, sqrt, where
import sys


def deproject( pmge, incl ):
    
    imge = recarray.copy( pmge )
    
    imge_q = pmge.q**2 - cos( incl )**2
    
    if size( where( imge_q < 0 ) ) > 0:
        print 'Inclination too low q < 0'
        sys.exit(1)
    
    imge_q = sqrt( imge_q ) / sin( incl )
    if size( where( imge_q < 0.05 ) ) > 0:
        print 'q < 0.05 components'
        sys.exit(1)
    
    imge.q = imge_q
    imge.i = pmge.i * pmge.q / imge.q / pmge.s / sqrt( 2. * pi )
    
    return imge
