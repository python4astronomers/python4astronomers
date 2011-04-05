Core packages for analysis: IPython and NumPy
=================================================

Workshop goals:

- Learn the key features of IPython for interactive analysis
- NumPy arrays

  - Define arrays and perform common manipulations
  - Basic array slicing
  - Documentation and tutorials for further work

- Python objects
   
  - Understand the basic concept
  - Know how to inspect an object and discover what it can do

- Develop a script that extracts a 1-d spectrum from a 2-d longslit image
- Gain familiarity with tools available within the SciPy package

Setup
-----

Before getting started you need to get the example data and script files for
the workshop.  Now that you have a working Python installation we can do this
without worrying about details of the platform (e.g. linux has wget,
Mac has curl, Windows does not have tar, etc etc).  

Change to your main Python for Astronomers working directory, start IPython
("ipython -pylab") and enter::

  import urllib2, tarfile
  url = 'http://python4astronomers.github.com/core/core_examples.tar'
  tarfile.open(fileobj=urllib2.urlopen(url), mode='r|').extractall()
  cd py4ast/core
  ls

Leave this IPython session open for the rest of the workshop.

.. admonition:: Exercise (for the interested reader): How did that code above work?
   
   Explain what's happening in each part of the previous code snippet to grab
   the file at a URL and untar it.  Google on "python urllib2" and "python
   tarfile" to find the relevant module docs.  Figure out how you would
   use the ``tarfile`` module to create a tarfile.

IPython
---------

As we saw in the Introduction and Installation workshops, for interactive data
analysis IPython has a special ``-pylab`` command line option which
automatically imports elements of the NumPy and the Matplotlib environments.
This provides a Matlab-like environment allowing very simple and direct
commands like::
  
  x = arange(0, 10, 0.2)
  y = sin(x)
  print x
  plot(x, y)

Keyboard navigation and history
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One of the most useful features of IPython is the ability to edit and navigate 
you command line history.  This lets you quickly re-do commands, perhaps with a
slight variation based on seeing the last result.  Try cut-n-pasting the above
lines in an IPython session.  This should bring up a plot of a sine wave.  

Now hit up-arrow once and get back the ``plot(x, y)`` line.  Hit the left-arrow
key (not backspace) once and type ``**2`` so that the line reads ``plot(x,
y**2)``.  Now you can hit Return to see the new curve overlayed within the same
plot window.  It is not necessary to forward-space to the end of the line, you
can hit Return with the cursor anywhere in the line.

Now say you want to change the ``x`` values slightly.  One option is to just hit the
up-arrow 5 times, but a much faster way is to remember that the line started
with ``x``, so type ``x`` and then start hitting up-arrow.  Only lines that
start with ``x`` will be displayed and you are immediately at the 
``x = arange(0, 10, 0.2)`` line.  Now use the right-arrow and backspace to change ``10`` to
``15`` and hit Return.  Of course ``y`` needs to be recalculated, so hit ``y``
then up-arrow, then Return.  Finally ``pl`` up-arrow and Return.  Nice and fast!

Bonus points: to speed up by another factor of several, use Ctrl-p (prev) instead of
up-arrow, Ctrl-n (next) instead of down-arrow, Ctrl-f (forward) instead of
right-arrow and Ctrl-b (back) instead of left-arrow.  That way your fingers
never leave the keyboard home keys.  Ctrl-a gets you to the beginning of the
line and Ctrl-e gets you to the end of the line.  Triple bonus: on a Mac or
Windows machine re-map the Caps-lock key to be Control so it's right next to
your left pinky.  How often do you need Caps-lock?

Your command history is saved between sessions (assuming that you exit IPython
gracefully) so that when you start a new IPython you can use up-arrow to re-do
old commands.  You can view your history within the current session by entering
``history``.

Linux and shell commands
^^^^^^^^^^^^^^^^^^^^^^^^^

A select set of useful linux commands are available from the IPython prompt.
These include ``ls`` (list directory), ``pwd`` (print working directory),
``cd`` (change directory), and ``rm`` (remove file).  Any shell command
can be executed by preceding it with an exclamation point "!".

Tab completion
^^^^^^^^^^^^^^^

IPython has a very useful tab completion feature that can be used both to
complete file names and to inspect python objects.  As an example do::

  ls ~/<TAB>

This will list everything in your home directory.  You can continue
this way searching through files or hit Return to complete the command.

Further resources
^^^^^^^^^^^^^^^^^^

