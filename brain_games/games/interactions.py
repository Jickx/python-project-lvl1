import prompt


def welcome_user() -> str:
    print('Welcome to the Brain Games!')
    name = prompt.string(prompt="May I have your name? ")
    print(f"Hello, {name}!")
    return name


def success(name: str) -> str:
    print(f'Congratulations, {name}!')


def failure(name: str) -> str:
    print(f'Let\'s try again, {name}!')
