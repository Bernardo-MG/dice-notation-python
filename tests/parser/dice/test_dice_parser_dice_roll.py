# -*- coding: utf-8 -*-

import sys
import unittest

from dice_notation.parser import DiceParser

"""
Dice parser tests for expressions only containing dice.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestSimpleDice(unittest.TestCase):
    """
    Tests that simple dice expressions can be parsed.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_minimalDice(self):
        """
        Tests that the minimal dice can be rolled.
        """
        result = self.parser.parse("1d1").roll()

        self.assertEqual(1, result)
