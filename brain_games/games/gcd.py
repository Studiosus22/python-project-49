import random
import math


# Boundaries of the gaming range
MIN_NUMBER = 1
MAX_NUMBER = 100

GAME_TASK = 'Find the greatest common divisor of given numbers.'


def generate_game_data():
    num_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    game_question = f'{num_1} {num_2}'
    correct_answer = str(math.gcd(num_1, num_2))

    return game_question, correct_answer
