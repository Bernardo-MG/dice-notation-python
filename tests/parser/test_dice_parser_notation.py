# -*- coding: utf-8 -*-

import unittest

from dice_notation.parser.dice import DiceParser
from dice_notation.parser.notation import ConstantOperand

"""
Dice parser tests for purely numeric expressions.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestNode(unittest.TestCase):
    """
    Tests that the parser can work with pure numeric operations.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_longSub_singleWrap(self):
        """
        Tests that numeric additions are done correctly.
        """
        result = self.parser.parse("1-2-3-4-5").operate()

        self.assertFalse(isinstance(result.constant, ConstantOperand))
