# -*- coding: utf-8 -*-

import unittest

from dice_notation.parser import DiceParser

"""
Dice parser tests for mixed numeric binary operation expressions.

A mixer operation contains additions and subtractions.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestNumericBinaryOperationMixed(unittest.TestCase):
    """
    Tests that mixed numeric binary operation expressions can be parsed.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_addAndSub(self):
        """
        Tests that additions followed by subtractions can be parsed, and the result is the expected one.
        """
        result = self.parser.parse("1+2-3").roll()

        self.assertEqual(0, result)

    def test_subAndAdd(self):
        """
        Tests that subtractions followed by additions can be parsed, and the result is the expected one.
        """
        result = self.parser.parse("3-1+2").roll()

        self.assertEqual(4, result)
