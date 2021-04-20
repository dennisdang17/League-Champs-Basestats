Feature: League Champion Base State Sorted List
  As a player,
  I want to know the base stats of a league champion,
  So that I can know what is the strongest champion level 1 without items.


  Scenario Outline: My API will be queried with a base_stat to return the champ with that highest base stat
    When the League API is queried with "<base_stat>"
    Then the response status code is 200
    And the response is the "<champion>"

    Examples: Champions
      | base_stat           | champion         |
      | armor               | Braum            |
      | movespeed           | MasterYi         |
      | hp                  | Tryndamere       |
