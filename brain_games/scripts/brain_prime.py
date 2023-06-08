#!/usr/bin/env python3


from brain_games.games_logic import do_the_game
from brain_games.games import is_prime_module


def main():
    do_the_game(is_prime_module)


if __name__ == '__main__':
    main()
