Reading and Writing files in Pure Python
========================================

Reading
-------

We have already talked about :ref:`python-built-in-types-and-operations`, but
there are more types that we did not speak about. One of these is the
``file()`` object which can be used to read or write files.

Let's start off by downloading :download:`this <../downloads/data.txt>` data file, then launching IPython the directory where you have the file::

    $ ipython -pylab

If you have trouble downloading the file, then start up IPython (``ipython -pylab``) and enter::

    import urllib2
    url = 'http://python4astronomers.github.com/_downloads/data.txt'
    open('data.txt', 'wb').write(urllib2.urlopen(url).read())
    ls

Now let's try and get the contents of the file into IPython. We start off by creating a file object::

    f = open('data.txt', 'r')

The ``'r'`` means that the file should be opened in *read* mode (i.e. you will get an error if the file does not exist). Now, simply type::

    f.read()

and you will see something like this::

    >>> f.read()
    'RAJ        DEJ                          Jmag   e_Jmag\n2000 (deg) 2000
    (deg) 2MASS             (mag)  (mag) \n---------- ----------
    ----------------- ------ ------\n010.684737 +41.269035 00424433+4116085
    9.453  0.052\n010.683469 +41.268585 00424403+4116069   9.321
    0.022\n010.685657 +41.269550 00424455+4116103  10.773  0.069\n010.686026
    +41.269226 00424464+4116092   9.299  0.063\n010.683465 +41.269676
    00424403+4116108  11.507  0.056\n010.686015 +41.269630
    00424464+4116106   9.399  0.045\n010.685270 +41.267124
    00424446+4116016  12.070  0.035\n'

The data file has been read in as a single string. Let's try that again::

    >>> f.read()
    ''

What's happened? We read the file, and the file 'pointer' is now sitting at the end of the file, and there is nothing left to read. Let's now try and do something more useful, and capture the contents of the file in a string::

    f = open('data.txt', 'r')  # We need to re-open the file
    data = f.read()

Now ``data`` contains a string::

    >>> type(data)
    <type 'str'>

But what we'd really like to do is read the file line by line. There are several ways to do this, the simplest of which is to use a ``for`` loop in the following way::

    f = open('data.txt', 'r')
    for line in f:
        print repr(line)

Notice the indent before ``print``, which is necessary to indicate that we are inside the loop (there is no ``end for`` in Python). Note that we are using ``repr()`` to show any invisible characters (this will be useful in a minute). The output should now look something like this::

    >>> for line in f:
            print repr(line)

    'RAJ        DEJ                          Jmag   e_Jmag\n'
    '2000 (deg) 2000 (deg) 2MASS             (mag)  (mag) \n'
    '---------- ---------- ----------------- ------ ------\n'
    '010.684737 +41.269035 00424433+4116085   9.453  0.052\n'
    '010.683469 +41.268585 00424403+4116069   9.321  0.022\n'
    '010.685657 +41.269550 00424455+4116103  10.773  0.069\n'
    '010.686026 +41.269226 00424464+4116092   9.299  0.063\n'
    '010.683465 +41.269676 00424403+4116108  11.507  0.056\n'
    '010.686015 +41.269630 00424464+4116106   9.399  0.045\n'
    '010.685270 +41.267124 00424446+4116016  12.070  0.035\n'

Each line is being returned as a string. Notice the ``\n`` at the end of each line - this is a line return character, which indicates the end of a line.

.. note:: You may also come across the following way to read files line by
          line::

              for line in f.readlines():
                  ...

          ``f.readlines()`` actually reads in the whole file and splits it
          into a list of lines, so for large files this can be memory
          intensive. Using::

              for line in f:
                  ...

          instead is more memory efficient because it only reads one line
          at a time.

Now we're reading in a file line by line, what would be really nice would be to get some values out of it.  Let's examine the last line in detail. If we just type ``line`` we should see the last line that was printed in the loop::

    >>> line
    '010.685270 +41.267124 00424446+4116016  12.070  0.035\n'

We can first get rid of the ``\n`` character with::

    >>> line = line.strip()
    >>> line
    '010.685270 +41.267124 00424446+4116016  12.070  0.035'

