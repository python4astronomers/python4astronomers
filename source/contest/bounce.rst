CONTEST: Make a fun bouncing balls demo
========================================

**Contest**: 
  Make the bouncing balls script more interesting.

**Judging**: 
  Submitted entries will be run during the Workshop and everyone will vote for the winner.

**Prize**: 
  One-year subscription to Wired Magazine or other geeky magazine of your choice (up to US$20 value).

**Submission**: 
  Email your script as an attachment to aldcroft@head.cfa.harvard.edu.  To make
  life easier please rename the script "bounce_<yourname>.py.txt" before
  attaching.

**Deadline**: 
  The deadline for submission is Noon on Friday.  

Bouncing balls
--------------

The script below shows a simple example of making an animation using
matplotlib.  The key feature is the `draw() <http://matplotlib.sourceforge.net/api/pyplot_api.html?highlight=pyplot.draw#matplotlib.pyplot.draw>`_ command which re-draws the plot
window.  

::

  figure(1)
  clf()
  axis([-10, 10, -10, 10])

  # Define properties of the "bouncing balls"
  n = 10
  pos = (20 * random(n*2) - 10).reshape(n, 2)
  vel = (0.3 * normal(size=n*2)).reshape(n, 2)
  sizes = normal(200, 100, size=n)

  # Colors where each row is (Red, Green, Blue, Alpha).  Each can go
  # from 0 to 1.  Alpha is the transparency.
  colors = random([n, 4])  

  # Draw all the circles and return an object ``circles`` that allows
  # manipulation of the plotted circles.
  circles = scatter(pos[:,0], pos[:,1], marker='o', s=sizes, c=colors)

  for i in range(100):
      pos = pos + vel
      bounce = abs(pos) > 10      # Find balls that are outside walls
      vel[bounce] = -vel[bounce]  # Bounce if outside the walls
      circles.set_offsets(pos)    # Change the positions
      draw()

    
In order to run this you should copy the lines above into a file
called ``bounce.py`` in your working directory.  Then start IPthon as usual
with ``ipython -pylab`` or with the Pylab application and enter the following::

  execfile("bounce.py")

This command essentially runs the lines of the file as if you had entered them
by hand, but this now allows for longer scripts.  This has the convenient
property that all the variables defined within the script are available at the
command line once the script finishes execution.  Use this to examine key
variables like ``pos``, ``sizes``, ``colors`` to understand how the script is
working.

The key plot routine being called is `scatter()
<http://matplotlib.sourceforge.net/api/pyplot_api.html?highlight=pyplot.scatter#matplotlib.pyplot.scatter>`_.
Read the documentation and understand how it is called.

Examine the ``circles`` object with ``help`` and ``?``.  Look for "set_*" 
methods (``circles.set_<TAB>``) that will let you set something and then get
help on those as well to learn how to use them.  There are corresponding "get_*"
methods that let you examine the existing values.

Contest
-------

Make the example script more interesting and visually stimulating!
Possibilities include:

- Change the colors and/or sizes dynamically
- Use other shapes and make them spin
- Add a lot more balls (at what point do things break?)
- Put in animated text with the `text()
  <http://matplotlib.sourceforge.net/api/pyplot_api.html?highlight=pyplot.scatter#matplotlib.pyplot.text>`_
  command.  You'll need to do something like 
  ``mytext = text(...)`` and then figure out how to change the properties of
  the text (e.g. rotation angle) using ``mytext.get_<TAB>`` and ``mytext.set_<TAB>`` and ``help mytext``.
- Do silly things like make the tick labels change colors and/or spin following the
  example code at the end of the `Axis containers
  <http://matplotlib.sourceforge.net/users/artists.html#axis-containers>`_ documentation.
- Put in physics, like making the balls bounce off each other, including gravity, or ???

