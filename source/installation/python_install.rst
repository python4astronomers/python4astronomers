:tocdepth: 2

.. _`installing_scientific_python`:

Installing Scientific Python 
==============================================

Unless you are confident with (and enjoy) tracking down compiler errors and
other issues related to package incompatibilities, we strongly recommend using
a pre-built binary Python distribution.  For MacOS in particular there are a
whole slew of options for Python which don't play well together.  Even if you
already have an installation on your system you will probably save time in
the long run by starting fresh with a binary Python distribution.  There are
two main options that we have experience installing:

**Enthought Python Distribution**

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

**ActiveState Community Python Distribution**

A second option is to use the `ActiveState Community Python Distribution
<http://www.activestate.com/activepython/downloads>`_, 
a.k.a. ActivePython.  This has no license requirements and is freely
available.  Features of ActivePython include:

- The initial distribution is much smaller, consisting mostly of Python and
  some utilities.  
- Packages can be added with a customized package manager ``pypm`` toolf which
  installs from the `ActiveState PyPM repository <http://code.activestate.com/pypm/>`_.  This
  handles the "difficult" packages like NumPy and SciPy with support for
  dependency resolution, and also includes most packages from `PyPI <pypi.python.org>`_.

Two tests of installing ActivePython on MacOS (snow leopard) and a linux
CentOS-5 system were successful and were simple to perform.  Although we don't
provide detailed instructions here, this option seems to be reasonable.

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

- MacOSX: Follow `the MacOS instructions <http://support.apple.com/kb/ht3696>`_
- Linux: Type ``uname -mpi`` at the command line.  If you see ``x86_64 x86_64
  x86_64`` you have a 64-bit machine and OS.  If you see one or more ``i686``
  or ``i386`` you are running a 32-bit OS.
- Windows:  Follow `the Windows instructions 
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

.. .. toctree::
   :maxdepth: 1
   
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


.. include:: ../references.rst
