# _*_conding:utf-8_*_
# 作者: 杨佳
# 创建时间: 2020/11/11 21:36
# 文件: test_login
import time
import allure
import pytest
from pages.login_page import Login_page
from common.deal_excel import DealExcel
from common.log import do_log


'''
    登录功能测试：
        管理员登录和普通用户登录
'''


# pytest.mark.parametrize 数据驱动
# broswer = fixture
# 普通用户登录
@allure.title("普通用户登录测试")
@pytest.mark.success
@pytest.mark.parametrize('data', DealExcel().read('login')[0])
def test_login_employ_success(data, browser):
    l = Login_page(browser)
    l.get().click_privacy_policy().login(data['phone'])
    time.sleep(5)
    acture_val = l.employ_login_info()

    try:
        assert data["expect_val"] == acture_val
        do_log.info("普通用户登录测试用例通过")
    except AssertionError as e:
        l.scapture('employlogin')
        do_log.error(f"普通用户登录测试用例不通过:{e}")
        raise e


# 退出登录
@allure.title("退出登录测试")
@pytest.mark.success
@pytest.mark.parametrize('data', DealExcel().read('login')[1])
def test_sign_out(data, browser):
    l = Login_page(browser)
    l.click_sign_out()
    acture_val = l.sign_out_info()

    try:
        assert data["expect_val"] == acture_val
        do_log.info("退出登录测试用例通过")
    except AssertionError as e:
        l.scapture('employlogin')
        do_log.error(f"退出登录测试用例不通过:{e}")
        raise e


# 管理员登录
@allure.title("管理员登录测试")
@pytest.mark.success
@pytest.mark.parametrize('data', DealExcel().read('login')[2])
def test_login_admin_success(data, browser):
    l = Login_page(browser)
    l.login(data['phone'])
    acture_val = l.admin_login_info()
    browser.quit()

    try:
        assert data["expect_val"] == acture_val
        do_log.info("管理员登录测试用例通过")
    except AssertionError as e:
        l.scapture('adminlogin')
        do_log.error(f"管理员登录测试用例不通过:{e}")
        raise e

