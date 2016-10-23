# -*- coding: utf-8 -*-

import unittest

from dice_notation.parser import DiceParser

"""
Dice parser tests for invalid expressions.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestIncompleteDice(unittest.TestCase):
    """
    Tests incomplete dice expressions.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_noNumbers(self):
        """
        Tests that the dice separator can't be parsed.
        """
        result = self.parser.parse("d")

        self.assertIsNone(result)

    def test_noQuantity(self):
        """
        Tests that a dice without quantity can't be parsed.
        """
        result = self.parser.parse("d6")

        # TODO
        # self.assertIsNone(result)

    def test_noSides(self):
        """
        Tests that a dice with no sides can't be parsed.
        """
        result = self.parser.parse("1d")

        self.assertIsNone(result)


class TestInvalidDice(unittest.TestCase):
    """
    Tests invalid expressions.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_negativeQuantity(self):
        """
        Tests that a negative dice can't be parsed.
        """
        result = self.parser.parse("-1d6")

        # TODO
        # self.assertIsNone(result)

    def test_negativeSides(self):
        """
        Tests that a expression with an incomplete dice can't be parsed.
        """
        result = self.parser.parse("1d-6")

        # TODO
        # self.assertIsNone(result)


class TestInvalidNumber(unittest.TestCase):
    """
    Tests invalid numeric expressions.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_doubleNegative(self):
        """
        Tests that a number with two negative markers can't be parsed.
        """
        result = self.parser.parse("--15")

        # TODO
        # self.assertIsNone(result)
