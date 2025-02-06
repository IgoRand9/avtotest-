import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Base():

    """ Base class containing generic methods """

    def __init__(self, driver):
        self.driver = driver


    """ Method get current url """

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)


    """ Method assert word """

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")


    """ Method Screenshot """

    def get_screenshot(self):

        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")  # create screenshots
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.save_screenshot(f"./Screen/{name_screenshot}")
        print('Screenshot')


    """ Method assert url """

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")



    """ Method filter price range slider """

    def filter_price_range(self):
        slider = self.driver.find_element(By.XPATH, "//*[@id='body']/div[1]/div[3]/div/div[1]/div/div/div[2]/div/div/div[1]/form/div[1]/div[3]/div[2]/span/span[6]")
        actions = ActionChains(self.driver)
        actions.click_and_hold(slider).move_by_offset(60, 0).release().perform()








