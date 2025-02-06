import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class PhonesPage(Base):


    page_url = "https://upstore24.ru/collection/phones?characteristics%5B%5D=109849136"

    # locators

    iphone_16_pro_max = "(//a[text()='Apple iPhone 16 Pro Max'])[3]"
    checkbox_brand_apple = "//label[@for='filter-value-109849115']"
    checkbox_brand_samsung = "//label[@for='filter-value-109849181']"
    checkbox_color_white = "//label[@for='filter-value-109849136']"
    checkbox_color_black = "//label[text()='Черный']"
    checkbox_CPU_a14 = "//label[@for='filter-value-100526770']"
    checkbox_CPU_a17_pro = "//label[@for='filter-value-217837500']"
    checkbox_60Hz = "//label[@for='filter-value-100530631']"
    checkbox_120Hz = "//label[@for='filter-value-100530658']"
    checkbox_NFC = "//label[@for='filter-value-100526784']"
    iphone_16_pro_max_256_gb_desert_titan = "//div[@class='col-6 col-sm-6 col-md-4 col-lg-4'][1]"





    # Getters

    def get_iphone_16_pro_max_256_gb_desert_titan(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.iphone_16_pro_max_256_gb_desert_titan)))

    def get_checkbox_brand_apple(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.checkbox_brand_apple)))

    def get_checkbox_brand_samsung(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.checkbox_brand_samsung)))

    def get_checkbox_color_white(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.checkbox_color_white)))

    def get_checkbox_color_black(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.checkbox_color_black)))

    def get_checkbox_CPU_a14(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.checkbox_CPU_a14)))

    def get_checkbox_CPU_a17_pro(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.checkbox_CPU_a17_pro)))

    def get_checkbox_60Hz(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.checkbox_60Hz)))

    def get_checkbox_120Hz(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.checkbox_120Hz)))

    def get_checkbox_NFC(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.checkbox_NFC)))





    # Actions

    def click_iphone_16_pro_max_256_gb_desert_titan(self):
        self.get_iphone_16_pro_max_256_gb_desert_titan().click()
        print("Click iphone 16 pro max desert titan")

    def click_checkbox_brand_apple(self):
        self.get_checkbox_brand_apple().click()
        print("Click checkbox brand apple")

    def click_checkbox_brand_samsung(self):
        self.get_checkbox_brand_samsung().click()
        print("Click checkbox brand samsung")

    def click_checkbox_color_white(self):
        self.get_checkbox_color_white().click()
        print("Click checkbox color white")

    def click_checkbox_color_black(self):
        self.get_checkbox_color_black().click()
        print("Click checkbox color black")

    def click_checkbox_CPU_a14(self):
        self.get_checkbox_CPU_a14().click()
        print("Click checkbox CPU a14")

    def click_checkbox_CPU_a17_pro(self):
        self.get_checkbox_CPU_a17_pro().click()
        print("Click checkbox CPU a17 pro")

    def click_checkbox_60Hz(self):
        self.get_checkbox_60Hz().click()
        print("Click checkbox 60Hz")

    def click_checkbox_120Hz(self):
        self.get_checkbox_120Hz().click()
        print("Click checkbox 120Hz")

    def click_checkbox_NFC(self):
        self.get_checkbox_NFC().click()
        print("Click checkbox NFC")




    # Methods

    def select_click_iphone_16_pro_max_256_gb_desert_titan(self):
       self.get_current_url()
       self.click_iphone_16_pro_max_256_gb_desert_titan()


    def select_range_filter(self):

       self.driver.get(self.page_url)
       self.driver.maximize_window()
       self.filter_price_range()
       self.get_screenshot()





    def select_checkbox(self):

       self.driver.get(self.page_url)
       self.driver.maximize_window()
       self.driver.execute_script("window.scrollTo(0, 1200)")
       self.click_checkbox_brand_apple()
       self.click_checkbox_brand_samsung()
       self.get_screenshot()
       self.click_checkbox_color_white()
       self.click_checkbox_color_black()
       self.driver.execute_script("window.scrollTo(0, 1500)")
       self.click_checkbox_CPU_a14()
       self.click_checkbox_CPU_a17_pro()
       self.get_screenshot()
       self.driver.execute_script("window.scrollTo(0, 1700)")
       self.click_checkbox_60Hz()
       self.click_checkbox_120Hz()
       self.driver.execute_script("window.scrollTo(0, 1800)")
       self.click_checkbox_NFC()
       self.get_screenshot()
