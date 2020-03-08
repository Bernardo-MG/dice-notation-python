# Generated from DiceNotation.g4 by ANTLR 4.7.2
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\t:\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write(u"\2\3\2\3\2\5\2\22\n\2\3\3\3\3\3\3\7\3\27\n\3\f\3\16\3")
        buf.write(u"\32\13\3\3\4\3\4\3\4\7\4\37\n\4\f\4\16\4\"\13\4\3\5\3")
        buf.write(u"\5\3\5\3\5\3\5\3\5\5\5*\n\5\3\6\5\6-\n\6\3\6\5\6\60\n")
        buf.write(u"\6\3\6\3\6\3\6\3\7\5\7\66\n\7\3\7\3\7\3\7\2\2\b\2\4\6")
        buf.write(u"\b\n\f\2\2\2<\2\21\3\2\2\2\4\23\3\2\2\2\6\33\3\2\2\2")
        buf.write(u"\b)\3\2\2\2\n,\3\2\2\2\f\65\3\2\2\2\16\22\5\n\6\2\17")
        buf.write(u"\22\5\f\7\2\20\22\5\4\3\2\21\16\3\2\2\2\21\17\3\2\2\2")
        buf.write(u"\21\20\3\2\2\2\22\3\3\2\2\2\23\30\5\6\4\2\24\25\7\5\2")
        buf.write(u"\2\25\27\5\6\4\2\26\24\3\2\2\2\27\32\3\2\2\2\30\26\3")
        buf.write(u"\2\2\2\30\31\3\2\2\2\31\5\3\2\2\2\32\30\3\2\2\2\33 \5")
        buf.write(u"\b\5\2\34\35\7\6\2\2\35\37\5\b\5\2\36\34\3\2\2\2\37\"")
        buf.write(u"\3\2\2\2 \36\3\2\2\2 !\3\2\2\2!\7\3\2\2\2\" \3\2\2\2")
        buf.write(u"#*\5\n\6\2$*\5\f\7\2%&\7\7\2\2&\'\5\2\2\2\'(\7\b\2\2")
        buf.write(u"(*\3\2\2\2)#\3\2\2\2)$\3\2\2\2)%\3\2\2\2*\t\3\2\2\2+")
        buf.write(u"-\7\5\2\2,+\3\2\2\2,-\3\2\2\2-/\3\2\2\2.\60\7\4\2\2/")
        buf.write(u".\3\2\2\2/\60\3\2\2\2\60\61\3\2\2\2\61\62\7\3\2\2\62")
        buf.write(u"\63\7\4\2\2\63\13\3\2\2\2\64\66\7\5\2\2\65\64\3\2\2\2")
        buf.write(u"\65\66\3\2\2\2\66\67\3\2\2\2\678\7\4\2\28\r\3\2\2\2\t")
        buf.write(u"\21\30 ),/\65")
        return buf.getvalue()


