from riotwatcher import LolWatcher
import pytest
from pytest_bdd import scenarios, when, then

lol_watcher = LolWatcher('RGAPI-ff1d3c7a-90c9-4e4b-954c-404ab6543f55')

my_region = 'na1'
scenarios('../Assignment2/features/league_champion.feature')


@pytest.fixture
@when('the League API is queried with "<champion>"')
def league_response(champion):
    versions = lol_watcher.data_dragon.versions_for_region(my_region)
    champions_version = versions['n']['champion']
    current_champ_list = lol_watcher.data_dragon.champions(champions_version)
    champ = current_champ_list['data'][champion]
    return champ


@then('the response status code is 200')
def league_response_code(league_response):
    try:
        league_response['title']
        return True
    except KeyError:
        return False


@then('the response is that "<title>"')
def schedule_response_has_episodes(league_response, title):
    assert title == league_response['title']
