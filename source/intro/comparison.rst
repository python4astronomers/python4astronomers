.. _comparison_sm_idl:

Comparison to SM and IDL
=========================

SM
---

`SM <http://www.astro.princeton.edu/~rhl/sm>`_ is now over 20 years old and
continues to be actively used in the astronomy community even among the younger
generation.  As of this writing there are much better options.

Pros
^^^^^

- Very easy to learn for simple plotting
- High-quality output (relative to what astronomers expect)
- Lightweight, no installation hassles
- Can be called from Python (!)

Cons
^^^^^

- Not free: you have to pay a modest fee and nobody else can see, fix, or develop the source
- Fully supports only 1-d vectors, limited 2-d image and no N-d arrays
- Primitive scripting capabilities
- Confusing and ugly distinction between vector variables and string
  variables (when to use SET vs. DEFINE etc)
- Limited input data format: ASCII tables (space/tab separated or via
  hard-coded C scanf format)
- Limited output formats, basically X11 and Postscript, and a number of dead formats
  (e.g. OS/2, VAX/VMS)
- Not actively developed (last release 2007, closed source, two authors?)


SET / DEFINE / PRINT weirdness
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Or why SM was a fleeting phase::

  DEFINE v 12            # string "12"
  SET x = 10             # 1-element vector 10 20
  SET y = $v + x*12      # Add strings and vectors (well... PERL does this too)
  DEFINE y $v+x*12       # Syntax error, why?
  DEFINE y <$v+x*12>     # String "10+x*12"
  DEFINE y ($v+x*12)     # String "130"

  PRINT x                # FAIL
  PRINT {x}              # prints x vector
  PRINT {x[0]}           # FAIL
  WRITE STANDARD $(x[0]) # OK

Python::

  v = "12"               # v is a string
  x = 10
  y = v + x * 12         # FAIL: Python refuses to add a string and a number
  v = 12                 # Make v a number
  y = v + x * 12         # OK
  y = str(v) + "+x*12"   # Two strings can be added (concatenated)
  y = str(v+x*12)        # Make a string from the number
  print x, y, v          # print x, y and v. 

IDL
-----

Switching away from IDL is more difficult case to make and there are long 
lists of pros and cons in this case.  The starting point for this discussion
is the comprehensive comparison in Appendix B of 
`Using Python for Interactive Data Analysis
<http://stsdas.stsci.edu/perry/pydatatut.pdf>`_.  Some of the points have 
been updated since that 2007 document and are available in the 
`IDL vs. Python wiki <http://www.astrobetter.com/wiki/tiki-index.php?page=idl_vs_python>`_.

Here we present an abridged version of the comparison, showing points where
there is a significant distinction for the average astronomer.


Pros
^^^^
- Many mature numerical and astronomical libraries available. e.g., 
  `Astro Library <http://idlastro.gsfc.nasa.gov/contents.html>`_
- Wide astronomical user base
- Many local users with deep experience
- Easier installation
- Good, unified documentation

Cons
^^^^
- Narrow applicability, not well suited to general programming
- Table support poor
- Limited ability to extend using C or Fortran
- Expensive
- Closed source (only RSI can fix bugs)
- Very awkward to integrate with IRAF / CIAO / XXXX tasks

Python
---------
Pros
^^^^^
- Very general and powerful programming language, yet easy to learn. 
- Very large user and developer community, very extensive and broad library base.
- Very extensible with C, C++, or Fortran, portable distribution mechanisms available
- Free; non-restrictive license; Open Source
- Becoming the standard scripting language for astronomy
- Easy to use with IRAF tasks: PyRAF
- Many books and on-line documentation resources available (for the language and its libraries)
- Better support for table structures

Cons
^^^^
- More items to install separately, installation can be difficult.
- Not as widely adopted in astronomical community (but support clearly growing)
- Scientific libraries not as mature:
- Documentation not as complete, not as unified
- Not as deep in astronomical libraries and utilities (but clearly improving)

