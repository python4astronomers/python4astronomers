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

The ``ConeSearch`` tool is a standardized interface to one of hundreds
of catalogs. The necessary parameters are:
    
* ``RA``: decimal degrees
* ``DEC``: decimal degrees
* ``SR``: cone radius in decimal degrees

An optional parameter ``VERB`` varies the verbosity of the query response.
Only ``VERB=1`` is standardized across all catalogs and returns only the
positions of objects in the queried catalog.

As with the web queries you can wrap up the parameters in a
dictionary and pass these to the query handler::

    from coatpy import ConeSearch
    
    params = {}
    params['RA'] = simbad.resolve("IC348")[0]
    params['DEC'] = simbad.resolve("IC348")[1]
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
    returned.   A good example is the `IRSA 2MASS 
    <http://irsa.ipac.caltech.edu/applications/2MASS/IM/docs/siahelp.html>`_ 
    service.  The ``Siap`` tool currently throws Exceptions on extra parameters.

.. admonition:: Exercise: find HST images of a young cluster

    In this exercise we will go through the steps necessary for downloading 
    images with ``Siap`` from the Hubble Legacy Archive.

    The first step is to set up the query, which is nearly identical to the
    previous examples. 
    ::

        import urllib2    
        from coatpy import Siap, Sesame
        import vo
    
        simbad = Sesame(opt="S")
    
        url = " http://hla.stsci.edu/cgi-bin/acsSIAP.cgi?strict=1"

        hla = Siap(url)
    
        params = {}
        position = simbad.resolve('IC348')
        params.update(zip(('RA', 'DEC'), position))
        params['SIZE'] = 1./60.
        params['FORMAT'] = 'image/fits'

        with open('hla_ic348_images.xml','wb') as f:
            f.write(hla.getRaw(**params))


    The main difference between a catalog and an image query is that an
    image query results in a series of **pointers** to the image files
    that can be examined and filtered before they are downloaded. We use
    the `vo <http://stsdas.stsci.edu/astrolib/vo/html/>`_ to parse the
    results, extracting the table of images that satisfy our query.
    ::
    
        vot = vo.table.parse_single_table('hla_ic348_images.xml')
        image_table = vot.array
        
    The returned array contains **66** fields! But if all we want is the 
    actual data then the important column is **URL**.
    ::
    
        # just grab the first image returned
        image_url = image_table[0]['URL']
        with open('image.fits','wb') as image_file:
            image_handler = urllib2.urlopen(image_url)
            image_file.write(image_handler.read())
            image_handler.close() 
           
.. url = "http://irsa.ipac.caltech.edu/applications/Spitzer/SHA/servlet/DataService?"
    