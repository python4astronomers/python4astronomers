.. include:: ../references.rst

.. _`Aladin`: http://aladin.u-strasbg.fr/

Installation
============

In addition to Scientific Python packages like numpy, and modules installed
for preceding classes (`asciitable`_, `ATpy`_, `APLpy`_, vo), the following
modules should be installed for this class::

    easy_install -U sampy
    easy_install -U https://github.com/python4vo/coatpy/tarball/master

COATPy
------

We have provided this "Collection of Online Astronomy Tools" for the
purposes of this workshop. The `COATPy`_ package wraps up a number (2
presently) other modules that exist but lack turnkey installation:

* `pyvolib`_ 
   - author: Shui Hung Kwok
   - comment:  an updated version of the python software used in past virtual observatory summer schools.
* `vaods9`_ 
    - author: Omar Laurino, SAO/VAO
    - comment:  a wrapper to the SAMPy interface for making private calls between python and ds9.


We will see how these tools are used in

.. note:: COATPy as a standalone module should be considered 
    alpha-ware and its content and wrapping of the underlying 
    packages may change in the near term.
    
SAMPy 
-----

`SAMPy`_ is a python library that provides a connector between the
python command line interface and other desktop applications such as
`ds9`_, `TOPCAT`_ or `Aladin`_. 