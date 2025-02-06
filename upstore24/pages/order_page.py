from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

class OrderPage(Base):




    # locators

    fio_field = "//input[@name='client[contact_name]']"
    phone_field = "(//input[@name='client[phone]'])[1]"
    comment_to_order_field = "(//textarea[@id='order_comment'])[1] "
    clients_email_field = "//input[@id='client_email']"
    checkbox_receive_order_notification = "//div[@class='co-input  co-input--checkbox co-input--messenger_subscription   ']"
    radio_button_courier = "(//span[@class='radio co-delivery_method-input co-toggable_field-input co-toggable_field-input--radio'])[2]"
    address_fields_for_courier = "//textarea[@id='shipping_address_address']"




    # Getters

    def get_fio_field(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.fio_field)))

    def get_phone_field(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.phone_field)))

    def get_comment_to_order_field(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.comment_to_order_field)))

    def get_clients_email_field(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.clients_email_field)))

    def get_checkbox_receive_order_notification(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.checkbox_receive_order_notification)))

    def get_radio_button_courier(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.radio_button_courier)))


    def get_address_fields_for_courier(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.address_fields_for_courier)))


    # Actions

    def input_fio(self, fio):
        self.get_fio_field().send_keys(fio)
        print("Input fio")

    def input_phone(self, phone):
        self.get_phone_field().send_keys(phone)
        print("Input phone")

    def input_comment_to_order(self, comment):
        self.get_comment_to_order_field().send_keys(comment)
        print("Input comment to order")

    def input_clients_email(self, email):
        self.get_clients_email_field().send_keys(email)
        print("Input clients email")

    def click_checkbox_receive_order_notification(self):
        self.get_checkbox_receive_order_notification().click()
        print("Input checkbox receive order notification")

    def click_radio_button_courier(self):
        self.get_radio_button_courier().click()
        print("Input radio button courier")

    def input_address_fields_for_courier(self, adress):
        self.get_address_fields_for_courier().send_keys(adress)
        print("Input address fields for courier")


    # Methods


    def input_info_client(self):
       self.get_current_url()
       self.input_fio("Ivan")
       self.input_phone("+7987654321")
       self.input_comment_to_order("Some text for oder")
       self.input_clients_email("qwertyt@qwer.com")
       self.click_checkbox_receive_order_notification()
       self.input_address_fields_for_courier("some adress")


