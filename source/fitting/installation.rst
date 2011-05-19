.. _`sherpa-4.3.0-EPD-7.0-i386.dmg`: http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa-4.3.0-EPD-7.0-i386.dmg
.. _`sherpa-4.3.0-EPD-7.0-x86_64.dmg`: http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa-4.3.0-EPD-7.0-x86_64.dmg
.. _`sherpa-4.3.0-EPD-7.0-linux-x86_64.egg`: http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa-4.3.0-EPD-7.0-linux-x86_64.egg
.. _`sherpa-4.3.0-EPD-7.0-linux-x86.egg`: http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa-4.3.0-EPD-7.0-linux-x86.egg
.. _`sherpa-4.3.0-py2.6-rh5-x86_64.egg`: http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa-4.3.0-py2.6-rh5-x86_64.egg

.. Python4Astronomers documentation file


Sherpa Installation
-------------------

In order to follow along with the Sherpa examples presented in this workshop,
your Python installation will need the following dependencies and Sherpa
version 4.3.0.

- Sherpa Dependencies

  - Python 2.6 or 2.7 (not Python 3.x)
  - NumPy >= 1.3
  - Matplotlib >= 0.99
  - pyFITS >= 1.3
  - DS9 >= 5

.. Note::
  EPD users, you have already satisfied the installation requirements
  above.  Continue with the installation notes below.  If you have been to
  previous workshops and are able to complete the examples, your installation is
  most likely sufficient.  See the Sherpa installation notes below to install
  Sherpa version 4.3.0.


Sherpa downloads
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Sherpa source tar file and pre-built binaries can be found here:

- `Sherpa downloads <http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/>`_:
  Sherpa source and binaries for Mac and Ubuntu.


Mac EPD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installed the Enthought EPD 7.0 following the
instructions for :ref:`Mac_OSX`.  Then download the appropriate Sherpa disk
image for your version of OSX:

  ===================  ===========================  ===================================
  OSX                  EPD disk image               Sherpa disk image
  ===================  ===========================  ===================================
  Leopard 10.5         epd-7.0-2-macosx-i386.dmg    `sherpa-4.3.0-EPD-7.0-i386.dmg`_
  Snow Leopard 10.6    epd-7.0-2-macosx-x86_64.dmg  `sherpa-4.3.0-EPD-7.0-x86_64.dmg`_
  ===================  ===========================  ===================================

Double-click on the disk image and follow the instructions in the install wizard.


Ubuntu (root)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users who use ``apt-get`` to manage their Python distribution can
download the appropriate Ubuntu package for their operating system.

  - `sherpa_4.3.0-1_amd64.deb
    <http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa_4.3.0-1_amd64.deb>`_
  - `sherpa_4.3.0-1_i386.deb
    <http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa_4.3.0-1_i386.deb>`_

Double-click on the Debian package file (.deb) and follow the instructions in
the install wizard.


EPD Linux
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install the EPD on Linux by following the instructions for
:ref:`linux_nonroot`.  Then download the appropriate Sherpa egg for your Linux
architecture

  =====================  ========================  ========================================
  Architecture           EPD Linux installer               Sherpa egg
  =====================  ========================  ========================================
  Linux i686   (32-bit)  epd-7.0-2-rh5-x86.sh      `sherpa-4.3.0-EPD-7.0-linux-x86.egg`_
  Linux x86_64 (64-bit)  epd-7.0-2-rh5-x86_64.sh   `sherpa-4.3.0-EPD-7.0-linux-x86_64.egg`_
  =====================  ========================  ========================================

Install Sherpa into your EPD installation using easy_install::

  easy_install sherpa-4.3.0-EPD-7.0-linux-x86.egg


Try It Out
^^^^^^^^^^

Try importing the Sherpa high level UI with::

  from sherpa.astro.ui import *

.. Note::
   If you see the following error messages

   WARNING: failed to import sherpa.plot.chips_backend; plotting routines will
   not be available

   WARNING: failed to import sherpa.astro.io; FITS I/O routines will not be available

   Be sure to edit your ~/.sherpa.rc file and indicate

   plot_pkg : pylab

   io_pkg : pyfits

   If you continue to see these messages, you should install pyFITS and 
   matplotlib.

.. Note::
   If you see the following error message, your installation of XSPEC may be
   incomplete.

   WARNING: failed to import sherpa.astro.xspec; XSPEC models will not be
   available

.. Note:: 
   The following error message indicates that Sherpa is unable to find your DS9 or
   XPA.

   WARNING: imaging routines will not be available, failed to import
   sherpa.image.ds9_backend due to 'RuntimeErr: DS9Win unusable: Could not find ds9
   on your PATH'

.. include:: ../references.rst