- `IPython docs page <http://ipython.github.com/ipython-doc/stable/html/index.html>`_
- `IPython customization
  <http://ipython.scipy.org/doc/rel-0.9.1/html/config/customization.html>`_ :
  E.g. to always import certain modules read `The ipythonrc approach
  <http://ipython.scipy.org/doc/rel-0.9.1/html/config/customization.html#the-ipythonrc-approach>`_
  which explains editing ``~/.ipython/ipythonrc`` and setting the
  ``import_mod`` configuration.

NumPy
-----

`NumPy`_ is at the core of nearly every scientific Python application or
module since it provides a fast N-d array datatype that can be manipulated in a
vectorized form.  This will be familiar to users of IDL or Matlab. 

NumPy has a good and systematic `basic tutorial
<http://www.scipy.org/Tentative_NumPy_Tutorial>`_ available.  It is highly
recommended that you read this tutorial to fill in the gaps left by this
workshop, but on its own it's a bit dry for the impatient astronomer.

Here we'll learn NumPy by performing a very simple reduction of a
2-dimensional long slit spectrum (3C120 from HST/STIS):

- Read in the 2-d image
- Plot the spatial profile and raw spectrum
- Fit and subtract the background from each wavelength column
- Sum the source signal
- Filter bad pixels  (SKIP?)
- Calculate errors

.. Topics:
   - Appending
   - Median
   - Making arrays
   - Broadcasting x = arange(5); y=x.reshape(5,1) ; x + y * 10
   - diff between list and array
   - vectorized ops (do a for loop)
   - exercise: make a mexican hat or similar
   - boolean masking / where
   - scipy 2-d median filter

Read in the 2-d image
^^^^^^^^^^^^^^^^^^^^^^

First read in the long-slit spectrum data.  The standard file format available
for download from MAST is a FITS file with three identically sized images
providing the 2-d spectral intensity, error values, and data quality for each
pixel.  The slit direction is along the rows (up and down) and wavelength is in
columns (left to right).
::

  import pyfits
  hdus = pyfits.open('3c120_stis.fits.gz')
  hdus?
  hdus

.. admonition:: Digression: ``print x`` versus plain ``x``

  So far we typed ``print x`` to look at the value of ``x``.  However,
  most of the time for interactive analysis it is faster and better to simply
  type ``x`` (or whatever the object name) followed by <Return>.  This returns
  the "representation" of the object which is often a cleaner and more
  informative than the "string" version that gets returned with ``print``.  In 
  many cases the "representation" of an object the same as Python
  code to create that object.

  Try::

    print hdus
    arange(5)
    print arange(5)

Now give meaningful names to each of the three images that are available in the
FITS HDU list.  You can access element ``n`` in a list with the index ``[n]``,
where the count starts from 0::

  primary = hdus[0].data
  img = hdus[1].data
  err = hdus[2].data
  dq = hdus[3].data

Next have a look at the images using a super-simple image viewer that I wrote in
about 50 lines of Python::

  from imgview import ImgView
  ImgView(img)

.. admonition:: Exercise: View the error and data quality images
  
  Bring up a viewer window for the other two images.  Play with the toolbar
  buttons on the lower-left (hint: try the four on the right first, then
  imagine a web browser for the three on the left).  Does the save button 
  work for you?

Now discover a little bit about the images you have read in::

  img?
  help img
  img.shape  # Get the shape of img
  img.min()  # Call object method min with no arguments
  img.argmax(axis=0) 

.. admonition:: Digression: Python Objects - or what's with the
   periods everywhere?

   Most things in Python are objects.  What does that mean?  What is an object?

   Every constant, variable, or function in Python is actually a object with a
   type and associated attributes and methods.  An *attribute* a property of
   the object that you get or set by giving the <object_name> + dot +
   <attribute_name>, for example ``img.shape``.  A *method* is a function
   that the object provides, for example ``img.argmax(axis=0)`` or ``img.min()``.

   Use tab completion in IPython to inspect objects and start to understand
   attributes and methods.  To start off create a list of 4 numbers::

     a = [3, 1, 2, 1]
     a.<TAB>

   This will show the available attributes and methods for the Python list ``a``::

     In [17]: a.<TAB>
     a.__add__           a.__ge__            a.__iter__          a.__repr__          a.append
     a.__class__         a.__getattribute__  a.__le__            a.__reversed__      a.count
     a.__contains__      a.__getitem__       a.__len__           a.__rmul__          a.extend
     a.__delattr__       a.__getslice__      a.__lt__            a.__setattr__       a.index
     a.__delitem__       a.__gt__            a.__mul__           a.__setitem__       a.insert
     a.__delslice__      a.__hash__          a.__ne__            a.__setslice__      a.pop
     a.__doc__           a.__iadd__          a.__new__           a.__sizeof__        a.remove
     a.__eq__            a.__imul__          a.__reduce__        a.__str__           a.reverse
     a.__format__        a.__init__          a.__reduce_ex__     a.__subclasshook__  a.sort

   For the most part you can ignore all the ones that begin with ``__`` since
   they are generally are internal methods that are not called directly.  At
   the end you see useful looking functions like ``append`` or ``sort`` which
   you can get help for and use::

     a.sort
     a.sort?
     a.sort()
     a

   *Question*:
     How do you tell the difference between an attribute and a
     callable method?  How can you find all attributes or methods?
 
   *Answer*:
     Use the ``callable`` function::

       callable(a.sort)

     To list all the "interesting" callable methods do::

       [x for x in dir(a) if callable(getattr(a, x)) and not x.startswith('__')]

