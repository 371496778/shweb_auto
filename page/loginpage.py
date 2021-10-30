# -*- coding: gbk -*-
import time

from common.base import Base
from config.config import *
from elements.elements import *
from common.logger import logger


class Login(Base):
    def __init__(self, driver):
        # super(Login, self).__init__()
        super().__init__(driver)
        self.base = Base(driver)
        self.base.open(web_url)

    def login(self):
        # self.driver.open(web_url)
        self.base.input_text(usernames[0], usernames[1], username_text)
        self.base.input_text(passwords[0], passwords[1], password_text)
        self.base.click_element(login_button[0], login_button[1])
        time.sleep(5)

    def q(self):
        self.base.execute_script('xpath', '//*[@id="sidebarnav"]/li[14]')
