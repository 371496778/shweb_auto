# -*- coding: gbk -*-
import os
import time

import allure
import pytest

from config.config import *

from common.logger import logger


class Base(object):

    def __init__(self, driver):
        self.d = driver
        # print("打开浏览器2")

    def open(self, url):
        self.d.get(url)
        logger.info('打开网址' + url)

    # 查找元素
    def get_element(self, by, value):
        logger.info("查找元素:" + value)
        try:
            return self.d.find_element(by=by, value=value)
        except:
            logger.exception(f"查找元素" + value + "失败")
            self.save_screenshot_fail()

    # 点击元素
    def click_element(self, by, value):
        logger.info("点击元素:" + value)
        ele = self.d.find_element(by=by, value=value)
        try:
            ele.click()
        except:
            logger.exception(f"点击元素失败" + value)
            self.save_screenshot_fail()

    # 根据文字点击
    def click_text(self, text):
        ele = self.d.find_element(by='xpath', value='//*[text()="{}"]'.format(text))
        ele.click()

    # 输入文本
    def input_text(self, by, value, text):
        logger.info(f"输入元素{value}文字:{text}")
        ele = self.d.find_element(by=by, value=value)
        try:
            ele.send_keys(text)
        except:
            logger.exception(f"在元素:{value}输入文本:{text}失败")
            self.save_screenshot_fail()

    # 获取文本
    def get_text(self, by, value):
        logger.info(f'获取元素:{value}文本')
        try:
            ele = self.d.find_element(by=by, value=value)
            return ele.text
        except:
            logger.exception(f"获取元素:{value}获取文本失败")
            self.save_screenshot_fail()

    # 失败截图
    def save_screenshot_fail(self):
        file_name = screenshots_folder + time.strftime("%Y%m%d%H%M%S") + ".png"
        self.d.save_screenshot(file_name)
        logger.info(f"成功获取截图，路径：{file_name}")
        with open(file_name, mode='rb') as f:
            file = f.read()
            allure.attach(file, '添加失败截图', allure.attachment_type.PNG)
        return file_name

    def save_screenshot_suss(self):
        file_name = screenshots_folder + time.strftime("%Y%m%d%H%M%S") + ".png"
        self.d.save_screenshot(file_name)
        return file_name

    # 移动到元素{value}对象的”顶端“，与当前窗口的”顶部“对齐
    def execute_script(self, by, value):
        try:
            time.sleep(5)
            div = self.d.find_element(by=by, value=value)
            js4 = "arguments[0].scrollIntoView();"
            self.d.execute_script(js4, div)
            logger.info(f"移动到元素{value}对象的”顶端“，与当前窗口的”顶部“对齐")
        except BaseException as e:
            self.save_screenshot_fail()
            logger.info(f"移动失败:{e}")

    def assert_all(self, txt1, txt2):
        try:
            assert txt1 == txt2
            self.save_screenshot_suss()
        except BaseException:
            self.save_screenshot_fail()

    def fail_picture(self):
        f = self.d.get_screenshot_as_file()
        allure.attach.file(f, '失败用例截图:{filename}'.format(filename=f), allure.attachment_type.PNG)



# if __name__ == '__main__':
#     d = Base(object)
#     d.open('http://101.251.192.227:5001/')
#     d.input_text("id", "LoginName", "test")
#     d.input_text("id", "Password", "acctrue1")
#     d.click_element('id', 'btnLogin')
#     time.sleep(5)
#     d.execute_script('xpath', '//*[@id="sidebarnav"]/li[14]')
