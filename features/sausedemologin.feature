Feature: SauceDemo Login

  Scenario: login to SauceDemo with valid parameters
    Given I launch chrome browser
    When  I open sauce demo homepage
    And enter username "standard_user" and password "secret_sauce"
    And click login button
    Then user must successfully login to Dashboard page


  Scenario Outline: Login to SauceDemo with multiple parameters
    Given I launch chrome browser
    When  I open sauce demo homepage
    And enter username "<username>" and password "<password>"
    And click login button
    Then user must successfully login to Dashboard page


    Examples:
      | username      | password     |
      | standard_user | secret_sauce |
      | visual_user   | secret_sauce |