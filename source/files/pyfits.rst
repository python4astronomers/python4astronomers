:tocdepth: 2

Pyfits - Reading and writing fits files
=======================================

`PyFITS <http://packages.python.org/pyfits/>`_  is a python module developed at STScI to read and write all types of fits files. The pdf version of the `manual <http://stsdas.stsci.edu/download/docs/The_PyFITS_Handbook.pdf>`_ is several hundert pages long, but the `tutorial <http://packages.python.org/pyfits/users_guide/users_tutorial.html>`_ just goes through the basics.

This tutorial is good and since this is the internet I will not reinvent the wheel. Use the `Pyfits tutorial <http://packages.python.org/pyfits/users_guide/users_tutorial.html>`_
then come back to this page for an exercise.

.. admonition::  Exercise

    Use the following code to download a fits file for this exercise::
        
        import urllib2, tarfile
        url = 'http://python4astronomers.github.com/core/core_examples.tar'
        tarfile.open(fileobj=urllib2.urlopen(url), mode='r|').extractall()
        cd py4ast/core
        ls

    Read in the fits file. Find the time and date of the observations. Then use ``plt.imshow()`` to display the intensity array using some sensible minimum and maximum value so that the spectrum is visible.


.. raw:: html

   <p class="flip6">Click to Show/Hide Solution</p> <div class="panel6">
    
    Here is a possible solution::
        
        import pyfits
        hdus = pyfits.open('3c120_stis.fits.gz')
        hdus.info()
        head = hdus[0].header
        head.keys()             # lists all keywords in a disctionary
        head['TDATEOBS']
        head['TTIMEOBS']
        primary = hdus[0].data  # Primary (NULL) header data unit
        img = hdus[1].data      # Intensity data
        err = hdus[2].data      # Error per pixel
        dq = hdus[3].data       # Data quality per pixel

        plt.clf()
        plt.imshow(img, origin = 'lower', vmin = -10, vmax = 65)
        plt.colorbar()

    Don't be surprised to recognize this piece of code. It was used before in
    the :ref:`NumPy` part of teh tutorial, but now you should understand the
    ``pyfits`` commands in more detail.

.. raw:: html

   </div>

