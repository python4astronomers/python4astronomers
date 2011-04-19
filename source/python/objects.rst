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
  a.__add__           a.__ge__            a.__iter__          a.__repr__          a.append
  a.__class__         a.__getattribute__  a.__le__            a.__reversed__      a.count
  a.__contains__      a.__getitem__       a.__len__           a.__rmul__          a.extend
  a.__delattr__       a.__getslice__      a.__lt__            a.__setattr__       a.index
  a.__delitem__       a.__gt__            a.__mul__           a.__setitem__       a.insert
  a.__delslice__      a.__hash__          a.__ne__            a.__setslice__      a.pop
  a.__doc__           a.__iadd__          a.__new__           a.__sizeof__        a.remove
  a.__eq__            a.__imul__          a.__reduce__        a.__str__           a.reverse
  a.__format__        a.__init__          a.__reduce_ex__     a.__subclasshook__  a.sort

For the most part you can ignore all the ones that begin with ``__`` since
they are generally are internal methods that are not called directly.  At
the end you see useful looking functions like ``append`` or ``sort`` which
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
