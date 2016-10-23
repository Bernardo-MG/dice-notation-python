# -*- coding: utf-8 -*-

import unittest

from dice_notation.parser.dice import DiceParser
from dice_notation.parser.notation import ConstantOperand

"""
Dice parser tests validating the returned classes.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class TestNotation(unittest.TestCase):
    """
    Tests that parsed expressions return a notation class.
    """

    def setUp(self):
        """
        Initializes parser.
        """
        self.parser = DiceParser()

    def test_longSub_singleWrap(self):
        """
        Tests that a long subtraction does not wrap the value into more than a single ConstantOperand.
        """
        result = self.parser.parse("1-2-3-4-5").operate()

        self.assertFalse(isinstance(result.constant, ConstantOperand))

    def test_longAdd_singleWrap(self):
        """
        Tests that a long addition does not wrap the value into more than a single ConstantOperand.
        """
        result = self.parser.parse("1+2+3+4+5").operate()

        self.assertFalse(isinstance(result.constant, ConstantOperand))
