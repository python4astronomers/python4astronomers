:tocdepth: 2

.. _`installing_scientific_python`:

Installing Scientific Python 
==============================================

Unless you enjoy tracking down compiler errors and other issues related to
package incompatibilities, we recommend using a pre-built binary Python
distribution.  For MacOS in particular there are a whole slew of options for
Python which don't play well together.  Even if you already have an
installation on your system you will probably save time in the long run by
starting fresh with a binary Python distribution.

Choosing your distribution
-----------------------------

The table below lists the recommended options for installing
scientific Python.  Note that there are *many* other installation
options, but these cover the ones which are well-supported and likely
to present the fewest problems.

Anaconda: The easiest and fastest solution
-------------------------------------------

The fastest way to get a basic Python installation up and running is
`Anaconda <https://store.continuum.io/cshop/anaconda>`_
Click on that link and download the installer (using the button marked
``free`` on the top right of the page). It will ask you for your email
and then you get an installer for your OS (Mac, Linux, or Windows).
Read `64 versus 32 bit`_ if you aren't sure if your CPU is 64-bit.

By default Anaconda is installed into your home directory (no root acress
required), but you can pick another location if you wish.
To use the Anaconda python installation, simply add that directory to your
path (instructions on the Anaconda page).

Anaconda includes the usual `core scientific packages
<http://docs.continuum.io/anaconda/pkgs.html>`_ and some interesting
next-generation packages `Numba <http://numba.pydata.org/numba-doc/0.6/index.html>`_ and `Blaze <http://continuum.io/blog/blaze>`_.
Also, Anaconda is the only packed installation so far that comes bundeled
with Astropy.

After you set up Anaconda, you should install one more astromy package, 
that you are likely to use. Use the following commands::

  pip install --upgrade aplpy

Now, you are done, your python should be up and running and can skip the 
rest of this page.

.. note::

   Installing Anaconda, you will probably have more than one python
   installation on your computer, e.g. a python included in the OS,
   Anaconda plus possible CASA or Sherpa. In general, that is not a problem.
   It also protects you from screwing up your system, should anything
   go wrong when you install additional packages. See :ref:`multiple-pythons`
   for more information.

Alternatives to Anaconda
-------------------------

Anaconda is not the only binary package available; alternatives are EPD,
ActiveState and STSci_Python (see table below for details). They work in a
similar way, but have more restrictive licenses (EPD) or less complete
package lists.
Notable is the `STSci_Python distribution 
<http://www.stsci.edu/institute/software_hardware/pyraf/stsci_python>`_
becaue it provides `PyRAF <http://www.stsci.edu/institute/software_hardware/pyraf>`_, as well as various analysis packages, and the core NumPy, SciPy, and Matplotlib packages. Howeverm the GUIs Qt and PyQt are not included.
Use your prefered internet search engine, if you need EPD or AcitveState python.


The second option is to use a package manager like RPM or APT on Linux and
MacPorts or HomeBrew on Macs. Many of the packages we need are available
in those package mangers; they are complied to work with your system python.


=====================  ========  =========  =========  ====================== 
Distribution             Mac      Linux      Windows    Notes
=====================  ========  =========  =========  ====================== 
MacPorts                   Y        --         --       [1]_
Linux Package Manager     --         Y         --       [2]_
=====================  ========  =========  =========  ======================

The last option is to compile everything from source. While possible, this
is beyond the scope of this introduction.

.. rubric:: Notes

.. raw:: html

   <span style="font-size: small">

.. [1] **MacPorts** has the best built-in support for Python and
   is generally stable after Mac OS system or security updates.
   MacPorts has the drawback of being slow to install so that it can
   take several hours to build a working Python distribution. 
  
.. [2] **Linux package managers**: 
   For recent versions of linux distributions like Ubuntu, the
   installed Python and supporting packages available through the
   package manager will be sufficiently current to support science
   analysis.  For a linux distribution like CentOS-5 this is not the
   case.  *This option requires root privilege.*


.. raw:: html

   </span>

Installation steps
^^^^^^^^^^^^^^^^^^^

In order to follow along with the examples to be presented in the workshops
your Python installation will need to meet the :ref:`python_pkg_requirements`.  The aim
of this workshop is to get this set up correctly.  This will proceed in three
steps:

- Install the core Python installation 
- Install additional packages which are used in the workshops
- Test the installation

The installation process is particular to each platform.  For some options you
will need to choose between 32-bit and 64-bit installations.  Generally
speaking you should choose 64-bit, but read `64 versus 32 bit`_ for some
caveats or if you aren't sure if your CPU is 64-bit.

Install core Python
^^^^^^^^^^^^^^^^^^^

.. toctree::
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

If you experience problems with installation for any of these packages you can
send an email to the `astropy mailing list
<http://mail.scipy.org/mailman/listinfo/astropy>`_.

MacOS or root linux install
############################
::

  sudo easy_install --upgrade pip
  sudo pip install --upgrade distribute
  sudo pip install --upgrade astropy
  sudo pip install --upgrade aplpy
  sudo pip install --upgrade pyregion
  sudo pip install --upgrade pyparsing
  sudo pip install --upgrade atpy


Non-root linux
############################
::

  easy_install --upgrade pip
  pip install --upgrade distribute
  pip install --upgrade astropy
  pip install --upgrade aplpy
  pip install --upgrade pyregion
  pip install --upgrade pyparsing
  pip install --upgrade atpy


Windows
############################

For Windows XP 32-bit the following are known to have problems: pywcs,
pyregion, and coords.
::

  cd C:\Python27\Scripts
  easy_install.exe --upgrade pip
  pip.exe install --upgrade distribute
  pip.exe install --upgrade astropy
  pip.exe install --upgrade aplpy  
  pip.exe install --upgrade pyregion
  pip.exe install --upgrade pyparsing
  pip.ext install --upgrade aty


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
  % ipython --pylab
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

  import astropy
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
  ipython --pylab

.. tip::
   For all of the workshops you should always start Python using the command::
   
     ipython --pylab  # (for Windows start the Pylab application)

   This will automatically load all of the main plotting functions from
   `Matplotlib`_ (e.g. ``plot()``, ``hist()``, and many more) as well as common
   math functions and array utilities from `NumPy`_ (e.g. ``sin()``, ``exp()``,
   ``array()``, etc).

   In my ``~/.cshrc`` file I define an alias that I commonly use::

     alias pylab "ipython --pylab"


.. admonition:: Exercise: Read a table and examine it
  
  Look at the documentation for the `astropy.Table.read() 
  <http://docs.astropy.org/en/v0.2.1/table/io.html>`_ function in
  `astropy`_.  Follow the very first example and use the ``read()`` function
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

64 versus 32 bit
-----------------

For several of the binary installers you need to make a decision: 32-bit or
64-bit download?  First you need to establish whether your computer has a
32-bit or 64-bit processor.  If you have a 32-bit processor then your decision
is easy (32-bit) but if you have a 64-bit processor then either 32 or 64 will
work.  See below if you don't know your processor architecture:

- MacOSX: Follow `the MacOS instructions <http://support.apple.com/kb/ht3696>`_
- Linux: Type ``uname -mpi`` at the command line.  If you see ``x86_64 x86_64
  x86_64`` you have a 64-bit machine and OS.  If you see one or more ``i686``
  or ``i386`` you are running a 32-bit OS.
- Windows:  Follow `the Windows instructions 
  <http://windows.microsoft.com/en-US/windows-vista/32-bit-and-64-bit-Windows-frequently-asked-questions>`_.


.. include:: ../references.rst
