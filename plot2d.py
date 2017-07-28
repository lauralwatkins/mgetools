#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.PLOT2D
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import numpy as np, matplotlib.pyplot as plt
from . import surf


def plot2d(mge_in, ml=1., cmap=None):
    
    """
    Plots a 2d surface density map for a given mge.
    
    INPUTS
      mge_in : projected MGE
    
    OPTIONS
      ml   : adjust central surface brightness values by mass-to-light ratio
      cmap : colormap to use
    """
    
    # adjust by mass-to-light ratio
    mge = mge_in.copy()
    mge["i"] *= ml
    
    # plotting grid
    lim = mge["s"].max()*2
    x = np.linspace(-lim, lim, 51)
    y = np.linspace(-lim, lim, 61)
    xx, yy = np.meshgrid(x, y)
    
    # surface brightness
    ss = surf(mge, xx, yy).reshape(y.size, x.size)
    
    # set up plotting
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.rc('xtick', labelsize='8')
    plt.rc('ytick', labelsize='8')
    plt.rc('axes', labelsize='10')
    
    
    fig = plt.figure(figsize=(4,3))
    
    # mge plot
    ax = fig.add_axes([0.15, 0.12, 0.65, 0.85])
    cols = ax.imshow(np.log10(ss.value), origin="lower", cmap=cmap, \
        extent=(xx.min().value, xx.max().value, yy.min().value, yy.max().value))
    ax.set_xlabel(r"$x' [\rm arcsec]$")
    ax.set_ylabel(r"$y' [\rm arcsec]$")
    
    # colour bar
    cax = fig.add_axes([0.81, 0.12, 0.04, 0.85])
    fig.colorbar(cols, cax=cax)
    cax.set_ylabel(r"$\log \; [I \; (\rm L_{\odot} pc^{-2})]$")
    
    plt.show()
