#!/usr/bin/env python
# -----------------------------------------------------------------------------
# ELLIP
#   
#   Plots an ellipticity profile for an input MGE.
#   
#   INPUTS
#     mge  : projected MGE
#   
#   OPTIONS
#     save : path to save location
#   
#   Laura L Watkins [lauralwatkins@gmail.com] - MPIA
# -----------------------------------------------------------------------------

from matplotlib.pyplot import *
from surf import surf
from numpy import array, linspace, log10
from colours import cmap_rainbow
from scipy.interpolate import spline


def ellip( mge, save="" ):
    
    # plotting range
    lim = mge.s.max() * 2.
    rr = linspace( lim, 0., 100 )
    
    # minor axis surface brightness profile
    minsb = array( [ log10( surf( mge, 0., r ) ) for r in rr ] )
    
    # ellipticity profile
    ell = array( [ spline( minsb, rr, log10( surf( mge, r, 0. ) ) ) / r
        for r in rr ] )
    
    # plot in arcmin not arcsec
    rr /= 60.
    
    # set up plotting
    rc( 'text', usetex=True )
    rc( 'font', family='serif' )
    rc( 'xtick', labelsize='8' )
    rc( 'ytick', labelsize='8' )
    rc( 'axes', labelsize='10' )
    rainbow = cmap_rainbow()
    
    # set up figure
    fig = figure( figsize=( 4, 3 ) )
    ax = fig.add_axes( [ 0.12, 0.12, 0.86, 0.87 ] )
    
    # ellipticity profile
    ax.plot( rr, ell, "k", lw=2, alpha=0.8 )
    
    # mge flattenings
    ax.scatter( mge.s / 60., mge.q, cmap=rainbow, edgecolor="None", s=70,
        c=range( mge.size )[::-1], zorder=10 )
    
    # axis limits
    ax.set_xlim( rr.min(), rr.max() )
    ax.set_ylim( mge.q.min() - 0.1 * mge.q.ptp(),
        mge.q.max() + 0.1 * mge.q.ptp() )
    
    # axis labels
    ax.set_xlabel( r"$R \; [ \mathrm{{arcmin}} ]$" )
    ax.set_ylabel( r"$q'$" )
    
    show()
    if save: savefig( save )
