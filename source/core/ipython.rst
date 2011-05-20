:tocdepth: 2

IPython
---------

IPython is an enhanced Python shell that creates a comprehensive environment
for interactive and exploratory computing.  In this section we'll learn the
basic features of IPython and how it benefits interactive analysis.

Before going further, open a new terminal window and change to your main Python
for Astronomers working directory.  Then start IPython by typing "ipython
-pylab" at the command prompt::

  % ipython -pylab

As we saw in the Introduction and Installation workshops, for interactive data
analysis IPython has a special ``-pylab`` command line option which
automatically imports elements of the NumPy and the Matplotlib environments.
This provides a Matlab-like environment allowing very simple and direct
commands like the following::
  
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

Showing data values
^^^^^^^^^^^^^^^^^^^^^^

So far we typed ``print x`` to look at the value of ``x``.  However,
most of the time for interactive analysis it is faster and better to simply
type ``x`` (or whatever the object name) followed by <Return>.  This returns
the "representation" of the object which is often a cleaner and more
informative than the "string" version that gets returned with ``print``.  In 
many cases the "representation" of an object the same as Python
code to create that object.

Try::

  y = dict((x, 'value is %d' % x**2) for x in range(10))
  y
  print y

Further resources
^^^^^^^^^^^^^^^^^^

- `IPython docs page <http://ipython.github.com/ipython-doc/stable/html/index.html>`_
- `IPython customization
  <http://ipython.scipy.org/doc/rel-0.9.1/html/config/customization.html>`_ :
  E.g. to always import certain modules read `The ipythonrc approach
  <http://ipython.scipy.org/doc/rel-0.9.1/html/config/customization.html#the-ipythonrc-approach>`_
  which explains editing ``~/.ipython/ipythonrc`` and setting the
  ``import_mod`` configuration.

