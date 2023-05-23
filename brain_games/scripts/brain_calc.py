#!/usr/bin/env python3

from brain_games.games_logic import game_process
from brain_games.questions_and_answers import calculator_qa as game_function

game_task = 'What is the result of the expression?'


def main():
    game_process(game_task, game_function)


if __name__ == '__main__':
    main()
