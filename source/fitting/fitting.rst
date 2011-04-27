.. include:: ../references.rst

.. _`sherpa-4.3.0-EPD-7.0-i386.dmg`: http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa-4.3.0-EPD-7.0-i386.dmg
.. _`sherpa-4.3.0-EPD-7.0-x86_64.dmg`: http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa-4.3.0-EPD-7.0-x86_64.dmg
.. _`sherpa-4.3.0-EPD-7.0-linux-x86_64.egg`: http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa-4.3.0-EPD-7.0-linux-x86_64.egg
.. _`sherpa-4.3.0-EPD-7.0-linux-x86.egg`: http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa-4.3.0-EPD-7.0-linux-x86.egg
.. _`sherpa-4.3.0-py2.6-rh5-x86_64.egg`: http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa-4.3.0-py2.6-rh5-x86_64.egg

.. Python4Astronomers documentation file



Fitting and modeling data
=========================

Setup
-----

In order to follow along with the Sherpa examples presented in the workshop on
April 29, your Python installation will need the following dependencies and
Sherpa version 4.3.0.

- Sherpa Dependencies

  - Python 2.6 or 2.7 (not Python 3.x)
  - NumPy >= 1.3
  - Matplotlib >= 0.99
  - pyFITS >= 1.3
  - DS9 >= 5

.. Note::
  EPD users, you have already satisfied the installation requirements
  above.  Continue with the installation Notes below.  If you have been to
  previous workshops and are able to complete the examples, your installation is
  most likely sufficient.  See the Sherpa installation notes below to install
  Sherpa version 4.3.0.


Users Interested in Maintaining their own Python Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Built Python binaries of Sherpa can be found here

- `Download Sherpa <http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/>`_:
  Sherpa binaries for Mac and Ubuntu


Install Notes for EPD Mac Users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install the Enthought EPD 7.0 at `EPD downloads <http://cxc.cfa.harvard.edu/contrib/python4astronomers>`_

  `Enthought <http://www.enthought.com>`_ is the company which leads most of the
  development of `NumPy`_ and `SciPy`_.  They provide a bundled binary
  distribution of Python with a large set of useful packages built in.  The
  `Academic version <http://www.enthought.com/products/edudownload.php>`_ of EPD
  is free for use by students or employees of a degree-granting institution
  (i.e. Harvard but not SAO) as specified in the `license terms
  <http://www.enthought.com/EPDAcademicTerms.html>`_.

  *By special permission from Enthought, all tutorial participants are allowed
  use the Academic EPD downloads we are providing.*

  However, please do not distribute these files to others without express
  permission.  The user name and password were emailed to the pythonusers
  mailing list on March 18.


Download the appropriate Sherpa disk image for your version of OSX

  ===================  ===========================  ===================================
  OSX                  EPD disk image               Sherpa disk image
  ===================  ===========================  ===================================
  Leopard 10.5         epd-7.0-2-macosx-i386.dmg    `sherpa-4.3.0-EPD-7.0-i386.dmg`_
  Snow Leopard 10.6    epd-7.0-2-macosx-x86_64.dmg  `sherpa-4.3.0-EPD-7.0-x86_64.dmg`_
  ===================  ===========================  ===================================

Double-click on the disk image and follow the instructions in the install wizard.


Install Notes for Ubuntu Users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users who use ``apt-get`` to manage their Python distribution can
download the appropriate Ubuntu package for their operating system.

  - `sherpa_4.3.0-1_amd64.deb
    <http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa_4.3.0-1_amd64.deb>`_
  - `sherpa_4.3.0-1_i386.deb
    <http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa_4.3.0-1_i386.deb>`_

Double-click on the Debian package file (.deb) and follow the instructions in
the install wizard.


Install Notes for EPD Linux Users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install the EPD on Linux by following the instructions `here. <http://python4astronomers.github.com/installation/linux-self.html#user-install-without-root>`_

Download the appropriate Sherpa egg for your Linux architecture

  =====================  ========================  ========================================
  Architecture           EPD Linux installer               Sherpa egg
  =====================  ========================  ========================================
  Linux i686   (32-bit)  epd-7.0-2-rh5-x86.sh      `sherpa-4.3.0-EPD-7.0-linux-x86.egg`_
  Linux x86_64 (64-bit)  epd-7.0-2-rh5-x86_64.sh   `sherpa-4.3.0-EPD-7.0-linux-x86_64.egg`_
  =====================  ========================  ========================================

