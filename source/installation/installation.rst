.. Python4Astronomers documentation file
.. include:: ../references.rst

.. toctree::
   :hidden:

   requirements

Installing Scientific Python
=============================

Installing the Python language itself on most platforms is generally very easy.
However, installing the other core packages that you will need in day to day
work can be more of a challenge.  

Workshop goals:

- Install Python and all packages needed for the rest of the workshops
- Understand the concept of Python modules and packages
- Learn how to find and install other 3rd party packages:
  
  - PyPI
  - using pip install
  - using python setup.py install

- Know where Python files live
- Learn how to solve installation problems
- Understand the issues involved with multiple Python installations

:Authors: Tom Aldcroft, Tom Robitaille
:Copyright: 2011 Smithsonian Astrophysical Observatory

Python Distributions
-----------------------------

Unless you are confident with (and enjoy) tracking down compiler errors and
other issues related to package incompatibilities, we strongly recommend using
a pre-built binary Python distribution.  For MacOS in particular there are a
whole slew of options for Python which don't play well together.  Even if you
already have an installation on your system you will probably save time in
the long run by starting fresh with a binary Python distribution.

Enthought Python Distribution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For Windows, MacOS and linux non-root installation, **the easiest option for
academics** is to use the `Enthought Python Distribution
<http://www.enthought.com/products/epd.php>`_ (EPD).  For the Python for
Astronomers workshop series held at the Harvard Center for Astrophysics in
2011, over 50 astronomers successfully installed and used EPD on a variety of
platforms (including Windows).  *All the installation instructions that follow
are written assuming this option.*

`Enthought <http://www.enthought.com>`_ is the company which leads most of the
development of `NumPy`_ and `SciPy`_.  EPD is a bundled binary
distribution of Python with a *large* set of useful packages built in.  The
`Academic version <http://www.enthought.com/products/edudownload.php>`_ of EPD
is free for use by students or employees of a degree-granting institution as
specified in the `license terms
<http://www.enthought.com/EPDAcademicTerms.html>`_.

If you do not meet the academic license requirements but are using Python for
research in astronomy (e.g. observatory staff scientist), we recommend
contacting Enthought directly and requesting permission.

ActiveState Community Python Distribution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A second option is to use the `ActiveState Community Python Distribution
<http://www.activestate.com/activepython/downloads>`_, 
a.k.a. ActivePython.  This has no license requirements and is freely
available.  Features of ActivePython include:

- The initial distribution is much smaller, consisting mostly of Python and
  some utilities.  
- Packages can be added with a customized package manager ``pypm`` toolf which
  installs from the `ActiveState PyPM repository <http://code.activestate.com/pypm/>`_.  This
  handles the "difficult" packages like NumPy and SciPy with support for
  dependency resolution, and also includes most packages from `PyPI`_.

Two quick tests of installing ActivePython on MacOS (snow leopard) and a linux
CentOS-5 system appeared to be successful and were simple to perform.  Beyond
that, unfortunately, our experience is limited.  Community inputs on using this
option would be welcome.

Installation steps
--------------------

In order to follow along with the examples to be presented in the workshops
your Python installation will need to meet the :ref:`python_pkg_requirements`.  The aim
of this workshop is to get this set up correctly.  This will proceed in three
steps:

- Download the appropriate Enthought Python Distribution (EPD) installer
- Install EPD as the core Python installation 
- Install additional packages which are used in the workshops
- Test the installation

The installation process is particular to each platform.  For all options
except "Linux on HEAD or CF network" you will need the EPD download as
discussed in the next section.

Download EPD
^^^^^^^^^^^^^

To download EPD go to the `EPD Academic Download
<http://www.enthought.com/products/edudownload.php>`_ page.  

Here you immediately need to make a decision: 32-bit or 64-bit download?  First
you need to establish whether your computer has a 32-bit or 64-bit processor.
If you have a 32-bit processor then your decision is easy (32-bit) but if you
have a 64-bit processor then either 32 or 64 will work.  See below if you don't
know your processor architecture:

