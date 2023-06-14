#!/usr/bin/env python3

from brain_games.games_logic import do_the_game
from brain_games.games import is_even


def main():
    do_the_game(is_even)


if __name__ == '__main__':
    main()
