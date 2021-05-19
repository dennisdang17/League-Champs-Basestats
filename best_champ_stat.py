from collections import OrderedDict
from flask import Flask, render_template, request
from riotwatcher import LolWatcher
from dotenv import load_dotenv

import os
import json

load_dotenv()
lol_watcher = LolWatcher(os.getenv('RIOT_TOKEN'))
my_region = os.getenv('REGION')

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/data', methods = ['POST','GET'])
def data():
    if request.method == 'GET':
        return f"The URL/data is accessed directly, try to submit a form first!"
    if request.method == 'POST':
        form_data = request.form
        base_stat = form_data['Basestat']
        print("\nTHIS IS THE BASESTAT QUERIED!\n")
        print(base_stat + "\n")
        response = best_champ_for_stat(base_stat)
        print("\nThis is the sorted list")
        print(response.sorted_list)
        print("\n")
        print(form_data)
        print("\n")
        output = json.dumps(response.sorted_list)
        return f"" + output

class Response:
    response_code = 0
    sorted_list = {}
    def __init__(self, sorted_list):
        self.response_code = 200
        self.sorted_list = sorted_list
    def __str__(self):
        return self.sorted_list

def best_champ_for_stat(base_stat):
    try:
        data_list = get_champ_data_list()
        sorted_list = OrderedDict()
        for champ in data_list:
            sorted_list[champ] = data_list[champ]['stats'][base_stat]
        sorted_list = sorted(sorted_list.items(), key = lambda x: int(x[1]), reverse=True)
        response = Response(sorted_list)
        return response
    except KeyError:
        return "Bruh that ain't a stat"

def get_champ_data_list():
    versions = lol_watcher.data_dragon.versions_for_region(my_region) #mock lolwatch data dragon. if(champ) give me back somethign back
    champions_version = versions['n']['champion'] #mock the right versions
    current_champ_list = lol_watcher.data_dragon.champions(champions_version)
    champion_data_list = OrderedDict(current_champ_list['data']) #mock the correct data_list is it in correct order
    return champion_data_list

def get_map(region):
    maps = lol_watcher.data_dragon.maps("11.10.1")
    try:
        return maps['data']
    except Exception as e:
        return maps

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
