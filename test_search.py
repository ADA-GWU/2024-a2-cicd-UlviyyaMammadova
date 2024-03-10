from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import unittest


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.twitch.tv")

    def test_search_game(self):
        game_name = "League of Legends"

        search_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-a-target='tray-search-input'] input")))

        search_field.send_keys(game_name)

        time.sleep(1)

        search_field.send_keys(Keys.RETURN)

        time.sleep(5)
        assert game_name in self.driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
