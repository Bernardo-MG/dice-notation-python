# -*- coding: utf-8 -*-

from dice_notation.dice import Dice, RollableDice, Rollable


class ConstantNode(Rollable):
    def __init__(self, constant):
        super(ConstantNode, self).__init__()
        self._constant = constant

    def __add__(self, other):
        return ConstantNode(self.constant + other)

    def __sub__(self, other):
        return ConstantNode(other - self.constant)

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
        self._function = function
        self._left = left
        self._right = right

    def __eq__(self, other):
        return self.operate() == other

    def __ne__(self, other):
        return self.operate() != other

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
        return self.function(self.left, self.right)

    def roll(self):
        return self.operate()
