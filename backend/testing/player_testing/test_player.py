from requests import get, post, put, delete
import json
from typing import Dict, List
from unittest import TestCase, main

HOST = 'http://127.0.0.1:5000'

player_dat = [
    {'player_name' : 'unnombre', 'height' : 2.45, 'weight' : 125, 'team_name' : 'unequipo', 'sport_name' : 'undeporte', 'team_sport_id' : 13, 'player_id' : 123},
    {'player_name' : 'udyr', 'height' : 4.56, 'weight' : 160, 'team_name' : 'Gatez', 'sport_name' : 'Breaching', 'team_sport_id' : 69, 'player_id' : 123456789},
    {'player_name' : 'ofe', 'height' : 69, 'weight' : 420, 'team_name' : 'Team_OP', 'sport_name' : 'FastEating', 'team_sport_id' : None, 'player_id' : 17},   
]

soccer_dummy_data = [
    (1, 'goalie', '2020', 1, 1, 5, 0, 0, 5, 0, 0, 0),
    (2, 'field', '2020', 3, 2, 5, 1, 0, 5, 2, 3, 0),
    (3, 'goalie', '2020', 4, 1, 5, 2, 1, 5, 1, 0, 0)
]






class PlayerTest(TestCase):    
    PLAYER_ROUTES = {
        'getall':HOST + '/player',        
        }        

    def test_get_all(self):
        print('\nTesting get all players method...')
        print(PlayerTest.PLAYER_ROUTES['getall'])
        content = get(PlayerTest.PLAYER_ROUTES['getall'])        
        obtained = content.content.decode()
        obtained = json.loads(obtained)         
        print(obtained)       
        # self.assertEquals(GETALLRES, obtained)        

    def test_get_by_player_id(self):
        print('\nTesting get player by id method...')
        url = HOST + '/player14'
        obtained = get(url).content.decode()
        print(obtained)
        # self.assertEquals(GETPLAYERID, obtained)

    def test_get_all_player_soccer_individual_statistics(self):
        print('\nTesting GET for all soccer method...')
        url = HOST + '/player/soccer'
        content = get(url).content.decode()
        print(content)
        # self.assertEquals(GETALLPLAYERISTAT, content)

    def test_get_player_by_attribute(self):
        print('\nTesting get player by attributes')
        url = HOST + '/player'
        obtained = get(url, params={'player_name':'udyr', 'team_name':'Gatez'}).content.decode()
        # self.assertEquals(GETATTRIBUTE, obtained)

    def test_add_player(self):
        print('\nTesting add Player to database by rest...')
        url = HOST + '/player'
        player_to_add = {
            'player_name' : 'Luis Markez',
            'height' : 4.6,
            'weight' : 169,
            'team_name' : 'Destroyers',
            'sport_name' : 'Soccer',
        }
        obtained = post(url, json=player_to_add)
        # self.assertEquals(201, obtained.status_code)



LINKS = [
    HOST + '/player',
    HOST + '/player123',
    HOST + '/player222',
    HOST + '/player30',
    HOST + '/player14'    
]

if __name__=='__main__':    
    main()

    # main() # Esto es para 
    # cheap_test(get, LINKS[0])
    # cheap_test(get, LINKS[1])
    # cheap_test(get, LINKS[2])

    # cheap_test(post, LINKS)
    # player_1 = json.dumps(player_dat[0])
    # player_2 = json.dumps(player_dat[1])
    # player_1 = player_dat[0]
    # player_2 = player_dat[1]
    # print(get(LINKS[0]).content)
    # # print(get(LINKS[1]).content)
    # print(get(LINKS[2]).content)
    # print(post(LINKS[0], json=player_dat[2]))
    # print(put(LINKS[3], json=player_dat[2]).content)
    # print(delete(LINKS[3]).content)
    # TODO En la base de datos cambia lo del key dependiente para que el edit sea mas sencillo
    
    # print(post(LINKS[0], json=player_1))
    # print(put(LINKS[1], json=player_2))
    # print(delete(LINKS[1]))