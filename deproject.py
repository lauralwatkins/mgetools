#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.DEPROJECT
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np
from astropy import table
import sys


def deproject(pmge, incl):
    
    """
    Deprojects an MGE given an inclination value.
    
    INPUTS
      pmge : projected MGE, must be given as an astropy Table or QTable
      incl : inclination [must be in radians unless unit explictly given]
    """
    
    imge = table.QTable()
    imge["n"] = pmge["n"]
    imge["s"] = pmge["s"]
    
    imge["q"] = pmge["q"]**2 - np.cos(incl)**2
    if np.any(imge["q"] <= 0):
        print("MGE.DEPROJECT: Inclination too low q < 0")
        sys.exit(1)
    
    imge["q"] = np.sqrt(imge["q"]) / np.sin(incl)
    if np.any(imge["q"] < 0.05):
        print("MGE.DEPROJECT: q < 0.05 components")
        sys.exit(1)
    
    imge["i"] = pmge["i"]*pmge["q"]/imge["q"]/pmge["s"]/np.sqrt(2.*np.pi)
    imge = imge["n", "i", "s", "q"]
    
    return imge
