Feature: League Champion Title Query
  As a player,
  I want to know the base stats of a league champion,
  So that I can know what is the strongest champion level 1 without items.


  Scenario Outline: League API will query a champion to return champion information
    When the League API is queried with "<champion>"
    Then the response status code is 200
    And the response is that "<base_stat>"

    Examples: Champions
      | champion           | base_stat                    |
      | Nasus              | the Curator of the Sands |
      | MonkeyKing         | the Monkey King          |
      | MasterYi           | the Wuju Bladesman       |