#!/usr/bin/env python3

import random


MIN_NUMBER = -20
MAX_NUMBER = 20
# Границы диапазона, из которого выбираются числа для задания.
# Заданы произвольно, но не слишком большими, для простоты подсчета в уме.
SIGN_TYPE = (1, 2, 3)
# Кортеж значений, определяющих арифметическое действие в задании.

game_task = 'What is the result of the expression?'


def question_and_answer():
    num_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    sign_num = random.choice(SIGN_TYPE)

    if sign_num == 1:
        game_question = f'{num_1} + {num_2}'
        correct_answer = num_1 + num_2
    if sign_num == 2:
        game_question = f'{num_1} - {num_2}'
        correct_answer = num_1 - num_2
    if sign_num == 3:
        game_question = f'{num_1} * {num_2}'
        correct_answer = num_1 * num_2

    return game_question, correct_answer