NumPy basics
^^^^^^^^^^^^

Slicing
#######

NumPy provides powerful methods for accessing particular subsets of an array,
e.g. the 4th column or every other row.  This is called slicing.  As a first
example plot column 300 of the longslit image to look at the spatial profile::

  clf(); plot(img[:, 300])

The ":" in the first axis means to select all elements in that axis (i.e. all
rows).  This is a short form for the full slicing syntax::

  i0 : i1 : step

- ``i0`` is the first index value (default is zero if not provided)
- ``i1`` is the index upper bound (default is last element index + 1)
- ``step`` is the step size (default is one).  When ``step`` is not specified then the final ":" is not required.

.. admonition:: Exercise: Slice the error array

  - For row 254 of the error array ``err`` plot columns 10 to 200 stepping by 3.
  - Print a rectangular region slice with rows 251 to 253 (inclusive) and columns 101 to
    104 (inclusive).  What did you learn about the index upper bound value?

Making arrays
#############

Arrays can be created in different ways::

  a = array([10, 20, 30, 40])   # create an array from a list of values
  b = arange(4)                 # create an array of 4 integers, from 0 to 3
  c = arange(0.0, 10.0, 0.1)    # create a float array from 0 to 100 stepping by 0.1
  d = linspace(-pi, pi, 5)      # create an array of 5 evenly spaced samples from -pi to pi

New arrays can be obtained by operating with existing arrays::

  e = a + b**2            # elementwise operations

Arrays may have more than one dimension::

  f = ones([3, 4])                 # 3 x 4 float array of ones
  g = zeros([2, 3, 4], dtype=int)  # 3 x 4 x 5 int array of zeros
  h = ones_like(f)                 # array of ones with same shape/type as f
  i = zeros_like(f)                # array of zeros with same shape/type as f

You can change the dimensions of existing arrays::

  w = arange(12)
  w.shape = [3, 4]       # does not modify the total number of elements
  x = arange(5)
  y = x.reshape(5, 1)
  y = x.reshape(-1, 1)   # Numpy determines the right value for "-1" axis

It is possible to operate with arrays of different dimensions as long as they fit well (broadcasting)::

  z = x + y * 10

.. admonition:: Exercise: Make a ripple

  Calculate a surface ``z = cos(r) / (r + 5)`` where ``r = sqrt(x**2 +
  y**2)``.  Set ``x`` to an array that goes from -20 to 20 stepping by 0.25
  Make ``y`` the same as ``x`` but "transposed" using the ``reshape`` trick above.
  Use ImgView to display the image of ``z``.


.. Solution
   x = arange(-20, 20, 0.25)
   y = x.reshape(-1, 1)
   r = sqrt(x**2 + y**2)
   z = cos(r) / (r + 5)
   imgview.ImgView(z)
   dist = sqrt((x-10)**2 + (y-15)**2)
   ok = dist < 10
   z[ok] = dist[ok] / 10


Plot the spatial profile and raw spectrum
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plot the spatial profile by summing along the wavelength direction::

  profile = img.sum(axis=1)
  figure()
  plot(profile)

Now plot the spectrum by summing along the spatial direction::

  spectrum = img.sum(axis=0)
  figure()
  plot(spectrum)

Since most of the sum is in the background region there is a lot of noise and
cosmic-ray contamination.

.. admonition:: Exercise: Use slicing to make a better spectrum plot

  Use slicing to do the spectrum sum using only the rows in the image where
  there is a signal from the source.
  Hint: zoom into the profile plot to find the right row range.

.. Solution
   spectrum = img[250:260, :].sum(axis=0)
   figure()
   plot(spectrum)


