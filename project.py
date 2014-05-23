#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.PROJECT
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import cos, pi, recarray, sin, sqrt


def project( mgei, incl ):
    
    """
    Projects an MGE given an inclination value.
    
    INPUTS
      imge : intrinsic MGE
      incl : inclination [radians]
    """
    
    pmge = recarray.copy( imge )
    
    pmge.q = sqrt( imge.q**2 * sin( incl )**2 + cos( incl )**2 )
    pmge.i = imge.i * sqrt( 2. * pi ) * imge.s * imge.q / pmge.q
    
    return pmge
