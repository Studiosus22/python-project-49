#!/usr/bin/env python3

import prompt


def do_the_game(game_module):
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game_module.game_task)

    i = 0
    while i < 3:
        game_question, correct_answer = game_module.question_and_answer()
        print(f'Question: {game_question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer.lower() != str(correct_answer):
            return print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.\nLet's try again, {name}!")

        else:
            print('Correct!')
            i += 1

    print(f'Congratulations, {name}!')
