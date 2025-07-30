import random

from brain_games.scripts.brain_games import run_game


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_question():
    number = random.randint(2, 100)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'
    return question, answer


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    run_game(
        generate_question,
        game_description='Answer "yes" if given number is prime. '
        'Otherwise answer "no".',
    )


if __name__ == '__main__':
    main()