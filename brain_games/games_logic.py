#!/usr/bin/env python3

import prompt


name = 0


def user_greeting():
    global name
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def game_process(game_task, question_and_answer):

    user_greeting()

    print(game_task)

    i = 0
    while i < 3:
        game_question, correct_answer = question_and_answer()
        print(f'Question: {game_question}')
        print('Your answer: ', end='')
        user_answer = input()
        if user_answer.lower() != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            i += 4
        else:
            print('Correct!')
            i += 1
            if i == 3:
                print(f'Congratulations, {name}!')
