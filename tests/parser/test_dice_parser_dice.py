# -*- coding: utf-8 -*-

import unittest

from dice_notation.dice import Rollable
from dice_notation.parser.dice import DiceParser

"""
Dice parser tests for expressions only containing dice.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestSimpleDice(unittest.TestCase):
    """
    Tests that simple dice expressions can be parsed into the Dice class.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_simpleDice(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        dice = self.parser.parse("1d6")

        self.assertEqual(1, dice.quantity)
        self.assertEqual(6, dice.sides)

    def test_simpleDice_alternativeSeparator(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        dice = self.parser.parse("1D6")

        self.assertEqual(1, dice.quantity)
        self.assertEqual(6, dice.sides)

    def test_onesDice(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        dice = self.parser.parse("1d1")

        self.assertEqual(1, dice.quantity)
        self.assertEqual(1, dice.sides)

    def test_zeroQuantity(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        dice = self.parser.parse("0d6")

        self.assertEqual(0, dice.quantity)
        self.assertEqual(6, dice.sides)

    def test_zeroSides(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        dice = self.parser.parse("1d0")

        self.assertEqual(1, dice.quantity)
        self.assertEqual(0, dice.sides)

    def test_zerosDice(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        dice = self.parser.parse("0d0")

        self.assertEqual(0, dice.quantity)
        self.assertEqual(0, dice.sides)


class TestDiceBinaryOperation(unittest.TestCase):
    """
    Tests that the parser can work with pure numeric operations.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_add(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("1d6+2d20")

        dice_left = result.left
        dice_right = result.right

        self.assertEqual(1, dice_left.quantity)
        self.assertEqual(6, dice_left.sides)

        self.assertEqual(2, dice_right.quantity)
        self.assertEqual(20, dice_right.sides)

    def test_sub(self):
        """
        Tests that numeric subtractions are done correctly.
        """
        result = self.parser.parse("3d12-1D6")

        dice_left = result.left
        dice_right = result.right

        self.assertEqual(3, dice_left.quantity)
        self.assertEqual(12, dice_left.sides)

        self.assertEqual(1, dice_right.quantity)
        self.assertEqual(6, dice_right.sides)


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
