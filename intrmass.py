#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.INTRMASS
# Glenn van de Ven [glenn@mpia.de]
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np
from deproject import deproject
from scipy.special import erf
from scipy.integrate import quad


def intg_intrmass(th, r, imge):
    
    scq = np.sqrt(np.sin(th)**2 + np.cos(th)**2 / imge["q"]**2)
    x = r*scq/imge["s"]/np.sqrt(2.)
    
    intg = np.sqrt(np.pi/2.)*erf(x) - np.sqrt(2.)*x*np.exp(-x**2)
    res = (imge["i"]*imge["s"]**3/scq**3*intg*np.sin(th)).sum()
    
    return res


def intrmass(r, pmge, incl=np.pi/2., ellrad=False):
    
    """
    Program calculates enclosed intrinsic mass for an MGE.
    
    INPUTS
      r    : intrinsic radius [*]
      pmge : projected mge [*]
    
    OPTIONS
      incl   : inclination angle [radians]
      ellrad : calculate within elliptic radius (only for constant flattening)
    
    NOTES
      [*] pmge.i will be in units of mass/distance^2, pmge.s will be in units
      of distance and r will be in units of distance.  You can use any distance
      units you want as long as they are ALL the same.  And the units of mass
      in pmge.i will be the units in which the mass profile is returned.
    """
    
    
    # deproject mge to get intrinsic parameters
    imge = deproject(pmge, incl)
    
    res = np.zeros(np.size(r))
    
    if ellrad:
        # within ellipsoidal radius for *constant* flattening
        for i in range(np.size(r)):
            x  = r[i]/np.sqrt(2.)/imge["s"]
            intg = np.sqrt(np.pi/2.)*erf(x) - np.sqrt(2.)*x*np.exp(-x**2)
            res[i] = 4.*np.pi*(imge["s"]**3*imge["q"]*imge["i"]*intg).sum()
    
    else:
        # within spherical radius
        for i in range(np.size(r)):
            intg = quad(lambda x: intg_intrmass(x, r[i], imge),0.,np.pi/2.)[0]
            res[i] = 4.*np.pi*intg
    
    return res
