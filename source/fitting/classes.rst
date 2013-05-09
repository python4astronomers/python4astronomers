
Python Classes
--------------

Basics
^^^^^^

Begin by starting IPython with pylab::

  $ ipython --pylab


Classes definitions include the ``class`` declaration, an identifier, and a
colon::

  class MyClass:
      pass

  h = MyClass()

This class ``MyClass`` isn't very interesting since it does not contain any
methods or attributes.  The ``pass`` is simply a placeholder in the class
declaration indicating a no-op.

Class instances are mutable, meaning that attributes and functions can be added
after instantiation::

  print h.msg

There is no attribute ``msg``, so add one::

  h.msg = "Hello World!"
  print h.msg

Create a class with a static string attribute ``msg1`` and a class method
``echo`` to print the attribute.  Comments begin with a ``#`` and extend to the
end of the line::

  class Hello:
      # static attribute string "msg1"
      msg1 = "Hello"
      def echo(self):
          print self.msg1

  print "Hello's msg1:", Hello.msg1
  h = Hello()
  h.echo()
  print h

Create a class with a constructor definition.  Initialize an attribute ``msg2``
at class instance creation time::

  class World:
      # class constructor
      def __init__(self, msg2="World"):
          # attribute "msg2" initialized in constructor
          self.msg2 = msg2
      def echo(self):
          print self.msg2

  w = World()
  w.echo()
  print w


Multiple Inheritance
^^^^^^^^^^^^^^^^^^^^

Create a class that inherits from ``Hello`` and ``World``.  Initialize an
attribute ``msg3`` using attributes from inherited classes.  Override the method
``echo`` to call methods from inherited classes.  Define the ``__str__`` to
return the attribute ``msg3`` when the class instance is printed with
``print``::

  class HelloWorld(Hello, World):
      def __init__(self):
          # self.msg1 is from Hello
	  # self.msg2 is from World
	  # World constructor is needed since msg2 is not static!
          World.__init__(self)
	  self.msg3 = self.msg1 + " " + self.msg2 + "!"
      def echo(self):
          Hello.echo(self)
          World.echo(self)
      def __str__(self):
          return self.msg3

  hw = HelloWorld()
  hw.echo()
  print hw


Class ``HelloWorld`` is of type ``Hello``, ``World``, and ``HelloWorld``::

  isinstance(hw, Hello)
  isinstance(hw, World)
  isinstance(hw, HelloWorld)
  isinstance(hw, MyClass)


Additional Notes on Classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Classes can contain other classes as attributes::

  class HelloWorld:
      def __init__(self, msg="World World"):
          # create Hello and World objects as attributes
          self.h = Hello()
          self.w = World(msg)
      def echo(self):
          # call their echo methods
          self.h.echo()
          self.w.echo()

  hw = HelloWorld()
  hw.echo()

  isinstance(hw, Hello)
  isinstance(hw, HelloWorld)


Classes have special methods that can be defined to correspond to certain
language operators.  Define how a class behaves using the '+' operator::

  class Hello:
      msg = "Hello"
      def __add__(self, lhs):
          print self.msg + lhs.msg

  class World:
      msg = "World"
      def __add__(self, rhs):
          print self.msg + rhs.msg

  Hello() + World()
  World() + Hello()


.. admonition:: Exercise (for the interested reader):

   Define a class ``Powlaw`` that accepts two keyword arguments in its
   constructor: ``index`` and ``norm``.  The keyword arguments are initialized
   as ``index=2.0`` and ``norm=0.01``.  In the class constructor definition, set
   ``index`` and ``norm`` as class attributes.  Define a class method ``calc``
   which takes an argument ``wave`` and computes a power-law on ``wave`` using
   ``index`` and ``norm``.  The ``wave`` argument can be assumed to be a 1-D
   NumPy array object.  ``calc`` should return the calculated result.

.. raw:: html

   <p class="flip0">Click to Show/Hide Solution</p> <div class="panel0">

Answer::

  class Powlaw:
      def __init__(self, index = 2.0, norm = 0.01):
	   self.index = index
	   self.norm = norm
      def calc(self, wave):
           return self.norm*(wave**self.index)

  p = Powlaw()
  p.calc(array([1,2,3]))

.. raw:: html

   </div>
