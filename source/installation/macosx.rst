.. _Mac_OSX:

Mac OSX
=======

First download the appropriate Mac OSX EPD installer from the `EPD downloads
<http://cxc.cfa.harvard.edu/contrib/python4astronomers>`_ page. The user name
and password were emailed to the pythonusers mailing list.

.. note:: If you are using MacOS X 10.5 or 10.6, we recommend that you install
          the 64-bit version (``epd-7.0-2-macosx-x86_64.dmg``). If you are
          using a PPC mac with MacOS X 10.4, you will need to download a
          special PPC 32-bit version (``epd_py25-4.2.30201-macosx-u.dmg``)

After downloading the disk image, open it, then double-click on EPD.mpkg and
follow the prompts to install. Choose all the defaults for installing (in
particular use the default installation location).

Once installed then follow the `Running Pylab
<http://www.enthought.com/products/epdgetstart.php?platform=mac#pylab>`_,
`Plain Python
<http://www.enthought.com/products/epdgetstart.php?platform=mac#plain>`_ and
the `Writing Python Code
<http://www.enthought.com/products/epdgetstart.php?platform=mac#writing>`_
sections on the `Getting Started with EPD
<http://www.enthought.com/products/epdgetstart.php?platform=mac>`_ page.

Next open a terminal window and do the following::

  easy_install asciitable
  easy_install http://www.stsci.edu/resources/software_hardware/pyfits/pyfits-2.4.0.tar.gz
  easy_install http://stsdas.stsci.edu/astrolib/pywcs-1.9-4.4.4.tar.gz
  easy_install atpy
  easy_install aplpy
  easy_install http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz
  easy_install http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz
  easy_install pyparsing
  easy_install pyregion

Now go back to the :ref:`installation_test` section to verify everything is working.


