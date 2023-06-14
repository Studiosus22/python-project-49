#!/usr/bin/env python3

import prompt

ATTEMPTS = 3
# Количество правильных ответов, необходимое для успешного завершения игры.


def do_the_game(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module.GAME_TASK)

    for i in range(0, ATTEMPTS):
        game_question, correct_answer = game_module.ask_and_answer()
        print(f'Question: {game_question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer.lower() != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            return

        else:
            print('Correct!')

    print(f'Congratulations, {name}!')
