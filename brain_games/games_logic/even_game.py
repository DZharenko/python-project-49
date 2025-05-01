from brain_games.game_engine import (
    attempt,
    check_correct,
    get_random_number,
    question_answer,
    welcome_user,
)

game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):

    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def start_game():

    name = welcome_user(game_rules)
    
    for _ in range(attempt):
        number = get_random_number()
        user_answer = question_answer(number)
        correct_answer = is_even(number)
        check_correct(user_answer, correct_answer, name)
    
    print(f'Congratulations, {name}')
