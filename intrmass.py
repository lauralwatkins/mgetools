#!/usr/bin/env python
# -----------------------------------------------------------------------------
# INTRMASS
#   
#   Program calculates enclosed intrinsic mass for an MGE.
#   
#   INPUTS
#     p : projected axis ratios
#     q : intrinsic acis ratios
#   
#   HISTORY
#     v1.0 : Glenn van de Ven [glenn@mpia.de] - MPIA, 2010
#     v1.1 : Laura L Watkins [lauralwatkins@gmail.com] - MPIA, 2012/06/19
#            - converted to python
# -----------------------------------------------------------------------------




#----------------------------------------------------------------------
# enclosed intrinsic mass M(<r)
#
# r             = intrinsic radius [in km]
# surf_pot_km   = central luminosity [in L_sun/km^2]
# sigobs_pot_km = dispersion [in km]
# qobs_pot      = observed flattening
# INCL = inclination [in degrees, default=90]
# ELLRADCONSTQ  = within elliptic radius for *constant* flattening 
#----------------------------------------------------------------------

from numpy import cos, exp, pi, sin, sqrt, zeros
from deproject import deproject
from scipy.special import erf
from scipy.integrate import quad


def intg_intrmass( th, r, imge ):
    
    scq = sqrt( sin(th)**2 + cos(th)**2 / imge.q**2 )
    x = r * scq / imge.s / sqrt(2.)
    
    intg = sqrt( pi / 2. ) * erf( x ) - sqrt(2.) * x * exp( -x**2 )
    res = ( imge.i * imge.s**3 / scq**3 * intg * sin(th) ).sum()
    
    return res


# NOTE THE UNITS - GLENN HAS EVERYTHING IN KM (WHY?)

def intrmass( r, pmge, incl=pi/2., ellrad=False ):
    
    # deproject mge to get intrinsic parameters
    imge = deproject( pmge, incl )
    
    res = zeros( r.size )
    
    if ellrad:
        # within ellipsoidal radius for *constant* flattening
        
        for i in range( r.size ):
            x  = r[i] / sqrt(2.) / imge.s
            intg = sqrt( pi / 2. ) * erf( x ) - sqrt(2.) * x * exp( -x**2 )
            res[i] = 4. * pi * ( imge.s**3 * imge.q * imge.i * intg ).sum()
            # why mutliply bt imge.q here???
    
    else:
        # within spherical radius
        
        for i in range( r.size ):
            intg, err = quad( lambda x: intg_intrmass( x, r[i], imge ),
                0., pi / 2. )
            res[i] = 4. * pi * intg
    
    return res
