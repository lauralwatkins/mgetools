#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.QMED
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np


def qmed(mge, lim=0):
    
    """
    Calculates the median axial ratio for a given MGE.
    
    INPUTS
      mge : MGE, as an astropy Table or QTable
      lim : if non-zero, consider only components within limit (default: 0)
            unit should be given if non-zero in 
    """
    
    if lim != 0:
        try: lim.to(mge["s"].unit)
        except:
            print("MGE.SURF: cannot convert lim units to MGE width units.")
            return np.nan
    
    wh = mge["s"]<lim
    
    if sum(wh)<3: qmed = np.median(mge["q"])
    else: qmed = np.median(mge[wh]["q"])
    
    return qmed
