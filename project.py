#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.PROJECT
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np
from astropy import table


def project(imge, incl):
    
    """
    Projects an MGE given an inclination value.
    
    INPUTS
      imge : intrinsic MGE, must be given as an astropy Table or QTable
      incl : inclination [must be in radians unless unit explictly given]
    """
    
    pmge = table.QTable()
    pmge["n"] = imge["n"]
    pmge["s"] = imge["s"]
    pmge["q"] = np.sqrt(imge["q"]**2 * np.sin(incl)**2 + np.cos(incl)**2)
    pmge["i"] = imge["i"]*np.sqrt(2.*np.pi)*imge["s"]*imge["q"]/pmge["q"]
    pmge = pmge["n", "i", "s", "q"]
    
    return pmge
