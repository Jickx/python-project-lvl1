#!/usr/bin/env python

import prompt


def welcome_user():
    name = prompt.string(prompt="May I have your name? ")
    print(f"Hello, {name}!")


if __name__ == "__main__":
    welcome_user()