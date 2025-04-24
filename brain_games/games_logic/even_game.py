from random import randint

import prompt

game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
attempt = 3


def welcome_user():

    print('"Welcome to the Brain Games!"')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n{game_rules}')
    return name


def get_random_number(begin=1, end=100):

    number = randint(begin, end)
    return number


def is_even(number):

    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def question(number):

    print(f'Question: {number}')


def answer():

    answer = prompt.string('Your answer: ')
    return answer


def start_game():

    name = welcome_user()
    
    for _ in range(attempt):
        number = get_random_number()
        question(number)
        user_answer = answer()
        correct_answer = is_even(number)

        if user_answer == correct_answer:
            print('Correct')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(.' 
                  f'Correct answer was \'{correct_answer}\'.\n'
                f'Let\'s try again, {name}]!')
            exit()
    
    print(f'Congratulations, {name}')
