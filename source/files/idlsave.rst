:tocdepth: 2

Reading IDL .sav files
======================

IDL is still a very common tool in astronomy. While IDL packages exist to read and write data in simple (ASCII) or standardized file formats (fits), that users of all platforms can use, IDL also offers a binary file format with an undocumented, proprietary structure. However, acess to this file format (usually called ``.sav``) is very simple and convenient in IDL. Therefore, many IDL users dump their data in this way and you might be forced to read ``.sav`` files a collegue has sent you.

Here is an examplary ``.sav`` :download:`file <../downloads/myidlfile.sav>`. 
If you have trouble downloading the file, then use IPython::

    import urllib2
    url = 'http://python4astronomers.github.com/_downloads/myidlfile.sav'
    open('myidlfile.sav', 'wb').write(urllib2.urlopen(url).read())
    ls


What can you do?
    1. Convert your collegue to use a different file format.
    2. Read that file in python.

If you have a relatively recent version (>0.9) of `scipy` then this is a matter of two lines::
    
    from scipy.io.idl import readsav
    data = readsav('myidlfile.sav')

If your scipy is older, then you need to install the package `idlsave <http://astrofrog.github.com/idlsave/>`_ yourself.

In a normal terminal (outside ``ipython``) do::
    
    pip install --upgrade idlsave
    
or, if you install packages as root user on your system::
    
    sudo pip install --upgrade idlsave

Then import the package and read the data::
    
    import idlsave
    data = idlsave.read('myidlfile.sav')
    
.. admonition::  Exercise: Where is your data?

    ``idlsave`` already prints some information on the screen while reading the file. Inspect the object ``data``, find out how you use it and plot
    the ``x`` and ``y`` data in it.

.. raw:: html

   <p class="flip6">Click to Show/Hide Solution</p> <div class="panel6">

    ``data`` is a dictionary and all the variables in the ``.sav`` file are
    fields in this dictionary. You get a list with ``data.keys()``. Then, this
    is easy::
        
        plt.plot(data['x'], data['y'])

.. raw:: html

   </div>

Note that ``idlsave`` cannot write files and that it will fail to read if the ``.sav`` file contains special structures like system variables or compiled IDL code.