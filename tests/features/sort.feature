Feature: Product Sorting Functionality

Scenario: Sort products by Name (A to Z)
Given user open login page
When user enters valid credetials
And user selects "Name (A to Z)" from dropdown
Then products should be sorted alphabetically from A to Z
And all products should be visible

Scenario: Sort products by Name (Z to A)
Given user open login page
When user enters valid credetials
And user selects "Name (Z to A)" from dropdown
Then products should be sorted alphabetically from Z to A
And all products should be visible

Scenario: Sort products by Price (Low to High)
Given user open login page
When user enters valid credetials
And user selects "Price (low to high)" from dropdown
Then products should be sorted by price from lowest to highest
And all products should be visible

Scenario: Sort products by Price (High to Low)
Given user open login page
When user enters valid credetials
And user selects "Price (high to low)" from dropdown
Then products should be sorted by price from highest to lowest
And all products should be visible

Scenario: Verify sort dropdown is visible
Given user open login page
When user enters valid credetials
Then sort dropdown should be visible on inventory page
And sort dropdown should contain all available options

Scenario: Verify default sort order
Given user open login page
When user enters valid credetials
Then products should be displayed in default order