- MacOSX: Follow `these instructions <http://support.apple.com/kb/ht3696>`_
- Linux: Type ``uname -mpi`` at the command line.  If you see ``x86_64 x86_64
  x86_64`` you have a 64-bit machine and OS.  If you see one or more ``i686``
  or ``i386`` you are running a 32-bit OS.
- Windows:  Follow `these instructions 
  <http://windows.microsoft.com/en-US/windows-vista/32-bit-and-64-bit-Windows-frequently-asked-questions>`_.

**64-bit**

- *Pro*: Faster for data- and compute-intensive applications
- *Con*: Have to submit an email address and wait for the download link in response

**32-bit**

- *Pro*: Comes with the `Mayavi <http://github.enthought.com/mayavi/mayavi/>`_ 3-d
  rendering package installed while the 64-bit does not (for technical reasons).
  If you are interested in using this cool package you should consider choosing 32-bit.
  Note that the standard matplotlib package supports some `3-d plotting
  <http://matplotlib.sourceforge.net/mpl_toolkits/mplot3d/tutorial.html>`_. 


Install core Python
^^^^^^^^^^^^^^^^^^^

Now install EPD as the core Python on your system following the instructions below:

.. toctree::
   :maxdepth: 2
   
   macosx
   linux
   windows

Install additional packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here you will install the additional packages listed in the
:ref:`python_pkg_requirements` section.  Copy and paste the lines applicable to your
system one at a time, checking that each one works.  The program outputs may
contain various "warnings", but watch for "errors" and look at the end to see
if a successful installation was reported.

Of these packages only ``pywcs`` was a significant issue during the CfA Python
for Astronomers series.  Most Windows users and a few MacOS users had
problems.  Since then a patch has been released, but it is still known to fail
for 32-bit Windows XP.  This package is required to make images with ``APLpy``
and do WCS coordinate transformations, but otherwise it is not absolutely needed.

MacOS or root linux install
############################
::

  easy_install --upgrade pip
  pip install --upgrade distribute
  pip install asciitable
  pip install pyfits
  pip install pywcs
  pip install atpy
  pip install aplpy
  pip install pyregion
  pip install pyparsing
  pip install http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz
  pip install http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz

Non-root linux
############################
::

  easy_install --user --upgrade pip
  pip install --user --upgrade distribute
  pip install --user asciitable
  pip install --user pyfits
  pip install --user pywcs
  pip install --user atpy
  pip install --user aplpy
  pip install --user pyregion
  pip install --user pyparsing
  pip install --user http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz
  pip install --user http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz

Windows
############################

For Windows XP 32-bit the following are known to have problems: pywcs,
pyregion, and coords.
::

  cd C:\Python27\Scripts
  easy_install.exe --upgrade pip
  pip.exe install --upgrade distribute
  pip.exe install asciitable
  pip.exe install pyfits
  pip.exe install pywcs     
  pip.exe install atpy
  pip.exe install aplpy
  pip.exe install pyregion  
  pip.exe install pyparsing
  pip.exe install http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz
  pip.exe install http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz


.. Admonition:: The soap opera of pip and easy_install and distribute and setuptools

   Here is where things can appear very confusing if you start installing
   packages on your own and looking through various projects and installation
   documentation.  First there was the ``distutils`` standard
   library module that specifies what a package provides and how it gets
   installed.  But this was found to be lacking and a 3rd party extension named
   ``setuptools`` was developed and adopted fairly widely.  In conjunction with
   ``setuptools`` was a script ``easy_install`` that took care of downloading,
   untarring, building, and installing packages.  Pretty good, except that the
   developer of both these stopped actively developing them.  

   So some people took matters into their own hands and did a "friendly fork"
   of ``setuptools`` named ``distribute``.  The not-so-friendly part is that
   the ``distribute`` package actually installs a module named
   ``setuptools.py`` and will overwrite an "original" ``setuptools`` package.
   The flame war that ensued was epic.  In any case now ``distribute`` is the
   standard, and likewise ``pip`` has replaced ``easy_install`` as the best
   (and actively developed) easy installer.

