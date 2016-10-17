# -*- coding: utf-8 -*-

import unittest

from dice_notation.parser.dice import DiceParser
from dice_notation.parser.node import ConstantNode

"""
Dice parser tests for purely numeric expressions.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestNumericBinaryOperation(unittest.TestCase):
    """
    Tests that the parser can work with pure numeric operations.
    """

    def setUp(self):
        """
        Here the tests environment would be prepared.
        """
        self.parser = DiceParser()

    def test_longSub_singleWrap(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("1-2-3-4-5").operate()

        # TODO: Add a test to verify this operation returns the value inside a single node

        self.assertFalse(isinstance(result.constant, ConstantNode))
