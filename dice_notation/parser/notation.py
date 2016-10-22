# -*- coding: utf-8 -*-

import logging

from dice_notation.dice import RollableDice, Rollable

"""
Dice notation classes.

Used to generate the parsed tree from a dice notation expression. These
expressions will be nodes in that tree.

All the classes are rollable, to allow generating a roll from any point of the
expression.
"""


class ConstantOperand(Rollable):
    """
    Expression for a constant value.

    It just wraps any value, allowing it to interface with the other nodes.

    The value contained in the node is called a constant, but actually it can
    be a mutable type. No validation is applied to the stored object.
    """

    def __init__(self, constant):
        super(ConstantOperand, self).__init__()
        self._constant = constant
        # If it received a constant node this is unwrapped
        # TODO: Maybe this problem should be fixed somewhere else
        while isinstance(self._constant, ConstantOperand):
            self._constant = constant.constant

    def __add__(self, other):
        return ConstantOperand(other + self.constant)

    def __sub__(self, other):
        return ConstantOperand(self.constant - other)

    def __radd__(self, other):
        return ConstantOperand(self.constant + other)

    def __rsub__(self, other):
        return ConstantOperand(other - self.constant)

    def __lt__(self, other):
        return self.constant < other

    def __le__(self, other):
        if isinstance(other, ConstantOperand):
            return self.constant <= other.constant
        elif isinstance(other, (int, float)):
            return self.constant <= other
        else:
            return NotImplemented

    def __eq__(self, other):
        return self.constant == other

    def __ne__(self, other):
        return self.constant != other

    def __gt__(self, other):
        return self.constant > other

    def __ge__(self, other):
        if isinstance(other, ConstantOperand):
            return self.constant >= other.constant
        elif isinstance(other, (int, float)):
            return self.constant >= other
        else:
            return NotImplemented

    def __int__(self):
        return self.constant

    def __str__(self):
        return '%s' % (self._constant)

    def __repr__(self):
        return '<class %s>(constant=%r)' % \
               (self.__class__.__name__, self._constant)

    @property
    def constant(self):
        """
        The stored constant value.

        This can be any type of object.
        :return: the stored value
        """

        return self._constant

    @constant.setter
    def constant(self, constant):
        self._constant = constant

    def roll(self):
        return self.constant


class DiceOperand(RollableDice):
    """
    Expression for a dice.

    It is mostly just its parent class, only adding comparison methods.
    """

    def __init__(self, quantity, sides):
        super(DiceOperand, self).__init__(quantity=quantity, sides=sides)

    def __add__(self, other):
        return ConstantOperand(other + self.roll())

    def __sub__(self, other):
        return ConstantOperand(self.roll() - other)

    def __radd__(self, other):
        return ConstantOperand(self.roll() + other)

    def __rsub__(self, other):
        return ConstantOperand(other - self.roll())

    def __str__(self):
        return '%sd%s' % (self.quantity, self.sides)

    def __repr__(self):
        return '<class %s>(quantity=%r, sides=%r)' % \
               (self.__class__.__name__, self.quantity, self.sides)


class BinaryOperation(Rollable):
    """
    Exprssion for a binary operation.

    Acquiring its value will execute a function with two parameters.
    """

    def __init__(self, function, left, right):
        super(BinaryOperation, self).__init__()
        self._logger = logging.getLogger(self.__class__.__name__)
        self._function = function
        self._left = left
        self._right = right

    def __add__(self, other):
        value = self.operate()
        self._logger.debug("%s + %s", value, other)
        return ConstantOperand(other + value)

    def __sub__(self, other):
        value = self.operate()
        self._logger.debug("%s - %s", other, value)
        return ConstantOperand(value - other)

    def __radd__(self, other):
        value = self.operate()
        self._logger.debug("(rear) %s + %s", value, other)
        return ConstantOperand(value + other)

    def __rsub__(self, other):
        value = self.operate()
        self._logger.debug("(rear) %s - %s", other, value)
        return ConstantOperand(other - value)

    def __lt__(self, other):
        return self.operate() < other

    def __le__(self, other):
        if isinstance(other, ConstantOperand):
            return self.operate() <= other.constant
        elif isinstance(other, (int, float)):
            return self.operate() <= other
        else:
            return NotImplemented

    def __eq__(self, other):
        return self.operate() == other

    def __ne__(self, other):
        return self.operate() != other

    def __gt__(self, other):
        return self.operate() > other

    def __ge__(self, other):
        if isinstance(other, ConstantOperand):
            return self.operate() >= other.constant
        elif isinstance(other, (int, float)):
            return self.operate() >= other
        else:
            return NotImplemented

    def __str__(self):
        return '%s %s %s' % (self._left, self._function, self._right)

    def __repr__(self):
        return '<class %s>(function=%r, left=%r, right=%r)' % \
               (self.__class__.__name__, self._function, self._left,
                self._right)

    @property
    def function(self):
        """
        Returns the function used for the binary operation.
        :return: function used
        """

        return self._function

    @function.setter
    def function(self, function):
        self._function = function

    @property
    def left(self):
        """
        Returns the left sided operand.
        :return:  the left sided operand
        """

        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        """
        Returns the right sided operand.
        :return:  the right sided operand
        """

        return self._right

    @right.setter
    def right(self, right):
        self._right = right

    def operate(self):
        """
        Executes the function using the stored operands.
        :return: the result from executing the function
        """

        self._logger.debug("Operating %s", self)
        result = self.function(self.left, self.right)
        self._logger.debug("Operation %s, result %s", self, result)
        return result

    def roll(self):
        return self.operate()
