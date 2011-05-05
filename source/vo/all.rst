
putting it all together
=======================

.. admonition::  Exercise X

    Get a WISE cutout and plot red sources in circles

.. raw:: html

   <p class="flip9">Click to Show/Hide Solution</p> <div class="panel9">

First get the image::

    f.show_grayscale(vmin=0., vmax=200.)

And use aplpy to make the plot::

    f.show_grayscale(vmin=0.,vmax=200., stretch='sqrt')

Now get the catalog::

    f.show_colorscale()

and overplot it::

    f.show_colorscale(cmap='gist_heat')

.. raw:: html

   </div>
