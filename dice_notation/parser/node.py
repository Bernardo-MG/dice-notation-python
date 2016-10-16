# -*- coding: utf-8 -*-

from dice_notation.dice import Dice, Rollable


class ConstantNode(Rollable):

    def __init__(self, constant):
        super(ConstantNode, self).__init__()
        self._constant = constant

    def __add__(self, other):
        return self.constant + other

    def __sub__(self, other):
        return other - self.constant

    def __radd__(self, other):
        return self.constant + other

    def __rsub__(self, other):
        return other - self.constant

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


class DiceNode(RollableNode):

    def __init__(self, quantity, sides):
        super(DiceNode, self).__init__(Dice(quantity, sides))

    @property
    def dice(self):
        return self.rollable

    @dice.setter
    def dice(self, dice):
        self.rollable = dice


class BinaryOperationNode(Rollable):

    def __init__(self, function, left, right):
        self._function = function
        self._left = left
        self._right = right

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

    def roll(self):
        return self.function(self.left, self.right)
