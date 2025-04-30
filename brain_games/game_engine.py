import prompt

from random import randint

attempt = 3

def welcome_user(game_rules):

    print('"Welcome to the Brain Games!"')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n{game_rules}')
    return name


def get_random_number(begin=1, end=100):

    number = randint(begin, end)
    return number

def choose_operand():
    list_of_operand = ['+', '-', '*']
    operand = list_of_operand[get_random_number(0, len(list_of_operand)-1)]
    return operand


def question_answer(question):

    print(f'Question: {question}')
    user_answer = prompt.string('Your answer: ')
    return user_answer


def check_correct(user_answer, correct_answer, name):
        
    if user_answer == correct_answer:
        print ('Correct')
    else: 
        print(f'\'{user_answer}\' is wrong answer ;(.' 
                  f'Correct answer was \'{correct_answer}\'.\n'
                f'Let\'s try again, {name}]!')
        exit() 

