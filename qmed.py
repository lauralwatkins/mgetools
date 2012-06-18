#!/usr/bin/env python
# -----------------------------------------------------------------------------
# QMED
#   
#   Calculates the median axial ratio for a given MGE.
#   
#   INPUTS
#     mge : MGE
#     lim : if non-zero, consider only components within limit (default: 0)
#   
#   HISTORY
#     v1.0 : Laura L Watkins [lauralwatkins@gmail.com] - MPIA, 2012/06/18
# -----------------------------------------------------------------------------

from numpy import median, size, where


def qmed( mge, lim=0. ):
    
    wh = where( mge.s < lim )
    
    if size( wh ) < 3:
        qmed = median( mge.q )
    else:
        qmed = median( mge[wh].q )
    
    return qmed
