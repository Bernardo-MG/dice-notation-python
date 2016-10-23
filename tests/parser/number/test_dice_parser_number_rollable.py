# -*- coding: utf-8 -*-

import unittest

from dice_notation.dice import Rollable
from dice_notation.parser import DiceParser

"""
Dice parser tests for numeric expressions, validating the output class.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestRollable(unittest.TestCase):
    """
    Tests that numeric expressions return instances of Rollable.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_number_rollable(self):
        """
        Tests that parsing numbers returns a Rollable.
        """
        result = self.parser.parse("1")

        self.assertTrue(isinstance(result, Rollable))

    def test_add_rollable(self):
        """
        Tests that parsing numeric additions returns a Rollable.
        """
        result = self.parser.parse("1+2")

        self.assertTrue(isinstance(result, Rollable))

    def test_sub_rollable(self):
        """
        Tests that parsing numeric subtractions returns a Rollable.
        """
        result = self.parser.parse("1-2")

        self.assertTrue(isinstance(result, Rollable))


class TestRoll(unittest.TestCase):
    """
    Tests that rolling the result from parsing numeric expressions returns the expected value.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_number_roll(self):
        """
        Tests that rolling a parsed number returns the expected value.
        """
        result = self.parser.parse("1")

        self.assertEqual(1, result.roll())

    def test_add_roll(self):
        """
        Tests that rolling a parsed numeric addition returns the expected value.
        """
        result = self.parser.parse("1+2")

        self.assertEqual(3, result.roll())

    def test_sub_roll(self):
        """
        Tests that rolling a parsed numeric subtraction returns the expected value.
        """
        result = self.parser.parse("1-2")

        self.assertEqual(-1, result.roll())