Install Sherpa into your EPD installation using easy_install::

  easy_install sherpa-4.3.0-EPD-7.0-linux-x86.egg


Install Notes for Linux Users using HEAD network installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Users relying on the Python located in /usr/local/bin accessible from their CfA
HEAD managed Linux machine can install Sherpa as an egg to their own directory

Download the Sherpa egg

`sherpa-4.3.0-py2.6-rh5-x86_64.egg <http://cxc.cfa.harvard.edu/contrib/sherpa/downloads/sherpa-4.3.0-py2.6-rh5-x86_64.egg>`_


Install Sherpa into your own directory using easy_install::

  easy_install --user sherpa-4.3.0-py2.6-rh5-x86_64.egg

.. Note::
   The Sherpa installation includes a number of XSPEC spectral FITS tables, so
   consider storage of ~= 250MB for Sherpa in your home directory.



Try It Out
----------

Try importing the Sherpa high level UI with::

  from sherpa.astro.ui import *

.. Note::
   If you see the following error messages

   WARNING: failed to import sherpa.plot.chips_backend; plotting routines will
   not be available

   WARNING: failed to import sherpa.astro.io; FITS I/O routines will not be available

   Be sure to edit your ~/.sherpa.rc file and indicate

   plot_pkg : pylab

   io_pkg : pyfits

   If you continue to see these messages, you should install pyFITS and 
   matplotlib.

.. Note::
   If you see the following error message, your installation of XSPEC may be
   incomplete.

   WARNING: failed to import sherpa.astro.xspec; XSPEC models will not be
   available

.. Note:: 
   The following error message indicates that Sherpa is unable to find your DS9 or
   XPA.

   WARNING: imaging routines will not be available, failed to import
   sherpa.image.ds9_backend due to 'RuntimeErr: DS9Win unusable: Could not find ds9
   on your PATH'


Classes
-------

Classes definitions include the ``class`` declaration, an identifier, and a
colon::

  class MyClass:
      pass

This class ``MyClass`` isn't very interesting since it does not contain any
methods or attributes.  The ``pass`` is simply a placeholder in the class
declaration indicating a no-op.

Class instances are mutable, meaning that attributes and functions can be added
after instantiation::

  h = MyClass()
  print h.msg

There is no attribute ``msg``, so add one::

  h.msg = "Hello World!"
  print h.msg


Multiple Inheritance
^^^^^^^^^^^^^^^^^^^^

Create a class with a static string attribute ``msg1`` and a class method
``echo`` to print the attribute.  Comments begin with a ``#`` and extend to the
end of the line::

  class Hello:
      # static attribute string "msg1"
      msg1 = "Hello"
      def echo(self):
          print self.msg1

  print 'Hello's msg1:', Hello.msg1
  h = Hello()
  h.echo()
  print h
  

Create a class with a constructor definition.  Initialize an attribute ``msg2``
at class instance creation time::

  class World:
      # class constructor
      def __init__(self, msg2="World"):
          # attribute "msg2" initialized in constructor
          self.msg2 = msg2
      def echo(self):
          print self.msg2

  w = World()
  w.echo()
  print w

Create a class that inherits from ``Hello`` and ``World``.  Initialize an
attribute ``msg3`` using attributes from inherited classes.  Override the method
``echo`` to call methods from inherited classes.  Define the ``__str__`` to
return the attribute ``msg3`` when the class instance is printed with
``print``::

  class HelloWorld(Hello, World):
      def __init__(self):
          # self.msg1 is from Hello
	  # self.msg2 is from World
	  # World constructor is needed since msg2 is not static!
          World.__init__(self)
	  self.msg3 = self.msg1 + " " + self.msg2 + "!"
      def echo(self):
          Hello.echo(self)
          World.echo(self)
      def __str__(self):
          return self.msg3

  hw = HelloWorld()
  hw.echo()
  print hw
  

Class ``HelloWorld`` is of type ``Hello``, ``World``, and ``HelloWorld``::

  type(hw)
  isinstance(hw, Hello)
  isinstance(hw, World)
  isinstance(hw, HelloWorld)
  isinstance(hw, MyClass)


