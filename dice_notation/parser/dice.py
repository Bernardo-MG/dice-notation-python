import io
import logging
from antlr4 import InputStream, CommonTokenStream

from dice_notation.parser.DiceNotationLexer import DiceNotationLexer
from dice_notation.parser.DiceNotationParser import DiceNotationParser


class DiceParser():

    def __init__(self):
        super(DiceParser, self).__init__()
        self._logger = logging.getLogger("DiceParser")

    def parse(self, input):
        input_stream = InputStream(input + "\n")
        lexer = DiceNotationLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = DiceNotationParser(stream)
        return parser.notation()
