# -*- coding: utf-8 -*-

import logging
from operator import add, sub

from dice_notation.parser.common import PlyParser
from dice_notation.parser.notation import BinaryOperationExpression, ConstantExpression, \
    DiceExpression

"""
Dice notation parsers.
"""


class DiceParser(PlyParser):
    """
    Dice notation parser.

    It handles the most common version of the dice notation.
    """

    tokens = (
        'DIGIT', 'DSEPARATOR', 'ADD', 'SUB'
    )

    def __init__(self):
        super(DiceParser, self).__init__()
        self._logger = logging.getLogger("DiceParser")

    # Tokens

    t_ADD = r'\+'
    t_DSEPARATOR = r'(d|D)'
    t_SUB = r'-'

    def t_DIGIT(self, t):
        r'\d+'
        try:
            t.value = int(t.value)
        except ValueError:
            self._logger.error("Integer value too large %s", t.value)
            t.value = 0
        # print "parsed number %s" % repr(t.value)
        return t

    def t_error(self, t):
        self._logger.error("Illegal character '%s'", t.value[0])
        t.lexer.skip(1)

    # Parsing rules

    precedence = (
        ('left', 'ADD', 'SUB'),
    )

    def p_statement_expr(self, p):
        'statement : expression'
        p[0] = p[1]
        self._logger.debug("Statement %s", p[0])

    def p_expression_dice(self, p):
        'expression : DIGIT DSEPARATOR DIGIT'
        p[0] = DiceExpression(p[1], p[3])
        self._logger.debug("Dice %s", p[0])

    def p_expression_binop(self, p):
        """
        expression : expression ADD expression
                  | expression SUB expression
        """
        # print [repr(p[i]) for i in range(0,4)]
        if p[2] == '+':
            p[0] = BinaryOperationExpression(add, p[1], p[3])
        elif p[2] == '-':
            p[0] = BinaryOperationExpression(sub, p[1], p[3])
        self._logger.debug("Binary operation %s", p[0])

    def p_expression_digit(self, p):
        'expression : DIGIT'
        if isinstance(p[1], ConstantExpression):
            p[0] = p[1]
        else:
            p[0] = ConstantExpression(p[1])
        self._logger.debug("Constant %s", p[0])

    def p_error(self, p):
        if p:
            self._logger.error("Syntax error at '%s'", p.value)
        else:
            self._logger.error("Syntax error at EOF")
