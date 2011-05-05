.. include:: ../references.rst

.. _`Aladin`: http://aladin.u-strasbg.fr/

Installation
============

In addition to Scientific Python packages like numpy, and modules
installed for preceding classes (asciitable, atpy, aplpy, vo), the
following modules should be installed for this class::  

    easy_install -U sampy
    easy_install -U https://github.com/python4vo/coatpy/tarball/master

COATPy
------

We have provided this "Collection of Online Astronomy Tools" for the
purposes of this workshop. The `COATPy`_ package wraps up a number (2
presently) other modules that exist but lack a turnkey installation:
`vaods9`_ and `pyvolib`_. We will see how these tools are used in

.. note:: COATPy as a standalone module should be considered 
    alpha-ware and its content and wrapping of the underlying 
    packages may change in the near term.
    
SAMPy 
-----

`SAMPy`_ is a python library that provides a connector between the
python command line interface and other desktop applications such as
`ds9`_, `TOPCAT`_ or `Aladin`_. Planned functionality also includes
direct interfacing between python and your desktop browser. For this
workshop we will use a higher level wrapper to SAMPy ().