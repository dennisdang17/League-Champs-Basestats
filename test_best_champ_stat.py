from best_champ_stat import get_map, lol_watcher, get_champ_data_list, best_champ_for_stat, my_region

#Tests for happy 
def test_get_map(mocker):
    mocker.patch.object(lol_watcher.data_dragon, 'maps')
    lol_watcher.data_dragon.maps.return_value = "Summoner's Rift"
    expected = lol_watcher.data_dragon.maps.return_value
    actual = get_map('11.10.1')
    assert expected == actual

#Tests for best_champ_for_stat
def test_best_champ_stat():
    actual = best_champ_for_stat('bruh')
    expected = "Bruh that ain't a stat"
    assert actual == expected

#Tests for get_champ_data_list
def test_get_champ_data_list(mocker):
    mocker.patch.object(lol_watcher.data_dragon, 'versions_for_region')
    lol_watcher.data_dragon.versions_for_region.return_value = {'n': {'item': '11.10.1', 'rune': '7.23.1', 'mastery': '7.23.1', 'summoner': '11.10.1', 'champion': '11.10.1', 'profileicon': '11.10.1', 'map': '11.10.1', 'language': '11.10.1', 'sticker': '11.10.1'}, 'v': '11.10.1', 'l': 'en_US', 'cdn': 'https://ddragon.leagueoflegends.com/cdn', 'dd': '11.10.1', 'lg': '11.10.1', 'css': '11.10.1', 'profileiconmax': 28, 'store': None}
    mocker.patch.object(lol_watcher.data_dragon, 'champions')
    lol_watcher.data_dragon.champions.return_value = {'data': {'Aatrox': {'version': '11.10.1', 'id': 'Aatrox', 'key': '266', 'name': 'Aatrox', 'title': 'the Darkin Blade', 'blurb': 'Once honored defenders of Shurima against the Void, Aatrox and his brethren would eventually become an even greater threat to Runeterra, and were defeated only by cunning mortal sorcery. But after centuries of imprisonment, Aatrox was the first to find...', 'info': {'attack': 8, 'defense': 4, 'magic': 3, 'difficulty': 4}, 'image': {'full': 'Aatrox.png', 'sprite': 'champion0.png', 'group': 'champion', 'x': 0, 'y': 0, 'w': 48, 'h': 48}, 'tags': ['Fighter', 'Tank'], 'partype': 'Blood Well', 'stats': {'hp': 580, 'hpperlevel': 90, 'mp': 0, 'mpperlevel': 0, 'movespeed': 345, 'armor': 38, 'armorperlevel': 3.25, 'spellblock': 32, 'spellblockperlevel': 1.25, 'attackrange': 175, 'hpregen': 3, 'hpregenperlevel': 1, 'mpregen': 0, 'mpregenperlevel': 0, 'crit': 0, 'critperlevel': 0, 'attackdamage': 60, 'attackdamageperlevel': 5, 'attackspeedperlevel': 2.5, 'attackspeed': 0.651}}}}
    expected = lol_watcher.data_dragon.champions.return_value['data']
    actual = get_champ_data_list()
    assert expected == actual