Additional Notes on Classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Classes can contain other classes as attributes::

  class HelloWorld:
      def __init__(self, msg="World World"):
          # create Hello and World objects as attributes
          self.h = Hello()
          self.w = World(msg)
      def echo(self):
          # call their echo methods
          self.h.echo()
          self.w.echo()

  hw = HelloWorld()
  hw.echo()
  
  isinstance(hw, Hello)
  isinstance(hw, HelloWorld)


Classes have special methods that can be defined to correspond to certain
language operators.  Define how a class behaves using the '+' operator::

  class Hello:
      msg = "Hello"
      def __add__(self, lhs):
          print self.msg + lhs.msg

  class World:
      msg = "World"
      def __add__(self, rhs):
          print self.msg + rhs.msg

  Hello() + World()
  World() + Hello()


.. admonition:: Exercise (for the interested reader): 
   
   Define a class ``Powlaw`` that accepts two keyword arguments in its
   constructor: ``index`` and ``norm``.  The keyword arguments are initialized
   as ``index=2.0`` and ``norm=0.01``.  In the class constructor definition, set
   ``index`` and ``norm`` as class attributes.  Define a class method ``calc``
   which takes an argument ``wave`` and computes a power-law on ``wave`` using
   ``index`` and ``norm``.  The ``wave`` argument can be assumed to be a 1-D
   NumPy array object.  ``calc`` should return the calculated result.

.. raw:: html
   
   <div class="panel0">

Answer::

  class Powlaw:
      def __init__(self, index = 2.0, norm = 0.01):
	   self.index = index
	   self.norm = norm
      def calc(self, wave):
           return self.norm*(wave**self.index)

.. raw:: html
   
   </div> <p class="flip0">Click to Show/Hide Solution</p>


Sherpa
------

`Sherpa`_ is a general purpose modeling and fitting application written in Python.

  - Uses Python's interactive capabilities and its Object Oriented Programming
    (OOP) approach.

  - Provides a flexible environment for resolving spectral and image properties,
    analyzing time series, and modeling generic types of data.

  - Implements the forward fitting technique for parametrized data modeling.

  - Includes functions to calculate goodness-of-fit and parameter confidence
    limits.

  - Data structures are contained in Python modules so users can easily add their
    own data structures, models, statistics or optimization methods to Sherpa.

  - Complex model expressions are supported using a general purpose and compact
    definition syntax.


Documentation
^^^^^^^^^^^^^

- `Sherpa home page
  <http://cxc.harvard.edu/sherpa>`_: Sherpa for CIAO users
- `Sherpa python page
  <http://cxc.harvard.edu/contrib/sherpa>`_: Sherpa for Python users

The Sherpa documentation collection includes a gallery of examples, fitting
threads, and AHELP pages that describe each Sherpa function:

- `Sherpa gallery
  <http://cxc.cfa.harvard.edu/sherpa/gallery/thumbnails.py.html>`_: Examples by plot
- `Sherpa fitting threads
  <http://cxc.cfa.harvard.edu/sherpa/threads/index.html>`_: Example scripts
- `Sherpa AHELP pages
  <http://cxc.cfa.harvard.edu/sherpa/ahelp/index_alphabet.html>`_: Function information


Explore the Sherpa Object Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In a new working directory, download a MAST spectrum of :download:`3C 273 <./3c273.fits>` 
and start IPython::

  $ ipython -pylab

Import a few Sherpa classes needed to characterize a fit::

  from sherpa.data import Data1D
  from sherpa.models import PowLaw1D
  from sherpa.stats import Chi2DataVar
  from sherpa.optmethods import LevMar
  from sherpa.fit import Fit

Import the Python FITS reader ``pyfits`` and open the spectrum as a table::

  import pyfits
  dat = pyfits.open('3c273.fits')[1].data

Access the `WAVELENGTH` and `FLUX` columns from the pyFITS ``RecArray``.  Populate
variables represented as ``wave``, ``flux``, and ``err``.  Normalize the flux and assume
uncertainties of 2% of the flux::

  wave = dat.field('WAVELENGTH')
  flux = dat.field('FLUX') * 1e14
  err  = dat.field('FLUX') * 0.02e14

