# -*- coding: utf-8 -*-

import unittest

from dice_notation.dice import Rollable
from dice_notation.parser import DiceParser

"""
Dice parser tests for numeric expressions, validating the output class.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestRollMixedBinaryOp(unittest.TestCase):
    """
    Tests that rolling the result from parsing mixed numeric binary operation expressions returns the expected value.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_addAndSub_roll(self):
        """
        Tests that rolling a parsed numeric additions followed by subtractions returns the expected value.
        """
        result = self.parser.parse("1+2-3").roll()

        self.assertEqual(0, result)

    def test_subAndAdd_roll(self):
        """
        Tests that rolling a parsed numeric subtractions followed by additions returns the expected value.
        """
        result = self.parser.parse("3-1+2").roll()

        self.assertEqual(4, result)
