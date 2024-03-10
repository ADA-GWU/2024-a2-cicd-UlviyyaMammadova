from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.twitch.tv/login")

    def test_valid_login(self):
        username = "ulyvean"
        password = "joonsonmin2024"

        username_field = self.driver.find_element(By.XPATH, "//input[@id='login-username']")
        password_field = self.driver.find_element(By.XPATH, "//input[@id='password-input']")
        login_button = self.driver.find_element(By.XPATH, "//button[@data-a-target='passport-login-button']")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        time.sleep(5)

        assert "Twitch" in self.driver.title

    def test_invalid_login(self):
        username = "invalid_username"
        password = "invalid_password"

        username_field = self.driver.find_element(By.XPATH, "//input[@id='login-username']")
        password_field = self.driver.find_element(By.XPATH, "//input[@id='password-input']")
        login_button = self.driver.find_element(By.XPATH, "//button[@data-a-target='passport-login-button']")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        time.sleep(5)

        assert "Login" in self.driver.title

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
