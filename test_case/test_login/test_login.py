# -*- coding: gbk -*-
import pytest

from conftest import browser
from page.loginpage import Login


@pytest.mark.usefixtures('driver_setup')
class Test_Login:

    @pytest.fixture()
    def my_fixture(self):
        self.login = Login(self.driver)

    def test_logins(self, my_fixture):
        self.login.login()
        # self.driver.click_element('id','LoginName')
        # self.login.assert_all(1, 2)
        assert 1 == 1

    def test_login(self, my_fixture):
        self.login.login()
        # self.driver.click_element('id','LoginName')
        # self.login.assert_all(1, 2)
        assert 1 == 2
