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
        # print("�������2")

    def open(self, url):
        self.d.get(url)
        logger.info('����ַ' + url)

    # ����Ԫ��
    def get_element(self, by, value):
        logger.info("����Ԫ��:" + value)
        try:
            return self.d.find_element(by=by, value=value)
        except:
            logger.exception(f"����Ԫ��" + value + "ʧ��")
            self.save_screenshot_fail()

    # ���Ԫ��
    def click_element(self, by, value):
        logger.info("���Ԫ��:" + value)
        ele = self.d.find_element(by=by, value=value)
        try:
            ele.click()
        except:
            logger.exception(f"���Ԫ��ʧ��" + value)
            self.save_screenshot_fail()

    # �������ֵ��
    def click_text(self, text):
        ele = self.d.find_element(by='xpath', value='//*[text()="{}"]'.format(text))
        ele.click()

    # �����ı�
    def input_text(self, by, value, text):
        logger.info(f"����Ԫ��{value}����:{text}")
        ele = self.d.find_element(by=by, value=value)
        try:
            ele.send_keys(text)
        except:
            logger.exception(f"��Ԫ��:{value}�����ı�:{text}ʧ��")
            self.save_screenshot_fail()

    # ��ȡ�ı�
    def get_text(self, by, value):
        logger.info(f'��ȡԪ��:{value}�ı�')
        try:
            ele = self.d.find_element(by=by, value=value)
            return ele.text
        except:
            logger.exception(f"��ȡԪ��:{value}��ȡ�ı�ʧ��")
            self.save_screenshot_fail()

    # ʧ�ܽ�ͼ
    def save_screenshot_fail(self):
        file_name = screenshots_folder + time.strftime("%Y%m%d%H%M%S") + ".png"
        self.d.save_screenshot(file_name)
        logger.info(f"�ɹ���ȡ��ͼ��·����{file_name}")
        with open(file_name, mode='rb') as f:
            file = f.read()
            allure.attach(file, '���ʧ�ܽ�ͼ', allure.attachment_type.PNG)
        return file_name

    def save_screenshot_suss(self):
        file_name = screenshots_folder + time.strftime("%Y%m%d%H%M%S") + ".png"
        self.d.save_screenshot(file_name)
        return file_name

    # �ƶ���Ԫ��{value}����ġ����ˡ����뵱ǰ���ڵġ�����������
    def execute_script(self, by, value):
        try:
            time.sleep(5)
            div = self.d.find_element(by=by, value=value)
            js4 = "arguments[0].scrollIntoView();"
            self.d.execute_script(js4, div)
            logger.info(f"�ƶ���Ԫ��{value}����ġ����ˡ����뵱ǰ���ڵġ�����������")
        except BaseException as e:
            self.save_screenshot_fail()
            logger.info(f"�ƶ�ʧ��:{e}")

    def assert_all(self, txt1, txt2):
        try:
            assert txt1 == txt2
            self.save_screenshot_suss()
        except BaseException:
            self.save_screenshot_fail()

    def fail_picture(self):
        f = self.d.get_screenshot_as_file()
        allure.attach.file(f, 'ʧ��������ͼ:{filename}'.format(filename=f), allure.attachment_type.PNG)



# if __name__ == '__main__':
#     d = Base(object)
#     d.open('http://101.251.192.227:5001/')
#     d.input_text("id", "LoginName", "test")
#     d.input_text("id", "Password", "acctrue1")
#     d.click_element('id', 'btnLogin')
#     time.sleep(5)
#     d.execute_script('xpath', '//*[@id="sidebarnav"]/li[14]')
