import prompt

from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def run_game(
    generate_question,
    check_answer=lambda user_ans, correct_ans: (
        user_ans.strip().lower() == str(correct_ans).strip().lower()
    ),
    game_description=''
):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    if game_description:
        print(game_description)
    else:
        print('Answer the following questions:')

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = generate_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if not check_answer(user_answer, correct_answer):
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')

def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()