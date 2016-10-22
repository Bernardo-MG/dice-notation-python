# -*- coding: utf-8 -*-

import unittest

from dice_notation.parser import DiceParser

"""
Dice parser tests for purely numeric expressions.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


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
