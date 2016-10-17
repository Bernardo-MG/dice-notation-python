# -*- coding: utf-8 -*-

import logging
from dice_notation.dice import Dice, RollableDice, Rollable


class ConstantNode(Rollable):
    def __init__(self, constant):
        super(ConstantNode, self).__init__()
        self._constant = constant
        # If it received a constant node this is unwrapped
        # TODO: Maybe the problem should be fixed somewhere else
        while isinstance(self._constant, ConstantNode):
            self._constant = constant.constant

    def __add__(self, other):
        return ConstantNode(other + self.constant)

    def __sub__(self, other):
        return ConstantNode(self.constant - other)

    def __radd__(self, other):
        return ConstantNode(self.constant + other)

    def __rsub__(self, other):
        return ConstantNode(other - self.constant)

    def __lt__(self, other):
        return self.constant < other

    def __le__(self, other):
        if isinstance(other, ConstantNode):
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
        if isinstance(other, ConstantNode):
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
        return self._constant

    @constant.setter
    def constant(self, constant):
        self._constant = constant

    def roll(self):
        return self.constant


class RollableNode(Rollable):
    def __init__(self, rollable):
        super(RollableNode, self).__init__()
        self._rollable = rollable

    def __add__(self, other):
        return ConstantNode(self.roll() + other)

    def __sub__(self, other):
        return ConstantNode(other - self.roll())

    def __radd__(self, other):
        return ConstantNode(self.roll() + other)

    def __rsub__(self, other):
        return ConstantNode(other - self.roll())

    def __str__(self):
        return '%s' % (self._rollable)

    def __repr__(self):
        return '<class %s>(rollable=%r)' % \
               (self.__class__.__name__, self._rollable)

    @property
    def rollable(self):
        """
        The rollable value stored in the node.

        :return: the number of dice
        """
        return self._rollable

    @rollable.setter
    def rollable(self, rollable):
        self._rollable = rollable

    def roll(self):
        return self.rollable.roll()


class DiceNode(RollableNode, Dice):
    def __init__(self, quantity, sides):
        super(DiceNode, self).__init__(RollableDice(quantity, sides))

    def __str__(self):
        return '%sd%s' % (self.quantity, self.sides)

    def __repr__(self):
        return '<class %s>(quantity=%r, sides=%r)' % \
               (self.__class__.__name__, self.quantity, self.sides)

    @property
    def quantity(self):
        return self.rollable.quantity

    @quantity.setter
    def quantity(self, quantity):
        self.rollable.quantity(quantity)

    @property
    def sides(self):
        return self.rollable.sides

    @sides.setter
    def sides(self, sides):
        self.rollable.sides(sides)


class BinaryOperationNode(Rollable):
    def __init__(self, function, left, right):
        super(BinaryOperationNode, self).__init__()
        self._logger = logging.getLogger(self.__class__.__name__)
        self._function = function
        self._left = left
        self._right = right

    def __add__(self, other):
        value = self.operate()
        self._logger.debug("%s + %s", value, other)
        return ConstantNode(other + value)

    def __sub__(self, other):
        value = self.operate()
        self._logger.debug("%s - %s", other, value)
        return ConstantNode(value - other)

    def __radd__(self, other):
        value = self.operate()
        self._logger.debug("(rear) %s + %s", value, other)
        return ConstantNode(value + other)

    def __rsub__(self, other):
        value = self.operate()
        self._logger.debug("(rear) %s - %s", other, value)
        return ConstantNode(other - value)

    def __lt__(self, other):
        return self.operate() < other

    def __le__(self, other):
        if isinstance(other, ConstantNode):
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
        if isinstance(other, ConstantNode):
            return self.operate() >= other.constant
        elif isinstance(other, (int, float)):
            return self.operate() >= other
        else:
            return NotImplemented

    def __str__(self):
        return '%s %s %s' % (self._left, self._function, self._right)

    def __repr__(self):
        return '<class %s>(function=%r, left=%r, right=%r)' % \
               (self.__class__.__name__, self._function, self._left, self._right)

    @property
    def function(self):
        return self._function

    @function.setter
    def function(self, function):
        self._function = function

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right

    def operate(self):
        self._logger.debug("Operating %s", self)
        result = self.function(self.left, self.right)
        self._logger.debug("Operation %s, result %s", self, result)
        return result

    def roll(self):
        return self.operate()
