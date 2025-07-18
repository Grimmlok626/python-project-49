import operator
import random

OPERATIONS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
}

def game():
	num1 = random.randint(1, 50)
	num2 = random.randint(1, 50)
	op_symbol, op_func = random.choice(list(OPERATIONS.items()))
	question = f"{num1} {op_symbol} {num2}"
	correct_answer = op_func(num1, num2)
	return question, correct_answer
