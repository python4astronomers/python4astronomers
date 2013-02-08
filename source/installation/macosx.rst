.. _Mac_OSX:

Mac OSX
=======

Install the distribution
------------------------

If you can follow instructions and have a little patience then MacPorts is
probably the best option.  If anything beyond a one-click install is too much
of a bother then choose EPD Academic or ActiveState.  For something in-between
choose Homebrew.

MacPorts
^^^^^^^^

To install Python using MacPorts follow the detailed instructions at `MacPorts
Python installation on Mac - 10 easy steps
<http://astrofrog.github.com/macports-python/>`_.  Another tutorial
on MacPorts for Python which is well-written and helpful is
`Setting Up a Mac for Python Development
<http://jakevdp.github.com/blog/2013/02/02/setting-up-a-mac-for-python-development/`_.

Homebrew
^^^^^^^^^

To install Python using `Homebrew < http://mxcl.github.com/homebrew/>`_ follow
the detailed instructions at `Install Python, NumPy, SciPy, and matplotlib on
Mac OS X <http://penandpants.com/2012/02/24/install-python/>`_.

Enthought Python Distribution (EPD)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assuming that you have downloaded the `EPD Academic
<http://www.enthought.com/products/edudownload.php>`_ or `EPD Free
<http://www.enthought.com/products/epd_free.php>`_ disk image, open it, then
double-click on ``EPD.mpkg`` and follow the prompts to install. Choose all the
defaults for installing (in particular use the default installation location).

Additional information can be found on the `Getting Started with EPD
<http://www.enthought.com/products/epdgetstart.php?platform=mac>`_ page.

ActiveState
^^^^^^^^^^^^

Download the `ActivePython community edition
<http://www.activestate.com/activepython/downloads>`_ disk image for Python 2.7
and run the installer, choosing all defaults at the prompts.  Next install the
core packages from the terminal command line::

  sudo /usr/local/bin/pypm -g install numpy scipy matplotlib ipython

Now edit the file `~/.bash_profile` and insert the following line at the end::

  export PATH="/Library/Frameworks/Python.framework/Versions/2.7/bin:${PATH}"

Quick installation check 
----------------------------------------

Open a new terminal window and type::

  which ipython

You should see one of the following:

===========  ===========================================================================
Dist         Path
===========  ===========================================================================
MacPorts     ``/opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin/ipython``
EPD          ``/Library/Frameworks/EPD64.framework/Versions/Current/bin/ipython``
ActiveState  ``/Library/Frameworks/Python.framework/Versions/2.7/bin/ipython``
===========  ===========================================================================

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

Fortran
------------------

Many of the Python scientific packages use Fortran libraries internally. To
avoid getting obscure errors, it is highly recommended to install the latest
``gfortran`` from `<http://r.research.att.com/tools/>`_.  Once you have
installed it, make sure that typing ``gfortran`` gives something like this::

    $ gfortran
    i686-apple-darwin8-gfortran-4.2: no input files

If you get ``gfortran: command not found``, then ``gfortran`` did not
install correctly.

Troubleshooting
---------------

Path
^^^^^

If the Python distribution installed successfully and you can start ``python`` but not ``ipython``
(error message like ``ipython: command not found``) then there is likely a
problem with your PATH.  In the instructions below use the correct PATH for your distribution:

===========  ====================================================================
Dist         Path
===========  ====================================================================
MacPorts     ``/opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin/``
EPD          ``/Library/Frameworks/EPD64.framework/Versions/Current/bin/``
ActiveState  ``/Library/Frameworks/Python.framework/Versions/2.7/bin/``
===========  ====================================================================

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

Determine if you are running csh/tcsh or bash by entering the command 
``echo $0`` in a terminal window.  For ``csh`` or ``tcsh`` you should edit the file
``~/.cshrc`` and add the following lines at the end::

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
