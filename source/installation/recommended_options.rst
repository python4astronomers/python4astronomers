.. _recommended_options:

Recommended installation options
================================

Summary of options
----------------------------

The table below lists other recommended options for installing scientific
Python.  These options have different features and different strengths, but all of them
are known to be well-supported and expected to work well.

This list includes both root-level package managers like RPM or MacPorts (for which Python
is just a small part of their content) along with a number of good distributions that
essentially just include Python and associated Python packages.

====================  ========  =========  =========  ======================
Distribution            Mac      Linux      Windows    Notes
====================  ========  =========  =========  ======================
Anaconda                  Y         Y          Y       [1]_
MacPorts                  Y        --         --       [2]_
Homebrew                  Y        --         --       [3]_
RPM, APT                 --         Y         --       [4]_
ActiveState CE            Y         Y          Y       [5]_
Enthought Canopy          Y         Y          Y       [6]_, [7]_
STSci_Python              Y        [8]_        Y       [9]_,
yt Project                Y         Y         --       [10]_
====================  ========  =========  =========  ======================

.. rubric:: Notes

.. raw:: html

   <span style="font-size: small">

.. [1] **Anaconda** is one of the easiest and fastest ways to
   install a full scientific Python stack.  See the section
   :ref:`anaconda_option` for details.

.. [2] **MacPorts** has the best built-in support for Python and
   is generally stable after Mac OS system or security updates.
   MacPorts has the drawback of being slow to install so that it can
   take several hours to build a working Python distribution.

.. [3] **Homebrew** is a simpler and faster solution for Mac but does
   not include Python packages and uses the MacOS libraries instead
   of building them separately.  It has been reported that
   MacOS system updates can break homebrew packages, but many people
   successfully use this system.

.. [4] **Linux package managers**:
   For recent versions of linux distributions like Ubuntu, the
   installed Python and supporting packages available through the
   package manager will be sufficiently current to support science
   analysis.  For a linux distribution like CentOS-5 this is not the
   case.  *This option requires root privilege.*

.. [5] **ActivePython**: The `ActiveState Community Python Distribution
   <http://www.activestate.com/activepython/downloads>`_, has no
   license requirements and is freely available.  It features a
   package manager tool which installs from the `ActiveState PyPM
   repository <http://code.activestate.com/pypm/>`_.  It handles the
   "difficult" packages like PyQt and SciPy with support for
   dependency resolution, and also includes most packages from `PyPI
   <pypi.python.org>`_.

.. [6] **Enthought Canopy**:
   The `Enthought Canopy <https://www.enthought.com/products/canopy/>`_
   environment is a bundled
   binary distribution of Python with a large set of useful packages
   built in.  There is also a bundled editor and GUI package manager.
   The full version of Canopy requires a paid subscription, but it
   is free for use by students or employees of a degree-granting institution
   (see `license details <https://www.enthought.com/products/canopy/academic/license>`_).

.. [7] **Enthought Canopy Express** is the free version and it has a useful subset of
   packages including NumPy, SciPy, Matplotlib, IPython, Traits, and Chaco.  It is
   available in 32-bit for Mac and Windows and 64-bit for Linux.  Qt and PyQt are *not*
   available.  These are GUI toolkits which are used by a number of useful applications,
   in particular the IPython Qt console.

.. [8] Available only as a source install on Linux.

.. [9] The `STSci_Python distribution
   <http://www.stsci.edu/institute/software_hardware/pyraf/stsci_python>`_
   provides `PyRAF <http://www.stsci.edu/institute/software_hardware/pyraf>`_,
   various analysis packages, and the core NumPy, SciPy, and Matplotlib packages.
   Qt and PyQt are not included.

.. [10] Provides NumPy, Matplotlib, HDF5, and `yt <http://yt-project.org/>` 
   (astrophysical simulation analysis).  See `Installing yt
   <http://yt-project.org/doc/orientation/installing.html>`_.

.. raw:: html

   </span>


Details for specific options
-----------------------------

The following two topic pages go into a bit more detail for MacOS and linux options that
do not use a standalone Python distribution installer:

.. toctree::
   :maxdepth: 1

   macosx
   linux

