#!/usr/bin/env python3


from brain_games.games_logic import game_process
from brain_games.questions_and_answers import is_prime_qa as question_and_answer


game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    result = game_process(game_task, question_and_answer)


if __name__ == '__main__':
    main()