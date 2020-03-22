import logging
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

from dice_notation.parser.DiceNotationLexer import DiceNotationLexer
from dice_notation.parser.DiceNotationParser import DiceNotationParser
from dice_notation.parser.DiceNotationListener import DiceNotationListener


class DiceParser():

    def __init__(self):
        super(DiceParser, self).__init__()
        self._logger = logging.getLogger("DiceParser")

    def parse(self, input):
        input_stream = InputStream(input + "\n")
        lexer = DiceNotationLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = DiceNotationParser(stream)
        tree = parser.notation()
        print(tree.toStringTree(recog=parser))

        walker = ParseTreeWalker()

        listener = DiceNotationListener()
        walker.walk(listener, tree)

        expression = listener.expression()
        self._logger.debug("Parsed expression %s", expression)
        return expression.value()
