Feature: Saucedemo logo

  Scenario: Logo presence on saucedemo login page
    Given launch chrome browser
    When open saucedemo website
    Then verify logo present on the page
    And close browser
