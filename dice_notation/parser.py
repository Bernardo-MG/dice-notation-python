# -*- coding: utf-8 -*-
import sys

import ply.lex as lex
import ply.yacc as yacc
import os

from abc import ABCMeta, abstractmethod

from dice_notation.dice import Dice


class Parser(object):
    """
    Interface for implementing parsers.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def parse(self, input):
        raise NotImplementedError('The parse method must be implemented')


class PlyParser(Parser):
    """
    Base class for a lexer/parser that has the rules defined as methods
    """
    tokens = ()
    precedence = ()

    def __init__(self, **kw):
        self.debug = kw.get('debug', 0)
        self.names = {}
        try:
            modname = os.path.split(os.path.splitext(__file__)[0])[
                1] + "_" + self.__class__.__name__
        except:
            modname = "parser" + "_" + self.__class__.__name__
        self.debugfile = modname + ".dbg"
        self.tabmodule = modname + "_" + "parsetab"
        # print self.debugfile, self.tabmodule

        # Build the lexer and parser
        lex.lex(module=self, debug=self.debug)
        yacc.yacc(module=self,
                  debug=self.debug,
                  debugfile=self.debugfile,
                  tabmodule=self.tabmodule)

    def parse(self, input):
        return yacc.parse(input)


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
        p[0] = Dice(p[1], p[3])

    def p_expression_binop(self, p):
        """
        expression : expression ADD expression
                  | expression SUB expression
        """
        # print [repr(p[i]) for i in range(0,4)]
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]

    def p_expression_digit(self, p):
        'expression : DIGIT'
        p[0] = p[1]

    def p_error(self, p):
        if p:
            print("Syntax error at '%s'" % p.value)
        else:
            print("Syntax error at EOF")

