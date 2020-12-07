# coding:utf-8
import time
import allure
import pytest
from pages.login_page import LoginPage
from common.deal_excel import DealExcel
from common.log import do_log


'''
    登录功能测试：
        管理员登录和普通用户登录
'''


# pytest.mark.parametrize 数据驱动
# broswer = fixture
@allure.title("普通用户验证码登录测试")
@pytest.mark.run(order=3)
@pytest.mark.success
@pytest.mark.parametrize('data', DealExcel().read('login')[0])
def test_login_employ_phone_success(data, browser):
    l = LoginPage(browser)
    l.click_privacy_policy().phone_login(data['phone'])
    time.sleep(5)
    acture_val = l.employ_login_info()

    try:
        assert data["expect_val"] == acture_val
        do_log.info("普通用户验证码登录测试用例通过")
    except AssertionError as e:
        l.scapture('employlogin')
        do_log.error(f"普通用户验证码登录测试用例不通过:{e}")
        raise e


@allure.title("退出登录测试")
@pytest.mark.run(order=4)
@pytest.mark.success
@pytest.mark.parametrize('data', DealExcel().read('login')[1])
def test_sign_out(data, browser):
    l = LoginPage(browser)
    l.click_sign_out()
    acture_val = l.sign_out_info()

    try:
        assert data["expect_val"] == acture_val
        do_log.info("退出登录测试用例通过")
    except AssertionError as e:
        l.scapture('employlogin')
        do_log.error(f"退出登录测试用例不通过:{e}")
        raise e


@allure.title("管理员验证码登录测试")
@pytest.mark.run(order=5)
@pytest.mark.success
@pytest.mark.parametrize('data', DealExcel().read('login')[2])
def test_login_admin_phone_success(data, browser):
    l = LoginPage(browser)
    l.phone_login(data['phone'])
    acture_val = l.admin_login_info()
    # 退出登录，执行后续登录测试用例
    l.click_sign_out()

    try:
        assert data["expect_val"] == acture_val
        do_log.info("管理员验证码登录测试用例通过")
    except AssertionError as e:
        l.scapture('adminlogin')
        do_log.error(f"管理员验证码登录测试用例不通过:{e}")
        raise e


@allure.title("普通用户密码登录测试")
@pytest.mark.run(order=6)
@pytest.mark.success
@pytest.mark.parametrize('data', DealExcel().read('login')[3])
def test_login_employ_password_success(data, browser):
    l = LoginPage(browser)
    l.password_login(data['phone'], data['password'])
    acture_val = l.employ_login_info()
    # 退出登录，执行后续登录测试用例
    l.click_sign_out()

    try:
        assert data["expect_val"] == acture_val
        do_log.info("普通用户密码登录测试用例通过")
    except AssertionError as e:
        l.scapture('employlogin')
        do_log.error(f"普通用户密码登录测试用例不通过:{e}")
        raise e


@allure.title("管理员验证码登录测试")
@pytest.mark.run(order=7)
@pytest.mark.success
@pytest.mark.parametrize('data', DealExcel().read('login')[4])
def test_login_admin_password_success(data, browser):
    l = LoginPage(browser)
    l.password_login(data['phone'], data['password'])
    acture_val = l.admin_login_info()

    try:
        assert data["expect_val"] == acture_val
        do_log.info("管理员密码登录测试用例通过")
    except AssertionError as e:
        l.scapture('adminlogin')
        do_log.error(f"管理员密码登录测试用例不通过:{e}")
        raise e
