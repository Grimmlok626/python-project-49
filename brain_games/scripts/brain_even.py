import random

from brain_games.scripts.brain_games import run_game


def generate_question():
    number = random.randint(1, 100)
    question = str(number)
    answer = 'yes' if number % 2 == 0 else 'no'
    return question, answer


def check_answer(user_ans, correct_ans):
    return user_ans.strip().lower() == correct_ans


def main():
    run_game(
        generate_question,
        check_answer=check_answer,
        game_description='Answer "yes" if the number is even, '
        'otherwise answer "no".'
    )


if __name__ == '__main__':
    main()