.. _installation_test:

Test your installation
^^^^^^^^^^^^^^^^^^^^^^^^

To do a very basic test whether you meet the requirements and have a functioning
core scientific Python installation, do the following and check version numbers::

  % python -V
  % ipython -V
  % ipython -pylab
  import numpy
  import scipy
  import scipy.linalg

  print numpy.__version__
  print scipy.__version__
  print matplotlib.__version__

  x = numpy.linspace(0, 20, 100)
  plot(x, sin(x))
  print scipy.linalg.eig([[1,2],[3,4]])

The commands above should succeed with no errors.  The version numbers should
meet the requirements, and finally you should see a plot of a sine wave.

To check the other required packages, do the following from within ipython::

  import asciitable
  import pyfits
  import pywcs
  import atpy
  import aplpy

Try it out!
--------------

Setup
^^^^^^^^^^^

First download the `<install_examples.tar>`_ tar file which has example data
files that will be used in subsequent exercises.
Then change to a working directory, untar the file, and start up IPython::

  tar xvf ~/Downloads/install_examples.tar   # or wherever your browser puts downloads
  cd py4ast/install
  ls
  ipython -pylab

.. tip::
   For all of the workshops you should always start Python using the command::
   
     ipython -pylab  # (for Windows start the Pylab application)

   This will automatically load all of the main plotting functions from
   `Matplotlib`_ (e.g. ``plot()``, ``hist()``, and many more) as well as common
   math functions and array utilities from `NumPy`_ (e.g. ``sin()``, ``exp()``,
   ``array()``, etc).

   In my ``~/.cshrc`` file I define an alias that I commonly use::

     alias pylab "ipython -pylab"


.. admonition:: Exercise: Read a table and examine it
  
  Look at the documentation for the `asciitable.read()
  <http://cxc.harvard.edu/contrib/asciitable/#reading-tables>`_ function in
  `asciitable`_.  Follow the very first example and use the ``read()`` function
  to read the data in the file ``table1.dat`` into the variable named ``data``.

  This table is in the "ApJ machine-readable format" (which is actually a bit
  tricky for machines to read).  This is very similar to the table format used
  by CDS / Vizier for input and storage of tables in astronomy.

  Once you have read the table into the variable ``data`` then print the table,
  print the column ``RAdeg``, and print the 3rd row.

  Hints:
     
     - You can print a ``<variable>`` by just typing ``print <variable>`` at the command line, for example ``print data``.
     - You can get tons of useful information about a variable with ``help`` or ``?``:

        - ``help <variable>``
        - ``? <variable>``

       These two commands are pretty similar except that ``?`` gives a little bit more information
       and in a more raw form.
     - The object returned by ``asciitable.read()`` is a NumPy record array, 
       which is just a fancy way of saying a table where you can access rows or columns of data.
     - You can get the column names and types with ``print data.dtype``
     - To print a column of data use ``print data["<column_name>"]``, for example ``print data["Name"]``
     - To print a row of data use ``print data[<row_number>]``

  Optional: use the `plot <http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.plot>`_ and 
  `hist <http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.hist>`_ functions to
  examine the data graphically.  For instance plot RAdeg versus DEdeg.  Look at the ``table1.dat`` file itself for
  detailed column descriptions.


Modules, Packages, and all that
----------------------------------

One of the key features of Python is that the actual core language is fairly
small.  This is an intentional design feature to maintain simplicity.  Much of
the powerful functionality comes through external modules and packages.  

The main work of installation so far has been to supplement the core Python
with useful modules for science analysis.

**Module**

A `module <http://docs.python.org/tutorial/modules.html>`_ is simply a file
containing Python definitions, functions, and statements.  Putting code into
modules is useful because of the ability to `import
<http://docs.python.org/reference/simple_stmts.html#import>`_ the module
functionality into your script or IPython session, for instance::

  import atpy
  data = atpy.Table('my_table.fits')

You'll see ``import`` in virtually every Python script and soon it will be
second nature.  

