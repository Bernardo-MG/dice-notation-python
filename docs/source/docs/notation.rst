==============
Notation model
==============

The dice notation grammar is meant to allow working with dice notation
expressions, which will be transformed into an equivalent structure by using
a custom model.

As the model user is very simple the structure generated will be a simple
tree, where nodes are connected by the use of operations.

For example, the expression “2d6+1d20+5” would become something like this:

.. image:: ../_static/diagram/dice_notation_tree_example.png
	:alt: Dice notation tree example
