import random

from brain_games.scripts.brain_games import run_game


def generate_question():
    number = random.randint(1, 100)
    question = str(number)
    answer = 'yes' if number % 2 == 0 else 'no'
    return question, answer


def main():
    run_game(
        generate_question=generate_question,
        game_description=(
            'Answer "yes" if the number is even, '
            'otherwise answer "no".'
        ),
    )


if __name__ == '__main__':
    main()