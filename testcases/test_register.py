# coding: utf-8
import time
import allure
import pytest
from common.deal_excel import DealExcel
from common.log import do_log
from common.random_data import RandomData
from pages.register_page import RegisterPage


# class Test_register:
def update_data(self):
    # 生成最新管理员和普通员工账号
    rd = RandomData()
    admin_data = {'company_name': rd.random_company_name(),
                  'company_address': rd.random_address('admin'),
                  'admin_name': rd.random_name('admin'),
                  'admin_email': rd.random_email('admin'),
                  'admin_phone': rd.random_phone('admin')}
    employ_data = {'employ_name': rd.random_name('employ'),
                   'company_name': rd.random_company_name(),
                   'employ_email': rd.random_email('employ'),
                   'employ_address': rd.random_address('employ'),
                   'employ_phone': rd.random_phone('employ')}
    # 更新测试用例中管理员和普通员工账号信息
    DealExcel().write(admin_data, 2, 4, 'register')
    DealExcel().write(employ_data, 3, 4, 'register')

# pytest.mark.parametrize 数据驱动
# broswer = fixture
# 管理员注册
@allure.title("管理员注册测试")
@pytest.mark.run(order=1)
@pytest.mark.parametrize('data', DealExcel().read('register')[0])
def test_register_admin_success(self, data, browser):
    update_data()
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
# 普通员工注册
@allure.title("普通员工注册测试")
@pytest.mark.run(order=2)
@pytest.mark.parametrize('data', DealExcel().read('register')[1])
def test_register_employ_success(self, data, browser):
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
