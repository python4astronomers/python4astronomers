.. _Mac_OSX:

Mac OSX
=======

Enthought Python Distribution (EPD)
-----------------------------------

Assuming that you have downloaded the EPD disk image, open it, then double-click on
``EPD.mpkg`` and follow the prompts to install. Choose all the defaults for
installing (in particular use the default installation location).

Additional information can be found on the `Getting Started with EPD
<http://www.enthought.com/products/epdgetstart.php?platform=mac>`_ page.

Quick installation check 
----------------------------------------

Open a new terminal window and type::

  which ipython

You should see something like:

  /Library/Frameworks/EPD64.framework/Versions/Current/bin/ipython

If not go to the `Troubleshooting`_ section.

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

Troubleshooting
---------------

Path
^^^^^

If EPD installed successfully and you can start ``python`` but not ``ipython``
(error message like ``ipython: command not found``) then there is likely a
problem with your PATH.

Step 1
######

Are you sure you opened a new terminal window after the installation finished?

Step 2
######

Try this in a new terminal window::

  echo $PATH

If you do not see something like
``/Library/Frameworks/EPD64.framework/Versions/Current/bin`` in your path then go
to step 3.  

Step 3
########

Determine if you are running csh/tcsh or bash by entering the command ``ps`` in a terminal window.
For ``csh`` or ``tcsh`` you should edit the file ``~/.cshrc`` and add the following lines at the end::

 # Setting PATH for Enthough Python Distribution
 set path=(/Library/Frameworks/EPD64.framework/Versions/Current/bin $path)

For ``bash`` you should edit the file ``~/.bash_profile`` and add the following lines at the end::

 # Setting PATH for Enthough Python Distribution
 export PATH=/Library/Frameworks/EPD64.framework/Versions/Current/bin:$PATH


32 vs. 64 bit
^^^^^^^^^^^^^^

If you get the following error when attempting to start up ``python``::

    $ python
    -bash: /Library/Frameworks/EPD64.framework/Versions/Current/bin/python: Bad CPU type in executable

then this means that your processor does not support 64-bit binaries. Start
by uninstalling EPD::

    cd /Library/Frameworks/EPD64.framework/Versions
    sudo rm -rf 7.0
    cd /Applications
    sudo rm -rf Enthought

then download and install EPD 7.0.2 32-bit.
