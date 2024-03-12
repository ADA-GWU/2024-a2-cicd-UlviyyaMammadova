from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import unittest

class TestSearch(unittest.TestCase):
    def setUp(self):
        # Set up the Chrome WebDriver and open the Twitch homepage
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.twitch.tv")

    def test_search_game(self):
        # Test case to search for a game on Twitch
        game_name = "League of Legends"

        # Find the search input field
        search_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-a-target='tray-search-input'] input")))

        # Enter the game name in the search field and press Enter
        search_field.send_keys(game_name)
        time.sleep(1)  # Wait for suggestions to load
        search_field.send_keys(Keys.RETURN)

        # Wait for the page to load
        time.sleep(5)

        # Assert that the game name is present in the page source
        assert game_name in self.driver.page_source

    def tearDown(self):
        # Close the WebDriver after each test
        self.driver.quit()

if __name__ == "__main__":
    # Run the test cases
    unittest.main()
