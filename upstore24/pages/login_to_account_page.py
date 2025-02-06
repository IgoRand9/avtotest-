from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from base.base_class import Base


class LoginToAccount(Base):

    url = 'https://upstore24.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#     # Locators

    personal_account = "(//a[text()='Личный кабинет'])[2]"
    login_field = "//input[@name='email']"
    password_field = "//input[@name='password']"
    button_login = "//button[@name='commit']"
    check_word = "//h1[@class='co-checkout-title co-title co-title--h1']"
    warning_text = "//div[@class='co-notice--danger co-notice--flash']"




    # Getters


    def get_personal_account(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.personal_account)))

    def get_login_field(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.login_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.button_login)))

    def get_check_word(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.check_word)))

    def get_warning_text(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.warning_text)))


    #  Actions

    def click_personal_account(self):
        self.get_personal_account().click()
        print("Click personal account")

    def input_login(self, user_name):
        self.get_login_field().send_keys(user_name)
        print("Input user name")

    def input_password(self, password_name):
        self.get_password_field().send_keys(password_name)
        print("Input password field")

    def click_button_login(self):
        self.get_button_login().click()
        print("Click button login")




    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_personal_account()
        self.input_login("+79658073453")
        self.input_password("Pass12345")
        self.click_button_login()
        self.assert_word(self.get_check_word(), 'История заказов')
        self.get_screenshot()



    def negative_authorization_pass(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_personal_account()
        self.input_login("+79658073453")
        self.input_password("Pass1234")
        self.click_button_login()
        self.assert_word(self.get_warning_text(), 'Сочетание логина и пароля не подходит')

    def negative_authorization_login(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_personal_account()
        self.input_login("+7965807")
        self.input_password("Pass12345")
        self.click_button_login()
        self.assert_word(self.get_warning_text(), 'Сочетание логина и пароля не подходит')
