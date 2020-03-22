# -*- coding: utf-8 -*-

import unittest

from dice_notation.parser import DiceParser

"""
Dice parser tests for purely numeric addition expressions.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestAdd(unittest.TestCase):
    """
    Tests that numeric addition expressions can be parsed.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_add(self):
        """
        Tests that additions can be parsed, and the result is the expected one.
        """
        result = self.parser.parse("1+2").roll()

        self.assertEqual(3, result)

    def test_add_toNegative(self):
        """
        Tests that additions to a negative value can be parsed, and the result is the expected one.
        """
        result = self.parser.parse("-1+2").roll()

        self.assertEqual(1, result)


class TestAddLong(unittest.TestCase):
    """
    Tests that long numeric addition expressions can be parsed.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_longAdd(self):
        """
        Tests that long additions can be parsed, and the result is the expected one.
        """
        result = self.parser.parse("1+2+3").roll()

        self.assertEqual(6, result)

    def test_longerAdd(self):
        """
        Tests that longer additions can be parsed, and the result is the expected one.
        """
        result = self.parser.parse("1+2+3+4+5").roll()

        self.assertEqual(15, result)
