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
Academic version of EPD is free for use by students or employees of a
degree-granting institution (i.e. Harvard but not SAO).  

*By special permission
from Enthought, all tutorial participants have permission use the Academic EPD
downloads we are providing.*

However, do not distribute these files to others
without express permission.

Installation
------------

The installation process is particular to each platform:

.. toctree::
   :maxdepth: 2
   
   macosx
   linux-self
   linux-network
   package-basics
