Python information for CfA
=================================

These instructions apply to the Harvard/Smithsonian Center for Astrophysics.

Using Python the HEAD network
--------------------------------

Using Python on the CF network
-----------------------------------


SciPy, matplotlib (and the rest) in CIAO on HEAD
---------------------------------------------------

First get into CIAO in the usual way::

  source /soft/ciao/bin/ciao.csh         # tcsh
  . /soft/ciao/bin/ciao.sh               # bash

Now set your local installation prefix to a directory of your choosing where
you have write permission and make some directories::

  set prefix=$HOME/ciaopy  # tcsh
  prefix=$HOME/ciaopy      # bash

  mkdir -p $prefix/bin
  mkdir -p $prefix/build
  mkdir -p $prefix/include
  mkdir -p $prefix/lib

Set up a couple of paths.  You'll probably want to do something similar to this
path setup in your shell startup file::

  # tcsh
  setenv PATH $prefix/bin:$PATH  # tcsh
  setenv PYTHONPATH $prefix/lib/python2.7/site-packages

  # bash
  export PATH=$prefix/bin:$PATH  
  export PYTHONPATH=$prefix/lib/python2.7/site-packages

  mkdir -p $PYTHONPATH

Now copy binary versions of the numerical libraries that are needed by SciPy.
These have only been verified to work on CentOS-5 on the HEAD network::

  cd $prefix/lib
  tar xf /proj/sot/ska/export/lapack_blas_atlas_x86-64.tar.gz

Now go to the build directory and untar the source distributions for the SciPy and distribute packages::

  cd $prefix/build
  tar xf /proj/sot/ska/pkgs/scipy-0.10.0.tar.gz
  tar xf /proj/sot/ska/pkgs/distribute-0.6.19.tar.gz

First build and install ``distribute``.  This provides ``setuptools`` and
``easy_install``.  It turns out that in this exercise ``easy_install`` works
better than ``pip`` because it provides a ``--prefix`` option that works.
::

  cd $prefix/build/distribute-0.6.19
  ciaorun python setup.py install --prefix=$prefix

Now set up the configuration file to build SciPy from source::

  cd $prefix/build/scipy-0.10.0

  rm -f site.cfg
  echo "[DEFAULT]" > site.cfg                                                 
  echo "library_dirs = ${prefix}/lib" >> site.cfg                        
  echo "include_dirs = ${prefix}/include" >> site.cfg                    
  echo "[lapack_opt]" >> site.cfg                                             
  echo "libraries = lapack, f77blas, cblas, atlas" >> site.cfg                
  echo "[fftw]" >> site.cfg                                                   
  echo "libraries = fftw3" >> site.cfg                                        

Start building and go get a coffee or read a paper for a little while, hopefully less than a half hour::

  rm -f build.log install.log
  ciaorun python setup.py build --fcompiler=gnu95 >& build.log 
  ciaorun python setup.py install --prefix=$prefix >& install.log

Inspect ``build.log`` and ``install.log`` for errors (e.g. 
``grep -i error build.log``).  If this looks OK then change to 
a different directory and start up ``sherpa`` or ``chips``::

  cd $prefix/build
  sherpa

Now within ``sherpa`` do::

  import scipy
  import scipy.linalg
  print(scipy.__version__)
  print(scipy.linalg.eig([[1,2],[3,4]]))

Now quit and install the rest::

  ciaorun easy_install --verbose --prefix=$prefix matplotlib
  ciaorun easy_install --verbose --prefix=$prefix asciitable
  ciaorun easy_install --verbose --prefix=$prefix pywcs
  ciaorun easy_install --verbose --prefix=$prefix pyfits
  ciaorun easy_install --verbose --prefix=$prefix atpy
  ciaorun easy_install --verbose --prefix=$prefix aplpy
  ciaorun easy_install --verbose --prefix=$prefix nose 

Once again fire up ``sherpa`` or ``chips`` and do::

  import numpy as np
  import matplotlib
  matplotlib.use('TkAgg')
  import matplotlib.pyplot as plt
  import asciitable
  import pyfits
  import pywcs
  import atpy
  import aplpy

  print(np.__version__)

  x = np.linspace(0, 20, 100)
  plt.plot(x, np.sin(x))

Hopefully you are done and have a CIAO Python that you can use for all your analysis!
