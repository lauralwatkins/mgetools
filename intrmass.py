#!/usr/bin/env python

import numpy as np
from astropy import units as u
from scipy import special
from scipy.integrate import quad


def IntegrandCumulative3D(theta, r, imge):
    
    scq = np.sqrt(np.sin(theta)**2 + np.cos(theta)**2 / imge["q"]**2)
    x = r*scq/imge["s"]/np.sqrt(2)
    
    intg = np.sqrt(np.pi/2)*special.erf(x.value) \
        - np.sqrt(2)*x.value*np.exp(-x.value**2)
    res = np.sum(imge["i"]*imge["s"]**3/scq**3*intg*np.sin(theta)).value
    
    return res


def Cumulative3D(r, imge, ellrad=False):
    
    """
    Calculates cumulative profile from a 3-dimensional (deprojected) MGE.
    
    INPUTS
      r    : intrinsic radius
      imge : intrinsic mge
    
    OPTIONAL KEYWORDS
      ellrad : calculate within elliptic radius (only for constant flattening)
    """
    
    res = np.zeros(len(r))*imge["i"].unit*imge["s"].unit**3
    
    # within ellipsoidal radius for *constant* flattening or no flattening
    if ellrad or not "q" in imge.colnames or np.all(imge["q"]==1):
        
        if "q" in imge.colnames and imge["q"].ptp()>0:
            print("MGE.Cumulative3D: you selected elliptical radius but " \
                + "your flattening is not constant.")
            return
        
        for i in range(len(r)):
            x  = r[i]/np.sqrt(2)/imge["s"]
            intg = np.sqrt(np.pi/2)*special.erf(x.value) \
                - np.sqrt(2)*x*np.exp(-x**2)
            res[i] = 4*np.pi*np.sum(imge["s"]**3*imge["q"]*imge["i"]*intg)
    
    # within spherical radius
    else:
        for i in range(len(r)):
            res[i] = 4*np.pi*quad(lambda x: IntegrandCumulative3D(x, r[i],
                imge), 0, np.pi/2)[0]*imge["i"].unit*imge["s"].unit**3
    
    return res
