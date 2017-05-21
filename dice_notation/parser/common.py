# -*- coding: utf-8 -*-

import os
from abc import ABCMeta, abstractmethod

import ply.lex as lex
import ply.yacc as yacc

"""
Base classes for parsers.

It contains some interfaces, along a base parser for the parsing library being
used.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'


class Parser(object, metaclass=ABCMeta):
    """
    Interface for implementing parsers.

    It just contains a single method, 'parse', which will receive a value
    and take care of parsing it into another.
    """

    def __init__(self):
        pass

    @abstractmethod
    def parse(self, value):
        raise NotImplementedError('The parse method must be implemented')


class PlyParser(Parser):
    """
    Base class for a lexer/parser that has the rules defined as methods.

    It makes use of Ply for the parsing.
    """

    tokens = ()
    precedence = ()

    def __init__(self, **kw):
        super(PlyParser, self).__init__()
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

        # Builds the lexer and parser
        lex.lex(module=self, debug=self.debug)
        yacc.yacc(module=self,
                  debug=self.debug,
                  debugfile=self.debugfile,
                  tabmodule=self.tabmodule)

    def parse(self, value):
        return yacc.parse(value)
