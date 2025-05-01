import math

from brain_games.game_engine import (
    attempt,
    check_correct,
    get_random_number,
    question_answer,
    welcome_user,
)

game_rules = 'Find the greatest common divisor of given numbers.'


def find_gcd(number_1, number_2):
    result = math.gcd(number_1, number_2)
    return result


def start_game():

    name = welcome_user(game_rules)
    
    for _ in range(attempt):
        number_1 = get_random_number(1, 100)
        number_2 = get_random_number(1, 100)
        expression = f'{number_1} {number_2}'
        user_answer = question_answer(expression)
        correct_answer = find_gcd(number_1, number_2)
        check_correct(int(user_answer), correct_answer, name)
    
    print(f'Congratulations, {name}')   
