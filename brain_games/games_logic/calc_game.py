from brain_games.game_engine import (
    attempt,
    check_correct,
    choose_operand,
    get_random_number,
    question_answer,
    welcome_user,
)

game_rules = 'What is the result of the expression?'


def calcualte_expression(expression):
    result = eval(expression)
    return result


def start_game():

    name = welcome_user(game_rules)
    
    for _ in range(attempt):
        number_1 = get_random_number(1, 10)
        number_2 = get_random_number(1, 10)
        operand = choose_operand()
        expression = f'{number_1} {operand} {number_2}'
        user_answer = question_answer(expression)
        correct_answer = calcualte_expression(expression)
        check_correct(int(user_answer), correct_answer, name)
    
    print(f'Congratulations, {name}')   
