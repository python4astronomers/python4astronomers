.. _`urllib2`: http://docs.python.org/library/urllib2
.. _`urllib`: http://docs.python.org/library/urllib

Core Modules
============

There are two standard modules that provide much of the functionality
necessary to access internet resources from inside python: `urllib2`_
and `urllib`_. You have seen ``urllib2`` in each of the prior
workshops when downloading example files or datasets, like this::

  import urllib2
  url = 'http://python4astronomers.github.com/_downloads/image_sources.csv'
  open('image_sources.csv', 'wb').write(urllib2.urlopen(url).read())

.. note:: You should download this file now!
    

Webpage Retrieval
-----------------

It is useful to write the example above a bit differently since
readability counts and we want to highlight a few steps.
::

    with open('image_sources.csv','wb') as outfile:
        handler = urllib2.urlopen(url)
        data = handler.read()
        outfile.write(data)
        handler.close()

First, `urllib2`_ has returned a file like object ``handler`` that
points to a specific web resource. Various attributes about the
webpage are available::

    print handler.code
    print handler.headers['content-type']
    
In this particular example the data request is handled after the
initial response has been examined; the data is streamed into a local
variable ``data`` and then saved to a local file. As demonstrated in
the :doc:`asciitable portion </files/asciitable>` of the :doc:`Reading
and Writing Files </files/files>` workshop, one alternatively could
parse the returned data stream into a table for further use.

Building Queries 
----------------

Now we are getting closer to searching for data online via python. 
Traditionally, each data archive has implemented its own set of 
query parameters; more often then not you experience it as a web
form with lots of check and input boxes. Most of the time these web
forms  are simply input wrappers that build a query string and 
process the result. 

Here is a very simple query example: search for HST 
images near M 51. It is worth noting that you have 
to find and read the `MAST HST documentation <http://archive.stsci.edu/vo/mast_services.html>`_ to 
learn which `parameters <http://archive.stsci.edu/vo/general_params.html>`_ are needed to build the query.
 
::

    import urllib2, urllib
    
    # this is the query url for this service. 
    url = 'http://archive.stsci.edu/hst/search.php?'

    # make a dictionary of search parameters
    p = {}
    p['target']="M 51"
    p['radius']=1.0
    p['max_records']=10
    p['outputformat']='CSV'
    p['action']='Search'
  
    # encode the http string
    query = urllib.urlencode(p)
    
    # create the handler
    handler = urllib2.urlopen(url, query)
    
    # check it
    print handler.code
    print handler.headers['content-type']
    
    # save it
    with open('hst_m51.csv','wb') as f:
        f.write(handler.read())        
    
The magic is that `urllib`_ module takes care of encoding the 
parameters using standard HTTP rules. You can compare the input
dictionary key,value pairs with the HTTP url encoding. 
::

    for k,v in p.items():
        print "%30s %10s" % (k,v)

    for i in query.split('&'):
        print "%30s" % i

.. admonition::  Exercise: import WISE catalog data for a young cluster

    In this exerice you will use a different service (IRSA) and
    with a different overall goal for these data. 
    ::

        import atpy, urllib, urllib2
    
        url = "http://irsa.ipac.caltech.edu/cgi-bin/Gator/nph-query?"
        p = {}
        p['spatial'] = "Cone"
        p['objstr'] = "IC 348"
        p['outfmt'] = 1    # IPAC table format
        p['catalog'] = 'wise_prelim_p3as_psd'
        p['radius'] = 300
    
        query = urllib.urlencode(p)
        handler = urllib2.urlopen(url, query)
        raw = handler.read()
        print raw[0:255]
        
        with open('ic348_wise.tbl','wb') as f:
            f.write(raw)

    The challenge is to immediately analyze the results of this query. The
    exercise is to make a simple color-color plot of these objects.
    
    
.. raw:: html

   <p class="flip9">Click to Show/Hide Solution</p> <div class="panel9">

There are MANY ways we have looked at in the workshops for converting
this result to a numpy array::

    t1 = atpy.Table('ic348_wise.tbl',type="ipac")
    
    t2 = asciitable.read(raw, Reader=asciitable.IpacReader)

    t3 = atpy.Table(raw,type='ascii')
    
    fill_values = [('null',numpy.nan)]

    t4 = asciitable.read(raw, Reader=asciitable.IpacReader, \   
        fill_values=fill_values)

    t5 = atpy.Table(raw,type='ascii', fill_values=fill_values)

Its important to realize that YMMV as to how these differ in their output.
For example::

    t = [t1, t2, t3, t4, t5]
    for i in t: 
        c = (type(i), i['j_m_2mass'].dtype,i['tmass_key'].dtype)
        print "%40s%10s%10s" % c

We will just use ``t1`` as the data types are correct. It also preserves
more of the metadata of the query. Just a quick plot.
::

    clf()
    plot(t1['w2mag']-t1['w3mag'],t1['j_m_2mass']-t1['h_m_2mass'],'ro')
    xlabel('W2 - W3')
    ylabel('J - H')
    title(t1.keywords['SKYAREA'],fontsize='small')
    
.. image:: wise_cc.png
   :scale: 50





    
    
.. raw:: html

   </div>



.. admonition:: Read the instructions!

    Because these web interfaces vary from archive to archive it is
    worth emphasizing that building the query string for a particular 
    data archive begins with reading the documentation page 
    for that archive's GET interface.

    Here are some links to these documentation pages for some archives

    * `IRSA <http://irsa.ipac.caltech.edu/applications/Gator/GatorAid/irsa/catsearch.html>`_

    * `MAST <http://archive.stsci.edu/vo/mast_services.html>`_

    and the service url for these are:

    * (IRSA) http://irsa.ipac.caltech.edu/cgi-bin/Gator/nph-query

    * (MAST, HST) http://archive.stsci.edu/hst/search.php

    
.. warning::

    Nothing I've shown actually checks that the data expected is the
    data retrieved. See also warnings in the documentation for
    `urllib2`_ and `urllib`_ about ``https`` transactions. As with
    everything web based, you should implement assertions or tests to
    check your results before continuing.

  