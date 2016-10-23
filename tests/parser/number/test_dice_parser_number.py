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
    Tests that the parser can work with pure numeric operations.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_positive(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("5")

        self.assertEqual(5, result)

    def test_zero(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("0")

        self.assertEqual(0, result)

    def test_negative(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("-5")

        # TODO: currently not supported
        # self.assertEqual(-5, result)
