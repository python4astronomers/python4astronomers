.. include:: ../references.rst

Virtual Observatory
===================

The `COATpy`_ wrapping of `pyvolib`_ exposes a number of different virtual
observatory tools. We will go over each of these in turn.

.. contents::
    :local:

Sesame Name Resolver
--------------------

This is a basic name resolver that returns the position of objects as a
tuple.  You can specify which service you wish to use::

    from coatpy import Sesame
    
    simbad = Sesame(opt='S')

    ned = Sesame(opt='N')

    ned.resolve('M51')
    
    # the services do not agree
    assert simbad.resolve('IC348') == ned.resolve('IC348')

.. note:: Presently the "names" of things have to be URL encoded or the tool
    will not resolve.  Use ``IC+348`` or ``IC348`` instead of ``IC 348``
    
ConeSearch
----------

The cone search option is a standardized interface to one of hundreds
of catalogs. The necessary parameters are:
    
* ``RA``: decimal degrees
* ``DEC``: decimal degrees
* ``SR``: cone radius in decimal degrees

An optional parameter ``VERB`` varies the verbosity of the query response. Only ``VERB=1`` is standardized across all catalogs and returns only the 
positions of objects in the queried catalog.

As with the web queries you can wrap up the parameters in a
dictionary and pass these to the query handler::

    params = {}
    position = simbad.resolve('IC348')
    params.update(zip(('RA','DEC'),position))
    params['SR'] = 1./60.
    params['VERB'] = 3

.. note:: At this point the system breaks down a little bit as we are not
    providing a programmatic tool for discovering catalogs. You have to
    search an online `Directory`_ to find the catalogs you might want. 
    There are work arounds but a handler that wraps this up would be valuable!
    
With the query URL for the Chandra Source Catalog you create a catalog handler 
that wraps the query tools::

    url = "http://heasarc.gsfc.nasa.gov/cgi-bin/vo/cone/coneGet.pl?table=ic348cxo&"
    csc = ConeSearch(url)
    
    with open('csc.xml','wb') as f:
        f.write(csc.getRaw(**params))
        
    data = atpy.Table(f.name,type='vo')
    
    
Siap Image Search
-----------------

The tool for querying image services is::

    from coatpy import Siap
    
The ``Siap`` tool stands for *Simple Image Access Protocol* and as with
``ConeSearch`` the inputs are fairly simple:

* ``RA``: Decimal Degrees
* ``DEC``: Decimal Degrees
* ``SIZE``: An image size in degrees
* ``FORMAT``:  [Optional] default: image/fits (or image/jpeg)

.. note:: Various image archives have appended other query parameters onto
    the SIAP standard to provide additional initial filtering of the images
    returned.   A good example is the `IRSA 2MASS <http://irsa.ipac.caltech.edu/applications/2MASS/IM/docs/siahelp.html>`_ service.  The ``Siap`` tool currently ignores these extra parameters.

.. admonition:: Exercise: find HST images of a young cluster

    In this exercise we will go through the steps necessary for downloading 
    images with ``Siap`` from the Hubble Legacy Archive.

    The first step is to set up the query, which is nearly identical to the
    previous examples.
    ::
    
        import atpy
        from coatpy import Siap, Sesame
    
        simbad = Sesame(opt="S")
    
        url = "http://www.stecf.org/hst-vo/hla_sia?"

        hla = Siap(url)
    
        params = {}
        params['RA'] = simbad.resolve("IC348")[0]
        params['DEC'] = simbad.resolve("IC348")[1]
        params['SIZE'] = 1./60.
        params['FORMAT'] = 'image/fits'

        with open('hst_ic348_images.xml','wb') as f:
            f.write(hla.getRaw(**params))

    The main difference between a catalog and an image query is that an
    image query results in a series of **pointers** to the image files
    that can be examined and filtered before they are downloaded.
    
    images = atpy.Table('hst_ic348_images.xml',type='vo')
    
    
.. admonition:: Exercise: import a 24 micron Spitzer image for a young cluster

    In this exercise we will go through the same exercise but tuned to deal
    with the unique formats provided by the Spitzer Heritage Archive (SHA).
    
    Everything begins the same::
        
        from coatpy import Siap
        
        url = "http://irsa.ipac.caltech.edu/applications/Spitzer/SHA/servlet/DataService?"

        sha = Siap(url)
        
    There are a couple of significant alterations in the input params and in 
    the format of the returned data. The SHA does not POS as object names
    
        params = {}
        params['POS'] = "IC348"
        params['SIZE'] = 1./60.
        
    
.. note:: We have provided a CSV file list of all the current virtual
    observatory standardized image services 
    :download:`here <../downloads/image_sources.csv>` 
    
    