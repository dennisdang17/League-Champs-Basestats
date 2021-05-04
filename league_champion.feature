Feature: League Champion Base State Sorted List
  As a player,
  I want to know the base stats of a league champion,
  So that I can know what is the strongest champion level 1 without items.

  Scenario Outline: My API Query
    When my API is queried with "<base_stat>"
    Then the response status code is 200
    And the champion is "<champion>"

    Examples: Champions
      | base_stat           | champion         |
      | armor               | Braum            |
      | movespeed           | MasterYi         |
      | hp                  | Tryndamere       |
