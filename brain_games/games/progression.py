import random


# Минимальное и максимальное значения первого члена прогрессии.
MIN_START_POINT = 0
MAX_START_POINT = 1000

# Минимальное и максимальное значения шага прогрессии.
MIN_STEP = 2
MAX_STEP = 10

# Минимальное и максимальное количество задаваемых членов прогрессии.
MIN_QUANTITY = 5
MAX_QUANTITY = 12

GAME_TASK = 'What number is missing in the progression?'


def ask_and_answer():
    p_start = random.randint(MIN_START_POINT, MAX_START_POINT)
    p_step = random.randint(MIN_STEP, MAX_STEP)
    p_quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)
    p_finish = p_start + p_step * p_quantity
    p_list = list(range(p_start, p_finish, p_step))
    hidden_item_num = random.randint(1, (p_quantity - 2))
    hidden_item = p_list[hidden_item_num]
    p_pre_hidden_part = " ".join(map(str, p_list[0:hidden_item_num]))
    p_past_hidden_part = " ".join(map(str, p_list[(hidden_item_num + 1):]))

    game_question = f'{p_pre_hidden_part} .. {p_past_hidden_part}'
    correct_answer = str(hidden_item)

    return game_question, correct_answer
