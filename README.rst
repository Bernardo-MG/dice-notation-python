==============================
Dice Notation Tools for Python
==============================

This notation is widely used on tabletop games, such as wargames or RPGs, and
was created on the late 70s for Dungeons & Dragons, as a way to allow generating
random values in specific distributions.

With the pass of years it has evolved, and while it never underwent a formal
standarization process a core set of rules is kept among all the variations,
mostly representing dice in a format such as '1d6', and the use of algebra
operations like addition and subtraction.

This project aims to give support to the dice notation, allowing parsing and
operating with it on any Python application.

.. image:: https://badge.fury.io/py/dice-notation.svg
    :target: https://pypi.python.org/pypi/dice-notation
    :alt: Dice Notation Tools for Python Pypi package page

.. image:: https://img.shields.io/badge/docs-release-blue.svg
    :target: http://docs.wandrell.com/dice-notation-python
    :alt: Dice Notation Tools for Python latest documentation
.. image:: https://img.shields.io/badge/docs-develop-blue.svg
    :target: http://docs.wandrell.com/development/dice-notation-python/
    :alt: Dice Notation Tools for Python development documentation

Features
--------

The library contains the following features:

- API for dice and dice notation, along classes to generate values from them
- Parser to create API instances from the notation

Documentation
-------------

Documentation sources are included with the project, and used to generate the
documentation sites:

- The `latest docs`_ are always generated for the latest release, kept in the 'master' branch
- The `development docs`_ are generated from the latest code in the 'develop' branch

You can also create the documentation from the source files, kept in the 'docs'
folder, with the help of `Sphinx`_. For this use the makefile, or the make.bat
file, contained on that folder.

Prerequisites
~~~~~~~~~~~~~

The project has been tested in the following versions of the interpreter:

- Python 2.7
- Python 3.3
- Python 3.4
- Python 3.5
- Pypy
- Pypy 3

All other dependencies are indicated on the requirements.txt file.
The included makefile can install them with the command:

``$ make requirements``

Installing
~~~~~~~~~~

The project is offered as a `Pypi package`_, and using pip is the preferred way
to install it. For this use the following command;

``$ pip install dice-notation``

If manual installation is required, the project includes a setup.py file, along
a makefile allowing direct installation of the library, which can be done with
the following command:

``$ make install``

Usage
-----

The application has been coded in Python, without using any particular
framework.

To use it just import the parser:

    >>> from dice_notation.parser import DiceParser

And then use it to parser a dice notation expression:

    >>> parser = DiceParser()
    >>> dice = parser.parse('1d6+2')

The result can be accessed just by calling the 'roll' method as many times as
needed, which will generate a new random value each time it is called.

    >>> print(dice.roll())
    >>> print(dice.roll())

Collaborate
-----------

Any kind of help with the project will be well received, and there are two main ways to give such help:

- Reporting errors and asking for extensions through the issues management
- or forking the repository and extending the project

Issues management
~~~~~~~~~~~~~~~~~

Issues are managed at the GitHub `project issues tracker`_, where any Github
user may report bugs or ask for new features.

Getting the code
~~~~~~~~~~~~~~~~

If you wish to fork or modify the code, visit the `GitHub project page`_, where
the latest versions are always kept. Check the 'master' branch for the latest
release, and the 'develop' for the current, and stable, development version.

License
-------

The project has been released under the `MIT License`_.

.. _GitHub project page: https://github.com/Bernardo-MG/dice-notation-python
.. _latest docs: http://docs.wandrell.com/dice-notation-python/
.. _development docs: http://docs.wandrell.com/development/dice-notation-python/
.. _Pypi package: https://pypi.python.org/pypi/dice-notation
.. _MIT License: http://www.opensource.org/licenses/mit-license.php
.. _project issues tracker: https://github.com/Bernardo-MG/dice-notation-python/issues
.. _Sphinx: http://sphinx-doc.org/
