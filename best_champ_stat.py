from collections import OrderedDict
from operator import itemgetter
from riotwatcher import LolWatcher
from dotenv import load_dotenv

import os

load_dotenv()
lol_watcher = LolWatcher(os.getenv('RIOT_TOKEN'))
my_region = os.getenv('REGION')

class Response:
    response_code = 0
    sorted_list = {}
    def __init__(self, sorted_list):
        self.response_code = 200
        self.sorted_list = sorted_list

def get_champ_data_list():
    versions = lol_watcher.data_dragon.versions_for_region(my_region) #mock lolwatch data dragon. if(champ) give me back somethign back
    champions_version = versions['n']['champion'] #mock the right versions
    current_champ_list = lol_watcher.data_dragon.champions(champions_version)
    champion_data_list = OrderedDict(current_champ_list['data']) #mock the correct data_list is it in correct order
    return champion_data_list

def best_champ_for_stat(base_stat):
    print(base_stat)
    data_list = get_champ_data_list()
    sorted_list = OrderedDict()
    for champ in data_list:
        sorted_list[champ] = data_list[champ]['stats'][base_stat]
    sorted_list = sorted(sorted_list.items(), key = lambda x: int(x[1]), reverse=True)
    response = Response(sorted_list)
    print(response.sorted_list[0][0])
    return response

def main():
    res = best_champ_for_stat("hp")
    print(res.response_code)
    print(res.sorted_list[0])
    print(res.sorted_list[0][0])
main()
