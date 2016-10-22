# -*- coding: utf-8 -*-

import unittest

from dice_notation.dice import Rollable
from dice_notation.parser import DiceParser

"""
Dice parser tests for expressions only containing dice.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestDiceAndNumber(unittest.TestCase):
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

        self.assertTrue(isinstance(result, Rollable))

    def test_mixed_subDice(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        result = self.parser.parse("10-1d6")

        self.assertTrue(isinstance(result, Rollable))

    def test_mixed_addNumber(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        result = self.parser.parse("1d6+10")

        self.assertTrue(isinstance(result, Rollable))

    def test_mixed_subNumber(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        result = self.parser.parse("1d6-10")

        self.assertTrue(isinstance(result, Rollable))

class TestMultipleRoll(unittest.TestCase):
    """
    Tests that simple dice expressions can be parsed into the Dice class.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_mixed_addNumber_multipleRoll(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        result = self.parser.parse("1d6+10")

        self.assertIsNotNone(result.roll())
        self.assertIsNotNone(result.roll())
