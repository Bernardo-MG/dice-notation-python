# -*- coding: utf-8 -*-

import unittest

from dice_notation.parser import DiceParser

"""
Dice parser tests for purely numeric expressions.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestNumber(unittest.TestCase):
    """
    Tests that numeric expressions can be parsed.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_positive(self):
        """
        Tests that positive numbers can be parsed.
        """
        result = self.parser.parse("5").roll()

        self.assertEqual(5, result)

    def test_zero(self):
        """
        Tests that the zero value can be parsed.
        """
        result = self.parser.parse("0").roll()

        self.assertEqual(0, result)

    def test_negative(self):
        """
        Tests that negative numbers can be parsed.
        """
        result = self.parser.parse("-5").roll()

        self.assertEqual(-5, result)
