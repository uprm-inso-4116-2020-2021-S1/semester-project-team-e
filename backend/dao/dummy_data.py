tid_count = 11

team_dummy_data = [
    (1, 'los coquis', 'info', 'soccer'),
    (2, 'vaqueros','info', 'soccer' ),
    (3, 'los gatos', 'info', 'soccer'),
    (4, 'los pitbulls', 'info', 'soccer'),
    (5, 'Tainos', 'info', 'soccer'),
    (6, 'Lakers', 'info', 'basketball'),
    (7, 'Dinos', 'info', 'basketball'),
    (8, 'Los arboles', 'info', 'basketball'),
    (9, 'Team E', 'info', 'basketball'),
    (10, 'Criollos', 'info', 'basketball'),
]

uid_count = 2

users_dummy_data = [
    (0, 'username', 'email', 'password'),
    (1, 'admin', 'admin@email.com', '$5$rounds=535000$EGnE9ruyR5gXHOBb$GcdcIzITasG45/Hb7jG84toDyyK8y0f/5FmFknI2ad/')
]
# player_id=None, player_name=None, height=None, weight=None, team_name=None, sport_name=None, team_sport_id=None

soccer_dummy_data = [
    (1, 'goalie', '2020', 1, 1, 5, 0, 0, 5, 0, 0, 0),
    (2, 'field', '2020', 3, 2, 5, 1, 0, 5, 2, 3, 0),
    (3, 'goalie', '2020', 4, 1, 5, 2, 1, 5, 1, 0, 0)
]

sport_player_stats = [
    {
        'player_id' : 123,
        'position' : 'back',
        'date' : '14Julio2020',
        'halve_number' : 78,
        'games_played' : 789,
        'saves' : 23,
        'goals_scored' : 243,
        'assists' : 31,
        'tackles_won' : 98,
        'passes_completed' : 567,
        'red_cards' : 12,
        'yellow_cards' : 67,        
    },
    {
        'player_id' : 123456789,
        'position' : 'front',
        'date' : '31Mayo2020',
        'halve_number' : 8,
        'games_played' : 89,
        'saves' : 2,
        'goals_scored' : 23,
        'assists' : 1,
        'tackles_won' : 8,
        'passes_completed' : 67,
        'red_cards' : 1,
        'yellow_cards' : 7,        
    },
    {
        'player_id' : 678,
        'position' : 'left',
        'date' : '11Febrero2020',
        'halve_number' : 823,
        'games_played' : 1234,
        'saves' : 67,
        'goals_scored' : 243,
        'assists' : 31,
        'tackles_won' : 98,
        'passes_completed' : 587,
        'red_cards' : 124,
        'yellow_cards' : 567,        
    }
]

player_dat = [
    {
    'player_name' : 'unnombre',
    'height' : 2.45,
    'weight' : 125,
    'team_name' : 'unequipo',
    'sport_name' : 'undeporte',
    'team_sport_id' : 13,
    'player_id' : 123
    },
    {
    'player_name' : 'udyr',
    'height' : 4.56,
    'weight' : 160,
    'team_name' : 'Gatez',
    'sport_name' : 'Breaching',
    'team_sport_id' : 69,
    'player_id' : 123456789
    },
    {
    'player_name' : 'profe',
    'height' : 69,
    'weight' : 420,
    'team_name' : 'Team_OP',
    'sport_name' : 'FastEating',
    'team_sport_id' : 789,
    'player_id' : 678
    },   
]
