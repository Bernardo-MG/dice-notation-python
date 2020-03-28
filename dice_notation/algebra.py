# -*- coding: utf-8 -*-

from dice_notation.dice import Rollable

"""
Algebraic classes.

These allow working with algebraic operations for dice notation.
"""

__author__ = 'Benardo Martínez Garrido'
__license__ = 'MIT'


class BinaryOperation(Rollable):
    """
    A binary operation. Matching an operator with two operands.
    """

    def __init__(self, left, right, operator, operation):
        super(BinaryOperation, self).__init__()
        self._left = left
        self._right = right
        self._operator = operator
        self._operation = operation

    def __str__(self):
        return '%s%s%s' % (self._left, self._operator, self._right)

    def __repr__(self):
        return '<class %s>(left=%r, right=%r, operator=%r)' % \
               (self.__class__.__name__, self._left, self._right, self._operator)

    def roll(self):
        return self._operation(self._left.roll(), self._right.roll())

    @property
    def left(self):
        """
        The left operand.

        :return: the left operand
        """
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        """
        The right operand.

        :return: the right operand
        """
        return self._right

    @right.setter
    def right(self, right):
        self._right = right

    @property
    def operator(self):
        """
        The operator.

        :return: the operator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        self._operator = operator


class Number(Rollable):
    """
    A numeric constant
    """

    def __init__(self, value):
        super(Number, self).__init__()
        self._value = value

    def __str__(self):
        return '%s' % (self._value)

    def __repr__(self):
        return '<class %s>(value=%r)' % \
               (self.__class__.__name__, self._value)

    def roll(self):
        return self._value

    @property
    def value(self):
        """
        The numeric value.

        :return: the numeric value
        """
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
