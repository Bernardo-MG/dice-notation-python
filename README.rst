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
    :target: http://docs.bernardomg.com/dice-notation-python
    :alt: Dice Notation Tools for Python latest documentation
.. image:: https://img.shields.io/badge/docs-develop-blue.svg
    :target: http://docs.bernardomg.com/development/dice-notation-python
    :alt: Dice Notation Tools for Python development documentation

Features
--------

- Ply-based parser to generate objects for dice notation
- Easy-to-use objects to handle the notation, just call the 'roll' method
- Classes to support plain dice

Documentation
-------------

Documentation sources are included with the project, and used to generate the
documentation sites:

- The `latest docs`_ are always generated for the latest release, kept in the 'master' branch
- The `development docs`_ are generated from the latest code in the 'develop' branch

The source files for the docs, a small `Sphinx`_ project, are kept in the 'docs folder.

These can be built if needed:

``python setup.py build_docs``

Prerequisites
~~~~~~~~~~~~~

The project has been tested in the following versions of the interpreter:

- Python 3.6
- Python 3.7
- Python 3.8

All other dependencies are indicated on the requirements.txt file.

These can be installed with:

``pip install --upgrade -r requirements.txt``

Building the grammar
~~~~~~~~~~~~~~~~~~~~

First of all install ANTLR `as told here <https://github.com/antlr/antlr4/blob/master/doc/getting-started.md/>`_.

Afterwards, follow `these indications <https://github.com/antlr/antlr4/blob/master/doc/python-target.md/>`_.

The command to generate the parser will be:

``antlr4 -Dlanguage=Python2 DiceNotation.g4 DiceNotationLexer.g4``

Installing
~~~~~~~~~~

The project is offered as a `Pypi package`_, and using pip is the preferred way
to install it. For this use the following command;

``pip install dice-notation``

If needed, manual installation is possible:

``python setup.py install``

Usage
-----

The application has been coded in Python, and does not require any particular
framework.

To use it just import the parser::

    from dice_notation.parser import DiceParser

And then use it to parse a dice notation expression::

    parser = DiceParser()
    dice = parser.parse('1d6+2')

The result can be accessed just by calling the 'roll' method as many times as
needed, which will generate a new random value each time it is called::

    print(dice.roll())
    print(dice.roll())

Testing
-------

The tests included with the project can be run with:

``python setup.py test``

This will delegate the execution to tox.

It is possible to run just one of the test profiles, in this case the py36 profile:

``python setup.py test -p "py36"``

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
.. _latest docs: http://docs.bernardomg.com/dice-notation-python
.. _development docs: http://docs.bernardomg.com/development/dice-notation-python
.. _Pypi package: https://pypi.python.org/pypi/dice-notation
.. _MIT License: http://www.opensource.org/licenses/mit-license.php
.. _project issues tracker: https://github.com/Bernardo-MG/dice-notation-python/issues
.. _Sphinx: http://sphinx-doc.org/
