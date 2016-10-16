# -*- coding: utf-8 -*-

import unittest

from dice_notation.parser.dice import DiceParser

"""
Dice parser tests for expressions only containing dice.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestParseSimpleDice(unittest.TestCase):
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
        dice = self.parser.parse("1d6").dice

        self.assertEqual(1, dice.quantity)
        self.assertEqual(6, dice.sides)

    def test_simpleDice_alternativeSeparator(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        dice = self.parser.parse("1D6").dice

        self.assertEqual(1, dice.quantity)
        self.assertEqual(6, dice.sides)

    def test_minimalDice(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        dice = self.parser.parse("1d1").dice

        self.assertEqual(1, dice.quantity)
        self.assertEqual(1, dice.sides)


class TestDiceBinaryOperation(unittest.TestCase):
    """
    Tests that the parser can work with pure numeric operations.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_add_dice(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("1d6+2d20")

        diceLeft = result.left.dice
        diceRight = result.right.dice

        self.assertEqual(1, diceLeft.quantity)
        self.assertEqual(6, diceLeft.sides)

        self.assertEqual(2, diceRight.quantity)
        self.assertEqual(20, diceRight.sides)

    def test_add_value(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("1d6+2d20")

        result.roll()

    def test_sub_dice(self):
        """
        Tests that numeric subtractions are done correctly.
        """
        result = self.parser.parse("3d12-1D6")

        diceLeft = result.left.dice
        diceRight = result.right.dice

        self.assertEqual(3, diceLeft.quantity)
        self.assertEqual(12, diceLeft.sides)

        self.assertEqual(1, diceRight.quantity)
        self.assertEqual(6, diceRight.sides)

    def test_sub_value(self):
        """
        Tests that numeric subtractions are done correctly.
        """
        result = self.parser.parse("3d12-1D6")

        result.roll()
