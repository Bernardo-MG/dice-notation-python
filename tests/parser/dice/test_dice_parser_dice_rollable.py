# -*- coding: utf-8 -*-

import unittest

from dice_notation.dice import Rollable
from dice_notation.parser import DiceParser

"""
Dice parser tests for expressions only containing dice.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestRollable(unittest.TestCase):
    """
    Tests that the parser can work with pure numeric operations.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_simpleDice_rollable(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        dice = self.parser.parse("1d6")

        self.assertTrue(isinstance(dice, Rollable))

    def test_add_rollable(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("1d6+2d20")

        self.assertTrue(isinstance(result, Rollable))

    def test_sub_rollable(self):
        """
        Tests that numeric subtractions are done correctly.
        """
        result = self.parser.parse("3d12-1D6")

        self.assertTrue(isinstance(result, Rollable))
