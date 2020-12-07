# coding: utf-8
import time
import allure
import pytest
from common.deal_excel import DealExcel
from common.log import do_log
from pages.register_page import RegisterPage


# class Test_register:
# pytest.mark.parametrize 数据驱动
# broswer = fixture
@allure.title("管理员注册测试")
@pytest.mark.run(order=1)
@pytest.mark.parametrize('data', DealExcel().read('register')[0])
def test_register_admin_success(data, browser):
    r = RegisterPage(browser)
    r.get().admin_register(data)
    time.sleep(5)
    acture_val = r.admin_register_info()

    try:
        assert data["expect_val"] == acture_val
        do_log.info("管理员注册测试用例通过")
    except AssertionError as e:
        do_log.error(f"管理员注册测试用例不通过:{e}")
        raise e

# pytest.mark.parametrize 数据驱动
# broswer = fixture
@allure.title("普通员工注册测试")
@pytest.mark.run(order=2)
@pytest.mark.parametrize('data', DealExcel().read('register')[1])
def test_register_employ_success(data, browser):
    r = RegisterPage(browser)
    r.get().employ_register(data)
    time.sleep(5)
    acture_val = r.employ_register_info()

    try:
        assert data["expect_val"] == acture_val
        do_log.info("普通员工注册测试用例通过")
    except AssertionError as e:
        do_log.error(f"普通员工注册测试用例不通过:{e}")
        raise e
