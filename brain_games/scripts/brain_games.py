#!/usr/bin/env python3

def welcoming():
    print('Welcome to the Brain Games!')

from brain_games.cli import welcome_user 

def main():
    welcoming()
    welcome_user()

if __name__ == '__main__':
    main()
