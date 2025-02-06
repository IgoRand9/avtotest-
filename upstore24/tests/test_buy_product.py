import datetime

import pytest
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_product_page import CartProductPage
from pages.catalog_page import CatalogPage
# from pages.iphone_16_pro_max_page import Iphone16ProMax
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.phones_page import PhonesPage


def test_buy_product(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start test buy product phones")


    mp = MainPage(driver)
    mp.select_catalog()

    cp = CatalogPage(driver)
    cp.select_phones()

    ph = PhonesPage(driver)
    ph.select_click_iphone_16_pro_max_256_gb_desert_titan()

    CPG = CartProductPage(driver)
    CPG.select_inCart()

    IC = OrderPage(driver)
    IC.input_info_client()



    print("Finish test buy product phones")


