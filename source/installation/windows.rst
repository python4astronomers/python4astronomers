Windows
========

First download the appropriate 32-bit or 64-bit EPD installer from the `EPD downloads
<http://cxc.cfa.harvard.edu/contrib/python4astronomers>`_ page.  The user name
and password were emailed to the pythonusers mailing list

The follow the instructions for `Getting Started with EPD
<http://www.enthought.com/products/epdgetstart.php?platform=win>`_ for
Windows.  Choose to install for All Users.  

Once installed then follow the
Getting Started page and look at Pylab, Plain Python and see how to write
Python code.

Next open a command window and do the following to install additional packages needed for the workshop::

  cd \Python27\Scripts
  easy_install.exe asciitable
  easy_install.exe http://www.stsci.edu/resources/software_hardware/pyfits/pyfits-2.4.0.tar.gz
  easy_install.exe pywcs
  easy_install.exe atpy
  easy_install.exe aplpy
  easy_install.exe http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz
  easy_install.exe http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz
  easy_install.exe pyparsing
  easy_install.exe pyregion
  
Now run the PyLab application from the Start menu or do
``C:\Python27\Scripts\ipython -pylab``.  Once this is running go back to the
:ref:`installation_test` section to verify that everything is working.
