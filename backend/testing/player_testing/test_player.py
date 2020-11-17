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


# GETALLRES = "{'Players': [{'height': 4.56, 'player_id': 12, 'player_name': 'udyr', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Breaching', 'team_name': 'Gatez', 'team_sport_id': None, 'weight': 160.0}, {'height': 4.56, 'player_id': 13, 'player_name': 'udyr', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Breaching', 'team_name': 'Gatez', 'team_sport_id': None, 'weight': 160.0}, {'height': 4.56, 'player_id': 14, 'player_name': 'udyr', 'player_sport_stats': {'SoccerPlayerStatistics': [{'assists': 18, 'date': 'Tue, 20 Oct 2020 00:00:00 GMT', 'games_played': 20, 'goals_scored': 13, 'id': 1, 'passes_completed': 24, 'player_id': 14, 'red_cards': 12, 'saves': 74, 'tackles_won': 19, 'yellow_cards': 45}, {'assists': 18, 'date': 'Tue, 20 Oct 2020 00:00:00 GMT', 'games_played': 20, 'goals_scored': 13, 'id': 2, 'passes_completed': 24, 'player_id': 14, 'red_cards': 12, 'saves': 74, 'tackles_won': 19, 'yellow_cards': 45}]}, 'sport_name': 'Breaching', 'team_name': 'Gatez', 'team_sport_id': None, 'weight': 160.0}, {'height': 4.56, 'player_id': 15, 'player_name': 'udyr', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Breaching', 'team_name': 'Gatez', 'team_sport_id': None, 'weight': 160.0}, {'height': 4.56, 'player_id': 16, 'player_name': 'udyr', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Breaching', 'team_name': 'Gatez', 'team_sport_id': None, 'weight': 160.0}, {'height': 4.56, 'player_id': 18, 'player_name': 'udyr', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Breaching', 'team_name': 'Gatez', 'team_sport_id': None, 'weight': 160.0}, {'height': 4.56, 'player_id': 19, 'player_name': 'udyr', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Breaching', 'team_name': 'Gatez', 'team_sport_id': None, 'weight': 160.0}, {'height': 4.56, 'player_id': 20, 'player_name': 'udyr', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Breaching', 'team_name': 'Gatez', 'team_sport_id': None, 'weight': 160.0}, {'height': 4.56, 'player_id': 21, 'player_name': 'udyr', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Breaching', 'team_name': 'Gatez', 'team_sport_id': None, 'weight': 160.0}, {'height': 4.56, 'player_id': 22, 'player_name': 'udyr', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Breaching', 'team_name': 'Gatez', 'team_sport_id': None, 'weight': 160.0}, {'height': 4.56, 'player_id': 23, 'player_name': 'udyr', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Breaching', 'team_name': 'Gatez', 'team_sport_id': None, 'weight': 160.0}, {'height': 4.56, 'player_id': 24, 'player_name': 'udyr', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Breaching', 'team_name': 'Gatez', 'team_sport_id': None, 'weight': 160.0}, {'height': 4.56, 'player_id': 25, 'player_name': 'udyr', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Breaching', 'team_name': 'Gatez', 'team_sport_id': None, 'weight': 160.0}, {'height': 4.56, 'player_id': 26, 'player_name': 'udyr', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Breaching', 'team_name': 'Gatez', 'team_sport_id': None, 'weight': 160.0}, {'height': 4.6, 'player_id': 37, 'player_name': 'Luis Markez', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': 'Destroyers', 'team_sport_id': None, 'weight': 169.0}, {'height': 23.1, 'player_id': 38, 'player_name': 'Joel K', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': 'Eaa', 'team_sport_id': None, 'weight': 234.0}, {'height': 5.12447, 'player_id': 2580, 'player_name': 'William Sanchez', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': 'Winterfox', 'team_sport_id': None, 'weight': 256.223}, {'height': 5.51953, 'player_id': 2581, 'player_name': 'William Rodriguez', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': 'Team Toast', 'team_sport_id': None, 'weight': 163.845}, {'height': 8.56551, 'player_id': 2582, 'player_name': 'Patricia Johnson', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': 'Team Toast', 'team_sport_id': None, 'weight': 317.906}, {'height': 7.90105, 'player_id': 2583, 'player_name': 'John Diaz', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': 'Evil Geniuses', 'team_sport_id': None, 'weight': 223.647}, {'height': 4.61511, 'player_id': 2584, 'player_name': 'Patricia Smith', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': 'Team Toast', 'team_sport_id': None, 'weight': 113.193}, {'height': 4.56051, 'player_id': 2585, 'player_name': 'Jennifer Rivera', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': 'Team Toast', 'team_sport_id': None, 'weight': 140.638}, {'height': 7.69025, 'player_id': 2586, 'player_name': 'Linda Burgos', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': 'Cloud9', 'team_sport_id': None, 'weight': 306.849}, {'height': 7.50627, 'player_id': 2587, 'player_name': 'John Diaz', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': 'Cloud9', 'team_sport_id': None, 'weight': 178.559}, {'height': 8.88077, 'player_id': 2588, 'player_name': 'Linda Sanchez', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': 'Winterfox', 'team_sport_id': None, 'weight': 185.659}, {'height': 5.70587, 'player_id': 2589, 'player_name': 'Elizabeth Narvaez', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': 'Golden Guardian', 'team_sport_id': None, 'weight': 302.335}, {'height': 5.70404, 'player_id': 2590, 'player_name': 'John Colon', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': '100 Thieves', 'team_sport_id': None, 'weight': 98.1367}, {'height': 6.62297, 'player_id': 2591, 'player_name': 'Patricia Vazquez', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': 'Dignitas', 'team_sport_id': None, 'weight': 92.5892}, {'height': 5.07374, 'player_id': 2592, 'player_name': 'Jennifer Vazquez', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': 'Clutch Gaming', 'team_sport_id': None, 'weight': 263.238}, {'height': 4.50634, 'player_id': 2593, 'player_name': 'James Diaz', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': 'Dignitas', 'team_sport_id': None, 'weight': 148.388}, {'height': 6.02384, 'player_id': 2594, 'player_name': 'James Smith', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': 'Immortals', 'team_sport_id': None, 'weight': 292.274}, {'height': 4.6, 'player_id': 2595, 'player_name': 'Luis Markez', 'player_sport_stats': {'SoccerPlayerStatistics': []}, 'sport_name': 'Soccer', 'team_name': 'Destroyers', 'team_sport_id': None, 'weight': 169.0}]}\n"
# GETPLAYERID = '{"SoccerPlayerStatistic":[{"assists":18,"date":"2020-10-20","games_played":20,"goals_scored":13,"halve_number":null,"id":1,"passes_completed":24,"player_id":14,"position":null,"red_cards":12,"saves":74,"tackles_won":19,"yellow_cards":45},{"assists":18,"date":"2020-10-20","games_played":20,"goals_scored":13,"halve_number":null,"id":2,"passes_completed":24,"player_id":14,"position":null,"red_cards":12,"saves":74,"tackles_won":19,"yellow_cards":45}]}\n'''
# GETALLPLAYERISTAT = '{"Player":{"height":4.56,"player_id":14,"player_name":"udyr","player_sport_stats":{"SoccerPlayerStatistics":[{"assists":18,"date":"Tue, 20 Oct 2020 00:00:00 GMT","games_played":20,"goals_scored":13,"id":1,"passes_completed":24,"player_id":14,"red_cards":12,"saves":74,"tackles_won":19,"yellow_cards":45},{"assists":18,"date":"Tue, 20 Oct 2020 00:00:00 GMT","games_played":20,"goals_scored":13,"id":2,"passes_completed":24,"player_id":14,"red_cards":12,"saves":74,"tackles_won":19,"yellow_cards":45}]},"sport_name":"Breaching","team_name":"Gatez","team_sport_id":null,"weight":160.0}}\n'
# GETATTRIBUTE = '[[12,"udyr",4.56,160.0,"Gatez","Breaching"],[13,"udyr",4.56,160.0,"Gatez","Breaching"],[14,"udyr",4.56,160.0,"Gatez","Breaching"],[15,"udyr",4.56,160.0,"Gatez","Breaching"],[16,"udyr",4.56,160.0,"Gatez","Breaching"],[18,"udyr",4.56,160.0,"Gatez","Breaching"],[19,"udyr",4.56,160.0,"Gatez","Breaching"],[20,"udyr",4.56,160.0,"Gatez","Breaching"],[21,"udyr",4.56,160.0,"Gatez","Breaching"],[22,"udyr",4.56,160.0,"Gatez","Breaching"],[23,"udyr",4.56,160.0,"Gatez","Breaching"],[24,"udyr",4.56,160.0,"Gatez","Breaching"],[25,"udyr",4.56,160.0,"Gatez","Breaching"],[26,"udyr",4.56,160.0,"Gatez","Breaching"]]\n'




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
