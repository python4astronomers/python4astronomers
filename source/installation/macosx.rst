.. _Mac_OSX:

Mac OSX
=======

Enthought Python Distribution (EPD)
-----------------------------------

First download the appropriate Mac OSX EPD installer from `this <http://cxc.cfa.harvard.edu/contrib/python4astronomers>`_ page.
The user name and password were emailed to the pythonusers mailing list.

.. note:: If you are using MacOS X 10.5 or 10.6 on an Intel Mac, you can
          either install the 32-bit or 64-bit version of EPD 7.0.2. To
          determine whether you have a 32-bit or 64-bit processor, see
          `this page <http://support.apple.com/kb/ht3696>`_. If you have a
          64-bit processor, we strongly recommend that you install the
          64-bit version of EPD (``epd-7.0-2-macosx-x86_64.dmg``).
          Otherwise, you will need the 32-bit version
          (``epd-7.0-2-macosx-i386.dmg``). If you are using a PPC or Intel
          Mac with MacOS X 10.4, you will need to download an older 32-bit
          version (``epd_py25-4.2.30201-macosx-u.dmg``).

After downloading the disk image, open it, then double-click on
``EPD.mpkg`` and follow the prompts to install. Choose all the defaults for
installing (in particular use the default installation location).

Optionally, you can go over to the `Getting Started with EPD
<http://www.enthought.com/products/epdgetstart.php?platform=mac>`_ page.

MacOS X Developer Tools
-----------------------

Before you install additional packages, you will need to make sure that you
have installed the MacOS X Developer Tools (XCode) so that the ``gcc``
compiler is available. If you are not sure if you have the developer tools
installed, try typing ``gcc`` in a Terminal. You should see something like this::

    $ gcc
    i686-apple-darwin10-gcc-4.2.1: no input files

If you get ``gcc: command not found`` then you need to install the
developer tools. **If you already have the developer tools installed, you can
proceed to the next section**.

There are several ways to install XCode:

* The developer tools should be present on one of the installation DVDs
  that came with your Mac. Often, this can be found on DVD 2 rather than on
  the main DVD.

* If you don't have the original installation DVDs, you can `register
  <http://developer.apple.com/programs/register/>`_ for free as an Apple
  Developer, which will give you access to XCode 2 or 3:

  - If you are using MacOS 10.6 you should be able to download XCode 3.2.6
    once you are logged in to the `Mac Dev Center
    <http://developer.apple.com/devcenter/mac/index.action>`_. Then, run
    the installer (``Xcode and iOS SDK``).

  - If you are using MacOS 10.5, first log in to the `Mac Dev Center
    <http://developer.apple.com/devcenter/mac/index.action>`_, then go
    `here
    <http://connect.apple.com/cgi-bin/WebObjects/MemberSite.woa/wa/downloads>`_.
    Click on `Developer Tools`, and download `Xcode 3.1.4 Developer DVD
    (Disk Image)`, then run the installer (``XcodeTools.mpkg``).

  - If you are using MacOS 10.4, first log in to the `Mac Dev Center
    <http://developer.apple.com/devcenter/mac/index.action>`_, then go
    `here
    <http://connect.apple.com/cgi-bin/WebObjects/MemberSite.woa/wa/downloads>`_.
    Click on `Developer Tools`, and download `Xcode 2.5 Developer Tools
    (Disk Image)`, then run the installer (``XcodeTools.mpkg``).

* If you like to live on the bleeding edge, have MacOS X 10.6.6, and don't
  mind shelling out $4.99, go to the App Store (``/Applications/App
  Store.app``) and buy XCode 4. Note that while this should work, we have
  not tested it so we can't guarantee that everything will go smoothly with
  the Enthought Python Distribution.

Fortran (Optional)
------------------

You may at some point come across packages which require a Fortran
compiler, or you may want to interface Fortran and Python code. If not, you
can proceed to the next section.

The preferred compiler to interface Fortran and Python code is ``gfortran``.
Other compilers `should` work, but if you want to be on the safe side, you
can download a one-click installer for gfortran 4.2.3 from `this page
<http://r.research.att.com/tools/>`_. Once you have installed it, make sure
that typing ``gfortran`` gives something like this::

    $ gfortran
    i686-apple-darwin8-gfortran-4.2: no input files

If you get ``gfortran: command not found``, then ``gfortran`` did not
install correctly.

Astro: required and useful
--------------------------

Next open a terminal window and do the following::

  easy_install asciitable
  easy_install http://www.stsci.edu/resources/software_hardware/pyfits/pyfits-2.4.0.tar.gz
  easy_install http://stsdas.stsci.edu/astrolib/pywcs-1.9-4.4.4.tar.gz
  easy_install atpy
  easy_install aplpy
  easy_install http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz
  easy_install http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz
  easy_install pyparsing
  easy_install pyregion

Now go back to the :ref:`installation_test` section to verify everything is working.

Troubleshooting
---------------

If you get the following error when attempting to start up ``python``::

    $ python
    -bash: /Library/Frameworks/EPD64.framework/Versions/Current/bin/python: Bad CPU type in executable

then this means that your processor does not support 64-bit binaries. Start
by uninstalling EPD::

    cd /Library/Frameworks/EPD64.framework/Versions
    sudo rm -rf 7.0
    cd /Applications
    sudo rm -rf Enthought

then download and install EPD 7.0.2 32-bit (``epd-7.0-2-macosx-i386.dmg``).