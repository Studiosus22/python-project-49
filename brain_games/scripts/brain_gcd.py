#!/usr/bin/env python3


from brain_games.games_logic import game_process
from brain_games.questions_and_answers import gcd_qa as question_and_answer


game_task = 'Find the greatest common divisor of given numbers.'


def main():
    result = game_process(game_task, question_and_answer)


if __name__ == '__main__':
    main()