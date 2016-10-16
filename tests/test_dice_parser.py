# -*- coding: utf-8 -*-

import unittest

from dice_notation.parser.dice import DiceParser

"""
Dice parser tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestParseSimpleDice(unittest.TestCase):
    """
    Tests that simple dice expressions can be parsed into the Dice class.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_simpleDice(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        dice = self.parser.parse("1d6").dice

        self.assertEqual(1, dice.quantity)
        self.assertEqual(6, dice.sides)


class TestParseNumber(unittest.TestCase):
    """
    Tests that the parser can work with pure numeric operations.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_number(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("5")

        self.assertEqual(5, result)


class TestBinaryOperation(unittest.TestCase):
    """
    Tests that the parser can work with pure numeric operations.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_add(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("1+2").roll()

        self.assertEqual(3, result)

    def test_sub(self):
        """
        Tests that numeric subtractions are done correctly.
        """
        result = self.parser.parse("3-1").roll()

        self.assertEqual(2, result)
