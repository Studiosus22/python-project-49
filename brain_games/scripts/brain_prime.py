#!/usr/bin/env python3


from brain_games.games_logic import play_game
from brain_games.games import is_prime


def main():
    play_game(is_prime)


if __name__ == '__main__':
    main()
