Feature: Scenario 13

  Scenario: User can go to settings and see the right number of UI elements
    Given Open the main page
    When Log in to the page, email: pohnsuda40249@gmail.com password: MP17041994
    Then Click on settings option
    Then Verify the right page opens
    Then Verify there are 12 options for the settings
    Then Verify “connect the company” button is available