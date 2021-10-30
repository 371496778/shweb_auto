from selenium import webdriver
from common.logger import logger


class Dirver:
    def open_driver(self):
        self.driver = webdriver.Chrome('C:\path\chromedriver.exe')
        self.driver.maximize_window()
        return self.driver
