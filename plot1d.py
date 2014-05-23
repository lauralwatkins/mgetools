#!/usr/bin/env python
# -----------------------------------------------------------------------------
# MGE.PLOT1D
# Laura L Watkins [lauralwatkins@gmail.com]
# -----------------------------------------------------------------------------

import matplotlib.pyplot as plt
from surf import surf
from numpy import array, linspace, log10
import colours


def plot1d( mge_in, ml=1., save="" ):
    
    """
    Plots 1d surface density profiles for a given mge.
    
    INPUTS
      mge_in : projected MGE
    
    OPTIONS
      ml     : adjust central surface brightness values by mass-to-light ratio
      save   : path to save location
    """
    
    mge = mge_in.copy()
    
    mge.i *= ml
    
    # plotting grid
    lim = mge.s.max() * 2.
    xx = linspace( 0., lim, 51 )
    yy = linspace( 0., lim, 51 )
    
    # surface brightness
    sx = array( [ log10( surf( mge, x, 0. ) ) for x in xx ] )
    sy = array( [ log10( surf( mge, 0., y ) ) for y in yy ] )
    sxx = array( [ [ log10( surf( mge[i:i+1], x, 0. ) ) for x in xx ] \
        for i in range( mge.size ) ] )
    syy = array( [ [ log10( surf( mge[i:i+1], 0., y ) ) for y in yy ] \
        for i in range( mge.size ) ] )
    
    # plot in arcmin not arcsec
    xx /= 60.
    yy /= 60.
    lim /= 60.
    
    # y axis limits
    vmin = max( -1, sxx.min() )
    vlim = sx.max() * 1.05 - vmin * 0.05
    
    # set up plotting
    plt.rc( 'text', usetex=True )
    plt.rc( 'font', family='serif' )
    plt.rc( 'xtick', labelsize='8' )
    plt.rc( 'ytick', labelsize='8' )
    plt.rc( 'axes', labelsize='10' )
    rainbow = colours.cmap_rainbow()
    rgb = colours.cmap2rgb( rainbow )
    cc = linspace( 255., 0., mge.size )
    
    
    yl = r"$\log \; $" \
        + r"$[ I \; ( \mathrm{{L}}_{{\odot}} \mathrm{{pc}}^{{-2}} ) ]$"
    
    fig = plt.figure( figsize=( 7.5, 3 ) )
    
    # x-axis plot
    ax = fig.add_axes( [ 0.07, 0.12, 0.41, 0.85 ] )
    ax.plot( xx, sx, "k", lw=3, alpha=0.8 )
    for i in range( mge.size ):
        ax.plot( xx, sxx[i], "k", lw=3, alpha=0.8, c=rgb( cc[i] ) )
    ax.set_xlim( 0., lim )
    ax.set_ylim( vmin, vlim )
    ax.set_xlabel( r"$x' [ \mathrm{{arcmin}} ]$" )
    ax.set_ylabel( yl )
    
    # y-axis plot
    ax = fig.add_axes( [ 0.58, 0.12, 0.41, 0.85 ] )
    ax.plot( yy, sy, "k", lw=3, alpha=0.8 )
    for i in range( mge.size ):
        ax.plot( yy, syy[i], "k", lw=3, alpha=0.8, c=rgb( cc[i] ) )
    ax.set_xlim( 0., lim )
    ax.set_ylim( vmin, vlim )
    ax.set_xlabel( r"$y' [ \mathrm{{arcmin}} ]$" )
    ax.set_ylabel( yl )
    
    plt.show()
    if save: plt.savefig( save )
