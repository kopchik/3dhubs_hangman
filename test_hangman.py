from hangman_advanced import ret, hangman, hang_format, State


def test_hangformat():
    assert hang_format("3dhubs", {}) == "______"
    assert hang_format("order", {'r'}) == "_r__r"
    assert hang_format("order", set('orde')) == "order"


def test_game():
    state = State("order", max_mistakes=1)
    # correctly guess one letter
    res, msg = hangman(state, 'r')
    assert res == ret.correct
    assert state.mistakes == 0
    assert msg == "_r__r"

    # another letter
    res, msg = hangman(state, 'o')
    assert res == ret.correct
    assert msg == 'or__r'

    # finally, win the game
    _, _ = hangman(state, 'd')
    res, msg = hangman(state, 'e')
    assert res == ret.win


def test_gameover():
    state = State("3dhubs", max_mistakes=2)
    # wrong guess
    res, msg = hangman(state, 'x')
    assert res == ret.mistake

    # another wrong guess and game over
    res, msg = hangman(state, 'y')
    assert res == ret.gameover


def test_main():
    # TODO: mock input() and play the game.
    pass
