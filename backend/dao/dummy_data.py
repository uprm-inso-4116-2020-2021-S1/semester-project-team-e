tid_count = 11

team_dummy_data = [
    (1, 'los coquis', 'info', 'soccer'),
    (2, 'vaqueros','info', 'soccer' ),
    (3, 'los gatos', 'info', 'soccer'),
    (4, 'los pitbulls', 'info', 'soccer'),
    (5, 'Tainos', 'info', 'soccer'),
    (6, 'Lakers', 'info', 'soccer'),
    (7, 'Dinos', 'info', 'soccer'),
    (8, 'Los arboles', 'info', 'soccer'),
    (9, 'Team E', 'info', 'soccer'),
    (10, 'Criollos', 'info', 'soccer'),
]

uid_count = 2

users_dummy_data = [
    (0, 'username', 'email', 'password', 'Jose Javier'),
    (1, 'admin', 'admin@email.com', '$5$rounds=535000$EGnE9ruyR5gXHOBb$GcdcIzITasG45/Hb7jG84toDyyK8y0f/5FmFknI2ad/', 'Tito Bambam')
]

#(user_id, team_id)
manages = [
    (0, 1),
    (0, 2),
    (1, 1)
]

soccerStat_count = 9

soccer_team_dummy_data = [
    (1, 1, 23, 5, 4, 25, 21, 74, 67, '2019'),
    (2, 2, 20, 10, 6, 20, 12, 62, 67, '2006'),
    (3, 'los gatos', 13, 7, 22, 15, 20, 50, 67, '2005'),
    (4, 'los pitbulls', 15, 6, 19, 16, 23, 15, 67, '2014'),
    (5, 'Tainos', 10, 10, 10, 12, 14, 34, 67, '2018'),
    (6, 'pata', 25, 3, 6, 30, 7, 58, 67, '2010'),
    (7, 'lake', 30, 2, 3, 45, 5, 65, 67, '2016'),
    (8, 'xd', 7, 12, 23, 9, 35, 84, 67, '2018'),
]

# (tid, wins, draws, loss, goals_for, goals_allowed, goal_difference, points)
soccer_team_avg_dummy_data = [
    (1, 2, 3, 2, 3, 4, 5, 1),
    (2, 1, 4, 2, 2, 5, 5, 0.2),
    (4, 2, 3, 3, 4, 6, 5, 1.2),
    (3, 2, 4, 2, 5, 4, 5, 0.5),
]