
import random

# Boundaries of the gaming range
MIN_NUMBER = -20
MAX_NUMBER = 20

OPERATORS = ('+', '-', '*')
GAME_TASK = 'What is the result of the expression?'


def generate_game_data():
    num_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator_type = random.choice(OPERATORS)
    game_question = f'{num_1} {operator_type} {num_2}'

    if operator_type == '+':
        correct_answer = str(num_1 + num_2)
    if operator_type == '-':
        correct_answer = str(num_1 - num_2)
    if operator_type == '*':
        correct_answer = str(num_1 * num_2)

    return game_question, correct_answer
