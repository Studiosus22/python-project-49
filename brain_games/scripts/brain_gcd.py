#!/usr/bin/env python3


from brain_games.games_logic import game_process
from brain_games.questions_and_answers import gcd_qa as game_function


game_task = 'Find the greatest common divisor of given numbers.'


def main():
    game_process(game_task, game_function)


if __name__ == '__main__':
    main()
