.. _`Linux HEAD or CF network`

Installation on Linux HEAD or CF network
========================================

This is the easiest of all because nearly everything is already set up on the
HEAD or CF networks.  

The main configuration that is needed is to set up your path to use the
correct Python version.  First make a directory and some links::

  mkdir -p ~/.local/bin
  cd ~/.local/bin

  # HEAD network
  ln -s /usr/local/bin/python ./
  ln -s /usr/local/bin/ipython ./

  # CF network
  ln -s /data/astropy/bin/python ./
  ln -s /data/astropy/bin/ipython ./

Next you need to edit the appropriate shell startup file and insert 
this corresponding command near the end::

======= ===== ============= =======================================
Network Shell File          Command
======= ===== ============= =======================================
HEAD    csh   ~/.cshrc.user   setenv PATH $HOME/.local/bin:$PATH
CF      csh   ~/.myrc         setenv PATH $HOME/.local/bin:$PATH
HEAD/CF bash  ~/.bashrc       export PATH=$HOME/.local/bin:$PATH
======= ===== ============= =======================================