*Question*: 
  Importing modules and putting the module name in front is such a bother, 
  why do I need to do this?

*Answer*: 
  It keeps everything modular and separate.  For instance many modules have a
  ``read()`` function since this is a common thing to do.  Without using the
  ``<module>.<function>(...)`` syntax there would be no way to know which one
  to call.

.. Tip::

  Sometimes it is convenient to make an end-run around the ``<module>.`` 
  prefixing.  For instance when you run ``ipython -pylab`` the interpreter
  does some startup processing so that a number of functions 
  from the `numpy`_ and `matplotlib`_ modules are available *without*
  using the prefix.
  
  Python allows this with this syntax::

    from <module> import *
  
  That means to import every function and definition from the module into the
  current namespace (in other words make them available without prefixing).
  For instance you could do::
  
    from atpy import *
    data = Table('my_table.fits')
  
  A general rule of thumb is that ``from <module> import *`` is OK for
  interactive analysis within IPython but you should avoid using it within
  scripts.

**Package**

A `package <http://docs.python.org/tutorial/modules.html#packages>`_ is just a
way of collecting related modules together within a single tree-like
hierarchy.  Very complex packages like `NumPy`_ or `SciPy`_ have hundreds of
individual modules so putting them into a directory-like structure keeps things
organized and avoids name collisions.  For example here is a partial list
of sub-packages available within `SciPy`_

================================== ======================================================
scipy.fftpack                      Discrete Fourier Transform algorithms 
scipy.stats                        Statistical Functions 
scipy.lib                          Python wrappers to external libraries 
scipy.lib.blas                     Wrappers to BLAS library 
scipy.lib.lapack                   Wrappers to LAPACK library 
scipy.integrate                    Integration routines 
scipy.linalg                       Linear algebra routines 
scipy.sparse.linalg                Sparse Linear Algebra 
scipy.sparse.linalg.eigen          Sparse Eigenvalue Solvers 
scipy.sparse.linalg.eigen.arpack   Eigenvalue solver using iterative methods. 
================================== ======================================================

.. admonition:: Exercise: Import a package module and learn about it
  
  Import the Linear algebra module from the SciPy package and find out what
  functions it provides.


Finding and installing other packages
--------------------------------------

If you've gotten this far you have a working scientific Python environment that
has *most* of what you will ever need.  Nevertheless it is almost certain that
you will eventually find a need that is not met within your current
installation.  Here we learn **where** to find other useful packages and
**how** to install them. 

Package resources
^^^^^^^^^^^^^^^^^^

.. sidebar:: Good vs. bad resources

   When you find some package on the web, look for a few things:
   
      - Good modern-looking documentation with examples
      - Installs easily without lots of dependencies (or has detailed
        installation instructions)
      - Actively developed

Google
#######

Google "python blah blah" or "python astronomy blah blah"

Resource lists
###############

There are a number of sites specifically devoted to Python for astronomy with
organized lists of useful resources and packages.

  - `Astropython.org resources <http://www.astropython.org/resources>`_
  - `Comfort at 1 AU
    <http://oneau.wordpress.com/2010/10/02/python-for-astronomy/>`_
  - `Astronomical Python <http://www.astro.washington.edu/users/rowen/AstroPy.html>`_

PyPI
#######

The `Python Package Index <http://pypi.python.org/pypi>`_ is the main
repository for 3rd party Python packages (about 14000 packages and growing).
An increasing number of `astronomy related packages
<http://pypi.python.org/pypi?:action=browse&show=all&c=385&c=387>`_
are available on PyPI, but this list misses a lot of available options.

The advantage of being on PyPI is the ease of installation using
``pip install <package_name>``.  

.. admonition:: Exercise: Find packages for coordinate manipulations

  Find one or more Python packages that will transform coordinates from Galactic to FK5 ecliptic.
  
  *Hint*: tags are helpful at astropython.org and don't forget the "next" button at
  the bottom.

Package installation
^^^^^^^^^^^^^^^^^^^^

There are two standard methods for installing a package. 

**pip install**