Create a Sherpa ``Data1D`` data set from the NumPy arrays ``wave``, ``flux``, and
``err``.  The data arrays are accessible from the ``data`` object as the attributes
``x``, ``y``, and ``staterror``::

  data = Data1D('3C 273', wave, flux, err)
  print data

Array access::

  print data.x, data.y, data.staterror


Define a a convenience function ``plot_data`` that calls the matplotlib functions
``plot`` and ``errorbar`` according to certain criteria.  Plot the ``x`` and
``y`` arrays using the format specified in the optional argument, ``fmt``.  Clear
the plot if the ``clear`` argument is ``True``.  Add the plot errorbars if the
``err`` array is present::

  def plot_data(x, y, err=None, fmt='.', clear=True):
      if clear:
          clf()
      plot(x, y, fmt)
      if err is not None:
          errorbar(x, y, err, fmt=None, ecolor='b')

Plot the spectrum by accessing the NumPy arrays in the Sherpa data set using the
default arguments::

  plot_data(data.x, data.y, data.staterror)

.. image:: 3c273_data_mast.png
   :scale: 75


Create a Sherpa power-law model ``pl``.  All Sherpa models maintain a tuple of
parameters in ``pars``.  Access each of the model's parameter objects and print
the ``name`` and ``val`` attributes::

  pl = PowLaw1D('powlaw1d.pl')
  pl.pars
  for par in pl.pars:
      print par.name, par.val


Print out the ``PowLaw1D`` object and its parameter information.  Set the
power-law reference to be 4000 Angstroms.  Each model parameter is accessible as
an attribute its model.  For example, the power-law amplitude is referenced
with ``pl.ampl``::

  print pl
  pl.ref = 4000.
  print pl

Model parameters are themselves class objects::

  print pl.ampl


.. admonition:: Exercise (for the interested reader): Special methods and properties

  Wait. Didn't we just set ``pl.ref`` to be an float?  How can ``pl.ref`` be an
  float and a ``Parameter`` object?

.. raw:: html
   
   <div class="panel0">

The answer is that pl.ref is in fact an object, but its model class supports a
special setter method ``__setattr__()`` that updates the pl.ref.val attribute
underneath.  The ``property`` function defines custom getter and setter
functions for a particular class attribute::


  class Parameter:
      def _get_val(self):
          return self._value
      def _set_val(self, val):
          self._value = val
      # setup a 'val' attribute
      val = property(_get_val, _set_val)
      def __init__(self):
          # private attribute intended to be reference as 'val'.
          self._value = 1.0


  class Model(object):
      def __setattr__(self, name, val):
          if hasattr(self, name) and isinstance(getattr(self, name), Parameter):
	      getattr(self, name).val = val
      def __init__(self):
          self.ref = Parameter()


.. raw:: html
   
   </div> <p class="flip0">Click to Show/Hide Solution</p>



Create a ``Fit`` object made up of a Sherpa data set, model, fit statistic, and
optimization method.  Fit the spectrum to a power-law with least squares
(Levenberg-Marquardt) using the chi-squared statistic with data variance::

  f = Fit(data, pl, Chi2DataVar(), LevMar())
  result = f.fit()
  print result
  # or alternatively
  print result.format()

Over-plot the fitted model atop the data points using our convenience function
``plot_data``.  This time calculate the model using the best-fit parameter
values over the ``data.x`` and plot using a custom format and indicate
``clear=False``::

  plot_data(data.x, pl(data.x), fmt="-", clear=False)

.. image:: 3c273_fit_mast.png
   :scale: 75


The Sherpa High Level UI
^^^^^^^^^^^^^^^^^^^^^^^^

Enough of the low-level API.  Sherpa includes a set of high-level procedural
functions that manipulate the API-level objects underneath.

We will start over with our 3C 273 spectrum using the Sherpa high-level UI::

  $ ipython -pylab

Begin by importing ``pyfits`` and then import the Sherpa UI module into a
namespace named ``ui``::

  import pyfits
  import sherpa.ui as ui

Read in the columns from the FITS file and load the arrays into a Sherpa data
set::

  dat = pyfits.open('3c273.fits')[1].data
  ui.load_arrays(1, dat.field('WAVELENGTH'), dat.field('FLUX')*1e14, dat.field('FLUX') * 0.02e14)

