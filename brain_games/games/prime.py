from random import randrange
import prompt


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def ask_question():
    num = randrange(100)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print(f'Question: {num}')
    answer = prompt.string(prompt='Your answer: ')
    correct_answer = 'yes' if is_prime(num) else 'no'
    return answer.lower(), correct_answer
