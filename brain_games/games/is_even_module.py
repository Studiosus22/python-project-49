#!/usr/bin/env python3

import random

MIN_NUMBER = 1
MAX_NUMBER = 100
# Границы диапазона, из которого выбирается число для вопроса.
# Заданы произвольно.

game_task = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_and_answer():

    game_question = random.randint(MIN_NUMBER, MAX_NUMBER)

    if game_question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return game_question, correct_answer
