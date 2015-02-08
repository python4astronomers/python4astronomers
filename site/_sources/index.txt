.. Python4Astronomers documentation master file, created by
   sphinx-quickstart on Sat Feb 26 13:39:46 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _guide:

Practical Python for Astronomers
===================================

Practical Python for Astronomers is a series of hands-on workshops to explore
the Python language and the powerful analysis tools it provides. *The emphasis
is on using Python to solve real-world problems that astronomers are likely to
encounter in research.*

- The workshops immediately make use of the full suite of plotting,
  analysis, and file reading tools.
- Along the way elements of the Python language such as data types, control structures,
  functions, and objects are introduced.
- This is an interactive experience using tutorial examples run by participants on their laptops.


**Workshop topics**

.. toctree::
   :maxdepth: 1

   intro/intro
   installation/installation
   core/core
   contest/bounce
   plotting/plotting
   files/files
   fitting/fitting
   astropy/astropy
   astropy-UVES/UVES


**Archival topic**

The following topic is based on packages that are not being actively
developed and have been superceded.  However there are still useful concepts
presented here and we keep it for reference.

.. toctree::
   :maxdepth: 1

   vo/vo

.. toctree::
   :hidden:

   local/local.rst

Sample Workshop Schedule
-------------------------

The workshop schedule is as follows.  Except for the first introductory session all
workshops are hands-on and participants should bring a laptop.

======== ======================================= ===================== =========
Date     Topic                                   Location and time     Presenter
======== ======================================= ===================== =========
TBD      Introduction to Python for Astronomers  TBD                   TBD          
TBD      Installation and Understanding Packages TDB                   TBD          
TBD      Core packages - NumPy, iPython, SciPy   TBD                   TBD          
TBD      Plotting and Images                     TBD                   TBD          
TBD      Reading and Writing Files               TBD                   TBD          
TBD      Fitting and Modeling 1-d and 2-d data   TBD                   TBD          
TBD      VO and Online astronomy                 TBD                   TBD          
======== ======================================= ===================== =========

About the Workshops
-------------------

The content presented here is suitable for self-study by those wishing to learn
Python for astronomy or other scientific research applications.  

**A greater goal is for those knowledgable in Python to teach the workshop
series at their local institutions, adapting the content as desired.** To that
end we have developed the content in `Sphinx <http://sphinx.pocoo.org>`_
RestructuredText and hosted the source on github at
`<https://github.com/python4astronomers/>`_.  Anyone interested can clone the
repository or download a tarball and make modifications needed to present the
material locally.

We would also welcome comments, fixes, or suggestions for improvement.  This
can be done as a Github issue or pull request, or by sending email to
aldcroft@head.cfa.harvard.edu.

The workshop material here was presented in the Spring of 2011 at the Harvard /
Smithsonian Center for Astrophysics.  A range of about 25 to 50 people
participated in the different workshops, which were 1.5 hours in duration.
Based on our experience a 2 hour slot would have been more reasonable to allow
time for the exercises and discussion.

About the Format
-----------------

The workshop presentations are formatted as Sphinx web documents instead of the
more traditional slide presentation.  This was a natural choice for the
authors who all use `Sphinx`_ for Python documenation.  Further inspiration was
drawn from `Dumping PowerPoint in Favor of Web Sites
<http://www.sal.ksu.edu/faculty/tim/prof-day/index.html>`_.  This site
highlights by discussion and examples the advantages in using a web-based study
guide.  In particular we found the non-linear format (e.g. jumping to different
sections or web sites) and ability to show longer examples were quite valuable.

Having full prose text results in a document which is far more useful as a
standalone study guide than presentation slides.  Ironically it also reduces
the temptation to read from the screen.

License
--------

The Practical Python for Astronomers workshop content is made available under
the terms of the `Creative Commons Attribution 3.0 License
<http://creativecommons.org/licenses/by/3.0>`_ (`legal code
<http://creativecommons.org/licenses/by/3.0/legalcode>`_).  You may distribute,
remix, tweak, and build upon this work, even commercially, as long as you
credit the authors and the Smithsonian Astrophysical Observatory for the
original creation.

+---+
|   |
+---+

:Authors: Tom Aldcroft, Tom Robitaille, Brian Refsdal, Gus Muench
:Copyright: 2011, 2012, 2013 Smithsonian Astrophysical Observatory

.. toctree::
   :hidden:

   astropy/data/README
   fitting/classes
   installation/recommended_options
   installation/requirements
   intro/comparison
   references
