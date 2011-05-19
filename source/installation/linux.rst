Linux 
==========================

There are three options for a linux Python installation that we describe:

- System install in /usr/bin and /usr/lib where you have root privilege
- User installation of EPD in a non-system directory without root
- Non-root setup with an existing full-featured Python on the system

System install with root
------------------------

For a modern linux installation such as Ubuntu 10, the system Python version
will be 2.6 or newer and all of the required core packages are available as 
package installs.  The instructions below have been developed and tested with
Ubuntu 10.  Corresponding packages for recent Fedora are probably available but
this has not been verified.  In this case you will NOT use the Enthought Python
Distribution.

The benefit of using a root install via the system package manager is that it
is simple and all dependencies are managed for you.  The downside is that the
package versions tend to be older and so you don't keep up with the latest
code development.  In Ubuntu 10 the core packages (NumPy, Matplotlib) are a
year or so out of date.  Unless you are really pushing for the latest features,
the older stable versions will work perfectly well.

Install the core packages for analysis with the following::

  sudo apt-get install python-dev
  sudo apt-get install ipython
  sudo apt-get install python-numpy
  sudo apt-get install python-scipy
  sudo apt-get install python-matplotlib
  sudo apt-get install python-setuptools

Quick installation check 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open a new terminal window and type::

  which ipython

You should see::

  /usr/bin/ipython

.. _linux_nonroot:

User install of EPD without root
--------------------------------

Assuming that you have downloaded the appropriate EPD tar file for your system,
follow the instructions for `Getting Started with EPD
<http://www.enthought.com/products/epdgetstart.php?platform=linux>`_ for Linux.

Once installed then follow the Getting Started page and look at Pylab and plain
Python.

Next you need to edit the appropriate shell startup file (e.g. ``~/.cshrc`` or
``~/.bash_profile``) and update your path to include the EPD path.  For
instance if you specified to install EPD in ``/home/me/epd7.0`` then the
following will work::

  export PATH=/home/me/epd7.0/bin:$PATH  # bash
  set path=(/home/me/epd7.0/bin $path)   # csh or tcsh

Quick installation check 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open a new terminal window and type::

  which ipython

You should see (where ``/home/me/epd7.0`` is replaced by your installation root
path)::

  /home/me/epd7.0/bin/ipython  

Alternate non-root setup with existing Python
---------------------------------------------

If you are using a computer on a system managed network which has Python 2.6 or
2.7 installed along with NumPy, SciPy, IPython, and matplotlib, then you might
want to look at the following.  This setup assumes you do not have root
privilege.

The main configuration that is needed is to set up your path to use the correct
Python version. Assume that the Python installation is installed in the root
directory ``$PYTHONROOT``, so that you find ``python`` and ``ipython`` in
``$PYTHONROOT/bin``.

Update path
^^^^^^^^^^^^^^
There are a couple of ways to do this.

Option A: put $PYTHONROOT in path
##################################

Put ``$PYTHONROOT/bin`` directly in your path:

===== ============= =========================================
Shell File          Command
===== ============= =========================================
csh   ~/.myrc         ``set path=($PYTHONROOT/bin $path)``
bash  ~/.bashrc       ``export PATH=$PYTHONROOT/bin:$PATH``
===== ============= =========================================

Option B: put ~/.local/bin in path
####################################

A slight variation occurs if the $PYTHONROOT path is actually a directory with
a bunch of other stuff that you might not want at the top of your path.  This
is the situation on a system-managed network at the Harvard CfA: the "modern"
Python 2.6 installation is in /usr/local/bin, but this happens to have a lot of
other stuff that is not expected to be in front of /usr/bin by the system
managers.  Hence putting /usr/local/bin first is risky.

In this case we make an end run and put links into a special directory
``~/.local``, which is basically a private user version of /usr/local.

  mkdir -p ~/.local/bin
  cd ~/.local/bin
  ln -s $PYTHONROOT/bin/python ./
  ln -s $PYTHONROOT/bin/ipython ./
  ln -s $PYTHONROOT/bin/easy_install ./

Now update your shell initialization file:

===== ============= =========================================
Shell File          Command
===== ============= =========================================
csh   ~/.cshrc.user   ``set path=($HOME/.local/bin $path)``
bash  ~/.bashrc       ``export PATH=$HOME/.local/bin:$PATH``
===== ============= =========================================

Quick installation check 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open a new terminal window and type::

  which ipython

You should see one of the following two (for options A and B respectively)::

  $PYTHONPATH/bin/ipython    # option A
  $HOME/.local/bin/ipython   # option B

