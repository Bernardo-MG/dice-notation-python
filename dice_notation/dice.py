# -*- coding: utf-8 -*-

import sys
from abc import ABCMeta, abstractmethod
from random import randint

"""
Dice classes.
"""

__author__ = 'Benardo Martínez Garrido'
__license__ = 'MIT'

if sys.version_info[0] >= 3:
    xrange = range


class Rollable(object):
    """
    Interface for rollable classes.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def roll(self):
        raise NotImplementedError('The roll method must be implemented')


class Dice(Rollable):
    """
    Represents a dice group
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        super(Dice, self).__init__()
        pass

    def __str__(self):
        return '%sd%s' % (self.quantity, self.sides)

    def __repr__(self):
        return '<class %s>(quantity=%r, sides=%r)' % \
               (self.__class__.__name__, self.quantity, self.sides)

    @property
    def quantity(self):
        """
        The number of dice which compose this group.

        :return: the number of dice
        """
        raise NotImplementedError('The quantity getter must be implemented')

    @quantity.setter
    def quantity(self, quantity):
        raise NotImplementedError('The quantity setter must be implemented')

    @property
    def sides(self):
        """
        The number of sides each die has.

        All the dice in the group have the same number of sides.

        :return: the number of sides
        """
        raise NotImplementedError('The sides getter must be implemented')

    @sides.setter
    def sides(self, sides):
        raise NotImplementedError('The sides setter must be implemented')


class RollableDice(Rollable):
    """
    Represents a dice group
    """

    def __init__(self, quantity, sides):
        super(RollableDice, self).__init__()
        self._quantity = quantity
        self._sides = sides

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def sides(self):
        return self._sides

    @sides.setter
    def sides(self, sides):
        self._sides = sides

    def roll(self):
        result = 0

        if self.quantity and self.sides and self.sides > 0:
            for x in xrange(self._quantity):
                result += randint(1, self._sides)

        return result
