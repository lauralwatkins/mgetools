#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.ADDBH
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np
from astropy import table


def addbh(mge, mbh, rbh):
    
    """
    Adds a black hole component to a projected MGE.
    
    INPUTS
      mge : projected MGE [area in Msun/pc^2, sigma in pc]
      mbh : black hole mass [Msun]
      rbh : black hole scale radius [pc]
    """
    
    if mbh>0. and rbh>0.:
        
        bh = mge[:1].copy()
        mge["n"] += 1
        
        bh["i"] = mbh/2./np.pi/rbh**2
        bh["s"] = rbh
        bh["q"] = 1.
        
        mgebh = table.vstack([bh, mge])
    
    else: mgebh = mge
    
    return mgebh
