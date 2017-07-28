#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.PLOT1DMAJ
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

from numpy import *
import matplotlib.pyplot as plt
from . import surf
import colours, toolbox


def plot1dmaj(mge_in, ml=1., logscale=True, cmap=None):
    
    """
    Plots 1d major-axis surface density profiles for a given mge.
    
    INPUTS
      mge_in : projected MGE
    
    OPTIONS
      ml       : adjust central surface brightness values by mass-to-light ratio
      logscale : make x-axis logatrithmic
      cmap     : colormap to use
    """
    
    # adjust by mass-to-light ratio
    mge = mge_in.copy()
    mge["i"] *= ml
    
    # plotting grid
    rlim = toolbox.lims(mge["s"], f=[0.4,0.25], log=True)
    rr = logspace(log10(rlim[0]), log10(rlim[1]), 101)
    
    # surface brightness
    sx = surf(mge, rr, 0)
    sxx = array([ surf(mge[i:i+1], rr, 0) for i in range(size(mge)) ])
    
    # y axis limits
    ss = array([sxx[:,0].min()] + sx.tolist())
    
    # set up plotting
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='8')
    plt.rc('ytick', labelsize='8')
    plt.rc('axes', labelsize='10')
    if not cmap: cmap = plt.rcParams["image.cmap"]
    rgb = colours.cmap2rgb(cmap)
    cc = linspace(255, 0, size(mge))
    
    
    yl = r"$I \; [\rm L_{\odot} pc^{-2}]$"
    
    fig = plt.figure(figsize=(4,3))
    
    # x-axis plot
    ax = fig.add_axes([0.14, 0.12, 0.84, 0.87])
    if logscale: plt.loglog()
    else: plt.semilogy()
    
    ax.plot(rr, sx, "k", lw=3, alpha=0.8)
    for i in range(size(mge)):
        ax.plot(rr, sxx[i], lw=3, alpha=0.8, c=rgb(cc[i]))
    
    ax.set_xlim(rlim)
    ax.set_ylim(toolbox.lims(sx, f=[0.2,0.1], log=True))
    
    ax.set_xlabel(r"$x' [\rm arcsec]$")
    ax.set_ylabel(yl)
    
    plt.show()
    
    return 0
