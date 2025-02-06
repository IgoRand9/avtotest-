from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class MainPage(Base):

    url = 'https://upstore24.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    logo = "(//a[@class='logo'])[1]"
    catalog = "//span[@class='hamburger hamburger--arrow-down']"
    cart = "//li[@class='user_icons-item js-user_icons-item']"
    about_us = "(//a[text()='О нас'])[2]"
    guarantee = "(//a[text()='Гарантия'])[2]"
    contacts = "(//a[text()='Контакты'])[2]"
    delivery = "(//a[text()='Доставка'])[2]"
    payment = "(//a[text()='Оплата'])[2]"
    feedback = "(//a[text()='Отзывы'])[2]"
    check_word_about_us = "//h1[@class='text-title']"
    check_word_guarantee = "//h1[@class='text-title']"
    check_word_contacts = "//h1[@class='text-title']"
    check_word_delivery = "//h1[@class='text-title']"
    check_word_payment = "//h1[@class='text-title']"
    search_field = "(//input[@type='search'])[1]"
    banner_apple_iPhone = "//span[text()='Смартфоны Apple iPhone']"
    check_word_banner_apple_iPhone = "//h1[@class='section-title']"
    banner_apple_tablets = "//span[text()='Планшеты Apple iPad']"
    check_word_apple_tablets = "//h1[@class='section-title']"
    banner_apple_watch = "//span[text()='Часы Apple Watch']"
    check_word_apple_watch = "//h1[@class='section-title']"
    banner_apple_macbook = "//span[text()='Ноутбуки Apple MacBook']"
    check_word_apple_macbook = "//h1[@class='section-title']"
    banner_apple_airpods = "//span[text()='Наушники Apple AirPods']"
    check_word_apple_airpods = "//h1[@class='section-title']"
    favorites_button = "(//a[@class='user_icons-icon js-user_icons-icon-favorites'])[1]"



    # Getters

    def get_select_catalog(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_select_cart(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.cart)))

    def get_about_us(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.about_us)))

    def get_guarantee(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.guarantee)))

    def get_contacts(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.contacts)))

    def get_delivery(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.delivery)))

    def get_feedback(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.feedback)))

    def get_payment(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.payment)))

    def get_check_word_contacts(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.check_word_contacts)))

    def get_check_word_about_us(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.check_word_about_us)))

    def get_check_word_guarantee(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.check_word_guarantee)))

    def get_check_word_delivery(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.check_word_delivery)))

    def get_check_word_payment(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.check_word_payment)))


    def get_search_field(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.search_field)))


    def get_banner_apple_iPhone(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.banner_apple_iPhone)))

    def get_check_word_banner(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.check_word_banner_apple_iPhone)))


    def get_banner_apple_tablets(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.banner_apple_tablets)))


    def get_banner_apple_watch(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.banner_apple_watch)))


    def get_banner_apple_macbook(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.banner_apple_macbook)))


    def get_banner_apple_airpods(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.banner_apple_airpods)))

    def get_logo(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.logo)))


    def get_favorites_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.favorites_button)))



    #  Actions

    def click_catalog(self):
        self.get_select_catalog().click()
        print("Click catalog")

    def click_cart(self):
        self.get_select_cart().click()
        print("Click cart")

    def click_about_us(self):
        self.get_about_us().click()
        print("Click about us")

    def click_guarantee(self):
        self.get_guarantee().click()
        print("Click guarantee")

    def click_contacts(self):
        self.get_contacts().click()
        print("Click contacts")

    def click_delivery(self):
        self.get_delivery().click()
        print("Click delivery")

    def click_payment(self):
        self.get_payment().click()
        print("Click payment")

    def click_feedback(self):
        self.get_feedback().click()
        print("Click feedback")


    def input_search_field(self, categ_product):
        self.get_search_field().send_keys(categ_product)
        print("Input search field")


    def click_search_field(self):
        self.get_search_field().send_keys(Keys.RETURN)
        print("Press search field")

    def click_banner_apple_iPhone(self):
        self.get_banner_apple_iPhone().click()
        print("Press banner apple iPhone")

    def click_banner_apple_tablets(self):
        self.get_banner_apple_tablets().click()
        print("Press banner apple tablets")

    def click_banner_apple_watch(self):
        self.get_banner_apple_watch().click()
        print("Press banner apple watch")

    def click_banner_apple_macbook(self):
        self.get_banner_apple_macbook().click()
        print("Press banner apple macbook")

    def click_banner_apple_airpods(self):
        self.get_banner_apple_airpods().click()
        print("Press banner apple airpods")

    def click_favorites_button(self):
        self.get_favorites_button().click()
        print("Click favorites button")


  # Methods

    def select_catalog(self):

        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_catalog()




    def section_clickability(self):

        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_about_us()
        self.assert_word(self.get_check_word_about_us(), 'О нас')
        self.click_guarantee()
        self.assert_word(self.get_check_word_guarantee(), 'Гарантия')
        self.click_contacts()
        self.assert_word(self.get_check_word_contacts(), 'Контакты')
        self.click_delivery()
        self.assert_word(self.get_check_word_delivery(), 'Доставка')
        self.click_payment()
        self.assert_word(self.get_check_word_payment(), 'Оплата')
        self.click_feedback()
        self.assert_url('https://yandex.ru/maps/org/upstore24/65273314325/reviews/?indoorLevel=1&ll=37.502786%2C55.741140&z=17')
        self.driver.back()
        self.get_current_url()
        self.get_logo().click()
        self.click_banner_apple_iPhone()
        self.assert_word(self.get_check_word_banner(), 'Смартфоны Apple iPhone')
        self.driver.back()
        self.click_banner_apple_tablets()
        self.assert_word(self.get_check_word_banner(), 'Планшеты Apple iPad')
        self.driver.back()
        self.click_banner_apple_watch()
        self.assert_word(self.get_check_word_banner(), 'Смарт часы Apple Watch')
        self.driver.back()
        self.click_banner_apple_macbook()
        self.assert_word(self.get_check_word_banner(), 'Ноутбуки Apple MacBook')
        self.driver.back()
        self.click_banner_apple_airpods()
        self.assert_word(self.get_check_word_banner(), 'Беспроводные наушники Apple AirPods')
        self.driver.back()



    def search_product(self):

        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.get_search_field()
        self.input_search_field('Смартфоны')
        self.click_search_field()
        self.get_screenshot()
        self.input_search_field('Планшеты')
        self.click_search_field()
        self.get_screenshot()
        self.input_search_field('Ноутбуки')
        self.click_search_field()
        self.get_screenshot()





