import sys
import importlib
import inspect

max_number_of_rounds = 2500
target_score = 1000
starting_number_of_dynamite = 100

if len(sys.argv) not in [2,3]:
    print('Run "python bot_runner.py example_bot" for example, to test a file called "example_bot.py" against the PaperBot')
    print('Or run "python bot_runner.py bot_one bot_two" to test a bot in bot_one.py against bot_two.py')
    exit()

def get_bot_class_from_module(module_name):
    if module_name[-3:] == '.py': module_name = module_name[0:-3]
    module = importlib.import_module(module_name)
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            return obj
    raise ImportError('No class found in file ' + module_name)

def player_one_wins_round(p1_move, p2_move):
    for move in [p1_move, p2_move]:
        if move not in ['R','P','S','D','W']:
            raise ValueError(f'Illegal move: "{move}"!')

    if p1_move == 'D':
        return p2_move != 'W'
    if p1_move == 'W':
        return p2_move == 'D'
    if p1_move == 'R':
        return p2_move in [ 'S', 'W' ]
    if p1_move == 'P':
        return p2_move in [ 'R', 'W' ]
    if p1_move == 'S':
        return p2_move in [ 'P', 'W' ]
        
def check_dynamite_supply(player):
    if player['move'] == 'D':
        player['dynamite'] -= 1
        if player['dynamite'] < 0:
            raise ValueError(f'Too much dynamite from {player["name"]}!')

def main():
    player_module = sys.argv[1]
    opponent_module = sys.argv[2] if len(sys.argv) == 3 else 'paper_bot'

    players = [{
        'bot': get_bot_class_from_module(player_module)(),
        'score': 0,
        'dynamite': starting_number_of_dynamite,
        'name': 'YOU'
    }, {
        'bot': get_bot_class_from_module(opponent_module)(),
        'score': 0,
        'dynamite': starting_number_of_dynamite,
        'name': 'opponent'
    }]
    gamestate = { 'rounds': [] }
    round_number = 1
    round_value = 1

    while all(p['score'] < target_score for p in players) and round_number <= max_number_of_rounds:
        for p in players:
            p['move'] = p['bot'].make_move(gamestate)
            check_dynamite_supply(p)
        p1_move, p2_move = players[0]['move'], players[1]['move']
        gamestate['rounds'].append({'p1': p1_move, 'p2': p2_move})

        if players[0]['move'] == players[1]['move']:
            round_value += 1
            result = 'DRAW'
        else:
            p1_wins_round = player_one_wins_round(p1_move, p2_move)
            if p1_wins_round:
                players[0]['score'] += round_value
                result = 'WIN'
            else:
                players[1]['score'] += round_value
                result = 'LOSE'
            round_value = 1

        print(f'#{round_number}: {p1_move} vs {p2_move} -> {result}')
        
        round_number += 1 

    print(f'Final scores: ({players[0]["name"]}) {players[0]["score"]} v {players[1]["score"]} ({players[1]["name"]})')

if __name__ == "__main__":
    main()
