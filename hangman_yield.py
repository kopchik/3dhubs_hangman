#!/usr/bin/env python3
from random import choice
from optparse import OptionParser
from enum import Enum
import logging
import sys


WORDS = "3dhubs marvin print filament order layer".split()
WORDS = list(map(str.lower, WORDS))
MAX_MISTAKES = 5

log = logging.getLogger('hangman')
log.setLevel(logging.DEBUG)


class ret(Enum):
    """ All possible return values of hangman(). """
    correct = 1
    mistake = 2
    win = 3
    gameover = 4


def hang_format(word, letters):
    guessed = [w if w in letters else "_" for w in word]
    return "".join(guessed)


def hangman(word, max_mistakes=MAX_MISTAKES):
    mistakes = 0
    guessed = set()
    to_guess = len(set(word))  # number of letters to guess
    print("Welcome to the most advanced version of hangman up to date!")
    while mistakes < max_mistakes:
        letter = yield
        if letter not in word:
            mistakes += 1
            yield ret.mistake, max_mistakes - mistakes
            continue
        guessed.add(letter)

        # congrats, all letters were guessed
        if len(guessed) == to_guess:
            yield ret.win, None
            break
        else:
            yield ret.correct, hang_format(word, guessed)
    else:
        yield ret.gameover, None


def get_letter():
    while True:
        letter = input("Input one letter: ")
        if len(letter) == 1:
            break
        print("Invalid input, please try again")
    return letter


def wrapper(word, max_mistakes):
    print("Hello, you need to guess {} letters".format(len(word)))
    assert isinstance(word, str) and len(word) >= 1, "invalid word"
    word = word.lower()
    game = hangman(word, max_mistakes)
    for x in game:
        letter = get_letter()
        ret, val = game.send(letter)
        if ret == ret.correct:
            print(val)
        elif ret == ret.mistake:
            print("Wrong, you have {} attempts left to guess the word".format(val))
        elif ret == ret.win:
            print()
            print("Congratulations, You won!!!")
            return 0
        elif ret == ret.gameover:
            print()
            print("Ha-ha, you dead. Have a nice day!")
            return 1


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-n", "--max-mistakes", type=int, default=MAX_MISTAKES,
                      help="How many mistakes player allowed to make")
    parser.add_option("-w", "--word",
                      help="Word to be used in game")
    options, args = parser.parse_args()
    word = options.word or choice(WORDS)
    sys.exit(wrapper(word, options.max_mistakes))
