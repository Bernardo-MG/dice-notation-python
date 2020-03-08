from io import StringIO
import sys
from antlr4 import *

from dice_notation.parser.dice import DiceParser


def main(argv):
    parser = DiceParser()
    tree = parser.parse("4d56")


if __name__ == '__main__':
    main(sys.argv)