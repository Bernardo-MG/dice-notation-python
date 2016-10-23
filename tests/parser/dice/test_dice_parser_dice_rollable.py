# -*- coding: utf-8 -*-

import unittest

from dice_notation.dice import Rollable
from dice_notation.parser import DiceParser

"""
Dice parser tests for dice expressions, validating the output class.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestRollable(unittest.TestCase):
    """
    Tests that dice expressions return instances of Rollable.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_simpleDice_rollable(self):
        """
        Tests that parsing simple dice notation returns a Rollable.
        """
        dice = self.parser.parse("1d6")

        self.assertTrue(isinstance(dice, Rollable))

    def test_add_rollable(self):
        """
        Tests that parsing dice notation additions return a Rollable.
        """
        result = self.parser.parse("1d6+2d20")

        self.assertTrue(isinstance(result, Rollable))

    def test_sub_rollable(self):
        """
        Tests that parsing dice notation subtractions return a Rollable.
        """
        result = self.parser.parse("3d12-1D6")

        self.assertTrue(isinstance(result, Rollable))
