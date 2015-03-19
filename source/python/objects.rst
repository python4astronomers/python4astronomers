Python Objects - or what's with the periods everywhere?
=========================================================

Most things in Python are objects.  But what is an object?

Every constant, variable, or function in Python is actually a object with a
type and associated attributes and methods.  An *attribute* a property of
the object that you get or set by giving the <object_name> + dot +
<attribute_name>, for example ``img.shape``.  A *method* is a function
that the object provides, for example ``img.argmax(axis=0)`` or ``img.min()``.

Use tab completion in IPython to inspect objects and start to understand
attributes and methods.  To start off create a list of 4 numbers::

  a = [3, 1, 2, 1]
  a.<TAB>

This will show the available attributes and methods for the Python list
``a``.  **Using <TAB>-completion and help is a very efficient way to learn and later
remember object methods!**
::

  In [17]: a.<TAB>
  a.append   a.extend   a.insert   a.remove   a.sort     
  a.count    a.index    a.pop      a.reverse  

Here you see useful looking functions like ``append`` or ``sort`` which
you can get help for and use::

  a.sort
  a.sort?
  a.sort()
  a

You can tell the difference between an attribute and a callable method with
the callable function::

    callable(a.sort)
    [x for x in dir(a) if callable(getattr(a, x)) and not x.startswith('__')]

*Mention classes and objects as class instances?*
