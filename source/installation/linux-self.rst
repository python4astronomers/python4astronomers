.. _`Linux self-managed`

Linux self-managed machine
==========================

System install with root
------------------------

For a modern linux installation such as Ubuntu 10, the system Python version
will be 2.6 or newer and all of the required core packages are available as 
Synaptic package installs.  The instructions below have been developed and tested with
Ubuntu 10.  Corresponding packages for recent Fedora are probably available but
this has not been verified.

The benefit of using a root install via the system package manager is that it
is simple and all dependencies are managed for you.  The downside is that the
package versions tend to be a bit old and so you don't keep up with the latest
code development.  In Ubuntu 10 the core packages (NumPy, Matplotlib) are a
year or so out of date.  This is not a problem and one of us (TLA) mostly uses
these older versions for stability reasons.

Core installation
^^^^^^^^^^^^^^^^^
::

  sudo apt-get install python-dev
  sudo apt-get install ipython
  sudo apt-get install python-numpy
  sudo apt-get install python-scipy
  sudo apt-get install python-matplotlib
  sudo apt-get install python-setuptools

Astro: required
^^^^^^^^^^^^^^^^
::

  sudo easy_install asciitable
  sudo easy_install http://www.stsci.edu/resources/software_hardware/pyfits/pyfits-2.4.0.tar.gz
  sudo easy_install http://stsdas.stsci.edu/astrolib/pywcs-1.9-4.4.4.tar.gz
  sudo easy_install atpy
  sudo easy_install aplpy

Astro: useful
^^^^^^^^^^^^^
::

  sudo easy_install http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz
  sudo easy_install http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz
  sudo easy_install pyparsing
  sudo easy_install pyregion

User install without root
-------------------------

In this case the easiest path is to use the Enthought Python Distribution.

Astro: required
^^^^^^^^^^^^^^^^
::

  easy_install --user asciitable
  easy_install --user http://www.stsci.edu/resources/software_hardware/pyfits/pyfits-2.4.0.tar.gz
  easy_install --user http://stsdas.stsci.edu/astrolib/pywcs-1.9-4.4.4.tar.gz
  easy_install --user atpy
  easy_install --user aplpy

Astro: useful
^^^^^^^^^^^^^
::

  easy_install --user http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz
  easy_install --user http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz
  easy_install --user pyparsing
  easy_install --user pyregion

