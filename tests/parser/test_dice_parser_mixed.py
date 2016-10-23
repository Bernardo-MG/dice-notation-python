# -*- coding: utf-8 -*-

import unittest

from dice_notation.dice import Rollable
from dice_notation.parser import DiceParser

"""
Dice parser tests for expressions mixing dice and numbers.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestRollable(unittest.TestCase):
    """
    Tests that mixed expressions return instances of Rollable.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_mixed_addDice(self):
        """
        Tests that parsing a dice addition to a number returns a Rollable.
        """
        result = self.parser.parse("10+1d6")

        self.assertTrue(isinstance(result, Rollable))

    def test_mixed_subDice(self):
        """
        Tests that parsing a dice subtraction to a number returns a Rollable.
        """
        result = self.parser.parse("10-1d6")

        self.assertTrue(isinstance(result, Rollable))

    def test_mixed_addNumber(self):
        """
        Tests that parsing an addition to a dice returns a Rollable.
        """
        result = self.parser.parse("1d6+10")

        self.assertTrue(isinstance(result, Rollable))

    def test_mixed_subNumber(self):
        """
        Tests that parsing a subtraction to a dice returns a Rollable.
        """
        result = self.parser.parse("1d6-10")

        self.assertTrue(isinstance(result, Rollable))
