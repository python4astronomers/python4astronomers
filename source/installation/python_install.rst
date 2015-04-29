:tocdepth: 2

.. _`installing_scientific_python`:

Installing Scientific Python
==============================================

The aim of this workshop is to get you set up with a working scientific Python
installation which meets the :ref:`python_pkg_requirements`.  This will proceed
in four steps:

- `Install core Python`_
- `Install additional packages`_
- `Test the installation`_
- `Take your Python for a spin!`_

The installation process is particular to each operating system and platform.
You may need to choose between 32-bit and 64-bit installations.  Generally
speaking you should choose 64-bit, but read `64 versus 32 bit`_ for some caveats
or if you aren't sure if your CPU is 64-bit.

For this workshop you can use either Python 2.6, 2.7 or Python 3 (version >=
3.3).  On the general question of whether to use Python 2 or Python 3, at this
point the major package support for both is quite similar, and (as of
early 2015) it appears that in the overall community Python 3 usage is
becoming substantial.

.. _`anaconda_option`:

Install core Python
--------------------

Unless you enjoy tracking down compiler errors and other issues related to
package incompatibilities, we recommend using a pre-built binary Python
distribution.  Even if you already have an installation on your system you will
probably save time in the long run by starting fresh with a binary Python
distribution.

**Anaconda: an easy and fast option**

On of the fastest way to get a basic Python installation up and running is
`Anaconda <http://continuum.io/downloads>`_.
Click on that link and download the installer (using the button marked
``free`` on the top right of the page). It will ask you for your email
and then you get an installer for your OS (Mac, Linux, or Windows).
Read `64 versus 32 bit`_ if you aren't sure if your CPU is 64-bit.

By default Anaconda is installed into your home directory (no root access
required), but you can pick another location if you wish.
To use the Anaconda python installation, simply add that directory to your
path, following the instructions on the Anaconda page.

Anaconda includes the usual `core scientific packages
<http://docs.continuum.io/anaconda/pkgs.html>`_ (including `astropy
<http://astropy.org>`_), and some interesting next-generation packages `Numba
<http://numba.pydata.org/>`_ and `Blaze
<http://blaze.pydata.org>`_.

.. note::

   After installing Anaconda, you will probably have more than one Python
   installation on your computer, e.g. a Python included in the OS,
   Anaconda plus possible CASA or CIAO/Sherpa. In general that is not a problem,
   but see :ref:`multiple-pythons` for more information on managing this situation.

**Alternate options**

There are a number of :ref:`recommended_options` besides Anaconda, and you are
encouraged to explore these options and decide what might be right for you.
This includes the use of system package managers like MacPorts or linux RPM.
Each of the other options has different features and strengths, and no single
solution works for everybody.


Install additional packages
-----------------------------


After you set up your core Python installation, you should install a few more
packages that are used in the tutorials.  Copy and paste the lines below one at
a time, checking that each one works.  The program outputs may contain various
"warnings", but watch for "errors" and look at the end to see if a successful
installation was reported.
::

  pip install --upgrade astropy  # NOT required for Anaconda
  pip install --upgrade aplpy
  pip install --upgrade pyregion
  pip install --upgrade pyparsing

Note that if you have used a root-installation option like MacPorts or a linux
package manager to install Python, then you will need to use the ``sudo`` prefix
in each of these commands, e.g.::

  sudo pip install --upgrade aplpy

If you experience problems with installation for any of these packages you can
send an email to the `astropy mailing list
<http://mail.scipy.org/mailman/listinfo/astropy>`_.


.. _installation_test:

Test the installation
-----------------------

To do a very basic test whether you meet the requirements and have a functioning
core scientific Python installation, do the following and check version numbers::

  $ python -V
  $ ipython -V
  $ ipython --matplotlib
  import numpy
  import scipy
  import scipy.linalg
  import matplotlib.pyplot as plt

  print(numpy.__version__)
  print(scipy.__version__)
  print(matplotlib.__version__)

  x = numpy.linspace(0, 20, 100)
  plt.plot(x, sin(x))
  print(scipy.linalg.eig([[1,2],[3,4]]))

The commands above should succeed with no errors.  The version numbers should
meet the requirements, and finally you should see a plot of a sine wave.

To check the other required packages, do the following from within ipython::

  import astropy
  import aplpy
  import pyregion
  import pyparsing


Take your Python for a spin!
-------------------------------

If you are following along with the Python for Astronomers tutorial and have
finished installing Python, you can give a real test drive now.

First download the :download:`install_examples.tar <../downloads/install_examples.tar>` file which has example data
files that will be used in subsequent exercises.
Then change to a working directory, untar the file, and start up IPython::

  $ tar xvf ~/Downloads/install_examples.tar   # or wherever your browser puts downloads
  $ cd py4ast/install
  $ ls
  $ ipython --matplotlib

.. tip::
   For all of the workshops you should always start Python using the shell command::

     $ ipython --matplotlib  # (for Windows start the Pylab application)

   Once IPython has started, make numpy and matplotlib available with::

     import numpy as np
     import matplotlib.pyplot as plt

.. admonition:: Exercise: Read a table and examine it

  Look at the documentation for the `astropy.Table.read()
  <http://docs.astropy.org/en/stable/io/ascii/index.html>`_ function in
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

  Optional: use the `plot
  <http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot>`_
  and `hist
  <http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.hist>`_
  functions to examine the data graphically.  For instance plot RAdeg versus
  DEdeg.  Look at the ``table1.dat`` file itself for detailed column
  descriptions.


Appendix
----------

64 versus 32 bit
^^^^^^^^^^^^^^^^^

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

Details for specific options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following two topic pages go into a bit more detail for MacOS and linux options that
do not use a standalone Python distribution installer:

.. toctree::
   :maxdepth: 1

   macosx
   linux

