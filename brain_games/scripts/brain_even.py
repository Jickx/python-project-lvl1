#!/usr/bin/env python
import prompt
from random import randrange
from brain_games.games.interactions import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    ctr = 0
    while True:
        if ctr == 3:
            print(f'Congratulations, {name}!')
            break
        number = randrange(100)
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer.lower() == correct_answer:
            print('Correct!')
            ctr += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer "
                  f"was '{correct_answer}'.")
            print(f'Let\'s try again, {name}!')
            ctr = 0
            break


if __name__ == '__main__':
    main()
