import time
import selenium
# print(selenium.__version__)
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:



    def setup_method(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        driver.get("https://www.python-unlimited.com/youtube/login-form.php")
        username = driver.find_element(By.ID, "username")
        username.send_keys("admin")
        password = driver.find_element(By.ID, "password")
        password.send_keys("admin")
        submit = driver.find_element(By.ID, "submit-button")
        submit.click()
        expected_text = "Login failed"
        actual_text = driver.find_element(By.ID, "result").text
        assert actual_text == expected_text, "Login should be successful but is not"
        time.sleep(5)
