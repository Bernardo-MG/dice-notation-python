==============================
Dice Notation Tools for Python
==============================

Created on the late 70s for Dungeons & Dragons, the tabletop notation has
become a standard on tabletop games, defining formulas used to generate random
values with the help of dice.

These are very simple: 2d6+5 means “roll two dice, add their values and then
add the number five to the result”.

--------
Features
--------

- ANTLR-based parser generates objects from dice notation (BNF grammar included)
- Easy-to-use model, just call the 'roll' method
- Classes to support plain dice

.. toctree::
   :hidden:

   acquire
   usage
   code/index
   docs/dice
   docs/grammar
   docs/notation
   docs/parser
