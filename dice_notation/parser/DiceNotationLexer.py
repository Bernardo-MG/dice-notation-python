# Generated from DiceNotationLexer.g4 by ANTLR 4.7.2
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\t;\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2")
        buf.write(u"\3\3\6\3\35\n\3\r\3\16\3\36\3\4\3\4\5\4#\n\4\3\5\3\5")
        buf.write(u"\5\5\'\n\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write(u"\13\3\13\3\f\6\f\66\n\f\r\f\16\f\67\3\f\3\f\2\2\r\3\3")
        buf.write(u"\5\4\7\5\t\6\13\2\r\2\17\2\21\2\23\7\25\b\27\t\3\2\4")
        buf.write(u"\4\2FFff\4\2\13\f\17\17\2:\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write(u"\7\3\2\2\2\2\t\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write(u"\3\2\2\2\3\31\3\2\2\2\5\34\3\2\2\2\7\"\3\2\2\2\t&\3\2")
        buf.write(u"\2\2\13(\3\2\2\2\r*\3\2\2\2\17,\3\2\2\2\21.\3\2\2\2\23")
        buf.write(u"\60\3\2\2\2\25\62\3\2\2\2\27\65\3\2\2\2\31\32\t\2\2\2")
        buf.write(u"\32\4\3\2\2\2\33\35\4\62;\2\34\33\3\2\2\2\35\36\3\2\2")
        buf.write(u"\2\36\34\3\2\2\2\36\37\3\2\2\2\37\6\3\2\2\2 #\5\13\6")
        buf.write(u"\2!#\5\r\7\2\" \3\2\2\2\"!\3\2\2\2#\b\3\2\2\2$\'\5\17")
        buf.write(u"\b\2%\'\5\21\t\2&$\3\2\2\2&%\3\2\2\2\'\n\3\2\2\2()\7")
        buf.write(u"-\2\2)\f\3\2\2\2*+\7/\2\2+\16\3\2\2\2,-\7,\2\2-\20\3")
        buf.write(u"\2\2\2./\7\61\2\2/\22\3\2\2\2\60\61\7*\2\2\61\24\3\2")
        buf.write(u"\2\2\62\63\7+\2\2\63\26\3\2\2\2\64\66\t\3\2\2\65\64\3")
        buf.write(u"\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\289\3\2")
        buf.write(u"\2\29:\b\f\2\2:\30\3\2\2\2\7\2\36\"&\67\3\b\2\2")
        return buf.getvalue()


class DiceNotationLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DSEPARATOR = 1
    DIGIT = 2
    ADDOPERATOR = 3
    MULTOPERATOR = 4
    LPAREN = 5
    RPAREN = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'('", u"')'" ]

    symbolicNames = [ u"<INVALID>",
            u"DSEPARATOR", u"DIGIT", u"ADDOPERATOR", u"MULTOPERATOR", u"LPAREN", 
            u"RPAREN", u"WS" ]

    ruleNames = [ u"DSEPARATOR", u"DIGIT", u"ADDOPERATOR", u"MULTOPERATOR", 
                  u"ADD", u"SUB", u"MULT", u"DIV", u"LPAREN", u"RPAREN", 
                  u"WS" ]

    grammarFileName = u"DiceNotationLexer.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(DiceNotationLexer, self).__init__(input, output=output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


