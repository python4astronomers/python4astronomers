.. include:: ../references.rst

.. _python_requirements:

Python requirements
====================

In order to follow along with the examples to be presented in the workshops
your must have at least the following installed in your working environment.

Core
----

- Python 2.6 or 2.7 [#]_
- IPython >= 0.10
- NumPy >= 1.3
- SciPy >= 0.7.2
- Matplotlib >= 0.99
- setuptools >= 0.6c11

Astro: required
---------------

- `asciitable`_ >= 0.5.0
- `pyfits`_ >= 2.3.0
- `pywcs <https://trac6.assembla.com/astrolib>`_ >= 1.9 ()
- `ATpy`_ >= 0.9.4
- `APLpy`_ >= 0.9.5 (pyparsing, pyregion, PIL, montage are optional but useful)

Astro: useful
-------------

- `coords <https://trac6.assembla.com/astrolib>`_
- `vo.table <https://trac6.assembla.com/astrolib>`_
- `pyparsing <http://pyparsing.wikispaces.com/>`_
- `pyregion <http://leejjoon.github.com/pyregion/>`_
- `PIL <http://www.pythonware.com/products/pil>`_
- `Montage <http://montage.ipac.caltech.edu/>`_ (compiled application and library)

Test
-----

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

The to check the other required packages do the following from within ipython::

  import asciitable
  import pyfits
  import pywcs
  import atpy
  import aplpy


.. [#] Python 3.x is the "next generation" Python but for astronomy analysis
       Python 2.x is still the best choice.
       
