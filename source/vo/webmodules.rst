.. _`urllib2`: http://docs.python.org/library/urllib2
.. _`urllib`: http://docs.python.org/library/urllib

Core Python Modules
===================

There are two core python modules that provide much of the
functionality necessary to access internet resources from inside your
programs: `urllib2`_ and `urllib`_. You have seen `urllib2` in each of
the prior workshops when downloading example files or datasets. This
is the typical format we have been using. **(You should download this
file now.)** 
::

  import urllib2
  url = 'http://python4astronomers.github.com/_downloads/image_sources.csv'
  open('image_sources.csv', 'wb').write(urllib2.urlopen(url).read())


Static Resource Retrieval
-------------------------   

It is useful to write the example above a bit differently since
readability counts and we want to highlight a few steps.
::

    with open('image_sources.csv','wb') as outfile:
        handler = urllib2.urlopen(url)
        data = handler.read()
        outfile.write(data)
        handler.close()

First, `urllib2`_ has returned a file like object ``handler`` that
points at a specific web resource. Various attributes about the
webpage are available::

    print handler.code
    print handler.headers['content-type']
    
In this particular example the data stream is dumped to a local
variable ``data`` and then to a local file. As demonstrated in the
:doc:`asciitable portion </files/asciitable>` of the :doc:`Reading and
Writing Files </files/files>` class, one alternatively could parse the
returned data stream into a table for further use.
          
Building Queries
----------------

Now we are getting closer to searching for data via python. Building
the query string for a particular data archive begins with reading the
documentation page for that archive and ends with properly encoding
the web address.

Here are some links to these documentation pages for some archives

* `IRSA <http://irsa.ipac.caltech.edu/applications/Gator/GatorAid/irsa/catsearch.html>`_
* `MAST <http://archive.stsci.edu/vo/mast_services.html>`_

and the service url for these are:

* (IRSA) http://irsa.ipac.caltech.edu/cgi-bin/Gator/nph-query
* (MAST) http://archive.stsci.edu/hst/search.php

Here is a very simple query example.
::

    # say we want to query MAST for images
    url = 'http://archive.stsci.edu/hst/search.php'
    # make a dictionary of search parameters
    p = {}
    p['RA']=53.084
    p['DEC']=-27.873
    p['radius']=1.0
    p['max_records']=10
    p['outputformat']='CSV'


The `urllib`_ module takes care of encoding the parameters
::

    # encode it
    e_p = urllib.urlencode(p)


    
.. warning::

    Nothing I've shown actually checks that the data expected is the
    data retrieved. See also warnings in the documentation for
    `urllib2`_ and `urllib`_ about ``https`` transactions. As with
    everything web based, you should implement assertions or tests to
    check your results before continuing.

  