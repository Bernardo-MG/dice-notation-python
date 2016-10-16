# -*- coding: utf-8 -*-

from operator import add, sub

from dice_notation.parser.common import PlyParser
from dice_notation.parser.node import BinaryOperationNode, ConstantNode, \
                                        DiceNode


class DiceParser(PlyParser):
    tokens = (
        'DIGIT', 'DSEPARATOR', 'ADD', 'SUB'
    )

    # Tokens

    t_ADD = r'\+'
    t_DSEPARATOR = r'(d|D)'
    t_SUB = r'-'

    def t_DIGIT(self, t):
        r'\d+'
        try:
            t.value = int(t.value)
        except ValueError:
            print("Integer value too large %s" % t.value)
            t.value = 0
        # print "parsed number %s" % repr(t.value)
        return t

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Parsing rules

    precedence = (
        ('left', 'ADD', 'SUB'),
    )

    def p_statement_expr(self, p):
        'statement : expression'
        p[0] = p[1]

    def p_expression_dice(self, p):
        'expression : DIGIT DSEPARATOR DIGIT'
        p[0] = DiceNode(p[1], p[3])

    def p_expression_binop(self, p):
        """
        expression : expression ADD expression
                  | expression SUB expression
        """
        # print [repr(p[i]) for i in range(0,4)]
        if p[2] == '+':
            p[0] = BinaryOperationNode(add, p[1], p[3])
        elif p[2] == '-':
            p[0] = BinaryOperationNode(sub, p[1], p[3])

    def p_expression_digit(self, p):
        'expression : DIGIT'
        p[0] = ConstantNode(p[1])

    def p_error(self, p):
        if p:
            print("Syntax error at '%s'" % p.value)
        else:
            print("Syntax error at EOF")
