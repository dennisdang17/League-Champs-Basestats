from collections import OrderedDict
from operator import itemgetter
from pytest_bdd import scenarios, when, then
from dotenv import load_dotenv
from riotwatcher import LolWatcher

import os
import pytest

load_dotenv()
lol_watcher = LolWatcher(os.getenv('RIOT_TOKEN'))
my_region = os.getenv('REGION')
scenarios('../mnt/c/Users/denni/Documents/Code/DeployingWorking/League-Champs-Basestats/league_champion.feature')

my_region = 'na1'

class Response:
    response_code = 0
    sorted_list = {}
    def __init__(self, sorted_list):
        self.response_code = 200
        self.sorted_list = sorted_list

def get_champ_data_list():
    versions = lol_watcher.data_dragon.versions_for_region(my_region)
    champions_version = versions['n']['champion']
    current_champ_list = lol_watcher.data_dragon.champions(champions_version)
    champion_data_list = OrderedDict(current_champ_list['data'])
    return champion_data_list

@pytest.fixture
@when('my API is queried with "<base_stat>"')
def best_champ_for_stat(base_stat):
    data_list = get_champ_data_list()
    sorted_list = OrderedDict()
    for champ in data_list:
        sorted_list[champ] = data_list[champ]['stats'][base_stat]
    sorted_list = sorted(sorted_list.items(), key = lambda x: int(x[1]), reverse=True)
    response = Response(sorted_list)
    print(response.sorted_list)
    return response
@then('the response status code is 200') 
def status_code_check(stat_response):
    assert stat_response.response_code == 200
@then('the champion is "<champion>"')
def base_stat_returns_champion(stat_response, champion):
    assert stat_response.sorted_list[0][0] == champion