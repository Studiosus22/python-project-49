import random

# Boundaries of the gaming range
MIN_NUMBER = 1
MAX_NUMBER = 100

GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_game_data():
    game_question = random.randint(MIN_NUMBER, MAX_NUMBER)
    if is_even(game_question) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return game_question, correct_answer
