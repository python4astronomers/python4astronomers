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

Python requirements
-----------------------

In order to follow along with the examples to be presented in the workshops
your must have at least the following installed in your working environment.
Once you have followed the installation instructions in the next section for
your platform then run the tests below to see if everything is OK.

Core
^^^^^

- Python 2.6 or 2.7 [#]_
- IPython >= 0.10
- NumPy >= 1.3
- SciPy >= 0.7.2
- Matplotlib >= 0.99
- setuptools >= 0.6c11

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

Test
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

To check the other required packages do the following from within ipython::

  import asciitable
  import pyfits
  import pywcs
  import atpy
  import aplpy


.. [#] Python 3.x is the "next generation" Python but for astronomy analysis
       Python 2.x is still the best choice.

Installation
------------

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
