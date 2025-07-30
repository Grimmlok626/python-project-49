import random

from brain_games.scripts.brain_games import run_game


def compute_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'
    answer = str(compute_gcd(num1, num2))
    return question, answer


def main():
    print('Find the greatest common divisor of given numbers.')
    run_game(
        generate_question,
        game_description='Find the greatest common divisor of given numbers.',
    )


if __name__ == '__main__':
    main()