# Generated from DiceNotation.g4 by ANTLR 4.7.2
from antlr4 import *

import logging
from dice_notation.dice import Dice

# This class defines a complete listener for a parse tree produced by DiceNotationParser.
class DiceNotationListener(ParseTreeListener):

    def __init__(self):
        super(DiceNotationListener, self).__init__()
        self._logger = logging.getLogger("DiceNotationListener")
        self._nodes = []

    # Enter a parse tree produced by DiceNotationParser#notation.
    def enterNotation(self, ctx):
        self._logger.warning("Entering notation %s", ctx.getText())
        pass

    # Exit a parse tree produced by DiceNotationParser#notation.
    def exitNotation(self, ctx):
        self._logger.warning("Exiting notation %s", ctx.getText())
        pass


    # Enter a parse tree produced by DiceNotationParser#addOp.
    def enterAddOp(self, ctx):
        self._logger.warning("Entering add %s", ctx.getText())
        pass

    # Exit a parse tree produced by DiceNotationParser#addOp.
    def exitAddOp(self, ctx):
        self._logger.warning("Exiting add %s", ctx.getText())
        pass


    # Enter a parse tree produced by DiceNotationParser#multOp.
    def enterMultOp(self, ctx):
        self._logger.warning("Entering multiplication %s", ctx.getText())
        pass

    # Exit a parse tree produced by DiceNotationParser#multOp.
    def exitMultOp(self, ctx):
        self._logger.warning("Exiting multiplication %s", ctx.getText())
        pass


    # Enter a parse tree produced by DiceNotationParser#operand.
    def enterOperand(self, ctx):
        self._logger.warning("Entering operand %s", ctx.getText())
        pass

    # Exit a parse tree produced by DiceNotationParser#operand.
    def exitOperand(self, ctx):
        self._logger.warning("Exiting operand %s", ctx.getText())
        pass


    # Enter a parse tree produced by DiceNotationParser#dice.
    def enterDice(self, ctx):
        self._logger.warning("Entering dice %s", ctx.getText())
        pass

    # Exit a parse tree produced by DiceNotationParser#dice.
    def exitDice(self, ctx):
        self._logger.warning("Exiting dice %s", ctx.getText())
        self._logger.warning("Quantity %s, sides %s", ctx.DIGIT()[0], ctx.DIGIT()[1])
        digits = iter(ctx.DIGIT())
        if(len(ctx.DIGIT()) > 1):
            # Contains the quantity of dice
            quantity = next(digits)
        else:
            # No quantity of dice defined
            # Defaults to 1
            quantity = 1

        sides = next(digits)

        self._nodes.append(Dice(quantity, sides))


    # Enter a parse tree produced by DiceNotationParser#number.
    def enterNumber(self, ctx):
        self._logger.warning("Entering number %s", ctx.getText())
        pass

    # Exit a parse tree produced by DiceNotationParser#number.
    def exitNumber(self, ctx):
        self._logger.warning("Exiting number %s", ctx.getText())
        pass


