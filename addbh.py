#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.ADDBH
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import pi
from numpy.lib.recfunctions import stack_arrays


def addbh( mge, mbh, rbh ):
    
    """
    Adds a black hole component to a projected MGE.
    
    INPUTS
      mge : projected MGE [area in Msun/pc^2, sigma in pc]
      mbh : black hole mass [Msun]
      rbh : black hole scale radius [pc]
    """
    
    if mbh > 0. and rbh > 0.:
        
        bh = mge[:1].copy()
        
        bh.i = mbh / 2. / pi / rbh**2
        bh.s = rbh
        bh.q = 1.
        
        mgebh = stack_arrays( ( bh, mge ), asrecarray=True )
    
    return mgebh
