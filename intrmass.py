#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.INTRMASS
# Glenn van de Ven [glenn@mpia.de]
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np
from astropy import units as u
from scipy import special
from scipy.integrate import quad


def intg_intrmass(th, r, imge):
    
    scq = np.sqrt(np.sin(th)**2 + np.cos(th)**2 / imge["q"]**2)
    x = r*scq/imge["s"]/np.sqrt(2.)
    
    intg = np.sqrt(np.pi/2.)*special.erf(x.value) \
        - np.sqrt(2.)*x.value*np.exp(-x.value**2)
    res = np.sum(imge["i"]*imge["s"]**3/scq**3*intg*np.sin(th)).value
    
    return res


def intrmass(r, imge, ellrad=False):
    
    """
    Calculates mass enclosed within intrinsic radius for an intrinsic MGE.
    
    INPUTS
      r    : intrinsic radius
      imge : intrinsic mge
    
    OPTIONS
      ellrad : calculate within elliptic radius (only for constant flattening)
    """
    
    res = np.zeros(len(r))*imge["i"].unit*imge["s"].unit**3
    
    if ellrad:
        # within ellipsoidal radius for *constant* flattening
        if imge["q"].std()!=0: print "MGE.INTRMASS WARNING: you selected " \
            + "elliptical radius but your flattening is not constant."
        for i in range(len(r)):
            x  = r[i]/np.sqrt(2.)/imge["s"]
            intg = np.sqrt(np.pi/2.)*special.erf(x.value) \
                - np.sqrt(2.)*x*np.exp(-x**2)
            res[i] = 4.*np.pi*np.sum(imge["s"]**3*imge["q"]*imge["i"]*intg)
    
    else:
        # within spherical radius
        for i in range(len(r)):
            res[i] = 4*np.pi*quad(lambda x: intg_intrmass(x, r[i], imge), \
                0., np.pi/2.)[0]*imge["i"].unit*imge["s"].unit**3
    
    return res
