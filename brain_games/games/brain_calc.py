import random

from brain_games.scripts.brain_games import run_game


def generate_question():
    operators = ['+', '-', '*']
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(operators)
    question = f'{num1} {operator} {num2}'
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:  # '*'
        answer = num1 * num2
    
    return question, str(answer)


def main():
    run_game(
        generate_question,
        game_description='What is the result of the expression?'
    )


if __name__ == '__main__':
    main()