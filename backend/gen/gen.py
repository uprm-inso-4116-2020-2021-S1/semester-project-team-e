from random import Random
from requests import get, put, post, delete
from time import sleep



HOST = 'http://127.0.0.1:5000'

OK = 200
CREATED = 201


FIRST_NAMES = [
    'James',
    'John',
    'Robert',
    'Michael',
    'William',
    'Mary',
    'Patricia',
    'Jennifer',
    'Linda',
    'Elizabeth'
]

LAST_NAMES = [
    'Smith',
    'Johnson',
    'Sanchez',
    'Rivera',
    'Diaz',
    'Rodriguez',
    'Narvaez',
    'Burgos',
    'Colon',
    'Vazquez'
]

WEIGHT_RANGE = (90.0, 327.0)
HEIGHT_RANGE = (4.5, 9.3)

TEAM_NAMES = [

]

SPORT_NAMES = [

]

PLAYER_NAMES = [

]

MAIN_MENU_OPTIONS = [
    'User Option',
    'Player Options',
    'Statistics Options',
    'Sport Options',
]

RANDOM_OR_MANUAL = [
    'Random Entry',
    'Manual Entry',    
]

PLAYER_OPTIONS = [
    'Get Player',
    'Add Player',
    'Update Player',
    'Delete Player',
]

TEAM_NAMES = [
    '100 Thieves',
    'Apex Gaming',
    'Cloud9',
    'Clutch Gaming',
    'Team Toast',
    'Dignitas',
    'Team Envy',
    'Evil Geniuses',
    'FlyQuest',
    'Golden Guardian',
    'Team Impulse',
    'Immortals',
    'Winterfox'
]




####################################################
#                   In Progress
####################################################



def _display_options(option_ls: list):
    for idx, opt in enumerate(option_ls):
        print(f'{idx + 1}. {opt}')


def get_player_by_id(player_id: int):
    print(f'\nGetting player with id: {player_id}')
    url = HOST + f'/player{player_id}'
    request = get(url) 
    if request.status_code == OK:
        return request.content.decode()
    else:
        return None

def add_player(player_data: dict):
    print('\nAdding player to database...\n')
    url = HOST + '/player'
    request = post(url, json=player_data)
    if request.status_code == CREATED:
        print('Player was added.')
    else:
        print('Could not add player.')

def add_random_player():
    rand = Random()
    player = {
        'player_name'  : f'{rand.choice(FIRST_NAMES)} {rand.choice(LAST_NAMES)}',
        'weight' : rand.uniform(*WEIGHT_RANGE),
        'height' : rand.uniform(*HEIGHT_RANGE),
        'team_name' : rand.choice(TEAM_NAMES),
        'sport_name' : 'Soccer'
    }
    url = HOST + '/player'
    request = post(url, json=player)
    if request.status_code == CREATED:
        print('Player added.')
    else:
        print('Player could not be added.')

RUNNING = True

while RUNNING:
    print('Easy Db Manager\nChoose one option:')
    _display_options(MAIN_MENU_OPTIONS)
    chosen = input()

    if chosen == '1':
        pass
    elif chosen =='2':
        print(MAIN_MENU_OPTIONS[int(chosen) - 1])
        _display_options(PLAYER_OPTIONS)
        option = input()
        if option == '1':
            player_id = input('Id of player to search: ')
            print(get_player_by_id(int(player_id)))

        elif option == '2':
            _display_options(RANDOM_OR_MANUAL)
            if input() == '1':
                qt = int(input('How many random players?\n'))
                for i in range(qt):
                    add_random_player()                
            else:
                player_info = {}
                player_info['player_name'] = input('Enter player name: ')
                player_info['height'] = input('Enter player height: ')
                player_info['weight'] = input('Enter player weight: ')
                player_info['team_name'] = input('Enter player team name: ')
                player_info['sport_name'] = input('Enter player sport name: ')
                add_player(player_info)
    elif chosen == '3':
        pass


    elif chosen == '4':
        pass