Next, we can use what we learned about strings and lists to do::

    >>> columns = line.split()
    >>> columns
    ['010.685270', '+41.267124', '00424446+4116016', '12.070', '0.035']

Finally, let's say we care about the source name, and the J band magnitude. We can extract these with::

    >>> name = columns[2]
    >>> j = columns[3]

    >>> name
    '00424446+4116016'

    >>> j
    '12.070'

Note that ``j`` is a string, but if we want a floating point number, we can instead do::

    >>> j = float(columns[3])

One last piece of information we need about files is how we can read a single line. This is done using::

    line = f.readline()

We can put all this together to write a little script to read the data from the file and display the columns we care about to the screen! Here is is::

    # Open file
    f = open('data.txt', 'r')

    # Read and ignore header lines
    header1 = f.readline()
    header2 = f.readline()
    header3 = f.readline()

    # Loop over lines and extract variables of interest
    for line in f:
        line = line.strip()
        columns = line.split()
        name = columns[2]
        j = float(columns[3])
        print name, j

The output should look like this::

    00424433+4116085 9.453
    00424403+4116069 9.321
    00424455+4116103 10.773
    00424464+4116092 9.299
    00424403+4116108 11.507
    00424464+4116106 9.399
    00424446+4116016 12.07

.. admonition::  Exercise

    Try and see if you can understand what the following script is doing::

        f = open('data.txt', 'r')
        header1 = f.readline()
        header2 = f.readline()
        header3 = f.readline()
        data = []
        for line in f:
            line = line.strip()
            columns = line.split()
            source = {}
            source['name'] = columns[2]
            source['j'] = float(columns[3])
            data.append(source)

    After this script is run, how would you access the name and J-band magnitude of the third source?

.. raw:: html

   <p class="flip7">Click to Show/Hide Solution</p> <div class="panel7">

The following line creates an empty list to contain all the data::

    data = []

For each line, we are then creating an empty dictionary and populating it with variables we care about::

    source = {}
    source['name'] = columns[2]
    source['j'] = float(columns[3])

Finally, we append this source to the ``data`` list::

    data.append(source)

Therefore, ``data`` is a list of dictionaries::


    >>> data
    [{'j': 9.453, 'name': '00424433+4116085'},
     {'j': 9.321, 'name': '00424403+4116069'},
     {'j': 10.773, 'name': '00424455+4116103'},
     {'j': 9.299, 'name': '00424464+4116092'},
     {'j': 11.507, 'name': '00424403+4116108'},
     {'j': 9.399, 'name': '00424464+4116106'},
     {'j': 12.07, 'name': '00424446+4116016'}]

You can access the dictionary for the third source with::

    >>> data[2]
    {'j': 10.773, 'name': '00424455+4116103'}

To get the name of this source, you can therefore do::

    >>> data[2]['name']
    '00424455+4116103'

.. raw:: html

   </div>

Writing
-------

To open a file for writing, use::

    f = open('data_new.txt', 'wb')

Then simply use ``f.write()`` to write any content to the file, for example::

    f.write("Hello, World!")

If you want to write multiple lines, you can either give a list of strings to the ``writelines()`` method::

    f.writelines(['spam\n', 'egg\n', 'spam\n'])

or you can write them as a single string::

    f.write('spam\negg\nspam')

To close a file, simply use::

    f.close()

(this also applies to reading files)

.. admonition::  Exercise

    Let's try combining reading and writing. Using at most seven lines, write a script which will read in ``data.txt``, replace any spaces with periods (``.``), and write the result out to a file called ``data_new.txt``.

    Can you do it in a single line? (you can ignore closing the file)

.. raw:: html

   <p class="flip6">Click to Show/Hide Solution</p> <div class="panel6">

Here is a possible solution::

    f1 = open('data.txt', 'r')
    content = f1.read()
    f1.close()

    content = content.replace(' ','.')

    f2 = open('data_new.txt', 'w')
    f2.write(content)
    f2.close()

And a possible one-liner!::

    open('data_new.txt', 'w').write(open('data.txt', 'r').read().replace(' ', '.'))

.. raw:: html

   </div>
