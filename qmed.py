#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.QMED
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import median, size, where


def qmed( mge, lim=0. ):
    
    """
    Calculates the median axial ratio for a given MGE.
    
    INPUTS
      mge : MGE
      lim : if non-zero, consider only components within limit (default: 0)
    """
    
    wh = where( mge.s < lim )
    
    if size( wh ) < 3:
        qmed = median( mge.q )
    else:
        qmed = median( mge[wh].q )
    
    return qmed
