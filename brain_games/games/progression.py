import prompt
from random import randrange


def generate_progression():
    prog_diff = randrange(2, 4)
    prog_length = randrange(5, 10)
    prog_start = randrange(5, 50)
    prog_end = prog_start + prog_diff * prog_length
    answer_index = randrange(0, prog_length)
    prog = [i for i in range(prog_start, prog_end + 1, prog_diff)]
    correct_answer = prog[answer_index]
    prog[answer_index] = '..'
    prog_str = ' '.join(str(i) for i in prog)
    return prog_str, correct_answer


def ask_question() -> int:
    prog_str, correct_answer = generate_progression()
    print('What number is missing in the progression?')
    print(f'Question: {prog_str}')
    answer = prompt.integer(prompt='Your answer: ')
    return answer, correct_answer
