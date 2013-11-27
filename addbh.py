#!/usr/bin/env python
# -----------------------------------------------------------------------------
# ADDBH
#   
#   Adds a black hole component to an MGE.
#   
#   INPUTS
#     mge : MGE [area in M/pc^2, sigma in pc]
#     mbh : black hole mass [Msun]
#     rbh : black hole scale radius [pc]
#   
#   HISTORY
#     v1.0 : Laura L Watkins [lauralwatkins@gmail.com] - MPIA, 2013/05/09
# -----------------------------------------------------------------------------

from numpy import pi
from numpy.lib.recfunctions import stack_arrays


def addbh( mge, mbh, rbh ):
    
    if mbh > 0. and rbh > 0.:
        
        bh = mge[:1].copy()
        
        bh.i = mbh / 2. / pi / rbh**2
        bh.s = rbh
        bh.q = 1.
        bh.k = 0.
        
        mgebh = stack_arrays( ( bh, mge ), asrecarray=True )
    
    return mgebh
