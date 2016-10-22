# -*- coding: utf-8 -*-

import unittest

from dice_notation.parser import DiceParser

"""
Dice parser tests for expressions only containing dice.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


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
