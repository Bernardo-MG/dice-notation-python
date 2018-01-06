=====
Usage
=====

To use the parser just import it::

    from dice_notation.parser import DiceParser

And then parse a dice notation expression::

    parser = DiceParser()
    dice = parser.parse('1d6+2')

The result can be accessed just by calling the 'roll' method as many times as
needed, which will generate a new random value each time it is called::

    print(dice.roll())
    print(dice.roll())

-------
Testing
-------

The tests included with the project can be run with:

.. code::

    $ python setup.py test

This will delegate the execution to tox.

It is possible to run just one of the test profiles, in this case the py36 profile:

.. code::

    $ python setup.py test -p "py36"

