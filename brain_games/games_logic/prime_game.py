from brain_games.game_engine import (
    attempt,
    check_correct,
    get_random_number,
    question_answer,
    welcome_user,
)

game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2: 
        return 'no'
    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            return 'no'
        divider += 1
    return 'yes'


def start_game():

    name = welcome_user(game_rules)
    
    for _ in range(attempt):
        number = get_random_number()
        user_answer = question_answer(number)
        correct_answer = is_prime(number)
        check_correct(user_answer, correct_answer, name)
    
    print(f'Congratulations, {name}!')

