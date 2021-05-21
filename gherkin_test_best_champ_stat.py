from best_champ_stat import best_champ_for_stat
from pytest_bdd import scenarios, when, then
import pytest

scenarios('league_champion.feature')

@pytest.fixture
@when('my API is queried with "<base_stat>"')
def stat_response(base_stat):
    response = best_champ_for_stat(base_stat)
    return response
    
@then('the response status code is 200')
def status_code_check(stat_response):
    assert stat_response.response_code == 200

@then('the champion is "<champion>"')
def base_stat_returns_champion(stat_response, champion):
    assert stat_response.sorted_list[0][0] == champion