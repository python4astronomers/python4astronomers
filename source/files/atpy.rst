:tocdepth: 2

ATpy
====

`ATpy <http://atpy.github.com>`_ is a high-level Python package providing a way to manipulate tables of astronomical data in a uniform way. The two main features of ATpy are:

* It provides an abstract Table object that contains tabular data along with
  meta-data to describe the columns, and methods to manipulate the table (e.g.
  adding/removing/renaming columns, selecting rows, changing values, sorting,
  ...).

* It provides built-in support for reading and writing to several common
  file/database formats, including FITS, VO, HDF5, and ASCII tables, as well
  as SQLite, MySQL and PostgreSQL databases, with a very simple interface.

Reading in an existing table
----------------------------

First, download :download:`this <../downloads/catalog.fits.gz>` FITS table, then launch IPython in the directory where you have the file::

    $ ipython --pylab

If you have trouble downloading the file, then start up IPython (``ipython --pylab``) and enter::

    import urllib2
    url = 'http://python4astronomers.github.com/_downloads/catalog.fits.gz'
    open('catalog.fits.gz', 'wb').write(urllib2.urlopen(url).read())
    ls

Then import ``atpy``::

    import atpy

and read in the table::

    t = atpy.Table('catalog.fits.gz')

We can now see what columns are available in the table::

    >>> t.describe()
    Table : MY CATALOG
    --------------------------------------
    |     Name |    Unit | Type | Format |
    --------------------------------------
    | SOURCEID |         | |S20 |    68s |
    |       RA | RADIANS |  >f8 | 25.17e |
    |      DEC | RADIANS |  >f8 | 25.17e |
    |    EPOCH |         |  >f8 | 25.17e |
    |   LAMBDA |         |  >f8 | 25.17e |
    |      ETA |         |  >f8 | 25.17e |
    | DISTANCE |         |  >f8 | 25.17e |
    --------------------------------------

and how many lines there are::

    >>> len(t)
    1002

To access a particular column, use::

    >>> t['RA']
    array([ 4.64681193,  4.64686867,  4.64682644, ...,  4.64694334,
            4.64690389,  4.64698136])

As you can see, a single column is returned as a Numpy array, so any Numpy operation will work on this::

    >>> t['RA'].min()
    4.6465723005143351

    >>> t['RA'].max()
    4.6472357622326737

and you can then specify a particular row to access a single value::

    >>> t['RA'][4]
    4.6467757499903897

Let's select a subset of the table::

    >>> tsub = t.where(t['RA'] < 4.647)
    >>> len(tsub)
    742

And we can also remove the ``'DISTANCE'`` column which we don't care about::

    tsub.remove_columns('DISTANCE')

As you can see, the column is no longer there::

    >>> tsub.describe()
    Table : MY CATALOG
    --------------------------------------
    |     Name |    Unit | Type | Format |
    --------------------------------------
    | SOURCEID |         | |S20 |    68s |
    |       RA | RADIANS |  >f8 | 25.17e |
    |      DEC | RADIANS |  >f8 | 25.17e |
    |    EPOCH |         |  >f8 | 25.17e |
    |   LAMBDA |         |  >f8 | 25.17e |
    |      ETA |         |  >f8 | 25.17e |
    --------------------------------------

We can sort the table by Declination::

    tsub.sort('DEC')

Finally, let's write out this sub-table as an IPAC table::

    tsub.write('subset.tbl')

Creating a table from scratch
-----------------------------

Making a table from scratch is also very easy::

    t = atpy.Table()
    t.add_column('time', [1., 2., 3])
    t.add_column('flux', [7.2, 1.1, 5.9])

and you can then write this out to e.g. a FITS file::

    t.write('simple.fits')

And much more!
--------------

For more information on how to use ATpy, see the `Documentation <http://atpy.github.com/#documentation>`_.
