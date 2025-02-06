import datetime

import pytest
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page import MainPage


def test_clickability(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))



    print("Start test section clickability")

    SC = MainPage(driver)
    SC.section_clickability()
    driver.quit()

    print("Finish test section clickability")



