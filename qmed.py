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
      mge : MGE
      lim : if non-zero, consider only components within limit (default: 0)
    """
    
    wh = np.where(mge["s"]<lim)
    
    if np.size(wh)<3: qmed = np.median(mge["q"])
    else: qmed = np.median(mge[wh]["q"])
    
    return qmed