The ``pip install`` script is available within our scientific Python
installation and is very easy to use (when it works).  During the installation
process you already saw many examples of ``pip install`` in action.  Features include:

  - If supplied with a package name then it will query the PyPI site to find out about
    that package.  Assuming the package is there then ``pip install`` will
    automatically download and install the package.  
  - Will accept a local tar file (assuming it contains an installable Python package) or a URL
    pointing to a tar file.
  - Can install in the user package area via ``pip install <package or URL>
    --user`` (see discussion further down)

**python setup.py install**

Some packages may fail to install via ``pip install``.  Most often there will
be some obvious (or not) error message about compilation or missing
dependency.  In this case the likely next step is to download the installation tar
file and untar it.  Go into the package directory and look for files like::

  INSTALL
  README
  setup.py
  setup.cfg

If there is an INSTALL or README file then hopefully you will find useful
installation instructions.  Most well-behaved python packages do the
installation via a standard ``setup.py`` script.  This is used as follows::

  python setup.py --help  # get options
  python setup.py install # install in the python area (root / admin req'd)
  python setup.py install --user # install to user's package area

More information is available in the `Installing Python Modules
<http://docs.python.org/install/index.html>`_ page.

Where to packages get installed?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An important option in the installation process is where to put the package
files.  We've seen the ``--user`` option in ``pip install`` and ``python
setup.py install``.  What's up with that?  In general, if you don't have to you
should not use ``--user``, but see the discussion in `Multiple Pythons on
your computer`_ for a reason you might.

WITH ``--user``
################

Packages get installed in a local user-owned directory when you do something
like either of the following::

  pip install --user asciitable 
  python setup.py install --user

This puts the packages into:

=======  ==============================================
Mac      ~/Library/Python/2.x/lib/python/site-packages
Linux    ~/.local/lib/python-2.x/site-packages
Windows  %APPDATA%/Python/Python2x/site-packages
=======  ==============================================

.. Note::
  On Mac if you did not use the EPD Python Framework then you may see user
  packages within ``~/.local/lib`` as for linux.  This depends on whether Python
  is installed as a MacOS Framework or not.

WITHOUT ``--user``
###################

This option requires root or admin privilege because the package will be
installed in the system area instead of your own local directories. 

Installing this way has the benefit of making the package available for all users of the
Python installation, but has the downside of possibly breaking things in a way
that is difficult to repair (see next topic).

How do I find a package once installed?
#######################################

Finding the file associated with a package or module is simple, just use the ``help``
command in IPython::

  import scipy
  help scipy

This gives something like::

  NAME
      scipy

  FILE
      /usr/local/lib/python2.6/site-packages/scipy/__init__.py

  DESCRIPTION
      SciPy: A scientific computing package for Python
      ================================================
      
      Documentation is available in the docstrings and
      online at http://docs.scipy.org.
      ... 

Uninstalling packages
^^^^^^^^^^^^^^^^^^^^^^^

There is no simple and fully consistent way to do this.  The Python
community is working on this one.  In most simple cases, however, you can just
delete the module file or directory that is revealed by the technique shown above.

Getting help on package installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you attempt to install a package but it does not work, your basic options are:

  - Dig in your heels and start reading the error messages to see why it is
    unhappy.  Often when you find a specific message it's time to start
    googling by pasting in the relevant parts of the message.
  - Send an email to the `AstroPy
    <http://mail.scipy.org/mailman/listinfo/astropy>`_ mailing list
    astropy@scipy.org.  Include:

      - Package you are trying to install
      - URL for downloading the package tar file
      - Your platform (machine architecture and exact OS version)
      - Exactly what you typed
      - Entire output from the ``python setup.py install`` process

    Do NOT just write and say "I tried to install BLAH and it failed, can 
    someone help?"
  

Multiple Pythons on your computer
---------------------------------

Apart from being a scary thought, this is a practical problem that you are
likely to encounter.  Straight away you probably have the system Python
(/usr/bin) and the EPD Python.  Then if you install PyRaf, CIAO, and CASA you
will get one more Python installation for each analysis package (there are good
reasons for this).  **In general, different Python installations cannot
reliably share packages or resources**.  Each installation should be considered
as its own local Python universe.

