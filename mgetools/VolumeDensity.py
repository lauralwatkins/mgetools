#!/usr/bin/env python

import numpy as np
from scipy import stats
from astropy import units as u


def VolumeDensity(imge, R, z):
    
    """
    Calculates the volume density of an MGE at given position (R,z).
    
    INPUTS
      imge : intrinsic MGE, must be given as an astropy Table or QTable
      R    : intrinsic R, should have the same units as MGE widths
      z    : intrinsic z, should have the same units as MGE widths
    """
    
    try:
        R.to(imge["s"].unit)
        z.to(imge["s"].unit)
    except:
        print("MGE.VolumeDensity: cannot convert R and z units to MGE "\
            +"width units.")
        return np.nan
    
    # copy R and z arrays Ncpt times
    RR = u.Quantity([R.T]*len(imge)).T
    zz = u.Quantity([z.T]*len(imge)).T
    
    # combine R and z arrays with flattening, make sure unit matches mge widths
    Rzq = np.sqrt(RR**2 + zz**2/imge["q"]**2).to(imge["s"].unit)
    
    # calculate density profile
    height = np.sqrt(2*np.pi)*imge["s"]*imge["i"]
    density = np.sum(height*stats.norm.pdf(Rzq, 0, imge["s"])/imge["s"].unit,
         axis=-1)
    
    return density
