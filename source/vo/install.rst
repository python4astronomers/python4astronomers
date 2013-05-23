.. include:: ../references.rst

.. _`Aladin`: http://aladin.u-strasbg.fr/

Modules
=======

This class assumes that you have have installed Scientific Python packages
such as numpy, as well as the :ref:`astro-required` modules used in preceding
classes (e.g., `ATpy`_, `APLpy`_, etc). In addition the
following modules should be installed for this class (may require sudo)::

    easy_install http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz
    easy_install sampy
    easy_install https://github.com/python4vo/coatpy/tarball/master
     
COATPy
------

.. sidebar:: COATPy is alphaware

    COATPy as a standalone module should be considered 
    alpha-ware and its content and wrapping of the underlying 
    packages may change in the near term.
    
We have provided this "Collection of Online Astronomy Tools" for the
purposes of this workshop. The `COATPy`_ package wraps up a number (2
presently) other modules that exist but lack turnkey installation:

* `pyvolib`_ 
   - author: Shui Hung Kwok
   - comment:  an updated version of the python software used in 
     past virtual observatory summer schools.
* `vaods9`_ 
    - author: Omar Laurino, SAO/VAO
    - comment:  a wrapper to the `SAMPy`_ interface for sending messages, 
      including "xpa"-like commands, between python and ds9.
    - `documentation <http://python4vo.github.com/vaods9/>`_


SAMPy 
-----

`SAMPy`_ is a python library that provides a connector between the
python command line interface and other desktop applications such as
`ds9`_, `TOPCAT`_ or `Aladin`_. 

.. Other Modules
.. -------------
.. 
.. This is a simple summary of other python modules for online astronomy and
.. virtual observatory.
.. 
.. AstroGrid Python
.. ^^^^^^^^^^^^^^^^
.. 
.. The AstroGrid project created a stand alone desktop tool `VODesktop
.. <http://www.astrogrid.org/wiki/Help/IntroVODesktop>`_ for finding and using
.. web based VO resources. A companion python module, `astrogrid
.. <http://pypi.python.org/pypi/astrogrid/1.0.4>`_ permits the same kinds of
.. queries to be performed programmatically. *VODesktop* has to be running along
.. side python because the ``astrogrid`` module is simply passing the queries off
.. to the engine in the desktop tool. It is known to work in Python 2.4 and 2.5
.. but there are packaging issues for installing it in Python 2.6 or later.
.. 
.. Telarchive / fetchdss
.. ^^^^^^^^^^^^^^^^^^^^^^
.. 
.. `Peter Erwin <http://www.mpe.mpg.de/~erwin/>`_ wrote this `pair of packages
.. <http://www.mpe.mpg.de/~erwin/code/index.html>`_ for querying remote telescope
.. archives to ascertain the existence of data in that archive at a particular
.. place on the sky (telarchive) or download SDSS images (fetchdss). They can be
.. installed directly (may required sudo)::
.. 
..     easy_install http://www.mpe.mpg.de/~erwin/code/telarchive/telarchive-1.6.2.tar.gz
..     easy_install http://www.mpe.mpg.de/~erwin/code/telarchive/fetchsdss-1.0.2.tar.gz
.. 
.. The documentation focuses on using the executable files, ``dosearch.py`` and
.. ``do_fetchsdss.py``, from the command line shell though the internal modules
.. in principle could be use inside other python scripts.
..                                                           








