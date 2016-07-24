# 3dhubs_hangman
Interview task from 3d hubs.

TL;DR:

~~~bash
# play game
$ ./hangman_advanced.py
[snip]
# run tests
$ py.test
~~~

## Overall Architecture

It is kind of staless in a way that all functions are [``pure''](https://en.wikipedia.org/wiki/Pure_function).
I used 'py.test', 'pyflakes' and 'autopep8' to ensure the result.

## Two flavors

The trivial version: "hangman_simple.py" .
Another one is "hangman_advanced.py" which is covered by tests.
The state is kept in a separate class so it is easy to refactor the code to use with Django.
In that case State would be a DB model and 'hangman' is a view.
