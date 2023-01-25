import prompt
from random import randint


def welcoming():
    print('Welcome to the Brain Games!')


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    correct_answers = 0
    while i < 3:
      random_number = randint(1, 100)
      print(f'Question: {random_number}')
      answer = prompt.string('Your answer: ')
      if random_number % 2 == 0 and answer.lower() == 'yes' or random_number % 2 != 0 and answer.lower() == 'no':
        print('Correct!')
        correct_answers = correct_answers + 1
      else:
        print('Inorrect!')
      i = i + 1
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
