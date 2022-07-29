from brain_games.games.interactions import welcome_user, success, failure
from brain_games.games.calc import ask_question, is_right_answer


def main():
    name = welcome_user()
    for i in range(3):
        answer, correct_answer = ask_question()
        if not is_right_answer(answer, correct_answer):
            failure(name)
            return None
    success(name)