Filter the spectral coordinates from 3000 to 5700 Angstroms and plot the
spectrum using Sherpa's high level plotting interface to matplotlib::

  ui.notice(3000, 5700)
  ui.plot_data()

.. image:: 3c273_data_mast_noticed.png
   :scale: 75

Define a power-law to start.  Notice the compact syntax for efficiently defining
model instances inline.  ``powlaw1d`` acts as a factory function that will
create new power-law model instance by simply accessing an attribute using a
choosen model identifier.  ``pow1`` is now a power-law model accessible in
scope::

  ui.set_model(ui.powlaw1d.pow1)
  pow1.ref = 4000.      # Set power-law reference to 4000 Angstroms
  print ui.get_model()  # or ui.show_model() for interactive use

Fit the filtered continuum using ``pow1`` and plot the fitted model atop the
data.  The default fit statistic is chi-squared with Gehrels variance and the
default optimization method is least squares (Levenberg-Marquardt)::

  ui.fit()
  ui.plot_fit()

.. image:: 3c273_fit_mast_noticed.png
   :scale: 75

Quickly access Sherpa fit information using ``show_all``.  This will open the
`less` program to display the fit information.  Quit `less` by pressing `q`::

  ui.show_all()

OK.  Time to fit the spectral lines.  We will build on the power-law model by
adding four Gaussian models in an arithmetic expression.  Notice how the model
definition instaniates and returns each instance.  Each instance also supports
the special ``__add__`` operator to combine the expression into a composite
model that is finally passed as a single argument to ``set_model``::

  # Add four Gaussian models, using cursor interactively to get
  # decent starting wavelength values
  ui.set_model(pow1 + ui.gauss1d.g1 + ui.gauss1d.g2 + ui.gauss1d.g3 + ui.gauss1d.g4)
  g1.pos = 3250
  g2.pos = 5000
  g3.pos = 5260
  g4.pos = 5600
  g1.fwhm = 50
  g2.fwhm = 50
  g3.fwhm = 50
  g4.fwhm = 50
  print ui.get_model()  # or ui.show_model() for interactive use

Now fit with the four Gaussian lines plus the continuum and plot the results
with the spectrum::

  # Fit and plot
  ui.fit()
  ui.plot_fit()
  print ui.get_model()


Next, we will add a broad line component to the first line.  Notice that the model
components previously defined are referenced using the identifier.  Also, we will
link the Gaussian positions together and define the broad line FWHM to be four
times the FHWM of the narrow line::

  ui.set_model(pow1 + g1 + g2 + g3 + g4 + ui.gauss1d.g1_broad)
  g1_broad.pos = g1.pos         # Force broad line to same wavelength as narrow
  g1_broad.fwhm = g1.fwhm * 4   # Link with algebraic expression

The link expressions for the position and FWHM can be seen in the model display
information::

  print ui.get_model() # or ui.show_model() for interactive use

Freeze the Gaussian lines at the red end of the spectrum at their current
best-fit parameter values::

  ui.freeze(g2, g3, g4)

Add an additional filter to ignore the Fe complex and other lines during
fitting::

  ui.ignore(3360, 4100)

Fit, then notice the full wavelength range to plot the fit::

  ui.fit()
  ui.notice(3000, 5700)
  ui.plot_fit()

Finally, overlay the power-law component atop the fit plot::

  ui.plot_model_component(pow1, overplot=True)


2-D Fitting in Sherpa
^^^^^^^^^^^^^^^^^^^^^

Fit image data of a supernova remnant G21.5-0.9 using a 2-D multi-component
source model.  First, download the FITS image of :download:`G21.5-0.9 <./image.fits>` 
and start IPython::

  $ ipython -pylab

Import the Sherpa's high-level UI with added routines for astronomy::

  from sherpa.astro.ui import *

Load in the FITS image using Sherpa's ``load_data``.  Sherpa includes built-in
convienence routines for reading FITS tables and images using pyFITS.  Show the
image using ``image_data`` in DS9::

  load_data("image2.fits")
  image_data()

Calculate the number of source counts in the full FOV::

  calc_data_sum2d()

Typically, X-ray data from Chandra contain low counts, so we will switch over
to a maximum likelihood statistic such as `Cash`::

  set_stat("cash")

The default fitting method, least squares, is not suitable for fitting low-count
data such as X-ray images, so we will choose `Simplex` as the optimization
method::

  set_method("simplex")

