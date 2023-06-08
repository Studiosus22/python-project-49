#!/usr/bin/env python3

import random


MIN_NUMBER = 1
MAX_NUMBER = 100
# Границы диапазона, из которого выбирается число для вопроса.
# Заданы произвольно.

game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_and_answer():
    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    game_question = num

    if num == 2 or num == 3:
        correct_answer = 'yes'
    if num > 3:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                correct_answer = 'no'
                break
            else:
                correct_answer = 'yes'

    return game_question, correct_answer
