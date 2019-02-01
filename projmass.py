#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.PROJMASS
# Glenn van de Ven [glenn@mpia.de]
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np
from astropy import units as u
from scipy.integrate import quad


def intg_projmass(phi, R, pmge):
    
    pjph = (1 + (1/pmge["q"]**2 - 1)*np.sin(phi)**2) / pmge["s"]**2
    res = np.sum(pmge["i"]*(1-np.exp(-0.5*R**2*pjph))/pjph).value
    
    return res


def projmass(R, pmge, ellrad=False):
    
    """
    Calculates mass enclosed within projected radius for a projected MGE.
    
    INPUTS
      R    : projected radius
      pmge : projected mge
    
    OPTIONS
      ellrad : calculate within elliptic radius (only for constant flattening)
    """
    
    res = np.zeros(len(R))*pmge["i"].unit*pmge["s"].unit**2
    
    if ellrad:
        # within elliptic radius for *constant* flattening 
        if pmge["q"].std()!=0: print("MGE.PROJMASS WARNING: you selected " \
            + "elliptical radius but your flattening is not constant.")
        for i in range(len(R)):
            intg = 1 - np.exp(-0.5*(R[i]/pmge["s"])**2)
            res[i] = 2*np.pi*np.sum(pmge["s"]**2*pmge["q"]*pmge["i"]*intg)
    
    else:
        # within circular radius
        for i in range(len(R)):
            res[i] = 4*quad(lambda x: intg_projmass(x, R[i], pmge),
                0, np.pi/2)[0]*pmge["i"].unit*pmge["s"].unit**2
    
    return res
