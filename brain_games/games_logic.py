
import prompt

# Quantity of correct answers to complete the game successfully.
ANSWERS_COUNT = 3


def play_game(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module.GAME_TASK)

    for i in range(0, ANSWERS_COUNT):
        game_question, correct_answer = game_module.generate_game_data()
        print(f'Question: {game_question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer.lower() != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(.\n"
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
