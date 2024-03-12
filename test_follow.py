from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest


class TestFollowUnfollow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.twitch.tv")

        self.login()

    def login(self):

        login_button = self.driver.find_element(By.XPATH, "//button[contains(@data-a-target, 'login-button')]")
        login_button.click()

        username_field = self.driver.find_element(By.ID, "login-username")
        password_field = self.driver.find_element(By.ID, "password-input")
        username_field.send_keys("ulyvean")
        password_field.send_keys("joonsonmin2024")
        password_field.submit()

        time.sleep(5)

    def test_follow_unfollow_channel(self):
        channel_url = "https://www.twitch.tv/relaxbeats"

        self.driver.get(channel_url)

        follow_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-a-target, 'follow-button')]")))

        follow_button.click()

        time.sleep(2)

        assert "Unfollow" in follow_button.text

        follow_button.click()

        time.sleep(2)

        assert "Follow" in follow_button.text

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
