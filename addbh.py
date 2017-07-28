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
      mge : projected MGE, must be given as an astropy Table or QTable
      mbh : black hole mass [Msun]
      rbh : black hole scale radius [pc]
    """
    
    if mbh>0. and rbh>0.:
        
        try:
            (mbh/rbh**2).to(mge["i"].unit)
        except:
            print "MGE.ADDBH: cannot convert mbh/rbh**2 units to MGE density units."
            return np.nan
        
        try:
            rbh.to(mge["s"].unit)
        except:
            print "MGE.ADDBH: cannot convert rbh units to MGE width units."
            return np.nan
        
        bh = mge[:1].copy()
        bh["n"] = 0
        bh["i"] = (mbh/2./np.pi/rbh**2).to(mge["i"].unit)
        bh["s"] = (rbh).to(mge["s"].unit)
        bh["q"] = 1.
        
        mgebh = table.join(bh, mge, join_type="outer")
        mgebh["n"] += 1
    
    else: mgebh = mge
    
    return mgebh
