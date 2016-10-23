# -*- coding: utf-8 -*-

import sys
import unittest

from dice_notation.parser import DiceParser

"""
Dice parser tests for expressions only containing dice.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestSimpleDice(unittest.TestCase):
    """
    Tests that simple dice expressions can be parsed.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_simpleDice(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        dice = self.parser.parse("1d6")

        self.assertEqual(1, dice.quantity)
        self.assertEqual(6, dice.sides)

    def test_simpleDice_upperCaseSeparator(self):
        """
        Tests that the upper case dice separator can be parsed.
        """
        dice = self.parser.parse("1D6")

        self.assertEqual(1, dice.quantity)
        self.assertEqual(6, dice.sides)

    def test_onesDice(self):
        """
        Tests that dice notation with a single dice and a single side can be parsed.
        """
        dice = self.parser.parse("1d1")

        self.assertEqual(1, dice.quantity)
        self.assertEqual(1, dice.sides)

    def test_zeroQuantity(self):
        """
        Tests that dice notation with zero dice is parsed.
        """
        dice = self.parser.parse("0d6")

        self.assertEqual(0, dice.quantity)
        self.assertEqual(6, dice.sides)

    def test_zeroSides(self):
        """
        Tests that dice notation with zero sides is parsed.
        """
        dice = self.parser.parse("1d0")

        self.assertEqual(1, dice.quantity)
        self.assertEqual(0, dice.sides)

    def test_zerosDice(self):
        """
        Tests that dice notation with zero dice and zero sides is parsed.
        """
        dice = self.parser.parse("0d0")

        self.assertEqual(0, dice.quantity)
        self.assertEqual(0, dice.sides)

    def test_max(self):
        """
        Tests that dice notation with the maximum integer values dice is parsed.
        """
        dice = self.parser.parse(str(sys.maxsize) + "d" + str(sys.maxsize))

        self.assertEqual(sys.maxsize, dice.quantity)
        self.assertEqual(sys.maxsize, dice.sides)
