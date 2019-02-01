MGETOOLS
========


CONTENTS
--------

* license and referencing
* code description
* requirements


-------------------------------------------------------------------------------


LICENSE AND REFERENCING
-----------------------

This code is released under a BSD 2-clause license.

If you find this code useful for your research, please mention it in your acknowledgements.


-------------------------------------------------------------------------------


CODE DESCRIPTION
----------------

This is a collection of python functions for generating various quantities for Multi-Gaussian Expansions (MGEs). Please use/add to/modify them.

* **Cumulative2D** : Cumulative profile from a 2-dimensional MGE.
* **Cumulative3D** : Cumulative profile from a 3-dimensional MGE.
* **Deproject**: De-project a 2-dimensional MGE.
* **Project** : Project an 3-dimensional MGE.
* **SurfaceDensity** : Surface density of 2-dimensional MGE.
* **VolumeDensity**: Volume density of 3-dimensional MGE.

The MGEs themselves should be given as an astropy Table or QTable, with units for the components as necessary. The structure assumes:

* "i" : central volume or surface density of the MGE component
* "s" : width of the MGE component
* "q" : flattening of the MGE component

[Emsellem, Monnet & Bacon (1994)](https://ui.adsabs.harvard.edu/#abs/1994A&A...285..723E/) and [Cappellari (2002)](https://ui.adsabs.harvard.edu/#abs/2002MNRAS.333..400C/) are good references if you wish to learn more about MGEs and their uses.


-------------------------------------------------------------------------------


REQUIREMENTS
------------

This code assumes you are using Python3. It uses [astropy](https://github.com/astropy/astropy) and the standard python libraries [numpy](http://www.numpy.org/) and [scipy](https://www.scipy.org/).
