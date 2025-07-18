import random

def game():
	num = random.randint(1, 100)
	question = f"Is {num} even? (yes/no)"
	correct_answer = 'yes' if num % 2 == 0 else 'no'
	return question, correct_answer
