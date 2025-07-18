from cli import welcome_user

def run_game(game_func):
	name = welcome_user()

	for _ in range(3):
		question, correct_answer = game_func()
		print(f"Question: {question}")
		answer = input("Your answer: ").strip()

		# Проверка ответа
		if answer.isdigit() or (answer.startswith('-') and answer[1:].isdigit()):
			if int(answer) == correct_answer:
				print("Correct!")
			else:
				print(f"'{answer}' is wrong. The correct answer was '{correct_answer}'.")
				print(f"Let's try again, {name}!")
				return
		else:
			if answer.lower() == str(correct_answer).lower():
				print("Correct!")
			else:
				print(f"'{answer}' is wrong. The correct answer was '{correct_answer}'.")
				print(f"Let's try again, {name}!")
				return

	print(f"Congratulations, {name}!")
