from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        # Set up the Chrome WebDriver and open the Twitch login page
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.twitch.tv/login")

    def test_valid_login(self):
        # Test case to verify login with valid credentials
        username = "ulyvean"
        password = "joonsonmin2024"

        # Find the username, password, and login button elements
        username_field = self.driver.find_element(By.XPATH, "//input[@id='login-username']")
        password_field = self.driver.find_element(By.XPATH, "//input[@id='password-input']")
        login_button = self.driver.find_element(By.XPATH, "//button[@data-a-target='passport-login-button']")

        # Enter the username and password, and click the login button
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        # Wait for the page to load
        time.sleep(5)

        # Assert that the page title contains "Twitch"
        assert "Twitch" in self.driver.title

    def test_invalid_login(self):
        # Test case to verify behavior with invalid credentials
        username = "invalid_username"
        password = "invalid_password"

        # Find the username, password, and login button elements
        username_field = self.driver.find_element(By.XPATH, "//input[@id='login-username']")
        password_field = self.driver.find_element(By.XPATH, "//input[@id='password-input']")
        login_button = self.driver.find_element(By.XPATH, "//button[@data-a-target='passport-login-button']")

        # Enter invalid username and password, and click the login button
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        # Wait for the page to load
        time.sleep(5)

        # Assert that the page title contains "Login"
        assert "Login" in self.driver.title

    def tearDown(self):
        # Close the WebDriver after each test
        self.driver.quit()

if __name__ == "__main__":
    # Run the test cases
    unittest.main()
