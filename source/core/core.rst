Core packages for analysis
===========================

IPython
---------
For interactive data analysis IPython has a special ``-pylab`` command line
option which automatically imports elements of the Numpy and the Matplotlib 
environments.  This provides a Matlab-like environment allowing very simple
and direct commands like::

  % ipython -pylab
  
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
complete file names and to inspect python objects.  As a first example do::

  ls /proj/sot/ska/<TAB>

This will list everything that matches ``/proj/sot/ska``.  You can continue
this way searching through files or hit Return to complete the command.

Tab completion also works to inspect object attributes.  Every variable or
constant in python is actually a object with a type and associated attributes
and methods.  For instance try to create a list of 3 numbers::

  a = [3, 1, 2, 4, 1]
  print a
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

  help a.sort
  a.sort()
  print a

To make it even easier you don't usually have to use ``print``.  Try the
following::

  a.count(1)

Don't be scared to try printing an array value (e.g. ``tephin.vals``) even if
it is a billion elements long.  Numpy will only print an abbreviated version if
it is too long.  But beware that this applies to Numpy arrays which as we'll
see are a special version of generic python lists.  If you print a
billion-element python list you'll be waiting for a while.

NumPy
-----

**UNDER CONSTRUCTION**

NumPy has an excellent `basic tutorial
<http://www.scipy.org/Tentative_NumPy_Tutorial>`_ available.  Here I just copy
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