class DiceNotationParser ( Parser ):

    grammarFileName = "DiceNotation.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'('", u"')'" ]

    symbolicNames = [ u"<INVALID>", u"DSEPARATOR", u"DIGIT", u"ADDOPERATOR", 
                      u"MULTOPERATOR", u"LPAREN", u"RPAREN", u"WS" ]

    RULE_startRule = 0
    RULE_addOp = 1
    RULE_multOp = 2
    RULE_operand = 3
    RULE_dice = 4
    RULE_number = 5

    ruleNames =  [ u"startRule", u"addOp", u"multOp", u"operand", u"dice", 
                   u"number" ]

    EOF = Token.EOF
    DSEPARATOR=1
    DIGIT=2
    ADDOPERATOR=3
    MULTOPERATOR=4
    LPAREN=5
    RPAREN=6
    WS=7

    def __init__(self, input, output=sys.stdout):
        super(DiceNotationParser, self).__init__(input, output=output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartRuleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DiceNotationParser.StartRuleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def dice(self):
            return self.getTypedRuleContext(DiceNotationParser.DiceContext,0)


        def number(self):
            return self.getTypedRuleContext(DiceNotationParser.NumberContext,0)


        def addOp(self):
            return self.getTypedRuleContext(DiceNotationParser.AddOpContext,0)


        def getRuleIndex(self):
            return DiceNotationParser.RULE_startRule

        def enterRule(self, listener):
            if hasattr(listener, "enterStartRule"):
                listener.enterStartRule(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStartRule"):
                listener.exitStartRule(self)




    def startRule(self):

        localctx = DiceNotationParser.StartRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_startRule)
        try:
            self.state = 15
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.dice()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.number()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.addOp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddOpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DiceNotationParser.AddOpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def multOp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DiceNotationParser.MultOpContext)
            else:
                return self.getTypedRuleContext(DiceNotationParser.MultOpContext,i)


        def ADDOPERATOR(self, i=None):
            if i is None:
                return self.getTokens(DiceNotationParser.ADDOPERATOR)
            else:
                return self.getToken(DiceNotationParser.ADDOPERATOR, i)

        def getRuleIndex(self):
            return DiceNotationParser.RULE_addOp

        def enterRule(self, listener):
            if hasattr(listener, "enterAddOp"):
                listener.enterAddOp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAddOp"):
                listener.exitAddOp(self)




    def addOp(self):

        localctx = DiceNotationParser.AddOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_addOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.multOp()
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DiceNotationParser.ADDOPERATOR:
                self.state = 18
                self.match(DiceNotationParser.ADDOPERATOR)
                self.state = 19
                self.multOp()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultOpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DiceNotationParser.MultOpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(DiceNotationParser.OperandContext)
            else:
                return self.getTypedRuleContext(DiceNotationParser.OperandContext,i)


        def MULTOPERATOR(self, i=None):
            if i is None:
                return self.getTokens(DiceNotationParser.MULTOPERATOR)
            else:
                return self.getToken(DiceNotationParser.MULTOPERATOR, i)

        def getRuleIndex(self):
            return DiceNotationParser.RULE_multOp

        def enterRule(self, listener):
            if hasattr(listener, "enterMultOp"):
                listener.enterMultOp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMultOp"):
                listener.exitMultOp(self)




    def multOp(self):

        localctx = DiceNotationParser.MultOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_multOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.operand()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==DiceNotationParser.MULTOPERATOR:
                self.state = 26
                self.match(DiceNotationParser.MULTOPERATOR)
                self.state = 27
                self.operand()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DiceNotationParser.OperandContext, self).__init__(parent, invokingState)
            self.parser = parser

        def dice(self):
            return self.getTypedRuleContext(DiceNotationParser.DiceContext,0)


        def number(self):
            return self.getTypedRuleContext(DiceNotationParser.NumberContext,0)


        def LPAREN(self):
            return self.getToken(DiceNotationParser.LPAREN, 0)

        def startRule(self):
            return self.getTypedRuleContext(DiceNotationParser.StartRuleContext,0)


        def RPAREN(self):
            return self.getToken(DiceNotationParser.RPAREN, 0)

        def getRuleIndex(self):
            return DiceNotationParser.RULE_operand

        def enterRule(self, listener):
            if hasattr(listener, "enterOperand"):
                listener.enterOperand(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOperand"):
                listener.exitOperand(self)




    def operand(self):

        localctx = DiceNotationParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_operand)
        try:
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.dice()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.number()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.match(DiceNotationParser.LPAREN)
                self.state = 36
                self.startRule()
                self.state = 37
                self.match(DiceNotationParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DiceContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DiceNotationParser.DiceContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DSEPARATOR(self):
            return self.getToken(DiceNotationParser.DSEPARATOR, 0)

        def DIGIT(self, i=None):
            if i is None:
                return self.getTokens(DiceNotationParser.DIGIT)
            else:
                return self.getToken(DiceNotationParser.DIGIT, i)

        def ADDOPERATOR(self):
            return self.getToken(DiceNotationParser.ADDOPERATOR, 0)

        def getRuleIndex(self):
            return DiceNotationParser.RULE_dice

        def enterRule(self, listener):
            if hasattr(listener, "enterDice"):
                listener.enterDice(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDice"):
                listener.exitDice(self)




    def dice(self):

        localctx = DiceNotationParser.DiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DiceNotationParser.ADDOPERATOR:
                self.state = 41
                self.match(DiceNotationParser.ADDOPERATOR)


            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DiceNotationParser.DIGIT:
                self.state = 44
                self.match(DiceNotationParser.DIGIT)


            self.state = 47
            self.match(DiceNotationParser.DSEPARATOR)
            self.state = 48
            self.match(DiceNotationParser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(DiceNotationParser.NumberContext, self).__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(DiceNotationParser.DIGIT, 0)

        def ADDOPERATOR(self):
            return self.getToken(DiceNotationParser.ADDOPERATOR, 0)

        def getRuleIndex(self):
            return DiceNotationParser.RULE_number

        def enterRule(self, listener):
            if hasattr(listener, "enterNumber"):
                listener.enterNumber(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNumber"):
                listener.exitNumber(self)




    def number(self):

        localctx = DiceNotationParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==DiceNotationParser.ADDOPERATOR:
                self.state = 50
                self.match(DiceNotationParser.ADDOPERATOR)


            self.state = 53
            self.match(DiceNotationParser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





