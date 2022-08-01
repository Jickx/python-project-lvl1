import prompt
from random import randrange, choice

OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
}


def ask_question() -> int:
    num1 = randrange(10)
    num2 = randrange(10)
    operator = choice(list(OPERATORS.keys()))
    print('What is the result of the expression?')
    print(f'Question: {num1} {operator} {num2}')
    answer = prompt.integer(prompt=('Your answer: '))
    correct_answer = OPERATORS[operator](num1, num2)
    return answer, correct_answer
