# -*- coding: utf-8 -*-

import os
from abc import ABCMeta, abstractmethod

import ply.lex as lex
import ply.yacc as yacc


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
