# -*- coding: utf-8 -*-

import unittest

from dice_notation.parser.dice import DiceParser

"""
Dice parser tests for purely numeric expressions.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


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


class TestNumericBinaryOperation(unittest.TestCase):
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
        result = self.parser.parse("1+2")

        self.assertEqual(3, result)

    def test_sub(self):
        """
        Tests that numeric subtractions are done correctly.
        """
        result = self.parser.parse("3-1")

        self.assertEqual(2, result)
