from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class TestFollowChannel(unittest.TestCase):
    def setUp(self):
        # Set up the Chrome WebDriver and open the Twitch homepage
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.twitch.tv")

        # Perform login before each test
        self.login()

    def login(self):
        # Method to login to Twitch
        login_button = self.driver.find_element(By.XPATH, "//button[contains(@data-a-target, 'login-button')]")
        login_button.click()

        username_field = self.driver.find_element(By.ID, "login-username")
        password_field = self.driver.find_element(By.ID, "password-input")
        username_field.send_keys("ulyvean")
        password_field.send_keys("joonsonmin2024")
        password_field.submit()
        time.sleep(5)

    def test_follow_channel(self):
        # Test case to follow a Twitch channel
        channel_url = "https://www.twitch.tv/relaxbeats"

        # Open the channel URL
        self.driver.get(channel_url)

        # Find and click the follow button
        follow_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-a-target, 'follow-button')]")))

        follow_button.click()

        # Wait for a short duration
        time.sleep(2)

        # Assert that the follow button text does not contain "Unfollow"
        assert "Unfollow" not in follow_button.text

    def tearDown(self):
        # Close the WebDriver after each test
        self.driver.quit()

if __name__ == "__main__":
    # Run the test cases
    unittest.main()
