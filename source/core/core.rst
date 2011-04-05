Core packages for analysis
===========================

Workshop goals:

- Learn the key features of IPython for interactive analysis
- NumPy arrays

  - Define arrays and perform common manipulations
  - Basic array slicing
  - Documentation and tutorials for further work

- Python objects
   
  - Understand the basic concept
  - Know how to inspect an object and discover what it can do

- Gain familiarity with tools available within the SciPy package
- Develop a script that extracts a 1-d spectrum from a 2-d longslit image

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
- Filter bad pixels
- Calculate errors

.. Topics:
   - Appending
   - Median
   - Making arrays
   - diff between list and array
   - vectorized ops (do a for loop)
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
FITS HDU list::

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
  figure()
  hist(img.flatten(), bins=100, log=True)

.. admonition:: Important Digression: Python Objects

   Most things in Python are objects.  What does that mean?  What is an object?

   Every constant, variable, or function in Python is actually a object with a
   type and associated attributes and methods.  An *attribute* a property of
   the object, for example ``img.shape``.  A *method* is a function
   that the object provides, for example ``img.argmax(axis=0)`` or ``img.min()``.

   Use tab completion in IPython to inspect objects and start to understand
   attributes and methods.  To start off create a list of 4 numbers::

     a = [3, 1, 2, 1]
     a.<TAB>

   This will show the available methods for ``a``::

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

   In general you can ignore all the ones that begin with ``__`` since these are
   internal methods that are not usually called directly.  However at the end you
   see useful looking functions like ``append`` or ``sort`` which you can get help
   for and use::

     a.sort
     a.sort?
     a.sort()
     a

.. tip:: Help
   
   Remember that you can always get help on an object::

     a = [3, 1, 2, 1]
     help a
     a?

   Discuss difference between ? and help.

   The ``help`` command gives help on the generic *class* of object ``a`` (e.g. a Python list or
   NumPy array) as opposed to the specific contents of ``a``.  You will again see
   a bunch of methods that start with ``__`` which you can ignore, but further
   down you will see all the useful methods.

   Generally ``print a`` or just ``a`` is the best way to learn about the specific
   contents in an object.  Each object has methods for printing information about
   itself, and depending on the class the print methods can be informative or not.


Plot the spatial profile and raw spectrum
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  spectrum = img.sum(axis=0)
  profile = img.sum(axis=1)
  figure()
  plot(spectrum)
  figure()
  plot(profile)




Other NumPy tidbits
^^^^^^^^^^^^^^^^^^^^^

Here I just copy
the Quick Tour from that tutorial but you should read the rest as well.  In
these examples the python prompt is shown as ">>>" in order to distinguish the
input from the outputs.

Arrays can be created in different ways::

  >>> a = array( [ 10, 20, 30, 40 ] )   # create an array out of a list
  >>> a
  array([10, 20, 30, 40])
  >>> b = arange( 4 )                   # create an array of 4 integers, from 0 to 3
  >>> b
  array([0, 1, 2, 3])
  >>> c = linspace(-pi,pi,3)            # create an array of 3 evenly spaced samples from -pi to pi
  >>> c
  array([-3.14159265,  0.        ,  3.14159265])

New arrays can be obtained by operating with existing arrays::

  >>> d = a+b**2                        # elementwise operations
  >>> d
  array([10, 21, 34, 49])

Arrays may have more than one dimension::

  >>> x = ones( (3,4) )
  >>> x
  array([[1., 1., 1., 1.],
         [1., 1., 1., 1.],
         [1., 1., 1., 1.]])
  >>> x.shape                            # a tuple with the dimensions
  (3, 4)

and you can change the dimensions of existing arrays::

  >>> y = arange(12)
  >>> y
  array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
  >>> y.shape = 3,4              # does not modify the total number of elements
  >>> y
  array([[ 0,  1,  2,  3],
         [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

It is possible to operate with arrays of different dimensions as long as they fit well (broadcasting)::

  >>> 3*a                                # multiply each element of a by 3
  array([ 30,  60,  90, 120])
  >>> a+y                                # sum a to each row of y
  array([[10, 21, 32, 43],
         [14, 25, 36, 47],
         [18, 29, 40, 51]])

Similar to Python lists, arrays can be indexed, sliced and iterated over::

  >>> a[2:4] = -7,-3                     # modify last two elements of a
  >>> for i in a:                        # iterate over a
  ...     print i
  ...
  10
  20
  -7
  -3

When indexing more than one dimension, indices are separated by commas::

  >>> x[1,2] = 20
  >>> x[1,:]                             # x's second row
  array([ 1,  1, 20,  1])
  >>> x[0] = a                           # change first row of x
  >>> x
  array([[10, 20, -7, -3],
         [ 1,  1, 20,  1],
         [ 1,  1,  1,  1]])
