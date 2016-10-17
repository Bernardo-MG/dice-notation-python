# -*- coding: utf-8 -*-

import unittest

from dice_notation.parser.dice import DiceParser

"""
Dice parser tests for expressions only containing dice.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestParseInvalid(unittest.TestCase):
    """
    Tests that simple dice expressions can be parsed into the Dice class.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_noNumbers(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        result = self.parser.parse("d")

        self.assertIsNone(result)

    def test_noQuantity(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        result = self.parser.parse("d6")

        self.assertIsNone(result)

    def test_noSides(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        result = self.parser.parse("1d")

        self.assertIsNone(result)
