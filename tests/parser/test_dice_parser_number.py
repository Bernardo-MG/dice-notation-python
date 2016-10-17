# -*- coding: utf-8 -*-

import unittest

from dice_notation.parser.dice import DiceParser

"""
Dice parser tests for purely numeric expressions.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestParseNumber(unittest.TestCase):
    """
    Tests that the parser can work with pure numeric operations.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_number(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("5")

        self.assertEqual(5, result)


class TestNumericBinaryOperation(unittest.TestCase):
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


class TestNumericBinaryOperationLong(unittest.TestCase):
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

    def test_longSub(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("1-2-3")

        self.assertEqual(-4, result)

    def test_longerSub(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("1-2-3-4-5")

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
