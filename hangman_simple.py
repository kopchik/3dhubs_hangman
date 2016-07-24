#!/usr/bin/env python3
from random import choice
from optparse import OptionParser
import logging
import sys

WORDS = "3dhubs marvin print filament order layer".split()
WORDS = list(map(str.lower, WORDS))
MAX_MISTAKES = 5

log = logging.getLogger('hangman')
log.setLevel(logging.DEBUG)


def hang_format(word, letters):
    guessed = [w if w in letters else "_" for w in word]
    return "".join(guessed)


def hangman(word, max_mistakes=MAX_MISTAKES):
    # very basic validation
    assert isinstance(word, str) and len(word) >= 1, "invalid word"
    word = word.lower()

    mistakes = 0
    guessed = set()
    to_guess = len(set(word))  # number of letters to guess
    log.debug("I chose %s", word)
    result = False
    print("Welcome to the most advanced version of hangman up to date!")
    while mistakes < max_mistakes:
        print("The word is", hang_format(word, guessed))
        print("You have {} attempts to guess the word".format(
            max_mistakes - mistakes))
        letter = input("Input one letter: ")
        if len(letter) != 1:
            print("Invalid input, please try again")
            continue
        letter = letter.lower()

        if letter not in word:
            mistakes += 1
            continue
        guessed.add(letter)

        # congrats, all letters were guessed
        if len(guessed) == to_guess:
            print()
            print("Congratulations, You won!!!")
            result = True
            break
    else:
        print()
        print("Ha-ha, you dead. Have a nice day!")
        result = False

    return result


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-n", "--max-mistakes", type=int, default=MAX_MISTAKES,
                      help="How many mistakes player allowed to make")
    parser.add_option("-w", "--word",
                      help="Word to be used in game")
    (options, args) = parser.parse_args()
    word = options.word or choice(WORDS)
    sys.exit(hangman(word))
