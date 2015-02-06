.. include:: ../references.rst
.. _`Here is an example Directory search.`: http://nvo.stsci.edu/vor10/index.aspx#Table||query_string=IC%20348
.. _`Here is the catalog used in this example.`: http://nvo.stsci.edu/vor10/getRecord.aspx?id=ivo://CDS.VizieR/J/AJ/122/866

Virtual Observatory
===================

The `COATpy`_ wrapping of `pyvolib`_ exposes a number of different virtual
observatory tools. We will go over each of these in turn.

.. contents::
    :local:

Name Position Resolver
----------------------

.. sidebar:: Names of things

    Presently the "names" of things have to be URL encoded or the tool
    will not resolve.  Use ``IC+348`` or ``IC348`` instead of ``IC 348``. 
    Programmatically this looks like::
    
        urllib.quote_plus("IC 348")
    
    This will be fixed in an upcoming update.

``Sesame`` is a basic name resolver that returns the position of objects as a
tuple. You can specify which service you wish to use::

    from coatpy import Sesame
    
    simbad = Sesame(opt='S')

    ned = Sesame(opt='N')

    ned.resolve('M51')
    
    # the services do not agree; doing this will produce an exception.
    assert simbad.resolve('IC348') == ned.resolve('IC348')
    
Catalog Search
--------------

The ``ConeSearch`` tool is a standardized interface to one of hundreds of
catalogs. The necessary parameters are:
    
* ``RA``: decimal degrees
* ``DEC``: decimal degrees
* ``SR``: cone radius in decimal degrees

An optional parameter ``VERB`` varies the verbosity of the query response.  

.. sidebar:: Verbs

    Only ``VERB=1`` is standardized across all catalogs. A ``VERB=1`` query
    returns only the positions of objects found the queried catalog. 
    ``VERB=2`` returns the "default" set of columns chosen by the
    archive.  ``VERB=3`` returns all columns.  Not all services respond
    to ``VERB`` parameters.

As with the web queries you can wrap up the parameters in a dictionary::

    from coatpy import ConeSearch, Sesame

    simbad = Sesame(opt='S')
    
    params = {}
    params['RA'] = simbad.resolve("IC348")[0]
    params['DEC'] = simbad.resolve("IC348")[1]
    params['SR'] = 1./60.
    params['VERB'] = 3

.. sidebar:: Discovering catalogs

    At this point the system breaks down a little bit as we are not providing
    a programmatic tool for discovering catalogs. You have to use an online
    `Directory`_ to search the catalogs you want. `Here is an example
    Directory search.`_ Once a catalog is found, you want to copy the
    "accessURL" from the search table or open the "Full Record" and open the
    "Simple Cone Search" option. `Here is the catalog used in this example.`_
    
enter the query URL for the target catalog (see sidebar), and create a catalog
handler ``ic348cxo`` that wraps the query tool. We use the ``getRaw`` function
of the ConeSearch to retrieve the raw string result that we then dump into a
file and extract back the data using `ATpy`_::

    url = "http://vizier.u-strasbg.fr/viz-bin/votable/-A?-source=J/AJ/122/866&"
    ic348cxo = ConeSearch(url)
    
    with open('ic348cxo.xml','wb') as f:
        f.write(ic348cxo.getRaw(**params))
        
    data = atpy.Table(f.name,type='vo')
    
    
Image Search
------------

``Siap`` is the tool for querying image services is::

    from coatpy import Siap
    
The ``Siap`` acronym stands for *Simple Image Access Protocol* and as with
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

        with open('hla_ic348_images.xml', 'wb') as f:
            f.write(hla.getRaw(**params))


    The main difference between a catalog and an image query is that an image
    query results in a series of **pointers** to the image files that can be
    examined and filtered before the reference files are downloaded. We use
    the `vo <http://stsdas.stsci.edu/astrolib/vo/html/>`_ module to parse the
    results, extracting the table of images that satisfy our query.
    ::
    
        vot = vo.table.parse_single_table('hla_ic348_images.xml')
        image_table = vot.array
        
    The returned array contains **66** fields! 
    ::
        
        print(image_table.dtype.names)
        
    If all we want is the actual data then the important column is **URL**
    while the **filename** column is also useful.
    ::
    
        # just grab the first image returned
        image = image_table[0]
        image_url = image['URL']
        filename = image['filename'] + '.fits'
        
        with open(filename, 'wb') as image_file:
            image_handler = urllib2.urlopen(image_url)
            image_file.write(image_handler.read())
            image_handler.close() 
           
    Continue this exercise by examining the resulting image.

.. raw:: html

   <p class="flip9">Click to Show/Hide Solution</p> <div class="panel9">
    
We use `astropy.io.fits`_ to open the image file and examine its contents.
::

    from astropy.io import fits
    import aplpy
    import matplotlib.pyplot as plt
    
    hdulist = fits.open(filename)

    # check for multiple FITS extensions and their contents
    # in this case the "PRIMARY" header is empty
    for hdu in hdulist:
        print('name: {0}  type: {1}'.format(hdu.name, type(hdu.data)))
    
    fig = plt.figure(figsize=(15, 7))
    f1 = aplpy.FITSFigure(filename, hdu=1, subplot=[0.1,0.1,0.3,0.65], figure=fig)    
    f1.set_tick_labels_font(size='x-small')
    f1.set_axis_labels_font(size='small')
    f1.show_grayscale()
    
    f2 = aplpy.FITSFigure(filename, hdu=2, subplot=[0.4,0.1,0.3,0.65], figure=fig)
    f2.hide_xaxis_label()
    f2.hide_xtick_labels()
    f2.hide_yaxis_label()
    f2.hide_ytick_labels()
    f2.show_colorscale()
    
    f3 = aplpy.FITSFigure(filename, hdu=3, subplot=[0.7,0.1,0.3,0.65], figure=fig)
    f3.hide_xaxis_label()
    f3.hide_xtick_labels()
    f3.hide_yaxis_label()
    f3.hide_ytick_labels()
    f3.show_colorscale(cmap='spring')
