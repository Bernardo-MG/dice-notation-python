# Generated from DiceNotation.g4 by ANTLR 4.7.2
from antlr4 import *

import logging
from dice_notation.dice import Dice
from dice_notation.algebra import BinaryOperation, Number

# This class defines a complete listener for a parse tree produced by DiceNotationParser.
class DiceNotationListener(ParseTreeListener):

    def __init__(self):
        super(DiceNotationListener, self).__init__()
        self._logger = logging.getLogger("DiceNotationListener")
        self._nodes = []

    def expression(self):
        expression = None

        self._logger.debug("Checking stack %s for parsed expression", self._nodes)
        if(self._nodes):
            expression = self._nodes.pop()
            self._logger.debug("Got expression %s from stack", expression)
        else:
            self._logger.debug("No expression found")

        return expression

    def binary_operation(self, operators):
        operands = []

        # There are as many operands as operators plus one
        for i in range(0, len(operators)+1):
            operands.append(self._nodes.pop())

        for operator in operators:
            left = operands.pop()
            right = operands.pop()

            if("+" == operator):
                func = lambda a, b: a + b
            elif("-" == operator):
                func = lambda a, b: a - b
            elif("*" == operator):
                func = lambda a, b: a * b
            elif("/" == operator):
                func = lambda a, b: a / b
            else:
                func = None
                self._logger.error("The %s operator is invalid", operator)
            operation = BinaryOperation(left, right, operator, func)
            self._logger.debug("Parsed operation %s", operation)
            operands.append(operation)

        return operands.pop()

    # Enter a parse tree produced by DiceNotationParser#notation.
    def enterNotation(self, ctx):
        self._logger.debug("Entering notation %s", ctx.getText())
        pass

    # Exit a parse tree produced by DiceNotationParser#notation.
    def exitNotation(self, ctx):
        self._logger.debug("Exiting notation %s", ctx.getText())
        pass


    # Enter a parse tree produced by DiceNotationParser#addOp.
    def enterAddOp(self, ctx):
        self._logger.debug("Entering add %s", ctx.getText())
        pass

    # Exit a parse tree produced by DiceNotationParser#addOp.
    def exitAddOp(self, ctx):
        self._logger.debug("Exiting add %s", ctx.getText())
        operators = []
        for operator in ctx.ADDOPERATOR():
            operators.append(operator.getText())
        expression = self.binary_operation(operators)
        self._nodes.append(expression)


    # Enter a parse tree produced by DiceNotationParser#multOp.
    def enterMultOp(self, ctx):
        self._logger.debug("Entering multiplication %s", ctx.getText())
        pass

    # Exit a parse tree produced by DiceNotationParser#multOp.
    def exitMultOp(self, ctx):
        self._logger.debug("Exiting multiplication %s", ctx.getText())
        operators = []
        for operator in ctx.MULTOPERATOR():
            operators.append(operator.getText())
        expression = self.binary_operation(operators)
        self._nodes.append(expression)


    # Enter a parse tree produced by DiceNotationParser#operand.
    def enterOperand(self, ctx):
        self._logger.debug("Entering operand %s", ctx.getText())
        pass

    # Exit a parse tree produced by DiceNotationParser#operand.
    def exitOperand(self, ctx):
        self._logger.debug("Exiting operand %s", ctx.getText())
        pass


    # Enter a parse tree produced by DiceNotationParser#dice.
    def enterDice(self, ctx):
        self._logger.debug("Entering dice %s", ctx.getText())
        pass

    # Exit a parse tree produced by DiceNotationParser#dice.
    def exitDice(self, ctx):
        self._logger.debug("Exiting dice %s", ctx.getText())
        self._logger.debug("Quantity %s, sides %s", ctx.DIGIT()[0], ctx.DIGIT()[1])
        digits = iter(ctx.DIGIT())
        if(len(ctx.DIGIT()) > 1):
            # Contains the quantity of dice
            quantity = int(next(digits).getText())
        else:
            # No quantity of dice defined
            # Defaults to 1
            quantity = 1

        sides = int(next(digits).getText())

        dice = Dice(quantity, sides)
        self._nodes.append(dice)


    # Enter a parse tree produced by DiceNotationParser#number.
    def enterNumber(self, ctx):
        self._logger.debug("Entering number %s", ctx.getText())
        value = Number(int(ctx.getText()))
        self._nodes.append(value)

    # Exit a parse tree produced by DiceNotationParser#number.
    def exitNumber(self, ctx):
        self._logger.debug("Exiting number %s", ctx.getText())
        pass


