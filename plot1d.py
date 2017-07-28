#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.PLOT1D
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np, matplotlib.pyplot as plt
from . import surf
import colours, toolbox


def plot1d(mge_in, ml=1., logscale=True, cmap=None):
    
    """
    Plots the 1d surface density profile for a given mge.
    
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
    rr = np.logspace(np.log10(rlim[0].value), np.log10(rlim[1].value),
        101)*rlim.unit
    
    # surface brightness
    sx = surf(mge, rr, 0*rr.unit)
    sxx = np.array([surf(mge[i:i+1], rr, 0*rr.unit) for i in range(len(mge))])*sx.unit
    sy = surf(mge, 0*rr.unit, rr)
    syy = np.array([surf(mge[i:i+1], 0*rr.unit, rr) for i in range(len(mge))])*sy.unit
    
    # y axis limits
    ss = np.array([sxx[:,0].min().value]+[syy[:,0].min().value]\
        +sx.value.tolist()+sy.value.tolist())
    
    # set up plotting
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='8')
    plt.rc('ytick', labelsize='8')
    plt.rc('axes', labelsize='10')
    if not cmap: cmap = plt.rcParams["image.cmap"]
    rgb = colours.cmap2rgb(cmap)
    cc = np.linspace(255, 0, len(mge))
    
    
    yl = r"$I \; [\rm L_{\odot} pc^{-2}]$"
    
    fig = plt.figure(figsize=(7.5, 3))
    
    
    # x-axis plot
    
    ax = fig.add_axes([0.07, 0.12, 0.41, 0.85])
    if logscale: plt.loglog()
    else: plt.semilogy()
    
    ax.plot(rr, sx, "k", lw=3, alpha=0.8)
    for i in range(len(mge)):
        ax.plot(rr, sxx[i], "k", lw=3, alpha=0.8, c=rgb(cc[i]))
    
    ax.set_xlim(rlim.value)
    ax.set_ylim(toolbox.lims(ss, f=[0.2,0.1], log=True))
    
    ax.set_xlabel(r"$x' [\rm arcsec]$")
    ax.set_ylabel(yl)
    
    
    # y-axis plot
    
    ax = fig.add_axes([0.58, 0.12, 0.41, 0.85])
    if logscale: plt.loglog()
    else: plt.semilogy()
    
    ax.plot(rr, sy, "k", lw=3, alpha=0.8)
    for i in range(len(mge)):
        ax.plot(rr, syy[i], "k", lw=3, alpha=0.8, c=rgb(cc[i]))
    
    ax.set_xlim(rlim.value)
    ax.set_ylim(toolbox.lims(ss, f=[0.2,0.1], log=True))
    
    ax.set_xlabel(r"$y' [\rm arcsec]$")
    ax.set_ylabel(yl)
    
    
    plt.show()
