Feature: eBay.com Functionality

  Scenario: User can search for a product
    Given the user is on the eBay main page
    When the user enters "iPhone" in the search bar
    And the user clicks the "Search" button
    Then the eBay search results page is displayed

  Scenario: User can add an item to the cart
    Given the user is on the eBay main page
    When the user enters "hdmi cable" in the search bar
    And the user clicks the "Search" button
    And user selects the "Buy It Now" filter
    And the user selects the "random" item
    And the user clicks the "Add to Cart" button
    Then the item is added to the cart

  Scenario: User can view the cart
    Given the user is on the eBay main page
    When the user clicks the "Cart" button
    Then the cart page is displayed

  Scenario: User can remove an item from the cart
    Given the user is on the eBay main page
    When the user enters "optics" in the search bar
    And the user clicks the "Search" button
    And user selects the "Buy It Now" filter
    And the user selects the "random" item
    And the user clicks the "Add to Cart" button
    Then the item is added to the cart
    When the user clicks the "Cart" button
    Then the cart page is displayed
    When the user removes one random item from the cart
    Then the item is removed from the cart

#  Scenario: User can proceed to checkout
#    Given the user is on the eBay cart page
#    When the user clicks the "Proceed to Checkout" button
#    Then the checkout page is displayed

#  Scenario: User can sign in to their account
#    Given the user is on the eBay homepage
#    When the user clicks the "Sign In" button
#    And the user enters their username and password
#    And the user clicks the "Sign In" button
#    Then the user is logged in to their account
#
#  Scenario: User can sign out of their account
#    Given the user is logged in to their account
#    When the user clicks the account dropdown menu
#    And the user clicks the "Sign Out" option
#    Then the user is logged out of their account
#
#  Scenario: User can view their purchase history
#    Given the user is logged in to their account
#    When the user clicks the "Purchase History" link
#    Then the purchase history page is displayed
#
#  Scenario: User can track a package
#    Given the user is logged in to their account
#    When the user clicks the "Track Package" link
#    And the user enters the tracking number
#    And the user clicks the "Track" button
#    Then the tracking information is displayed
#
#  Scenario: User can change their account settings
#    Given the user is logged in to their account
#    When the user clicks the account dropdown menu
#    And the user clicks the "Account Settings" option
#    Then the account settings page is displayed
#
#  Scenario: User can update their email address
#    Given the user is on the account settings page
#    When the user clicks the "Edit" button for the email address
#    And the user enters a new email address
#    And the user clicks the "Save" button
#    Then the email address is updated successfully
#
#  Scenario: User can view seller information
#    Given the user is on the product details page
#    When the user clicks the seller's username
#    Then the seller's profile page is displayed
#
#  Scenario: User can ask a question to the seller
#    Given the user is on the seller's profile page
#    When the user clicks the "Ask a question" button
#    And the user enters a question
#    And the user clicks the "Send" button
#    Then the question is submitted successfully
#
#  Scenario: User can view seller feedback
#    Given the user is on the seller's profile page
#    When the user clicks the "View feedback" link
#    Then the seller's feedback page is displayed
#
#  Scenario: User can leave feedback for a seller
#    Given the user is on the seller's feedback page
#    When the user clicks the "Leave feedback" button
#    And the user selects a feedback rating
#    And the user enters feedback comments
#    And the user clicks the "Submit" button
#    Then the feedback is submitted successfully
