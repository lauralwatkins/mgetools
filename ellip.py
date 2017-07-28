#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.ELLIP
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import *
from matplotlib.pyplot import *
from . import surf
import toolbox
from scipy.interpolate import spline


def ellip(mge, cmap=None, logscale=True):
    
    """
    Plots an ellipticity profile for an input MGE.
    
    INPUTS
      mge  : projected MGE
    
    OPTIONS
      logscale : make x-axis logatrithmic
      cmap     : colormap to use
    """
    
    # radial range for minor axis profile (need to be wide for interpolation)
    rlim_min = toolbox.lims(mge["s"], f=[0.45,0.3], log=True)
    rmin = logspace(log10(rlim_min[1]), log10(rlim_min[0]), 101)
    
    # radial range for major axis profile
    rlim = toolbox.lims(mge["s"], f=[0.4,0.25], log=True)
    rr = logspace(log10(rlim[1]), log10(rlim[0]), 101)
    
    # major and minor axis surface brightness profile
    majsb = log10(surf(mge, rr, 0))
    minsb = log10(surf(mge, 0, rmin))
    
    # ellipticity profile
    ell = spline(minsb, rmin, majsb) / rr
    
    
    # set up plotting
    rc('text', usetex=True)
    rc('font', family='serif')
    rc('xtick', labelsize='8')
    rc('ytick', labelsize='8')
    rc('axes', labelsize='10')
    
    # set up figure
    fig = figure(figsize=(4,3))
    ax = fig.add_axes([0.12, 0.12, 0.86, 0.87])
    if logscale: semilogx()
    
    # ellipticity profile
    ax.plot(rr, ell, "k", lw=2, alpha=0.8)
    
    # mge flattenings
    ax.scatter(mge["s"], mge["q"], cmap=cmap, lw=0, s=50, c=range(mge.size)[::-1],
        zorder=10)
    
    # axis limits
    ax.set_xlim(rlim)
    ax.set_ylim(toolbox.lims(mge["q"], f=0.15))
    
    # axis labels
    ax.set_xlabel(r"$R$")
    ax.set_ylabel(r"$q'$")
    
    show()
