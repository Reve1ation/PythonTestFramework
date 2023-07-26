Feature: disney functionality

  Scenario Outline: User can open header menus
    Given the user opens custom main page
    Then the custom main page is displayed
    When the user navigate to <main_menu>
    Then Check that page has <title>

    Examples:
      | main_menu     | title                                                     |
      |Parks & Travel | Family Vacations at Disney Parks & Resorts                |
      |Disney+        |Stream Disney, Pixar, Marvel, Star Wars, Nat Geo \| Disney+|



  Scenario Outline: User can use submenus in the header
    Given the user opens custom main page
    Then the custom main page is displayed
    When the user hover <main_menu> and select <submenu>
    Then Check that page has <title>

    Examples: Disney+
    |main_menu  |submenu            |title                                                 |
    |Disney+    |On Disney+         |On Disney+ \| What's New and Coming Soon on Disney+   |
    |Disney+    |The Disney Bundle  |Disney Bundle - Stream Disney+, Hulu, and ESPN+       |