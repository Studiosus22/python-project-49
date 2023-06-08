#!/usr/bin/env python3

import random
import math


MIN_NUMBER = 1
MAX_NUMBER = 100
# Минимальное и максимальное значения диапазона, из которого выбираются числа для задания.
# Заданы произвольно, но не слишком большими, для простоты подсчета в уме.

game_task = 'Find the greatest common divisor of given numbers.'

def question_and_answer():
    num_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    game_question = f'{num_1} {num_2}'
    correct_answer = math.gcd(num_1, num_2)

    return game_question, correct_answer
