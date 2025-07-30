import random
from brain_games.scripts.brain_games import run_game

def generate_question():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = 10
    progression = [start + i * step for i in range(length)]
    missing_index = random.randint(0, length - 1)
    answer = str(progression[missing_index])
    progression[missing_index] = '..'
    question = ' '.join(str(num) for num in progression)
    return question, answer

def main():
    run_game(
        generate_question,
        game_description='What number is missing in the progression?',
    )

if __name__ == '__main__':
    main()