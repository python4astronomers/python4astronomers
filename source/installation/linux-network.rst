.. _`Linux HEAD or CF network`

Linux on HEAD or CF network
===========================

This is the easiest of all because nearly everything is already set up on the
HEAD or CF networks.  


Path configuration
------------------
The main configuration that is needed is to set up your path to use the
correct Python version.  First make a directory and some links::

  mkdir -p ~/.local/bin
  cd ~/.local/bin

HEAD network
^^^^^^^^^^^^
::

  ln -s /usr/local/bin/python ./
  ln -s /usr/local/bin/ipython ./
  ln -s /usr/local/bin/easy_install ./

CF network
^^^^^^^^^^
::

  ln -s /data/astropy/bin/python ./
  ln -s /data/astropy/bin/ipython ./
  ln -s /data/astropy/bin/easy_install ./


Next you need to edit the appropriate shell startup file and insert 
this corresponding command near the end::

======= ===== ============= =======================================
Network Shell File          Command
======= ===== ============= =======================================
HEAD    csh   ~/.cshrc.user   setenv PATH $HOME/.local/bin:$PATH
CF      csh   ~/.myrc         setenv PATH $HOME/.local/bin:$PATH
HEAD/CF bash  ~/.bashrc       export PATH=$HOME/.local/bin:$PATH
======= ===== ============= =======================================

For tcsh use the csh command.

Packages
--------

Now install a few extra packages into your local area (_~/.local/lib/python2.6/site-packages_):

Astro: required
^^^^^^^^^^^^^^^^

  easy_install --user install asciitable
  easy_install --user http://www.stsci.edu/resources/software_hardware/pyfits/pyfits-2.4.0.tar.gz
  easy_install --user http://stsdas.stsci.edu/astrolib/pywcs-1.9-4.4.4.tar.gz
  easy_install --user atpy
  easy_install --user aplpy

Astro: useful
^^^^^^^^^^^^^

  easy_install --user http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz
  easy_install --user http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz
  easy_install --user pyparsing
  easy_install --user pyregion

