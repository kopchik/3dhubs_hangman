#!/usr/bin/env python3
from random import choice
from optparse import OptionParser
from enum import Enum
import sys

WORDS = "3dhubs marvin print filament order layer".split()
WORDS = list(map(str.lower, WORDS))
MAX_MISTAKES = 5


class Error(Exception):
    """ Module-specific errors. """


class ret(Enum):
    """ All game states. """
    correct = 1
    mistake = 2
    win = 3
    gameover = 4
    invalid = 5


class State:

    def __init__(self, word: str, max_mistakes=MAX_MISTAKES):
        assert isinstance(word, str) and len(word) >= 1, "Invalid word"
        self.mistakes = 0
        self.max_mistakes = max_mistakes
        self.guessed = set()
        self.to_guess = len(set(word))
        self.word = word


def hang_format(word: str, letters: set):
    guessed = [w if w in letters else "_" for w in word]
    return "".join(guessed)


def hangman(state, guess):
    assert state.mistakes <= state.max_mistakes, "Invalid state: gameover"

    if not (isinstance(guess, str) and len(guess) == 1):
        return (ret.invalid, "Invalid input")
    guess = guess.lower()

    if guess not in word:
        state.mistakes += 1
        if state.mistakes >= state.max_mistakes:
            return (ret.gameover, "Game over.")
        else:
            return (ret.mistake, "No such letter in the word")

    state.guessed.add(guess)
    if len(state.guessed) == state.to_guess:
        return (ret.win, "You won.")
    return (ret.correct, hang_format(state.word, state.guessed))


def main(word, max_mistakes):
    state = State(word, max_mistakes)
    print("Try to guess the following word:\n{}\n".format(
        hang_format(word, state.guessed)))
    while True:
        guess = input("Input one letter: ")
        res, msg = hangman(state, guess)
        if res == ret.win:
            print()
            print(msg)
            return 0
        elif res == ret.gameover:
            print()
            print(msg)
            print("The word was", word)
            return 1
        elif res == ret.correct:
            print("That's right!\n{}".format(msg))
        elif res == ret.mistake:
            print("Wrong. {} attempts left".format(
                state.max_mistakes - state.mistakes))
        elif res == ret.invalid:
            print(msg)
        else:
            raise Exception


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-n", "--max-mistakes", type=int, default=MAX_MISTAKES,
                      help="How many mistakes player allowed to make")
    parser.add_option("-w", "--word",
                      help="Word to be used in game")
    (options, args) = parser.parse_args()
    word = options.word or choice(WORDS)
    sys.exit(main(word, options.max_mistakes))
