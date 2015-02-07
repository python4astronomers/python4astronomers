Astropy I: core functions
=========================

`Astropy <http://www.astropy.org>`_ is a community-developed core Python
package for Astronomy (with the term used in the broad sense, from Solar
System work to Cosmology). The first public release (v0.2) took place on
February 20th 2013, bug-fixes are released a regular intervals.

Installation instructions for the most current version and the full
documentation can be found on `www.astropy.org <http://www.astropy.org>`_.

After this workshop you will be familiar with some parts of Astropy, a
second workshop will cover the remaining functionality. 

Beginners in Python should be able to follow, but please ensure that you have
a functional Python distribution installed prior to the workshop.

**Workshop topics**

.. toctree::
   :maxdepth: 1

   tables
   fits
   wcs
   coordinates

Before you proceed
------------------
Please download this
:download:`this tar file <../downloads/astropy_examples.tar>` and extract
the content, either by clicking on the link or by executing this
python code::

    from astropy.extern.six.moves.urllib import request
    import tarfile
    url = 'http://python4astronomers.github.io/_downloads/astropy_examples.tar'
    tarfile.open(fileobj=request.urlopen(url), mode='r|').extractall()
    cd data
    ls

Then start up IPython with the ``--matplotlib`` option to enable interactive
plotting and then import numpy and matplotlib::

    $ ipython --matplotlib

    import numpy as np
    import matplotlib.pyplot as plt

Acknowledgments
---------------

This workshop is based heavily on an introduction to Astropy written
by Tom Robitaille, which can be found at
`http://astropy4mpik.readthedocs.org/en/latest/index.html <http://astropy4mpik.readthedocs.org/en/latest/index.html>`_.

:Authors: Thomas Robitaille, Moritz Guenther
:Copyright: 2013 Moritz Guenther
