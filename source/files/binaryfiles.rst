:tocdepth: 2

Binary formats useful for astronomers
*************************************

Pyfits - Reading and writing fits files
=======================================

`PyFITS <http://packages.python.org/pyfits/>`_  is a python module developed at STScI to read and write all types of fits files. The pdf version of the `manual <http://stsdas.stsci.edu/download/docs/The_PyFITS_Handbook.pdf>`_ is several hundert pages long, but the `tutorial <http://packages.python.org/pyfits/users_guide/users_tutorial.html>`_ just goes through the basics.

.. admonition:: External resource!

    The PyFITS tutorial itself is good for our purpose and since this
    is the internet I will not reinvent the wheel. Read the `Pyfits tutorial <http://packages.python.org/pyfits/users_guide/users_tutorial.html>`_
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
    head.keys()             # lists all keywords in a dictionary
    head['TDATEOBS']
    head['TTIMEOBS']
    primary = hdus[0].data  # Primary (NULL) header data unit
    img = hdus[1].data      # Intensity data


    plt.clf()
    plt.imshow(img, origin = 'lower', vmin = -10, vmax = 65)
    plt.colorbar()

Don't be surprised to recognize this piece of code. It was used before in
the :doc:`../core/numpy_scipy` part of the tutorial, but now you should understand the
``pyfits`` commands in more detail.

.. raw:: html

   </div>



Reading IDL .sav files
======================

IDL is still a very common tool in astronomy. While IDL packages exist to read and write data in simple (ASCII) or standardized file formats (fits), that users of all platforms can use, IDL also offers a binary file format with an undocumented, proprietary structure. However, acess to this file format (usually called ``.sav``) is very simple and convenient in IDL. Therefore, many IDL users dump their data in this way and you might be forced to read ``.sav`` files a collegue has sent you.

Here is an examplary ``.sav`` :download:`file <../downloads/myidlfile.sav>`. 
If you have trouble downloading the file, then use IPython::

    import urllib2
    url = 'http://python4astronomers.github.com/_downloads/myidlfile.sav'
    open('myidlfile.sav', 'wb').write(urllib2.urlopen(url).read())
    ls


What can you do?
    1. Convert your collegue to use a different file format.
    2. Read that file in python.

If you have a relatively recent version (at least 0.9) of ``scipy`` then this is a matter of two lines::
    
    from scipy.io.idl import readsav
    data = readsav('myidlfile.sav')

If your scipy is older, then you need to install the package `idlsave <http://astrofrog.github.com/idlsave/>`_ yourself.
(Go back to :doc:`../installation/packages` for details on package installation.)

In a normal terminal (outside ``ipython``) do::
    
    pip install --upgrade idlsave
    
or, if you install packages as root user on your system::
    
    sudo pip install --upgrade idlsave

Then import the package and read the data::
    
    import idlsave
    data = idlsave.read('myidlfile.sav')
    
.. admonition::  Exercise: Where is your data?

    ``idlsave`` already prints some information on the screen while reading the file. Inspect the object ``data``, find out how you use it and plot
    the ``x`` and ``y`` data in it.

.. raw:: html

   <p class="flip6">Click to Show/Hide Solution</p> <div class="panel6">

``data`` is a dictionary and all the variables in the ``.sav`` file are
fields in this dictionary. You get a list with ``data.keys()``. Then, this
is easy::
    
    plt.plot(data['x'], data['y'])

.. raw:: html

   </div>

Note that ``idlsave`` cannot write files and that it will fail to read if the ``.sav`` file contains special structures like system variables or compiled IDL code.


.. include:: ../references.rst


