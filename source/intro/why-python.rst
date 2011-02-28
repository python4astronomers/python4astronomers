Why Python?
============

With deepest apologies to the author:

|    *One Language to rule them all, One Language to find them,*
|    *One Language to bring them all and in the darkness bind them.*

Translation: the Python ecosystem provides a single environment that is
sufficient for the vast majority of astronomical analysis.  It does so 
on several levels:

- Clean and powerful language designed by people who are highly concerned with elegance.
- Strong set of 3rd party analysis tools that are professionally and actively developed.
- Robust methods for binding with C, C++ and FORTRAN libraries (speed, legacy)
- Standard library support for web, GUI, databases, process management, etc.
- Very active developer community

==> *Easy for astronomers* but with virtually no limits for gurus.  <==

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

Python and the necessary tools are FREE, as in free beer and Free Open
Source Software.

**Bad**

You may not care about that now, particularly if your institution already
pays for software licences (e.g. IDL or supermongo).

- Your collaborators may not want to pay licence fees
- You may want to run on a personal laptop

Switching from a familiar analysis environment is NOT FREE (hours *
dollars/hour * overhead_rate)

**Ugly**

If switching, you need to commit to a frustrating 6 months to a year:

- "Ugh, I could do this so much faster the old way."
- "Stupid Python, why isn't this working?!"
- "These plots look ugly."

**Good**

Learning to use Python for astronomy analysis will pay back the time
commitment.  If you analyze data from Chandra, LOFAR, Fermi, Herschel, HST,
JWST, ALMA, EVLA (etc etc) you may end up using Python even if you don't realize
it.

The `HIPE <http://herschel.esac.esa.int/HIPE_download.shtml>`_ (Herschel
Interactive Processing Environment) `data analysis guide
<http://herschel.esac.esa.int/hcss-doc-5.0/print/howtos/howtos.pdf>`_ is a
great example.  They barely mention in this guide that the dozens of "command
line" examples are just Python (well actually Jython).  That would be too
scary.

.. image:: hipe.png

Comparison to IDL
-------------------


Comparison to SM
-------------------

- Not free
- Supports only 1-d vectors, no 2-d image or N-d arrays
- Very primitive scripting capabilities:

  - Confusing and ugly distinction between vector variables and string
    variables (when to use SET vs. DEFINE etc)
  - Macro capability 


