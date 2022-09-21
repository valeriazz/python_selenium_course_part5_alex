from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import Login_page

"""smoke путь от авторизации до перехода в корзину с товаром и другим юзером"""

class Test_2():

    def select_product(self):
        driver = webdriver.Chrome(executable_path='C:\\resource\\chromedriver.exe')
        # executable_path=... - это аналог s = Service('C:\\pythonSelenium\\chromedriver.exe')
        # driver = webdriver.Chrome(service=s)

        base_url = 'https://www.saucedemo.com'
        driver.get(base_url)
        driver.maximize_window()
        # если запускать тест через метод класса, то браузер закрывается автоматически, не требуя close()

        print('Start Test')

        login_problem_user = 'problem_user'
        password_all = 'secret_sauce'

        login = Login_page(driver)
        login.authorization(login_problem_user, password_all)

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print('Select Product 1')

        go_to_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 "//a[@class='shopping_cart_link']")))
        go_to_cart.click()
        print('Go to Cart')

        success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        value_success_test = success_test.text
        assert value_success_test == 'YOUR CART'  # здесь YOUR CART написан заглавными, несмотря на то, что в теге
        # идет Your Cart, т.к. в css стилях для your cart стоит галочка "uppercase". Так assert проходит!
        print('Test is Over!')


test = Test_2()
test.select_product()



