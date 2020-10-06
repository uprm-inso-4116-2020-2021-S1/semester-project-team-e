import requests
import json
from typing import Dict, List
from dao.dummy_data import player_dat 
from unittest import TestCase, main

HOST = 'http://127.0.0.1:5000'

class PlayerTest(TestCase):
    
    PLAYER_ROUTES = {
        'getall':HOST + '/player',
        
        }


    def test_get_all(self):
        print('Testing get all players method...')
        print(PlayerTest.PLAYER_ROUTES['getall'])
        content = requests.get(PlayerTest.PLAYER_ROUTES['getall'])        
        obtained = content.content.decode()
        obtained = json.loads(obtained)                
        obtained: Dict        
        self.assertEqual(list(obtained.values())[0], player_dat)        
        





if __name__=='__main__':
    main()