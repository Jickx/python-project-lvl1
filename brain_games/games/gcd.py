import prompt
from random import randrange


def compute_gcd(num1: int, num2: int) -> int:
    while(num2):
        num1, num2 = num2, num1 % num2
    return abs(num1)


def ask_question() -> int:
    num1 = randrange(100)
    num2 = randrange(100)
    print('Find the greatest common divisor of given numbers.')
    print(f'Question: {num1} {num2}')
    answer = prompt.integer(prompt='Your answer: ')
    correct_answer = compute_gcd(num1, num2)
    return answer, correct_answer
