# Automated Testing for Twitch Web Application

This repository contains automated tests for various functionalities of the Twitch web application using Selenium WebDriver and Python unittest framework.

## Prerequisites

- Python installed on your system
- Chrome WebDriver installed and added to your system's PATH

## Setup

- Clone this repository to your local machine.
- Install the required Python packages 

## Running the Tests

You can run the tests individually or all at once.

To run individual tests, use the following command:

```
python test_filename.py
```


## Test Descriptions

### 1. test_login.py

This test suite includes tests for validating the login functionality of the Twitch web application.

#### Test Cases:
1. `test_valid_login`: Validates the login process with valid credentials. It enters valid username and password, clicks the login button, and verifies that the user is redirected to the Twitch home page.
   
2. `test_invalid_login`: Validates the behavior when invalid credentials are provided. It enters invalid username and password, clicks the login button, and verifies that the login page is displayed again.

### 2. test_search.py

This test suite verifies the search functionality of the Twitch web application.

#### Test Cases:
1. `test_search_game`: Searches for a specific game and verifies that the search result contains the expected game name. It enters the game name in the search field, submits the search, and checks if the search results page displays the expected game.

### 3. test_follow.py

This test suite tests the follow functionality of the Twitch web application.

#### Test Cases:
1. `test_follow_channel`: Logs in to Twitch, navigates to a specific channel, follows the channel, and verifies that the follow action is successful. It clicks on the follow button for the specified channel and checks if the button text changes to "Unfollow" to confirm successful follow.

## Notes

- These tests use the Chrome WebDriver. Make sure you have the Chrome browser installed on your system.
- Ensure that you have a stable internet connection while running the tests.
- The test scripts are written using Python's unittest framework and Selenium WebDriver.
