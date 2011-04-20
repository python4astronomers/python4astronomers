.. include:: ../references.rst

.. _`sherpa-4.3.0-EPD-7.0-i386.dmg`: http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa-4.3.0-EPD-7.0-i386.dmg
.. _`sherpa-4.3.0-EPD-7.0-x86_64.dmg`: http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa-4.3.0-EPD-7.0-x86_64.dmg
.. _`sherpa-4.3.0-EPD-7.0-linux-x86_64.egg`: http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa-4.3.0-EPD-7.0-linux-x86_64.egg
.. _`sherpa-4.3.0-EPD-7.0-linux-x86.egg`: http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa-4.3.0-EPD-7.0-linux-x86.egg
.. _`sherpa-4.3.0-py2.6-rh5-x86_64.egg`: http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa-4.3.0-py2.6-rh5-x86_64.egg

.. Python4Astronomers documentation file



Fitting and modeling data
=========================

Setup
-----

In order to follow along with the Sherpa examples presented in the workshop on
April 29, your Python installation will need the following dependencies and
Sherpa version 4.3.0.

- Sherpa Dependencies

  - Python 2.6 or 2.7 (not Python 3.x)
  - NumPy >= 1.3
  - Matplotlib >= 0.99
  - pyFITS >= 1.3
  - DS9 >= 5

.. Note::
  EPD users, you have already statisfied the installation requirements
  above.  Continue with the installation Notes below.  If you have been to
  previous workshops and are able to complete the examples, your installation is
  most likely sufficient.  See the Sherpa installation notes below to install
  Sherpa version 4.3.0.


Users Interested in Maintaining their own Python Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Built Python binaries of Sherpa can be found here

- `Download Sherpa <http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/>`_:
  Sherpa binaries for Mac and Ubuntu


Install Notes for EPD Mac Users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install the Enthought EPD 7.0 at `EPD downloads <http://cxc.cfa.harvard.edu/contrib/python4astronomers>`_

  `Enthought <http://www.enthought.com>`_ is the company which leads most of the
  development of `NumPy`_ and `SciPy`_.  They provide a bundled binary
  distribution of Python with a large set of useful packages built in.  The
  `Academic version <http://www.enthought.com/products/edudownload.php>`_ of EPD
  is free for use by students or employees of a degree-granting institution
  (i.e. Harvard but not SAO) as specified in the `license terms
  <http://www.enthought.com/EPDAcademicTerms.html>`_.

  *By special permission from Enthought, all tutorial participants are allowed
  use the Academic EPD downloads we are providing.*

  However, please do not distribute these files to others without express
  permission.  The user name and password were emailed to the pythonusers
  mailing list on March 18.


Download the appropriate Sherpa disk image for your version of OSX

  ===================  ===========================  ===================================
  OSX                  EPD disk image               Sherpa disk image
  ===================  ===========================  ===================================
  Leopard 10.5         epd-7.0-2-macosx-i386.dmg    `sherpa-4.3.0-EPD-7.0-i386.dmg`_
  Snow Leopard 10.6    epd-7.0-2-macosx-x86_64.dmg  `sherpa-4.3.0-EPD-7.0-x86_64.dmg`_
  ===================  ===========================  ===================================

Double-click on the disk image and follow the instructions in the install wizard.


Install Notes for Ubuntu Users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users who use ``apt-get`` to manage their Python distribution can
download the appropriate Ubuntu package for their operating system.

  - `sherpa_4.3.0-1_amd64.deb
    <http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa_4.3.0-1_amd64.deb>`_
  - `sherpa_4.3.0-1_i386.deb
    <http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa_4.3.0-1_i386.deb>`_

Double-click on the Debian package file (.deb) and follow the instructions in
the install wizard.


Install Notes for EPD Linux Users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install the EPD on Linux by following the instructions `here. <http://python4astronomers.github.com/installation/linux-self.html#user-install-without-root>`_

Download the appropriate Sherpa egg for your Linux architecture

  =====================  ========================  ========================================
  Architecture           EPD Linux installer               Sherpa egg
  =====================  ========================  ========================================
  Linux i686   (32-bit)  epd-7.0-2-rh5-x86.sh      `sherpa-4.3.0-EPD-7.0-linux-x86.egg`_
  Linux x86_64 (64-bit)  epd-7.0-2-rh5-x86_64.sh   `sherpa-4.3.0-EPD-7.0-linux-x86_64.egg`_
  =====================  ========================  ========================================

Install Sherpa into your EPD installation using easy_install::

  easy_install sherpa-4.3.0-EPD-7.0-linux-x86.egg


Install Notes for Linux Users using HEAD network installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users relying on the Python located in /usr/local/bin accessible from their CfA
HEAD managed Linux machine can install Sherpa as an egg to their own directory

Download the Sherpa egg

`sherpa-4.3.0-py2.6-rh5-x86_64.egg <http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa-4.3.0-py2.6-rh5-x86_64.egg>`_


Install Sherpa into your own directory using easy_install::

  easy_install --user sherpa-4.3.0-py2.6-rh5-x86_64.egg

.. Note::
   The Sherpa installation includes a number of XSPEC spectral FITS tables, so
   consider storage of ~= 250MB for Sherpa in your home directory.



Try It Out
----------

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
