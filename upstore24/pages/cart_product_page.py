from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class CartProductPage(Base):




    # locators

    inCart_Button = "//button[@class='button button--primary button--block button--medium']"
    open_card_Button = "(//a[text()='Открыть корзину'])[3]"
    order_button = "//input[@value='Оформить заказ']"
    add_in_favorite_button = "//button[@class='button button--empty button--icon button--favorites not-added']"

    # Getters

    def get_inCart_Button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.inCart_Button)))

    def get_open_card_Button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.open_card_Button)))


    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.order_button)))


    def get_add_in_favorite_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.add_in_favorite_button)))



    # Actions

    def click_inCart_Button(self):
        self.get_inCart_Button().click()
        print("Click inCart Button")

    def click_open_card_Button(self):
        self.get_open_card_Button().click()
        print("Click open card Button")

    def click_order_button(self):
        self.get_order_button().click()
        print("Click order Button")


    def click_add_in_favorite_button(self):
        self.get_add_in_favorite_button().click()
        print("Click add in Favorite button")



    # Methods


    def select_inCart(self):
       self.get_current_url()
       self.click_inCart_Button()
       self.click_open_card_Button()
       self.click_order_button()

    def select_in_favorite(self):
        self.get_current_url()
        self.click_add_in_favorite_button()
        print("Click add in favorite button")