Fit and subtract the background from each wavelength column
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plot five columns (wavelength) from the spectrum image as follows::

  clf()
  plot(img[:, 254:259])

The basic idea in spectral extraction is to subtract out the background and sum
over rows with the source signal.

It's evident that there are significant cosmic ray defects in the data.  In
order to do a good job of subtracting the background we need to filter them
out.  Doing this correctly in general is difficult and in reality one would
just use the answers already provided by STSci.

**Strategy**: Use a median filter to smooth out single-pixel deviations.  Then
use sigma-clipping to remove large variations between the actual and smoothed
image.

::

  import scipy.signal
  img_sm = scipy.signal.medfilt(img, 5)
  sigma = median(err)
  bad = abs(img - img_sm) / sigma > 8.0
  img_cr = img.copy()
  img_cr[bad] = img_sm[bad]
  img_cr[230:280,:] = img[230:280,:]  # Filter only for background

Check if it worked::

  clf()
  plot(img_cr[:, 254:259])

This introduces the important concept of slicing with a boolean mask.  Let's
look at a smaller example::

   a = array([1, 4, -2, 4, -5])
   neg = (a < 0)    # Parentheses here for clarity but are not required
   a[neg] = 0

A slightly more complex example shows that this works the same on N-d arrays
and that you can compose logical expressions::

   a = arange(25).reshape(5,5)
   ok = (a > 6) & (a < 17)     # "ok = a > 6 & a < 17" will FAIL!
   a[~ok] = 0                  # Note the "logical not" operator

.. admonition:: Digression: copy versus reference

   **Question**
     In the median filtering commands above we wrote ``img_cr = img.copy()``.  Why
     was that needed instead of just ``img_cr = img``?

   **Answer**
     Because the statement ``img_cr = img`` would just create another reference
     pointing to the underlying N-d array object that ``img`` references.

   Remember that the variable names are just pointers to the actual Python
   object.  To see this clearly do the following::

     a = arange(8)
     b = a
     id(a)
     id(b)
     b[3] = -10
     print a
    
   After getting over the initial confusion this behavior is actually a good
   thing because it is efficient and consistent within Python.  If you really
   need a copy of an array then use the copy() method as shown.

   **BEWARE** of one common pitfall: NumPy "basic" slicing like ``a[3:6]``
   does NOT make a copy::

     b = a[3:6]
     print b
     b[1] = 100
     print a

   However if you do arithmetic or boolean mask then a copy is always made::

     a = arange(4)
     b = a**2
     a[1] = 100
     print a
     print b    # Still as expected after changing "a"
      

Fit the background for a single column::

  x = append(arange(10, 200), arange(300, 480))
  y = img_bkg[x, 10]
  clf()
  plot(x, y)
  pfit = polyfit(x, y, 2)
  yfit = polyval(pfit, x)
  plot(x, yfit)

Now do this for every column and store the results in a background image::

  xrows = arange(img_bkg.shape[0])
  bkg = zeros_like(img_cr)
  for col in range(img_bkg.shape[1]):
      pfit = polyfit(x, img_cr[x, col], 2)
      bkg[:, col] = polyval(pfit, xrows)

  ImgView(bkg)

Finally subtract this background and see if it worked::

  img_bkg = img_cr - bkg
  ImgView(img_bkg)

.. Solution
   badimg = zeros(bad.shape)
   badimg[bad] = 1
   imgview.ImgView(badimg)

Sum the source signal
^^^^^^^^^^^^^^^^^^^^^^

Now the final step is easy and is left as an exercise.

.. admonition:: Exercise: Make the final spectrum

   Sum the rows of the background subtracted spectrum and plot.  Hint: you
   already did it once in a previous exercise.


SciPy
-----

It is impossible to do justice to the full contents of the `SciPy`_ package: is
entirely too large!  What is left as homework for the reader is to 
click through to the main `SciPy Reference Manual
<http://docs.scipy.org/doc/scipy/reference/>`_ and skim the `tutorial
<http://docs.scipy.org/doc/scipy/reference/tutorial/index.html>`_.  Keep 
this repository of functionality in mind whenever you need some numerical
functionality that isn't in NumPy: there is a good chance it is in SciPy:

- Basic functions in Numpy (and top-level scipy)
- Special functions (scipy.special)
- Integration (scipy.integrate)
- Optimization (optimize)
- Interpolation (scipy.interpolate)
- Fourier Transforms (scipy.fftpack)
- Signal Processing (signal)
- Linear Algebra
- Statistics
- Multi-dimensional image processing (ndimage)
- File IO (scipy.io)
- Weave
