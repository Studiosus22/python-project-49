#!/usr/bin/env python3

import random
import math


def is_even_qa():
    game_question = random.randint(1, 100)

    if game_question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return game_question, correct_answer


def calculator_qa():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    sign_list = [1, 2, 3]
    sign_num = random.choice(sign_list)

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


def gcd_qa():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(0, 100)
    game_question = f'{num_1} {num_2}'
    correct_answer = math.gcd(num_1, num_2)

    return game_question, correct_answer


def progression_qa():
    p_start = random.randint(0, 20)
    p_step = random.randint(2, 10)
    p_quantity = random.randint(5, 12)
    p_finish = p_start + p_step * p_quantity
    p_list = list(range(p_start, p_finish, p_step))
    hidden_item_num = random.randint(1, (p_quantity - 2))
    hidden_item = p_list[hidden_item_num]
    p_pre_hidden_part = " ".join(map(str, p_list[0:hidden_item_num]))
    p_past_hidden_part = " ".join(map(str, p_list[(hidden_item_num + 1):]))

    game_question = f'{p_pre_hidden_part} .. {p_past_hidden_part}'
    correct_answer = str(hidden_item)

    return game_question, correct_answer


def is_prime_qa():
    num = random.randint(2, 100)
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
