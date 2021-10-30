# -*- coding: gbk -*-
import pytest
import os

if __name__ == '__main__':
    pytest.main(['-s', 'test_case', '--alluredir', './temp'])
    os.system('allure generate ./temp -o ./reports --clean')
    # os.system('')
