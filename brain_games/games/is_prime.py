import random


# Boundaries of the gaming range
MIN_NUMBER = 0
MAX_NUMBER = 100

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 0 or number == 1:
        return False
    if number == 2:
        return True
    if number > 2:
        for i in range(2, (number // 2 + 1)):
            if number % i == 0:
                return False
        return True


def generate_game_data():
    game_question = random.randint(MIN_NUMBER, MAX_NUMBER)
    if is_prime(game_question) is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return game_question, correct_answer
