.. _python-built-in-types-and-operations:

Python Built-in Types and Operations
====================================

Let's discuss `Python Built-in Types and Operations
<http://docs.python.org/library/stdtypes.html>`_.

Python supports the following built-in types:

- **Numerics**: int float long complex
- **Sequences**: str (string), unicode (string), list, tuple, bytearray, buffer,
  xrange
- **Mappings**: dict
- **Sets**: set, frozenset
- **Files**: file
- **Classes**: class
- **Instances**: class instance (object)
- **Exceptions**: runtime exception (e.g. divide by zero or file not found error)

::

Numeric types
--------------

Python numeric data types behave like you might expect::

  >>> width = 20      # int
  >>> height = 5 * 9  # int
  >>> width * height
  900
  
  >>> height = 5.0 * 9  # int * float => float
  >>> height
  45.0

*There is one important exception*: if you divide two integers the result is truncated to the nearest integer::

  >>> 3 / 2
  1
  >>> 3.0 / 2
  1.5

This is behavior is widely regarded as a huge design mistake and the future
more-perfect Python (Python 3.x) behaves like you would expect.  In fact you can visit the
future today with Python 2.x with this little trick::

  >>> from __future__ import division
  >>> 3 / 2
  1.5
  >>> 3 // 2
  1

Sequences
----------

Str (string)
^^^^^^^^^^^^

Python strings can be enclosed in single or double quotes::

  >>> 'spam eggs'
  'spam eggs'
  >>> 'doesn\'t'
  "doesn't"
  >>> "doesn't"
  "doesn't"
  >>> '"Yes," he said.'
  '"Yes," he said.'
  >>> "\"Yes,\" he said."
  '"Yes," he said.'
  >>> '"Isn\'t," she said.'
  '"Isn\'t," she said.'

It should not surprise you that a string is an object with methods::

  a = 'hello'
  a.<TAB>
  a.__add__          a.__mod__                 a.decode           a.partition
  a.__class__        a.__mul__                 a.encode           a.replace
  a.__contains__     a.__ne__                  a.endswith         a.rfind
  a.__delattr__      a.__new__                 a.expandtabs       a.rindex
  a.__doc__          a.__reduce__              a.find             a.rjust
  a.__eq__           a.__reduce_ex__           a.format           a.rpartition
  a.__format__       a.__repr__                a.index            a.rsplit
  a.__ge__           a.__rmod__                a.isalnum          a.rstrip
  a.__getattribute__ a.__rmul__                a.isalpha          a.split
  a.__getitem__      a.__setattr__             a.isdigit          a.splitlines
  a.__getnewargs__   a.__sizeof__              a.islower          a.startswith
  a.__getslice__     a.__str__                 a.isspace          a.strip
  a.__gt__           a.__subclasshook__        a.istitle          a.swapcase
  a.__hash__         a._formatter_field_name_  a.isupper          a.title
  a.__init__         a._formatter_parser       a.join             a.translate
  a.__le__           a.capitalize              a.ljust            a.upper
  a.__len__          a.center                  a.lower            a.zfill
  a.__lt__           a.count                   a.lstrip           

The most non-obvious feature of Python strings is that they are *immutable*,
meaning that you cannot change a string in place like you might expect::

  >>> a = 'hello world'
  >>> a[3:5]
  'lo'
  >>> a[3:5] = 'XX'
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: 'str' object does not support item assignment
  >>> a[:3] + 'XX' + a[5:]  
  'helXX world'

List
^^^^^^^

The Python ``list`` is a versatile data type which can be written as a list of
comma-separated values (items) between square brackets. List items need not all
have the same type.

  >>> a = ['spam', 'eggs', 100, 1234]
  >>> a
  ['spam', 'eggs', 100, 1234]

Like string indices, list indices start at 0, and lists can be sliced, concatenated and so on::

  >>> a[0]
  'spam'
  >>> a[3]
  1234
  >>> a[-2]
  100
  >>> a[1:-1]
  ['eggs', 100]
  >>> a[:2] + ['bacon', 2*2]
  ['spam', 'eggs', 'bacon', 4]

  >>> a[0] = 'ham'
  >>> a
  ['ham', 'eggs', 100, 1234]

Unlike NumPy arrays:

- Python lists can contain anything, including other lists, objects, or complex data structures.
- When you slice a Python list it returns a copy.
- Vector math does not work on lists:
  - Multiplying a list by an int ``n`` gives ``n`` copies of the list.  
  - Adding another list concatentates.
  - Multiplying by a float gives an error.

::

  >>> b = a[0:2]
  >>> b
  ['ham', 'eggs']
  >>> b[1] = 'chickens'
  >>> a
  ['ham', 'eggs', 100, 1234]
  >>> 3*a[:3] + ['Boo!']
  ['spam', 'eggs', 100, 'spam', 'eggs', 100, 'spam', 'eggs', 100, 'Boo!']

Tuple
^^^^^^^^

A Python ``tuple`` is like an immutable ``list``.  There are reasons why this
is a useful feature (faster and `hashable
<http://docs.python.org/glossary.html#term-hashable>`_ are two biggies), but
for now you should know how to recognize and make a tuple.

  >>> a = (1, 2, 'hello')
  >>> a
  (1, 2, 'hello')
  >>> a[1] = 10
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: 'tuple' object does not support item assignment
  
  >>> b = 1,        # note trailing comma
  >>> b
  (1,)
  >>> c = 1, 2, 3
  >>> c
  (1, 2, 3)
  >>> x, y, z = c
  >>> x, y = y, x   # One step swap

Dict
^^^^^^^^

A Python ``dict`` is fundamentally like an actual dictionary that 
contains a list of unique words (*keys*) each with a definition (*values*)::

  >>> tel = {'jack': 4098, 12.0: 4139}    # key can be any hashable object
  >>> tel['guido'] = 4127
  >>> tel
  {12.0: 4139, 'jack': 4098, 'guido': 4127}
  >>> tel['jack']
  4098
  >>> del tel[12.0]                       # delete from the hash
  >>> tel
  {'jack': 4098, 'guido': 4127}
  >>> tel.keys()
  ['jack', 'guido']
  >>> tel.values()
  [4098, 4127]
  >>> 'guido' in tel
  True

As for lists a ``dict`` can contain arbitrarily complex data structures for
values.
