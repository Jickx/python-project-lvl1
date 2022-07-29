import prompt


def welcome_user() -> str:
    print('Welcome to the Brain Games!')
    name = prompt.string(prompt="May I have your name? ").capitalize()
    print(f"Hello, {name}!")
    return name


def success(name: str) -> str:
    print(f'Congratulations, {name}!')


def failure(name: str) -> str:
    print(f'Let\'s try again, {name}!')


def is_right_answer(answer: str, correct_answer: str) -> bool:
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return False
