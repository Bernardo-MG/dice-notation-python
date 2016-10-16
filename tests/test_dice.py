# -*- coding: utf-8 -*-

import unittest

from dice_notation.dice import RollableDice

"""
Dice class tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestRoll(unittest.TestCase):
    """
    Tests the Dice roll method.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        pass

    def test_minimal_rolls1(self):
        """
        Tests that the minimal possible dice returns 1.
        """
        dice = RollableDice(1, 1)

        self.assertEqual(1, dice.roll())

    def test_multipleDice_multiplies(self):
        """
        Tests that quantity of dice is multiplied by the sides when rolling.
        """
        dice = RollableDice(3, 1)

        self.assertEqual(3, dice.roll())

    def test_singleDie_range(self):
        """
        Tests that the result of rolling a die is kept in the expected range.
        """
        dice = RollableDice(1, 6)

        roll = dice.roll()

        self.assertTrue(roll >= dice.quantity)
        self.assertTrue(roll <= dice.sides)

    def test_multipleDie_range(self):
        """
        Tests that the result of rolling multiple dice is kept in the expected
        range.
        """
        dice = RollableDice(3, 6)

        roll = dice.roll()

        self.assertTrue(roll >= dice.quantity)
        self.assertTrue(roll <= (dice.quantity * dice.sides))
