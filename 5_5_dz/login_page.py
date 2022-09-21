from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                     "//input[@id='user-name']")))
        user_name.send_keys(login_name)
        print("Input login")
        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                    "//input[@id='password']")))
        password.send_keys(login_password)
        print("Input password")
        login_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        "//input[@id='login-button']")))
        login_button.click()
        print("Click login button")
