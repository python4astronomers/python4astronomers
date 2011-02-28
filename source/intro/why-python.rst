Why use Python?
================

With deepest apologies to Tolkien:

|    *One Language to rule them all, One Language to find them,*
|    *One Language to bring them all and in the darkness bind them.*

Translation: the Python ecosystem provides a single environment that is
sufficient for the vast majority of astronomical analysis.  It does so 
on several levels:

- Clean and powerful language designed by people who highly value elegance.
- Strong set of 3rd party analysis tools that are professionally and actively developed.
- Robust methods for binding with C, C++ and FORTRAN libraries (speed, legacy)
- Standard library support for web, GUI, databases, process management, etc.
- Very active developer community

==> `Easy for astronomers <http://www.manning.com/sande/>`_ but with virtually no limits for gurus.  <==

The Zen of Python
------------------
From `PEP 20 <http://www.python.org/dev/peps/pep-0020/>`_:

|    Beautiful is better than ugly.
|    Explicit is better than implicit.
|    Simple is better than complex.
|    Complex is better than complicated.
|    Flat is better than nested.
|    Sparse is better than dense.
|    Readability counts.
|    Special cases aren't special enough to break the rules.
|    Although practicality beats purity.
|    Errors should never pass silently.
|    Unless explicitly silenced.
|    In the face of ambiguity, refuse the temptation to guess.
|    There should be one-- and preferably only one --obvious way to do it.
|    Although that way may not be obvious at first unless you're Dutch.
|    Now is better than never.
|    Although never is often better than *right* now.
|    If the implementation is hard to explain, it's a bad idea.
|    If the implementation is easy to explain, it may be a good idea.
|    Namespaces are one honking great idea -- let's do more of those!

Freedom and commitment
----------------------

**Good**

Python and the necessary tools are FREE, as in free beer and Free Open Source
Software.  IDL and SM are not free.  Maybe you don't care because someone else
pays, but perhaps your collaborators don't want to pay, or you want to run on a
personal laptop.  *Using unlicensed versions is not cool*.

**Bad**

Switching from a familiar analysis environment is NOT FREE (hours *
dollars/hour * overhead_rate)

**Ugly**

If switching, you need to commit to a frustrating 6 months to a year:

- "Ugh, I could do this so much faster the old way."
- "Stupid Python, why isn't this working?!"
- "These plots look ugly."

**Good**

Using just one scripting language for everything is *efficient* and saves
brain-power for astronomy.  Compare to using a mish-mash of IDL, csh, SM, awk
to get the job done.

Learning to use Python for astronomy analysis will pay back the time
commitment.  If you analyze data from Chandra, LOFAR, Fermi, Herschel, HST,
JWST, ALMA, EVLA (etc etc) you will likely end up using Python even if you
didn't intend it.

The `HIPE <http://herschel.esac.esa.int/HIPE_download.shtml>`_ (Herschel
Interactive Processing Environment) `data analysis guide
<http://herschel.esac.esa.int/hcss-doc-5.0/print/howtos/howtos.pdf>`_ is a
great example.  They barely mention in this guide that the dozens of "command
line" examples are just Python (well actually Jython).  That would be too
scary.

.. image:: hipe.png

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

Reprise on Why
-------------------------
And the number one reason to use Python is:

...

*You want to be a cool, with-it person.*

(Credit again to 
`Using Python for Interactive Data Analysis
<http://stsdas.stsci.edu/perry/pydatatut.pdf>`_.)

