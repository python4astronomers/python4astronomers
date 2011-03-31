.. Python4Astronomers documentation file
.. include:: ../references.rst

Installing Scientific Python
=============================

Installing the Python language itself on most platforms is generally very easy.
However, installing the other core packages that you will need in day to day
work can be more of a challenge.  

Workshop goals:

- Install Python and all packages needed for the rest of the workshops
- Learn how to find and install other 3rd party packages:
  
  - PyPI
  - using easy_install
  - using python setup.py install

- Learn where Python files live

Enthought Python Distribution
-----------------------------

For Windows, MacOS and linux non-root installation we will make use of the
`Enthought Python Distribution <http://www.enthought.com/products/epd.php>`_
(EPD).  `Enthought <http://www.enthought.com>`_ is the company which leads most
of the development of `NumPy`_ and `SciPy`_.  They provide a bundled binary
distribution of Python with a large set of useful packages built in.  The
`Academic version <http://www.enthought.com/products/edudownload.php>`_ of EPD
is free for use by students or employees of a degree-granting institution
(i.e. Harvard but not SAO) as specified in the `license terms
<http://www.enthought.com/EPDAcademicTerms.html>`_. 

*By special permission
from Enthought, all tutorial participants are allowed use the Academic EPD
downloads we are providing.*

However, please do not distribute these files to others without express permission.

Installation
------------

In order to follow along with the examples to be presented in the workshops
your Python installation will need to meet the `Python requirements`_.  The aim
of this workshop is to get this set up correctly. Once you have followed the
installation instructions in the next section for your platform then go to the
`Tests`_ section to see if everything is OK

The installation process is particular to each platform.  For all options
except "Linux on HEAD or CF network" you will need the EPD download as
discussed in the next section.

EPD downloads
^^^^^^^^^^^^^

For workshop participants the Enthought Python Distribution download files have been
mirrored to the `EPD downloads
<http://cxc.cfa.harvard.edu/contrib/python4astronomers>`_ page.  The user name
and password were emailed to the pythonusers mailing list on March 18.


Instructions
^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 2
   
   macosx
   linux-self
   linux-network
   windows
   package-basics

Python requirements
-----------------------

Following are a list of required and optional (but useful) packages for the workshops.

Core
^^^^^

- Python 2.6 or 2.7 (not Python 3.x [#]_)
- IPython >= 0.10
- NumPy >= 1.3
- SciPy >= 0.7.2
- Matplotlib >= 0.99
- setuptools >= 0.6c11

.. [#] Python 3.x is the "next generation" Python but for astronomy analysis
       Python 2.x is still the best choice.

Astro: required
^^^^^^^^^^^^^^^^^^

- `asciitable`_ >= 0.5.0
- `pyfits`_ >= 2.3.0
- `pywcs <https://trac6.assembla.com/astrolib>`_ >= 1.9 ()
- `ATpy`_ >= 0.9.4
- `APLpy`_ >= 0.9.5 (pyparsing, pyregion, PIL, montage are optional but useful)

Astro: useful
^^^^^^^^^^^^^^

- `coords <https://trac6.assembla.com/astrolib>`_
- `vo.table <https://trac6.assembla.com/astrolib>`_
- `pyparsing <http://pyparsing.wikispaces.com/>`_
- `pyregion <http://leejjoon.github.com/pyregion/>`_
- `PIL <http://www.pythonware.com/products/pil>`_
- `Montage <http://montage.ipac.caltech.edu/>`_ (compiled application and library)

.. _installation_test:

Tests
^^^^^^^^^^

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

**Google**

Google "python blah blah" or "python astronomy blah blah"

**Resource lists**

There are a number of sites specifically devoted to Python for astronomy with
organized lists of useful resources and packages.

  - `Astropython.org resources <http://www.astropython.org/resources>`_
  - `Comfort at 1 AU
    <http://oneau.wordpress.com/2010/10/02/python-for-astronomy/>`_
  - `Astronomical Python <http://www.astro.washington.edu/users/rowen/AstroPy.html>`_

**PyPI**

The `Python Package Index <http://pypi.python.org/pypi>`_ is the main
repository for 3rd party Python packages (about 14000 packages and growing).
An increasing number of `astronomy related packages
<http://pypi.python.org/pypi?:action=browse&show=all&c=385&c=387>`_
are available on PyPI, but this list misses a lot of available options.

The advantage of being on PyPI is the ease of installation using
``easy_install <package_name>``.  

.. admonition:: Exercise: Find packages for coordinate manipulations

  Find one or more Python packages that will transform coordinates from Galactic to FK5 ecliptic.
  
  *Hint*: tags are helpful at astropython.org and don't forget the "next" button at
  the bottom.

Package installation
^^^^^^^^^^^^^^^^^^^^

There are two standard methods for installing a package. 

**Easy_install**

The ``easy_install`` script is available within our scientific Python
installation and is very easy to use (when it works).  During the installation
process you already saw many examples of ``easy_install`` in action.  Features include:

  - If supplied with a package name then it will query the PyPI site to find out about
    that package.  Assuming the package is there then ``easy_install`` will
    automatically download and install the package.  
  - Will accept a local tar file (assuming it contains an installable Python package) or a URL
    pointing to a tar file.
  - Can install in the user package area via ``easy_install <package or URL>
    --user`` (see discussion further down)

**python setup.py install**

Some packages may fail to install via ``easy_install``.  Most often there will
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

**What to do if these don't work**

If you attempt to install a package with these methods but it does not work,
your basic options are:

  - Dig in your heels and start reading the error messages to see why it is
    unhappy.  Often when you find a specific message it's time to start
    googling by pasting in the relevant parts of the message.
  - Send an email to the pythonusers mailing list.  Include: 

      - Package you are trying to install
      - URL for downloading the package tar file
      - Your platform (machine architecture and exact OS version)
      - Exactly what you typed
      - Entire output from the ``python setup.py install`` process

    Do NOT write and say "I tried to install BLAH and it failed, can 
    someone help?"
  
Where to packages get installed?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An important option in the installation process is where to put the package
files.  We've seen the ``--user`` option in ``easy_install`` and ``python
setup.py install``.  What's up with that?

WITH ``--user``
################

This option is generally a good idea and will work in all cases.  Packages get
installed in a local user-owned directory when you do something like either of
the following::

  easy_install --user asciitable 
  python setup.py install --user

.. warning::
   If you installed Python with a distribution *other* than EPD, then you might get an error using
   ``easy_install --user``.  There is an older (deprecated) version of easy_install
   in some Python distributions which does not support ``--user``.  You should be able 
   to get the latest ``easy_install`` with::

     easy_install distribute  # maybe need "sudo" in front

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

.. Note::
   As a side benefit of always installing with ``--user``, if you use multiple
   Python installations (for instance PyRaf, CASA, and CIAO), *each* of those will
   provide its own version of Python which is essentially its own universe as far
   as packages.  The only reliable way to make a package available to all of them
   at once is to install with ``--user``.  (There are limitations even in this
   case, for instance Python 2.6 will not always play with Python 2.7).

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

There is no simple way to do this.  (Python community is working on this one).


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


