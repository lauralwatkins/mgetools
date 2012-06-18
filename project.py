#!/usr/bin/env python
# -----------------------------------------------------------------------------
# PROJECT
#   
#   Projects an MGE given an inclination value.
#   
#   INPUTS
#     imge : intrinsic MGE
#     incl : inclination [radians]
#   
#   HISTORY
#     v1.0 : Laura L Watkins [lauralwatkins@gmail.com] - MPIA, 2012/03/14
# -----------------------------------------------------------------------------

from numpy import cos, pi, recarray, sin, sqrt


def project( mgei, incl ):
    
    pmge = recarray.copy( imge )
    
    pmge.q = sqrt( imge.q**2 * sin( incl )**2 + cos( incl )**2 )
    pmge.i = imge.i * sqrt( 2. * pi ) * imge.s * imge.q / pmge.q
    
    return pmge
