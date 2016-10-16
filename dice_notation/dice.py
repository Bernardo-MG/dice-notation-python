# -*- coding: utf-8 -*-

import sys

from random import randint

from abc import ABCMeta, abstractmethod

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

    def __init__(self, quantity, sides):
        self._quantity = quantity
        self._sides = sides

    @property
    def quantity(self):
        """
        The number of dice which compose this group.

        :return: the number of dice
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def sides(self):
        """
        The number of sides each die has.

        All the dice in the group have the same number of sides.

        :return: the number of sides
        """
        return self._sides

    @sides.setter
    def sides(self, sides):
        self._sides = sides

    def roll(self):
        result = 0

        for x in xrange(self._quantity):
            result += randint(1, self._sides)

        return result
