# -*- coding: utf-8 -*-

import unittest

from dice_notation.dice import Rollable
from dice_notation.parser import DiceParser

"""
Dice parser tests for numeric expressions, validating the output class.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestRollableMixedBinaryOp(unittest.TestCase):
    """
    Tests that mixed numeric binary operation expressions return instances of Rollable.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_addAndSub_rollable(self):
        """
        Tests that parsing numeric additions followed by subtractions returns a Rollable.
        """
        result = self.parser.parse("1+2-3")

        self.assertTrue(isinstance(result, Rollable))

    def test_subAndAdd_rollable(self):
        """
        Tests that parsing numeric subtractions followed by additions returns a Rollable.
        """
        result = self.parser.parse("3-1+2")

        self.assertTrue(isinstance(result, Rollable))


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
        result = self.parser.parse("1+2-3")

        self.assertEqual(3, result.roll())

    def test_subAndAdd_roll(self):
        """
        Tests that rolling a parsed numeric subtractions followed by additions returns the expected value.
        """
        result = self.parser.parse("3-1+2")

        self.assertEqual(-1, result.roll())
