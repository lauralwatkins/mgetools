#!/usr/bin/env python
# -----------------------------------------------------------------------------
# PLOT1DMAJ
#   
#   Plots 1d major-axis surface density profiles for a given mge.
#   
#   INPUTS
#     mge_in : projected MGE
#   
#   OPTIONS
#     ml     : adjust central surface brightness values by mass-to-light ratio
#     save   : path to save location
#   
#   Laura L Watkins [lauralwatkins@gmail.com] - MPIA
# -----------------------------------------------------------------------------

import matplotlib.pyplot as plt
from surf import surf
from numpy import array, linspace, log10
from colours import cmap_rainbow


def plot1dmaj( mge_in, ml=1., save="", xlog=False ):
    
    mge = mge_in.copy()
    
    mge.i *= ml
    
    # plotting grid
    lim = mge.s.max() * 3.
    inlim = mge.s.min() / 2.
    if xlog: xx = 10**linspace( log10( inlim ), log10( lim ), 51 )
    else: xx = linspace( 0., lim, 51 )
    
    # surface brightness
    sx = array( [ log10( surf( mge, x, 0. ) ) for x in xx ] )
    sxx = array( [ [ log10( surf( mge[i:i+1], x, 0. ) ) for x in xx ] \
        for i in range( mge.size ) ] )
    
    # plot in arcmin not arcsec
    xx /= 60.
    lim /= 60.
    
    # y axis limits
    vmin = log10( mge.i.min() / 2. )
    vlim = sx.max()
    ptp = vlim - vmin
    vlim = vlim + ptp * 0.1
    vmin = vmin - ptp * 0.1
    
    # set up plotting
    plt.rc( 'text', usetex=True )
    plt.rc( 'font', family='serif' )
    plt.rc( 'xtick', labelsize='8' )
    plt.rc( 'ytick', labelsize='8' )
    plt.rc( 'axes', labelsize='10' )
    rainbow = cmap_rainbow()
    
    # plot colours
    import matplotlib.colors as colors
    import matplotlib.cm as cmx
    cnorm = colors.Normalize( vmin=0, vmax=255 )
    cols = cmx.ScalarMappable( norm=cnorm, cmap=rainbow ).to_rgba
    cc = linspace( 255., 0., mge.size )
    
    
    yl = r"$\log \; $" \
        + r"$[ I \; ( \mathrm{{L}}_{{\odot}} \mathrm{{pc}}^{{-2}} ) ]$"
    
    fig = plt.figure( figsize=( 4, 3 ) )
    
    # x-axis plot
    ax = fig.add_axes( [ 0.12, 0.12, 0.86, 0.87 ] )
    
    if xlog: ax.semilogx( xx, sx, "k", lw=3, alpha=0.8 )
    else: ax.plot( xx, sx, "k", lw=3, alpha=0.8 )
    
    for i in range( mge.size ):
        ax.plot( xx, sxx[i], "k", lw=3, alpha=0.8, c=cols( cc[i] ) )
    
    ax.set_xlim( 0., lim )
    ax.set_ylim( vmin, vlim )
    
    if xlog: ax.set_xlabel( r"$\log[ x' (\mathrm{{arcmin}}) ]$" )
    else: ax.set_xlabel( r"$x' [ \mathrm{{arcmin}} ]$" )
    ax.set_ylabel( yl )
    
    plt.show()
    if save: plt.savefig( save )
