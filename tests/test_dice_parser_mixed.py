# -*- coding: utf-8 -*-

import unittest

from dice_notation.parser.dice import DiceParser

"""
Dice parser tests for expressions only containing dice.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestParseMixed(unittest.TestCase):
    """
    Tests that simple dice expressions can be parsed into the Dice class.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_mixed_addDice(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        result = self.parser.parse("10+1d6")

        result.roll()

    def test_mixed_subDice(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        result = self.parser.parse("10-1d6")

        result.roll()

    def test_mixed_addNumber(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        result = self.parser.parse("1d6+10")

        result.roll()

    def test_mixed_subNumber(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        result = self.parser.parse("1d6-10")

        result.roll()
