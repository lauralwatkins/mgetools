#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.DEPROJECT
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import *
import sys


def deproject(pmge, incl):
    
    """
    Deprojects an MGE given an inclination value.
    
    INPUTS
      pmge : projected MGE
      incl : inclination [radians]
    """
    
    imge = pmge.copy()
    
    imge_q = pmge["q"]**2 - cos(incl)**2
    
    if any(imge_q <= 0):
        print 'Inclination too low q < 0'
        sys.exit(1)
    
    imge_q = sqrt(imge_q) / sin(incl)
    if any(imge_q < 0.05):
        print 'q < 0.05 components'
        sys.exit(1)
    
    imge["q"] = imge_q
    imge["i"] *= pmge["q"] / imge["q"] / pmge["s"] / sqrt(2.*pi)
    
    return imge
