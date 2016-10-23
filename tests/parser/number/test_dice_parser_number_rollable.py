# -*- coding: utf-8 -*-

import unittest

from dice_notation.dice import Rollable
from dice_notation.parser import DiceParser

"""
Dice parser tests for purely numeric expressions.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestRollable(unittest.TestCase):
    """
    Tests that the parser can work with pure numeric operations.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_number_rollable(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        result = self.parser.parse("1")

        self.assertTrue(isinstance(result, Rollable))

    def test_add_rollable(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        result = self.parser.parse("1+2")

        self.assertTrue(isinstance(result, Rollable))

    def test_sub_rollable(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        result = self.parser.parse("1-2")

        self.assertTrue(isinstance(result, Rollable))


class TestRoll(unittest.TestCase):
    """
    Tests that the parser can work with pure numeric operations.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_number_rollable(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        result = self.parser.parse("1")

        self.assertEqual(1, result.roll())

    def test_add_rollable(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        result = self.parser.parse("1+2")

        self.assertEqual(3, result.roll())

    def test_sub_rollable(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        result = self.parser.parse("1-2")

        self.assertEqual(-1, result.roll())
