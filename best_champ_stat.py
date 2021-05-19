from collections import OrderedDict
from flask import Flask, render_template, request, redirect, url_for
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
    
@app.route('/data', methods=['GET', 'POST'])
def data():
    form_data = request.form
    print("\n This is form data \n")
    base_stat = form_data['Basestat']
    #base_stat formatter!
    try:
        return redirect(url_for(base_stat))
    except Exception as e:
        return f"Base stat does not exist"


@app.route('/hp', methods = ['GET'])
def hp():
    if request.method == 'GET':
        response = best_champ_for_stat("hp")
        output = json.dumps(response.sorted_list)
        return f"" + output

#hp per level
@app.route('/hpperlevel', methods = ['GET'])
def hpperlevel():
    if request.method == 'GET':
        response = best_champ_for_stat("hpperlevel")
        output = json.dumps(response.sorted_list)
        return f"" + output

#mana pool
@app.route('/mp')
def mp():
    if request.method == 'GET':
        response = best_champ_for_stat("mp")
        output = json.dumps(response.sorted_list)
        return f"" + output

#mana per level
@app.route('/mpperlevel')
def mpperlevel():
    if request.method == 'GET':
        response = best_champ_for_stat("mpperlevel")
        output = json.dumps(response.sorted_list)
        return f"" + output

#move speed
@app.route('/movespeed')
def movespeed():
    if request.method == 'GET':
        response = best_champ_for_stat("movespeed")
        output = json.dumps(response.sorted_list)
        return f"" + output

#armor
@app.route('/armor')
def armor():
    if request.method == 'GET':
        response = best_champ_for_stat("armor")
        output = json.dumps(response.sorted_list)
        return f"" + output

#armor per level
@app.route('/armorperlevel')
def armorperlevel():
    if request.method == 'GET':
        response = best_champ_for_stat("armorperlevel")
        output = json.dumps(response.sorted_list)
        return f"" + output

#spell block / magic resist
@app.route('/spellblock')
def spellblock():
    if request.method == 'GET':
        response = best_champ_for_stat("spellblock")
        output = json.dumps(response.sorted_list)
        return f"" + output

#spell block per level / magic resist per level
@app.route('/spellblockperlevel')
def spellblockperlevel():
    if request.method == 'GET':
        response = best_champ_for_stat("spellblockperlevel")
        output = json.dumps(response.sorted_list)
        return f"" + output

#attack range
@app.route('/attackrange')
def attackrange():
    if request.method == 'GET':
        response = best_champ_for_stat("attackrange")
        output = json.dumps(response.sorted_list)
        return f"" + output

#hpregen
@app.route('/hpregen')
def hpregen():
    if request.method == 'GET':
        response = best_champ_for_stat("hpregen")
        output = json.dumps(response.sorted_list)
        return f"" + output

#hpregenperlevel
@app.route('/hpregenperlevel')
def hpregenperlevel():
    if request.method == 'GET':
        response = best_champ_for_stat("hpregenperlevel")
        output = json.dumps(response.sorted_list)
        return f"" + output

#mana regen
@app.route('/mpregen')
def mpregen():
    if request.method == 'GET':
        response = best_champ_for_stat("mpregen")
        output = json.dumps(response.sorted_list)
        return f"" + output
        
#mana regen per level
@app.route('/mpregenperlevel')
def mpregenperlevel():
    if request.method == 'GET':
        response = best_champ_for_stat("mpregenperlevel")
        output = json.dumps(response.sorted_list)
        return f"" + output
        
#crit
@app.route('/crit')
def crit():
    if request.method == 'GET':
        response = best_champ_for_stat("crit")
        output = json.dumps(response.sorted_list)
        return f"" + output
        
#mana regen per level
@app.route('/critperlevel')
def critperlevel():
    if request.method == 'GET':
        response = best_champ_for_stat("critperlevel")
        output = json.dumps(response.sorted_list)
        return f"" + output
                
#AD
@app.route('/attackdamage', methods = ['GET'])
def attackdamage():
    if request.method == 'GET':
        response = best_champ_for_stat("attackdamage")
        output = json.dumps(response.sorted_list)
        return f"" + output
    
#AD per level
@app.route('/attackdamageperlevel', methods = ['GET'])
def attackdamageperlevel():
    if request.method == 'GET':
        response = best_champ_for_stat("attackdamageperlevel")
        output = json.dumps(response.sorted_list)
        return f"" + output
    
#attackspeedperlevel
@app.route('/attackspeedperlevel', methods = ['GET'])
def attackspeedperlevel():
    if request.method == 'GET':
        response = best_champ_for_stat("attackspeedperlevel")
        output = json.dumps(response.sorted_list)
        return f"" + output

#attackspeed
@app.route('/attackspeed', methods = ['GET'])
def attackspeed():
    if request.method == 'GET':
        response = best_champ_for_stat("attackspeed")
        output = json.dumps(response.sorted_list)
        return f"" + output
    
#custom response class
class Response:
    response_code = 0
    sorted_list = {}
    def __init__(self, sorted_list):
        self.response_code = 200
        self.sorted_list = sorted_list
    def __str__(self):
        return self.sorted_list

#Gets a sorted list of champions from best to worst with a given base stat
def best_champ_for_stat(base_stat):
    try:
        data_list = get_champ_data_list()
        sorted_list = OrderedDict()
        for champ in data_list:
            print(data_list[champ]['stats'])
            sorted_list[champ] = data_list[champ]['stats'][base_stat]
        sorted_list = sorted(sorted_list.items(), key = lambda x: int(x[1]), reverse=True)
        response = Response(sorted_list)
        return response
    except KeyError:
        return "Bruh that ain't a stat"

#helper function that helps getting the list of champs from the riot api
def get_champ_data_list():
    versions = lol_watcher.data_dragon.versions_for_region(my_region) #mock lolwatch data dragon. if(champ) give me back somethign back
    champions_version = versions['n']['champion'] #mock the right versions
    current_champ_list = lol_watcher.data_dragon.champions(champions_version)
    champion_data_list = OrderedDict(current_champ_list['data']) #mock the correct data_list is it in correct order
    return champion_data_list

#gets the current map
def get_map(region):
    maps = lol_watcher.data_dragon.maps("11.10.1")
    try:
        return maps['data']
    except Exception as e:
        return maps

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
