.. _python-built-in-types-and-operations:

Python Built-in Types and Operations
====================================

Python supports a number of built-in types and operations. This tutorial covers the most common types, but information about additional types is available `here <http://docs.python.org/library/stdtypes.html>`_

Basic numeric types
-------------------

The basic data numeric types are similar to those found in other languages, including:

* Integers (``int``)::

    >>> i = 1

* Floating point values (``float``)::

    >>> f = 4.3

* Complex values (``complex``)::

    >>> c = complex(4., -1.)

Manipulating these behaves the way you would expect, so an operation (``+``, ``-``, ``/``, ``*``, ``**``, etc.) on two values of the same type produces another value of the same type, while an operation on two values with different types produces a value of the more 'advanced' type:

* Adding two integers gives an integer::

    >>> 1 + 3
    4

* Multiplying two floats gives a float::

    >>> 3. * 2.
    6.0

* Subtracting two complex numbers gives a complex number::

    >>> complex(2.,4.) - complex(1.,6.)
    (1-2j)

* Multiplying an integer with a float gives a float::

    >>> 3 * 9.2
    27.599999999999998  # int * float = float

* Multiplying a float with a complex number gives a complex number::

    >>> 2. * complex(-1.,3.)
    (-2+6j)  # float * complex = complex

* Multiplying an integer and a complex number gives a complex number::

    >>> 8 * complex(-3.3,1)
    (-26.4+8j)  # int * complex = complex

However, there is one case where this happens but is not desirable, and that you should be aware of, which is the division of two integer numbers::

    >>> 3 / 2
    1

This is behavior is widely regarded as a huge design mistake and Python 3.x has been fixed to behave like you would expect. To see how Python 3.x behaves, we can use::

    >>> from __future__ import division

After typing this, we can use the Python 3.x syntax::

    >>> 3 / 2
    1.5

    >>> 3 // 2
    1

Another way to prevent this is to cast at least one of the integers in the division to a ``float``::

    >>> 3 / float(2)
    1.5

Lists, tuples, and sets
-----------------------

There are two types of sequences that appear similar at first glance, both of which can contain inhomogeneous data types:

* Lists (``list``)::

    >>> l = [4, 5.5, "spam"]
    >>> l[0]
    4
    >>> l[1]
    5.5
    >>> l[2]
    'spam'

* Tuples (``tuple``)::

    >>> t = (4, 5.5, "spam")
    >>> t[0]
    4
    >>> t[1]
    5.5
    >>> t[2]
    'spam'

The difference between these two types is that lists are mutable, and tuples are immutable::

    >>> l[0] = 3
    >>> l.append('egg')  # For a full list of methods, type l. then press TAB!
    >>> l.insert(3,'spam')
    >>> l
    [3, 5.5, 'spam', 'spam', 'egg']

    >>> t[0] = 3
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment

There are reasons why tuples are a useful feature (faster and `hashable
<http://docs.python.org/glossary.html#term-hashable>`_ are the two main ones), but for now, it's enough for you to know there is such a difference.

One useful operation with lists and tuples is ``+``, which can be used for concatenation::

    >>> [1,2,3] + [4,5,6]
    [1, 2, 3, 4, 5, 6]

    >>> ('spam', 'egg') + ('more spam','!')
    ('spam', 'egg', 'more spam', '!')

.. note:: Unlike Numpy arrays:

        * Python lists can contain anything, including other lists, objects, or complex data structures.
        * When you slice a Python list it returns a copy.
        * Vector math does not work on lists
            * Multiplying a list by an int ``n`` gives ``n`` copies of the list.
            * Adding another list concatentates.
            * Multiplying by a float gives an error.

Sets (``set``) are a third type of sequence which you can make from a tuple or a list::

    >>> set([1, 2, 3, 2, 'spam', 'egg', 'spam'])
    set([1, 2, 3, 'egg', 'spam'])

Note that duplicate items have been removed. This is the mathematical definition of a set, i.e. a collection of *distinct* objects. The order of the objects is arbitrary (order is not preserved). Various operators can be used to represent set operations::

    >>> set([1,2,3]) - set([3,4])
    set([1, 2])

    >>> set([1,2,3]) & set([3,4])
    set([3])

    >>> set([1,2,3]) | set([3,4])
    set([1, 2, 3, 4])

Strings
-------

Strings (``str``) will be familiar from other programming languages::

    >>> s = "Spam egg spam spam"

You can use either single quotes (``'``), double quotes (``"``), or triple quotes (``'''``) to enclose a string (the last one is used for multi-line strings). To include single or double quotes inside a string, you can either use the opposite quote to enclose the string::

    >>> "I'm"
    "I'm"

    >>> '"hello"'
    '"hello"'

or you can *escape* them::

    >>> 'I\'m'
    "I'm"

    >>> "\"hello\""
    '"hello"'

You can access individual characters or chunks of characters::

    >>> s[5]
    'e'

    >>> s[9:13]
    'spam'

Note that strings are immutable (like tuples), that is you cannot change the value of certain characters without creating a new string::

    >>> s[5] = 'r'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment

As for lists, and tuples, concatenation is done with ``+``::

    >>> "hello," + " " + "world!"
    'hello, world!'

Finally, strings have many methods associated with them, here are a few examples::

    >>> s.upper()
    'SPAM EGG SPAM SPAM'  # An uppercase version of the string

    >>> s.index('egg')
    5  # An integer giving the position of the sub-string

    >>> s.split()
    ['Spam', 'egg', 'spam', 'spam']  # A list of strings

Dictionaries
------------

One of the remaining types are dictionaries (``dict``) which you can think of
as look-up tables::

    >>> d = {'name':'m31', 'ra':10.68, 'dec':41.27}
    >>> d['name']
    'm31'
    >>> d['flux'] = 4.5
    >>> d
    {'flux': 4.5, 'dec': 41.27, 'name': 'm31', 'ra': 10.68}


A note on Python objects
------------------------

Most things in Python are objects.  But what is an object?

Every constant, variable, or function in Python is actually a object with a
type and associated attributes and methods. An *attribute* a property of the
object that you get or set by giving the <object_name> + dot +
<attribute_name>, for example ``img.shape``. A *method* is a function that the
object provides, for example ``img.argmax(axis=0)`` or ``img.min()``.

Use tab completion in IPython to inspect objects and start to understand
attributes and methods. To start off create a list of 4 numbers::

    l = [3, 1, 2, 1]
    l.<TAB>

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
