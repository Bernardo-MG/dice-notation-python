# -*- coding: utf-8 -*-

import unittest

from dice_notation.parser import DiceParser

"""
Dice parser tests for purely numeric subtraction expressions.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestSub(unittest.TestCase):
    """
    Tests that numeric subtraction expressions can be parsed.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_sub_positive(self):
        """
        Tests that subtractions can be parsed, and the result is the expected one.
        """
        result = self.parser.parse("2-1").roll()

        self.assertEqual(1, result)

    def test_sub_negative(self):
        """
        Tests that subtractions ending in a negative value can be parsed, and the result is the expected one.
        """
        result = self.parser.parse("1-2").roll()

        self.assertEqual(-1, result)

    def test_sub_zero(self):
        """
        Tests that subtractions ending in zero can be parsed, and the result is the expected one.
        """
        result = self.parser.parse("1-1").roll()

        self.assertEqual(0, result)

    def test_sub_negatives(self):
        """
        Tests that subtractions of negative values can be parsed, and the result is the expected one.
        """
        result = self.parser.parse("-1-1").roll()

        self.assertEqual(-2, result)


class TestSubLong(unittest.TestCase):
    """
    Tests that long numeric subtraction expressions can be parsed.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_longSub(self):
        """
        Tests that long subtractions can be parsed, and the result is the expected one.
        """
        result = self.parser.parse("1-2-3").roll()

        # TODO: Maybe it should be "-1-2-3"

        self.assertEqual(-4, result)

    def test_longerSub(self):
        """
        Tests that longer subtractions can be parsed, and the result is the expected one.
        """
        result = self.parser.parse("1-2-3-4-5").roll()

        # TODO: Maybe it should be "-1-2-3-4-5"

        self.assertEqual(-13, result)
