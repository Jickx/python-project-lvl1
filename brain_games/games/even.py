import prompt
from random import randrange


def ask_question():
    number = randrange(100)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return answer.lower(), correct_answer