Installing within each Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that you know about all the great packages within our Scientific Python
installation, you might want to start using them in your PyRaf or CASA
or CIAO analysis.

If you start digging into Python you will likely come across the technique of
setting the ``PYTHONPATH`` environment variable to extend the list of search
paths that Python uses to look for a module.  Let's say you are using CIAO
Python and want to use SciPy functions.  You might be tempted to set
``PYTHONPATH`` to point to the directory in EPD where the SciPy modules live.
This will fail because the EPD Python modules were compiled and linked assuming
they'll be run with EPD Python.  With effort you might find a way to make this
work, but in general it's not a workable solution.

What *will* often work is to follow the package installation procedure for
each desired package within each Python installation.  This assumes that you
have write permission into the directories where the analysis package files
live.  Simply enter the appropriate analysis environment, then do then
following:

- Download http://pypi.python.org/packages/source/p/pip/pip-1.0.1.tar.gz
- Untar that file, go in the tar directory, and do ``python setup.py install``
- Now you can do ``pip install <package>`` for each desired package within
  that analysis environment.

It's worth noting that the original example of SciPy will not install with
``pip``.  It requires a very tricky installation from source, so unless SciPy
ships with your favorite analysis environment you are out of luck with that
one.

If you do *not* have write access to the analysis package directories, then you
need to use the ``--prefix`` option in ``pip`` to install in a local area and
then set a corresponding ``PYTHONPATH``.

Can we share packages?
^^^^^^^^^^^^^^^^^^^^^^^

If you are careful there is a way to get limited sharing between Pythons.  The
first rule is that they need to be the same major version, i.e. all 2.6 or 2.7.
This is because Python always includes a major version like ``python2.6/`` in
the default search path so Python 2.7 will never find 2.6 packages.  The second
rule is to install packages using the ``--user`` option in ``pip install`` or
``setup.py install``.  This results in the situation shown below where each
Python can find common packages in the local user area:

.. image:: antisocial_pythons_trans.png
   :width: 650

Be sure to test that the package you installed works within the other Python
environments.

.. Caution::
   
   Be very wary of installing a package with ``--user`` if one of your Python
   installations already contains that package.  This is because the local user
   version will always take precedence and thus potentially upset that Python
   installation.  Big analysis packages like CIAO or CASA are carefully tested
   assuming the integrated environment they provide.  If you start mucking this
   up then all bets are off.


Final exercises
---------------

.. admonition:: Exercise [intermediate]: Fully install APLpy

  Go to the `APLpy install page <http://aplpy.github.com/install.html>`_ and
  read the instructions.  Manually install all of the Python package dependencies with the
  ``--user`` option or try the auto-install script available there.

  For extra credit install the `Montage
  <http://montage.ipac.caltech.edu/>`_ C library as discussed on the APLpy
  install page.  Then try to run the example `Making a publication quality plot
  <../intro/quick-tour.html#making-a-publication-quality-image>`_ that was shown
  in the introductory talk.  The necessary input files are in the
  ``install_examples.tar`` file.

.. admonition:: Exercise [intermediate]: Install HDF5 and PyTables

  Install `HDF5 <http://www.hdfgroup.org/HDF5/>`_ and
  `PyTables <http://www.pytables.org/moin>`_.  This will let you read HDF5 tables
  in Python.  HDF5 is a data file format which can store and manipulate extremely
  large or complex datasets in a scalable manner.  It is the baseline for some data-heavy
  facilities such as LOFAR.

.. admonition:: Exercise [expert]: Install SciPy and all dependencies from source

  Attempt to follow the instructions for building from source in the `Installing
  SciPy <http://www.scipy.org/Installing_SciPy>`_ page.  (No binary downloads!).
  This will be useful if you want to use the very latest development version of
  Python or else want to use the system-dependent build optimization so your
  numerical libraries are the fastest possible.  For most people this is not needed.

  If you can do this then consider yourself an expert on Python installation.


