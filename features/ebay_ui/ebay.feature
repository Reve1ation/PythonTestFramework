Feature: eBay.com Functionality

  @id_1
  Scenario: User can search for a product
    Given the user opens eBay main page
    Then the eBay main page is displayed
    When the user searches "iPhone"
    Then the eBay search results page has specific results

  @id_2
  Scenario: User can add an item to the cart
    Given the user opens eBay main page
    Then the eBay main page is displayed
    When the user searches "hdmi cable"
    And user selects the "Buy It Now" filter
    And the user selects the "random" item
    And the user adds item to cart
    Then the item is added to the cart

  @id_3
  Scenario: User can view empty cart
    Given the user opens eBay Cart Page
    Then the eBay cart page is displayed

  @id_4
  Scenario: User can remove an item from the cart
    Given the user opens eBay main page
    Then the eBay main page is displayed
    When the user searches "optics"
    And user selects the "Buy It Now" filter
    And the user selects the "random" item
    And the user adds item to cart
    Then the item is added to the cart
    Given the user opens eBay cart page
    Then the eBay cart page is displayed
    When the user removes one random item from the cart
    Then the item is removed from the cart

  @id_5
  Scenario: User can sign in to their account
    Given the user opens eBay main page
    Then the user is not signed in
    Given the user signing in as Valid eBay User
    Then the user is signed in

  @id_6
  Scenario: User can sign out of their account
    Given the user signing in as Valid eBay User
    Then the user is signed in
    When the user leaves its account
    Given the user opens eBay main page
    Then the user is not signed in

  @id_7
  Scenario: User can filter search results
    Given the user opens eBay main page
    When the user searches "shoes"
    And the user applies the "Brand" filter as "adidas"
    Then the eBay search results page has specific results
