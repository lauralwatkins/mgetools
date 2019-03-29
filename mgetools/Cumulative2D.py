#!/usr/bin/env python

import numpy as np
from astropy import units as u
from scipy.integrate import quad


def IntegrandCumulative2D(phi, R, pmge):
    
    pjph = (1 + (1/pmge["q"]**2 - 1)*np.sin(phi)**2) / pmge["s"]**2
    res = np.sum(pmge["i"]*(1-np.exp(-0.5*R**2*pjph))/pjph).value
    
    return res


def Cumulative2D(R, pmge, ellrad=False, distance=None):
    
    """
    Calculates cumulative profile from a 2-dimensional (projected) MGE.
    
    If the projected widths are given in angular units a distance is required 
    to cancel with the physical units in the density. The code works fine 
    without a distance, but will give mixed units (eg Msun arcsec^2 pc^-2).
    
    INPUTS
      R    : projected radius
      pmge : projected mge
    
    OPTIONAL KEYWORDS
      ellrad : calculate within elliptic radius (only for constant flattening)
      distance : distance to object [requires units, default None]
    """
    
    res = np.zeros(len(R))*pmge["i"].unit*pmge["s"].unit**2
    
    # within ellipsoidal radius for *constant* flattening or no flattening
    if ellrad or not "q" in pmge.colnames or np.all(pmge["q"]==1):
        
        if "q" in pmge.colnames and pmge["q"].std()!=0:
            print("MGE.Cumulative2D: you selected elliptical radius but " \
                + "your flattening is not constant.")
            return
        
        for i in range(len(R)):
            intg = 1 - np.exp(-0.5*(R[i]/pmge["s"])**2)
            res[i] = 2*np.pi*np.sum(pmge["s"]**2*pmge["q"]*pmge["i"]*intg)
    
    # within circular radius
    else:
        for i in range(len(R)):
            res[i] = 4*quad(lambda x: IntegrandCumulative2D(x, R[i], pmge),
                0, np.pi/2)[0]*pmge["i"].unit*pmge["s"].unit**2
    
    if distance is not None and pmge["s"].unit.physical_type is "angle":
        
        # base units of surface density and their powers
        bases = np.array(pmge["i"].unit.bases)
        powers = np.array(pmge["i"].unit.powers)
        
        # numerator of density
        area_unit = bases[bases==bases[powers==-2]][0]
        value_unit = pmge["i"].unit * area_unit**2
        
        # cancel angular and physical units
        res = (res*distance**2/u.rad**2).to(value_unit)
    
    return res
