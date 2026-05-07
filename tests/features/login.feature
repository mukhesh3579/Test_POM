Feature: Login functionality

#@smoke
#Scenario: Successful login
#Given user open login page
#When user enters valid credetials
#Then user should navigate to inventory page

@negative
Scenario: Invalid login
Given user open login page
When user enters invalid credentials
Then login error should display


