import time
import pytest
import allure
from selenium import webdriver
from common.logger import logger
from config.config import *

driver = None


def save_screenshot_suss():
    file_name = screenshots_folder + time.strftime("%Y%m%d%H%M%S") + ".png"
    driver.save_screenshot(file_name)
    return file_name


# 用例失败后自动截图
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取用例执行结果的钩子函数
    :param item:
    :param call:
    :return:
    """
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            if "tmpir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
                f.write(report.nodeid + extra + "\n")
            with allure.step('添加失败截图...'):
                save_screenshot_suss()
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
    if report.when == "call" and report.passed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            if "tmpir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
                f.write(report.nodeid + extra + "\n")
            with allure.step('添加成功截图...'):
                save_screenshot_suss()
                allure.attach(driver.get_screenshot_as_png(), "成功截图", allure.attachment_type.PNG)


# @pytest.fixture(autouse=True)
def browser(headless=True):
    """
    定义一个总的调用driver的方法，前置中直接调用browser
    :return:
    """
    global driver
    opts = webdriver.FirefoxOptions()
    opts.add_argument('--headless') if headless else None
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


@pytest.fixture()
def driver_setup(request):
    logger.info("自动化测试开始--------------------")
    request.instance.driver = browser()
    logger.info('初始化成功')

    def driver_teardown():
        request.instance.driver.quit()
        logger.info("自动化测试结束--------------------")

    request.addfinalizer(driver_teardown)


if __name__ == '__main__':
    d = browser()
