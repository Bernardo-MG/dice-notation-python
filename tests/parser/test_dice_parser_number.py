# -*- coding: utf-8 -*-

import unittest

from dice_notation.dice import Rollable
from dice_notation.parser.dice import DiceParser

"""
Dice parser tests for purely numeric expressions.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestNumber(unittest.TestCase):
    """
    Tests that the parser can work with pure numeric operations.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_positive(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("5")

        self.assertEqual(5, result)

    def test_zero(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("0")

        self.assertEqual(0, result)

    def test_negative(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("-5")

        # TODO: currently not supported
        # self.assertEqual(-5, result)


class TestAdd(unittest.TestCase):
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
        result = self.parser.parse("1+2")

        self.assertEqual(3, result)

    def test_add_toNegative(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("-1+2")

        # TODO: currently not supported
        # self.assertEqual(1, result)


class TestSub(unittest.TestCase):
    """
    Tests that the parser can work with pure numeric operations.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_sub_positive(self):
        """
        Tests that numeric subtractions are done correctly.
        """
        result = self.parser.parse("2-1")

        self.assertEqual(1, result)

    def test_sub_negative(self):
        """
        Tests that numeric subtractions are done correctly.
        """
        result = self.parser.parse("1-2")

        self.assertEqual(-1, result)

    def test_sub_zero(self):
        """
        Tests that numeric subtractions are done correctly.
        """
        result = self.parser.parse("1-1")

        self.assertEqual(0, result)

    def test_sub_negatives(self):
        """
        Tests that numeric subtractions are done correctly.
        """
        result = self.parser.parse("-1-1")

        # TODO: Currently not supported
        # self.assertEqual(-2, result)


class TestAddLong(unittest.TestCase):
    """
    Tests that the parser can work with pure numeric operations.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_longAdd(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("1+2+3")

        self.assertEqual(6, result)

    def test_longerAdd(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("1+2+3+4+5")

        self.assertEqual(15, result)


class TestSubLong(unittest.TestCase):
    """
    Tests that the parser can work with pure numeric operations.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_longSub(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("1-2-3")

        # TODO: Maybe it should be "-1-2-3"

        self.assertEqual(-4, result)

    def test_longerSub(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("1-2-3-4-5")

        # TODO: Maybe it should be "-1-2-3-4-5"

        self.assertEqual(-13, result)


class TestNumericBinaryOperationMixed(unittest.TestCase):
    """
    Tests that the parser can work with pure numeric operations.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_addAndSub(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("1+2-3")

        self.assertEqual(0, result)

    def test_subAndAdd(self):
        """
        Tests that numeric subtractions are done correctly.
        """
        result = self.parser.parse("3-1+2")

        self.assertEqual(4, result)


class TestRollable(unittest.TestCase):
    """
    Tests that the parser can work with pure numeric operations.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_number_rollable(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        dice = self.parser.parse("1")

        self.assertTrue(isinstance(dice, Rollable))

    def test_add_rollable(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        dice = self.parser.parse("1+2")

        self.assertTrue(isinstance(dice, Rollable))

    def test_sub_rollable(self):
        """
        Tests that a simple dice notation can be parsed.
        """
        dice = self.parser.parse("1-2")

        self.assertTrue(isinstance(dice, Rollable))
