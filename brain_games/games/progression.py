import random


# Minimum and maximum value of progression's first item.
MIN_START_POINT = 0
MAX_START_POINT = 1000

# Minimum and maximum value of progression's step.
MIN_STEP = 2
MAX_STEP = 10

# Minimum and maximum quantity of progression's items in game.
MIN_QUANTITY = 5
MAX_QUANTITY = 12

GAME_TASK = 'What number is missing in the progression?'


def create_progression(start, step, quantity):
    finish = start + step * quantity
    return list(range(start, finish, step))


def generate_game_data():
    start = random.randint(MIN_START_POINT, MAX_START_POINT)
    step = random.randint(MIN_STEP, MAX_STEP)
    quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)
    hidden_item_num = random.randint(1, (quantity - 2))

    progression = create_progression(start, step, quantity)
    hidden_item = progression[hidden_item_num]
    progression[hidden_item_num] = '..'
    game_question = " ".join(map(str, progression))
    correct_answer = str(hidden_item)

    return game_question, correct_answer
