Linux 
==========================

There are three options for a linux Python installation that we describe:

- System install in /usr/bin and /usr/lib where you have root privilege
- User installation of EPD in a non-system directory without root
- Non-root setup with an existing full-featured Python on the system

System install with root
------------------------

For a modern linux installation such as Ubuntu, the system Python version
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


Non-root setup using virtualenv
---------------------------------------------

If you are using a computer on a system managed network which has Python 2.6 or
2.7 installed along with NumPy, SciPy, matplotlib, and easy_install, then you
might want to look at the following.  This setup assumes you do not have root
privilege and takes advantage of the `virtualenv <http://www.virtualenv.org/>`_
package.  This allows you to install new and updated packages to a virtual
clone of this Python installation without having root.

Assume that the system Python installation is installed in the root directory
``$PYTHONROOT``, so that you find ``python`` and ``easy_install`` in
``$PYTHONROOT/bin``.  Now install ``pip``, ``distribute``, and ``virtualenv``::

  $PYTHONROOT/bin/easy_install --user --upgrade virtualenv

Now use ``virtualenv`` to make a local virtual Python which is a clone of the
system Python but resides in a directory (e.g. ``~/py27``) where you have write
access::

  ~/.local/bin/virtualenv --system-site-packages ~/py27

The ``--system-site-packages`` option tells ``virtualenv`` to make links to all of the
packages that are already installed in the system Python.  In general this is convenient,
but you may want to start with a clean Python installation by leaving out that option.

To use this virtual Python just do:

=====  =========================================
Shell  Command
=====  =========================================
csh      ``source ~/py27/bin/activate.csh``
bash     ``. ~/py27/bin/activate``
=====  =========================================

For convience you might make an alias for these startup commands in your csh or
bash startup file.  Once you've activated the virtual Python environment then
you *do not* use the ``--user`` option in ``easy_install`` or ``pip install``.
All installs will be made in your local environment.

To finish up you need to install ``ipython`` in this virtual environment, even
if it already exists in the system python::

  pip install --upgrade ipython

Quick installation check 
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open a new terminal window and type::

  which ipython

You should see something like the following::

  ~/py27/bin/ipython

