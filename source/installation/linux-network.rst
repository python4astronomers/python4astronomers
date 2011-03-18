Linux on HEAD or CF network
===========================

This is the easiest of all because nearly everything is already set up on the
HEAD or CF networks.  


Path configuration
------------------
The main configuration that is needed is to set up your path to use the
correct Python version. 

For the HEAD network (but *not* the CF network) you need to make a local bin directory with links to
three executables that are found in ``/usr/local/bin``.  Do the following::

  mkdir -p ~/.local/bin
  cd ~/.local/bin
  ln -s /usr/local/bin/python ./
  ln -s /usr/local/bin/ipython ./
  ln -s /usr/local/bin/easy_install ./

.. Note:: You might ask why not just put
   ``/usr/local/bin`` at the head of your PATH?  The answer is that there are 
   many executables in /usr/local/bin that will override their counterparts
   in ``/usr/bin``.  Given current setup on the HEAD network this can
   have unpredictable consequences and it is not recommended.

Next you need to edit the appropriate shell startup file and insert 
this corresponding command near the end:

======= ===== ============= =========================================
Network Shell File          Command
======= ===== ============= =========================================
HEAD    csh   ~/.cshrc.user   ``set path=($HOME/.local/bin $path)``
HEAD    bash  ~/.bashrc       ``export PATH=$HOME/.local/bin:$PATH``
CF      csh   ~/.myrc         ``set path=(/data/astropy/bin $path)``
CF      bash  ~/.bashrc       ``export PATH=/data/astropy/bin:$PATH``
======= ===== ============= =========================================

Additional packages
-----------------------------

Now the extra packages needed for the workshop into your local area
(``~/.local/lib/python2.6/site-packages``) with the following commands::

  easy_install --user asciitable
  easy_install --user http://www.stsci.edu/resources/software_hardware/pyfits/pyfits-2.4.0.tar.gz
  easy_install --user pywcs
  easy_install --user atpy
  easy_install --user aplpy
  easy_install --user http://stsdas.stsci.edu/astrolib/vo-0.6.tar.gz
  easy_install --user http://stsdas.stsci.edu/astrolib/coords-0.37.tar.gz
  easy_install --user pyparsing
  easy_install --user pyregion

Now go back to the :ref:`installation_test` section to verify everything is working.
