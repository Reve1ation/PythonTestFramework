Feature: amazon.com Functionality

  @id_1
  Scenario: User can search for a product
    Given the user opens amazon main page
    Then the amazon main page is displayed
    When search "iPhone" in the search field
    Then the amazon search results page is displayed
    When the user in "Brand" filter selects "Apple"
    Then user verify all results have "Apple" text in it


