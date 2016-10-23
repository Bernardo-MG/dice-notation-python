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