Set the coordinate system for this image to use `physical` coordinates with
``set_coord`` (Chandra chip coordinates).  Valid coordinate systems include
`image`, `physical`, and `wcs`::

  set_coord("physical")

Next, we will setup a 2-D region to filter the image.  Here we define a 2-D
`CIRCLE` with `x` and `y` defined in physical coordinates and the `radius`
defined in pixels::

  notice2d("CIRCLE(4072.46,4249.34,108)")

.. Important::

   The coordinate system of the data must match the coordinate system used in
   the 2-D region definition.  Typically, a call to ``set_coord`` is made before
   using ``notice2d`` or ``ignore2d``.

.. admonition:: Sherpa also supports 2-D regions from file (either ASCII or FITS).

  Sherpa supports CIAO region files to define 2-D noticed regions::

    f = file("circle.reg", "w")
    f.write("CIRCLE(4072.46,4249.34,108)\n")
    f.close()

    notice2d("circle.reg")

View the filtered image data in DS9::

  image_data()

Calculate the source counts inside the noticed 2-D region::

  calc_data_sum2d("CIRCLE(4072.46,4249.34,108)")

Define a 2-D Gaussian as the source model.  This example is simply an
illustration for describing the source emission.  Initialize the parameter
values according to coordinate system.  The `xpos` and `ypos` parameters are in
`physical` coordinates::

  set_source(gauss2d.g1)
  g1.ampl = 20
  g1.fwhm = 20
  g1.xpos = 4065.5
  g1.ypos = 4250.5

**NOTE:** The function ``set_source`` is synonymous to ``set_model``

Next, constraint the parameter limits to roughly the size of the image::

  g1.fwhm.max = 4300
  g1.xpos.max = 4300
  g1.ypos.max = 4300
  g1.ampl.min = 1
  g1.ampl.max = 1000

View the current model definition and view the 2-D Gaussian in DS9::

  print get_model()
  image_model()

Calculate the Gaussian model counts inside the noticed 2-D region::

  calc_model_sum2d("CIRCLE(4072.46,4249.34,108)")

Now, include a background component to the source model.  In this case, an
estimate of (0.2) is made from the radial profile::

  set_source(g1+const2d.bgnd)
  bgnd.c0 = 0.2
  bgnd.c0.max = 100

View the updated model expression::

  print get_model()

**NOTE:** The function ``get_model`` is **not** synonymous to ``get_source``.
Typically, Sherpa functions that end in ``_source`` refer to unconvolved model
components (e.g. components to be convolved with a Point Spread Function
(PSF)).  Sherpa functions that end in ``_model`` access the complete convolved
model expression including any convolution components (e.g. PSF).

Fit with ``fit`` and display the data, model, and residuals in DS9 with
``image_fit``::

  fit()
  image_fit()

Calculate the model counts inside the noticed 2-D region using the best-fit
parameter values::

  calc_model_sum2d("CIRCLE(4072.46,4249.34,108)")

Calculate the FWHM in arcseconds using the ACIS conversion factor by accessing
the parameter value with the attribute ``val``::

  g1.fwhm.val * 0.492

Save the fitted model to a FITS image using ``save_model`` and save the fit
residuals using ``save_resid``::

  save_model("model.fits")
  save_resid("resid.fits")

Calculate the parameter confidence limits on thawed parameter values using the
Sherpa method ``conf``::

  set_conf_opt("sigma", 1.64485)
  conf()

Notice how the parameter confidence limits are displayed as soon as they are
known.  The parameter confidence limits are accessed using ``get_conf_results``.
Save and display the 90% calculated parameter limits::

  results = get_conf_results()
  f = file("fit_results.out", "w")
  for name, val, minval, maxval in zip(results.parnames,results.parvals,results.parmins,results.parmaxes):
      line = [name, str(val+minval), "--", str(val+maxval)]
      print line
      f.write(" ".join(line)+"\n")

  f.close()

View the new output file::

  !cat fit_results.out

Notice how the function ``zip`` rotates the list of tuples into rows of names,
values, min values, and max values::

  tbl = zip(results.parnames,results.parvals,results.parmins,results.parmaxes)
  print tbl[0]
  name, val, min, max = tbl[0]
