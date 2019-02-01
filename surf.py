#!/usr/bin/env python

import numpy as np
from scipy import stats
from astropy import units as u


def SurfaceDensity(pmge, x, y):
    
    """
    Calculates the surface density of an MGE at given position (x',y').
    
    INPUTS
      pmge : projected MGE, must be given as an astropy QTable
      x    : projected x', should have the same units as MGE widths
      y    : projected y', should have the same units as MGE widths
    """
    
    try:
        x.to(pmge["s"].unit)
        y.to(pmge["s"].unit)
    except:
        print("MGE.SurfaceDensity: cannot convert x and y units to MGE "\
            +"width units.")
        return np.nan
    
    # copy x and y arrays Ncpt times
    xx = u.Quantity([x.T]*len(pmge)).T
    yy = u.Quantity([y.T]*len(pmge)).T
    
    # combine R and z arrays with flattening, make sure unit matches mge widths
    xyq = np.sqrt(xx**2 + yy**2/pmge["q"]**2).to(pmge["s"].unit)
    
    # calculate density profile
    height = np.sqrt(2*np.pi)*pmge["s"]*pmge["i"]
    density = np.sum(height*stats.norm.pdf(xyq, 0, pmge["s"])/pmge["s"].unit,
         axis=-1)
    
    return density
