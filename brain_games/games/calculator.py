
import random


MIN_NUMBER = -20
MAX_NUMBER = 20
# Границы диапазона, из которого выбираются числа для задания.
# Заданы произвольно, но не слишком большими, для простоты подсчета в уме.
SIGN = ("+", "-", "*")
GAME_TASK = 'What is the result of the expression?'


def ask_and_answer():
    num_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    sign_type = random.choice(SIGN)
    game_question = f'{num_1} {sign_type} {num_2}'

    if sign_type == "+":
        correct_answer = num_1 + num_2
    if sign_type == "-":
        correct_answer = num_1 - num_2
    if sign_type == "*":
        correct_answer = num_1 * num_2

    return game_question, correct_answer
