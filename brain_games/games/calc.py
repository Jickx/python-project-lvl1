import prompt
from random import randrange, choice

operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
}


def ask_question() -> bool:
    num1 = randrange(10)
    num2 = randrange(10)
    operator = choice(list(operators.keys()))
    print('What is the result of the expression?')
    print(f'Question: {num1} {operator} {num2}')
    answer = prompt.integer(prompt=('Your answer: '))
    correct_answer = operators[operator](num1, num2)
    return answer, correct_answer


def is_right_answer(answer: str, correct_answer: str) -> bool:
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return False
