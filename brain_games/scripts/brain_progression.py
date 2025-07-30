import random

from brain_games.scripts.brain_games import run_game


def generate_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    missing_index = random.randint(0, length - 1)

    progression = [start + i * step for i in range(length)]
    correct_answer = progression[missing_index]
    progression_with_gap = progression.copy()
    progression_with_gap[missing_index] = '..'

    question = ' '.join(str(num) for num in progression_with_gap)
    return question, str(correct_answer)


def main():
    run_game(
        generate_progression,
        game_description='What number is missing in the progression?',
    )


if __name__ == '__main__':
    main()