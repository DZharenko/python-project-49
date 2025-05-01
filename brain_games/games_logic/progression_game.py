from brain_games.game_engine import welcome_user, attempt, get_random_number, question_answer, check_correct


game_rules = 'What number is missing in the progression?'


def make_progression():

    first_number = get_random_number(1,10)
    step = get_random_number(1,10)
    length = get_random_number(5,10)
    hidden_elem = get_random_number(0, length-1)

    progeression = list(range(first_number, first_number + step * length - 1, step))
    hidden_number = progeression[hidden_elem]
    progeression[hidden_elem] = '..'
    expression = ' '.join(str(i)for i in progeression)    
    
    return hidden_number, expression


def start_game():

    name = welcome_user(game_rules)

    for _ in range(attempt):
        hidden_number, expression = make_progression()    
        user_answer = question_answer(expression)
        correct_answer = hidden_number
        check_correct(int(user_answer), correct_answer, name)
    
    print(f'Congratulations, {name}')   

start_game()