import datetime

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.phones_page import PhonesPage


def test_range_filter():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))


    print("Start test range filter")

    pf = PhonesPage(driver)
    pf.select_range_filter()
    # driver.quit()

    print("Finish test range filter")



