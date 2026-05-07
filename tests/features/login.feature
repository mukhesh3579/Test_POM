Feature: Login functionality

@smoke
Scenario: Successful login
Given user open login page
When user enters valid credetials
Then user should navigate to inventory page

@negative
Scenario: Invlid login
Given user open login page
When user enters invalid credentials
Then login error should display

@logout
Scenario: Successful logout
Given user open login page
When user enters valid credetials
And user clicks logout button
Then user should navigate to login page