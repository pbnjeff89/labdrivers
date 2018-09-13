#################
Using the drivers
#################

For examples of how to use the various instrument drivers please see 
the example Jupyter notebooks included in the github repository
`(link) <http://github.com/masonlab/labdrivers/tree/master/example_nbs>`_.

Importing the classes
---------------------

The design choice for the `__init__.py` was made to avoid having to memorize all the various package and
file names. In the `__init__.py` file, we imported all the classes. E.g. in the file
`/labdrivers/keithley/__init__.py` we wrote::

    from .keithley2400 import Keithley2400

This enables us to simply write out::

    from labdrivers.keithley import Keithley2400

The namespace of the `keithley` subpackage includes the `Keithley2400` class, so we can go ahead and
import the class without having to reference the file. You *may* write the following, but it is
a bit more unwieldy::

    from labdrivers.keithley.keithley2400 import Keithley2400

To summarize, the second `import` statement is permissible, but not recommended; the first `import` statement
is easier to remember and takes advantage of the structure of the package we set up.