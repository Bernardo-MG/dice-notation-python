# -*- coding: utf-8 -*-

import unittest

from dice_notation.dice import RollableDice

"""
Dice class tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestMinimalRoll(unittest.TestCase):
    """
    Tests the Dice roll method.
    """

    def test_empty_rolls0(self):
        """
        Tests that the minimal possible dice returns 1.
        """
        dice = RollableDice(0, 0)

        self.assertEqual(0, dice.roll())

    def test_noQuantity_rolls0(self):
        """
        Tests that the minimal possible dice returns 1.
        """
        dice = RollableDice(0, 6)

        self.assertEqual(0, dice.roll())

    def test_noSides_rolls0(self):
        """
        Tests that the minimal possible dice returns 1.
        """
        dice = RollableDice(1, 0)

        self.assertEqual(0, dice.roll())

    def test_minimal_rolls1(self):
        """
        Tests that the minimal possible dice returns 1.
        """
        dice = RollableDice(1, 1)

        self.assertEqual(1, dice.roll())


class TestRoll(unittest.TestCase):
    """
    Tests the Dice roll method.
    """

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

    def test_singleDie_multipleRoll(self):
        """
        Tests that the result of rolling a die is kept in the expected range.
        """
        dice = RollableDice(1, 6)

        self.assertIsNotNone(dice.roll())
        self.assertIsNotNone(dice.roll())
        self.assertIsNotNone(dice.roll())


class TestRollInvalid(unittest.TestCase):
    """
    Tests the Dice roll method.
    """

    # TODO: Check if these cases should throw exceptions

    def test_negativeQuantity(self):
        """
        Tests that quantity of dice is multiplied by the sides when rolling.
        """
        dice = RollableDice(-1, 1)

        self.assertIsNone(dice.roll())

    def test_negativeSides(self):
        """
        Tests that quantity of dice is multiplied by the sides when rolling.
        """
        dice = RollableDice(1, -1)

        self.assertIsNone(dice.roll())

    def test_noneQuantity(self):
        """
        Tests that quantity of dice is multiplied by the sides when rolling.
        """
        dice = RollableDice(None, 1)

        self.assertIsNone(dice.roll())

    def test_noneSides(self):
        """
        Tests that quantity of dice is multiplied by the sides when rolling.
        """
        dice = RollableDice(1, None)

        self.assertIsNone(dice.roll())
