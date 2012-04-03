:tocdepth: 2

.. _`installing_scientific_python`:

Installing Scientific Python 
==============================================

Unless you are enjoy tracking down compiler errors and other issues related to
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


.. admonition:: For the completely impatient

  The fastest way to get a basic Python installation up and running is
  `EPD Academic <http://www.enthought.com/products/edudownload.php>`_ if you
  meet these `license terms
  <http://www.enthought.com/EPDAcademicTerms.html>`_ or `EPD Free
  <http://www.enthought.com/products/epd_free.php>`_ otherwise.  Click on that
  link, download the installer and then go to the `Install core Python`_
  section and click on the link for your OS (Mac, Linux, or Windows).
  
====================  ========  =========  =========  ====================== 
Distribution            Mac      Linux      Windows    Notes
====================  ========  =========  =========  ====================== 
MacPorts                  Y        --         --       [1]_
Homebrew                  Y        --         --       [2]_
RPM, APT                 --         Y         --       [3]_
EPD Academic              Y         Y          Y       [4]_, [5]_
ActiveState CE            Y	    Y          Y       [6]_
EPD Free                  Y         Y          Y       [7]_, [8]_, [9]_
STSci_Python              Y       [10]_        Y       [11]_
====================  ========  =========  =========  ======================

.. rubric:: Notes

.. raw:: html

   <span style="font-size: small">

.. [1] **MacPorts** has the best built-in support for Python and
   is generally stable after Mac OS system or security updates.
   MacPorts has the drawback of being slow to install so that it can
   take several hours to build a working Python distribution. 

.. [2] **Homebrew** is a simpler and faster solution for Mac but does
   not include Python packages and uses the MacOS libraries instead
   of building them separately.  It has been reported that 
   MacOS system updates can break homebrew packages, but many people
   successfully use this system.
  
.. [3] **Linux package managers**: 
   For recent versions of linux distributions like Ubuntu, the
   installed Python and supporting packages available through the
   package manager will be sufficiently current to support science
   analysis.  For a linux distribution like CentOS-5 this is not the
   case.  *This option requires root privilege.*

.. [4] **EPD**: 
   The `Enthought Python Distribution
   <http://www.enthought.com/products/epd.php>`_ is a bundled
   binary distribution of Python with a large set of useful packages
   built in.  This is the **simplest option for academics**.

.. [5] The EPD `Academic version
   <http://www.enthought.com/products/edudownload.php>`_ is a full
   version of EPD that is free
   for use by students or employees of a degree-granting institution as
   specified in the `license terms
   <http://www.enthought.com/EPDAcademicTerms.html>`_.

.. [6] **ActivePython**: The `ActiveState Community Python Distribution
   <http://www.activestate.com/activepython/downloads>`_, has no
   license requirements and is freely available.  It features a 
   package manager tool which installs from the `ActiveState PyPM
   repository <http://code.activestate.com/pypm/>`_.  It handles the
   "difficult" packages like PyQt and SciPy with support for
   dependency resolution, and also includes most packages from `PyPI
   <pypi.python.org>`_.

.. [7] Available only in 32-bit for Mac and Windows.

.. [8] The EPD `Free version
   <http://www.enthought.com/products/epd_free.php>`_  provides
   NumPy, SciPy, Matplotlib, IPython, Traits, and Chaco, 

.. [9] Qt and PyQt *not* available.  
   These are GUI toolkits which are used by a number of useful
   applications, in particular the IPython Qt console.

.. [10] Available only as a source install on Linux.

.. [11] The `STSci_Python distribution 
   <http://www.stsci.edu/institute/software_hardware/pyraf/stsci_python>`_
   provides `PyRAF <http://www.stsci.edu/institute/software_hardware/pyraf>`_,
   various analysis packages, and the core NumPy, SciPy, and Matplotlib packages.
   Qt and PyQt are not included.

.. raw:: html

   </span>

Installation steps
--------------------

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

Now install EPD as the core Python on your system following the instructions below:

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
  sudo pip install --upgrade asciitable
  sudo pip install --upgrade pyfits
  sudo pip install --upgrade pywcs
  sudo pip install --upgrade atpy
  sudo pip install --upgrade aplpy
  sudo pip install --upgrade pyregion
  sudo pip install --upgrade pyparsing
  sudo pip install --upgrade http://stsdas.stsci.edu/astrolib/vo-0.7.2.tar.gz
  sudo pip install --upgrade http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz

Non-root linux
############################
::

  easy_install --upgrade pip
  pip install --upgrade distribute
  pip install --upgrade asciitable
  pip install --upgrade pyfits
  pip install --upgrade pywcs
  pip install --upgrade atpy
  pip install --upgrade aplpy
  pip install --upgrade pyregion
  pip install --upgrade pyparsing
  pip install --upgrade http://stsdas.stsci.edu/astrolib/vo-0.7.2.tar.gz
  pip install --upgrade http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz

Windows
############################

For Windows XP 32-bit the following are known to have problems: pywcs,
pyregion, and coords.
::

  cd C:\Python27\Scripts
  easy_install.exe --upgrade pip
  pip.exe install --upgrade distribute
  pip.exe install --upgrade asciitable
  pip.exe install --upgrade pyfits
  pip.exe install --upgrade pywcs     
  pip.exe install --upgrade atpy
  pip.exe install --upgrade aplpy
  pip.exe install --upgrade pyregion  
  pip.exe install --upgrade pyparsing
  pip.exe install --upgrade http://stsdas.stsci.edu/astrolib/vo-0.7.2.tar.gz
  pip.exe install --upgrade http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz


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

**64-bit**

- *Pro*: Faster for data- and compute-intensive applications
- *Con*: Have to submit an email address and wait for the download link in response

**32-bit**

- *Pro*: Comes with the `Mayavi <http://github.enthought.com/mayavi/mayavi/>`_ 3-d
  rendering package installed while the 64-bit does not (for technical reasons).
  If you are interested in using this cool package you should consider choosing 32-bit.
  Note that the standard matplotlib package supports some `3-d plotting
  <http://matplotlib.sourceforge.net/mpl_toolkits/mplot3d/tutorial.html>`_. 

.. include:: ../references.rst
