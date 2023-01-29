#!/usr/bin/env python3

import random
from random import randint

def welcoming():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask():
    print('What is the result of the expression?')
    i = 0
    correct_answers = 0
    while i < 3:
      random_number = randint(1, 10)
      random_number2 = randint(1, 10)
      operators = ["+","-","*"]
      picked_operator = random.choice(operators)
      print(f'Question: {random_number} {picked_operator} {random_number2}')
      answer = prompt.string('Your answer: ')
      if picked_operator == '+':
        result = random_number + random_number2
      elif picked_operator == '-':
          result = random_number - random_number2
      elif picked_operator == '*':
          result = random_number * random_number2
      if int(answer) == result:
        print('Correct!')
        correct_answers = correct_answers + 1
        i = i + 1
      else:
        print(f'{answer} is wrong answer ;(. Correct answer was {result}')
        i = 3
    return correct_answers


def result(name, correct_answers):
    if correct_answers == 3:
      print(f'Congratulations, {name}!')
    elif correct_answers != 3: 
      print(f"Let's try again, {name}!")


def main():
    welcoming()
    name = welcome_user()
    answers = ask()
    result(name, answers)


if __name__ == '__main__':
    main()
