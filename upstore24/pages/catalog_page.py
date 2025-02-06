from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class CatalogPage(Base):



    # locators

    phones = "(//a[text()='Смартфоны'])[5]"
    tablets = "(//a[text()='Планшеты'])[5]"
    laptops = "(//a[text()='Ноутбуки'])[5]"
    computers = "(//a[text()='Компьютеры'])[5]"
    watches_and_bracelets = "(//a[text()='Смарт часы и браслеты'])[5]"
    game_consoles = "(//a[text()='Игровые приставки'])[5]"
    virtual_reality_helmets = "(//a[text()='Шлемы виртуальной реальности'])[3]"
    audio = "(//a[text()='Аудио'])[5]"
    quadrocopters_and_accessories = "(//a[text()='Квадрокоптеры и аксессуары'])[5]"
    photos_and_videos = "(//a[text()='Фото и видео'])[5]"
    video_cards = "(//a[text()='Видеокарты'])[3]"
    gadgets = "(//a[text()='Гаджеты'])[5]"
    accessories = "(//a[text()='Аксессуары'])[7]"
    dyson = "(//a[text()='Услуги'])[3]"





    # Getters

    def get_phones(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.phones)))

    def get_tablets(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.tablets)))

    def get_laptops(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.laptops)))

    def get_computers(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.computers)))

    def get_watches_and_bracelets(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.watches_and_bracelets)))

    def get_game_consoles(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.game_consoles)))

    def get_virtual_reality_helmets(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.virtual_reality_helmets)))

    def get_audio(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.audio)))

    def get_quadrocopters_and_accessories(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.quadrocopters_and_accessories)))

    def get_photos_and_videos(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.photos_and_videos)))

    def get_video_cards(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.video_cards)))

    def get_gadgets(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.gadgets)))

    def get_accessories(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.accessories)))

    def get_dyson(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.dyson)))

    # Actions

    def click_phones(self):
        self.get_phones().click()
        print("Click Phones")

    def click_tablets(self):
        self.get_tablets().click()
        print("Click Tablets")

    def click_laptops(self):
        self.get_laptops().click()
        print("Click Laptops")

    def click_computers(self):
        self.get_computers().click()
        print("Click Computers")

    def click_watches_and_bracelets(self):
        self.get_watches_and_bracelets().click()
        print("Click Watches and Bracelets")

    def click_game_consoles(self):
        self.get_game_consoles().click()
        print("Click Game consoles")

    def click_virtual_reality_helmets(self):
        self.get_virtual_reality_helmets().click()
        print("Click Virtual reality helmets")

    def click_audio(self):
        self.get_audio().click()
        print("Click Audio")

    def click_quadrocopters_and_accessories(self):
        self.get_quadrocopters_and_accessories().click()
        print("Click Quadrocopters and Accessories")

    def click_photos_and_videos(self):
        self.get_photos_and_videos().click()
        print("Click Photos and Videos")

    def click_video_cards(self):
        self.get_video_cards().click()
        print("Click Video cards")

    def click_gadgets(self):
        self.get_gadgets().click()
        print("Click Gadgets")

    def click_accessories(self):
        self.get_accessories().click()
        print("Click Accessories")

    def click_dyson(self):
        self.get_dyson().click()
        print("Click Dyson")

    # Methods

    def select_phones(self):
       self.get_current_url()
       self.click_phones()

    def select_tablets(self):
       self.get_current_url()
       self.click_tablets()

    def select_laptops(self):
       self.get_current_url()
       self.click_laptops()

    def select_computers(self):
       self.get_current_url()
       self.click_computers()

    def select_watches_and_bracelets(self):
       self.get_current_url()
       self.click_watches_and_bracelets()

    def select_game_consoles(self):
       self.get_current_url()
       self.click_game_consoles()

    def select_virtual_reality_helmets(self):
       self.get_current_url()
       self.click_virtual_reality_helmets()

    def select_audio(self):
       self.get_current_url()
       self.click_audio()

    def select_quadrocopters_and_accessories(self):
       self.get_current_url()
       self.click_quadrocopters_and_accessories()

    def select_photos_and_videos(self):
       self.get_current_url()
       self.click_photos_and_videos()

    def select_video_cards(self):
       self.get_current_url()
       self.click_video_cards()

    def select_gadgets(self):
       self.get_current_url()
       self.click_gadgets()

    def select_accessories(self):
       self.get_current_url()
       self.click_accessories()

    def select_dyson(self):
       self.get_current_url()
       self.click_dyson()








