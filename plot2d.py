#!/usr/bin/env python
# -----------------------------------------------------------------------------
# PLOT2D
#   
#   Plots a 2d surface density map for a given mge.
#   
#   INPUTS
#     mge_in : projected MGE
#   
#   OPTIONS
#     save   : path to save location
#   
#   HISTORY
#     v1.0 : Laura L Watkins [lauralwatkins@gmail.com] - MPIA, 2013/04/08
# -----------------------------------------------------------------------------

import matplotlib.pyplot as plt
from surf import surf
from numpy import array, linspace, log10
from colours import cmap_rainbow


def plot2d( mge_in, ml=1., save="" ):
    
    mge = mge_in.copy()
    
    mge.i *= ml
    
    # plotting grid
    lim = mge.s.max() * 2.
    xx = linspace( -lim, lim, 51 )
    yy = linspace( -lim, lim, 51 )
    
    # surface brightness
    ss = array( [ [ log10( surf( mge, x, y ) ) for x in xx ] for y in yy ] )
    
    # plot in arcmin not arcsec
    xx /= 60.
    yy /= 60.
    
    
    # set up plotting
    plt.rc( 'text', usetex=True )
    plt.rc( 'font', family='serif' )
    plt.rc( 'xtick', labelsize='8' )
    plt.rc( 'ytick', labelsize='8' )
    plt.rc( 'axes', labelsize='10' )
    rainbow = cmap_rainbow()
    
    
    fig = plt.figure( figsize=( 4, 3 ) )
    
    # mge plot
    ax = fig.add_axes( [ 0.14, 0.12, 0.65, 0.85 ] )
    cols = ax.imshow( ss, origin="lower", cmap=rainbow, \
        extent=( xx.min(), xx.max(), yy.min(), yy.max() ) )
    ax.set_xlabel( r"$x' [ \mathrm{{arcmin}} ]$" )
    ax.set_ylabel( r"$y' [ \mathrm{{arcmin}} ]$" )
    
    # colour bar
    cax = fig.add_axes( [ 0.80, 0.12, 0.04, 0.85 ] )
    fig.colorbar( cols, cax=cax )
    cax.set_ylabel( r"$\log \; $" \
        + r"$[ I \; ( \mathrm{{L}}_{{\odot}} \mathrm{{pc}}^{{-2}} ) ]$" )
    
    plt.show()
    if save: plt.savefig( save )
