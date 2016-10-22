# -*- coding: utf-8 -*-

from dice_notation.parser import DiceParser

if __name__ == '__main__':
    parser = DiceParser()
    while 1:
        try:
            s = raw_input('Dice notation > ')
        except EOFError:
            break
        if not s:
            continue

        print('Rolled {}'.format(parser.parse(s).roll()))
