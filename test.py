# coding: utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.deal_excel import DealExcel
from common.get_verify_code import GetVerifyCode
from common.random_data import RandomData


def find(driver, locator):
    """查找元素"""
    try:
        e = driver.find_element_by_xpath(locator)
    except Exception as err:
        print(f"元素定位失败：{err}")
        return None
    else:
        return e

def test_login_administrator():
    # 姓名搜索输入框
    name_search_input_locator = ('//*[@id="app"]/section/section/section/main/div/div/div[1]/div/input')
    # 搜索按钮
    search_btn_locator = ('//*[@id="but20"]')
    # 查看搜索结果中姓名/邮箱和地址值
    name_result_locator = ('//*[@id="app"]/section/section/section/main/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[3]/div')
    email_result_locator = ('//*[@id="app"]/section/section/section/main/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[5]/div')
    address_result_locator = ('//*[@id="app"]/section/section/section/main/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[6]/div')
    # 修改员工按钮
    modify_employ_locator = ('//*[@id="but23"]')
    # 姓名输入框
    modify_employ_name_locator = ('//*[@id="app"]/section/section/section/main/div/div/div[2]/div[7]/div/div[2]/form/div[1]/div[2]/div/input')
    # 部门名称下拉展开按钮
    modify_employ_department_locator = ('//*[@id="app"]/section/section/section/main/div/div/div[2]/div[5]/div/div[2]/form/div[2]/div[2]/div/div/span/span/i')
    # 部门选定
    modify_employ_department_select_locator = ('/html/body/div[3]/div[1]/div[1]/ul/li[2]')
    # 邮箱输入框
    modify_employ_email_locator = ('//*[@id="app"]/section/section/section/main/div/div/div[2]/div[7]/div/div[2]/form/div[4]/div[2]/div/input')
    # 地址输入框
    modify_employ_address_locator = ('//*[@id="app"]/section/section/section/main/div/div/div[2]/div[7]/div/div[2]/form/div[5]/div[2]/div/input')
    # 修改普通员工提交
    modify_employ_commit_locator = ('//*[@id="but32"]')
    # 查看搜索结果中姓名/邮箱和地址值
    name_result_locator = ('//*[@id="app"]/section/section/section/main/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[3]/div')
    email_result_locator = ('//*[@id="app"]/section/section/section/main/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[5]/div')
    address_result_locator = ('//*[@id="app"]/section/section/section/main/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[6]/div')
    # 删除员工按钮
    del_employ_locator = ('//*[@id="but24"]')
    # 删除员工确认按钮
    del_employ_commit_locator = ('/html/body/div[2]/div/div[3]/button[2]')

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://10.88.64.54/')
    # 登录
    driver.find_element_by_xpath('//*[@id="warp3"]/div[2]/input').send_keys('18352538378')
    driver.find_element_by_xpath('//*[@id="warp3"]/div[3]/input').send_keys('123456')
    driver.find_element_by_xpath('//*[@id="logo"]/div[2]/label/span/span').click()
    driver.find_element_by_xpath('//*[@id="button1"]').click()
    time.sleep(5)
    # 切换至通讯录页面
    driver.find_element_by_xpath('//*[@id="app"]/section/section/aside/div/ul/div/li[4]').click()
    time.sleep(2)
    # search_elem = driver.find_element_by_xpath(name_search_input_locator)
    # search_elem.clear()
    # search_elem.send_keys('delete')
    # driver.find_element_by_xpath(search_btn_locator).click()
    # # 点击删除按钮
    # driver.find_element_by_xpath(del_employ_locator).click()
    # # 确定删除员工
    # driver.find_element_by_xpath(del_employ_commit_locator).click()
    # time.sleep(2)
    # driver.refresh()
    # 按删除员工姓名搜索
    search_elem = driver.find_element_by_xpath(name_search_input_locator)
    search_elem.clear()
    search_elem.send_keys('delete')
    driver.find_element_by_xpath(search_btn_locator).click()
    time.sleep(2)
    result = find(driver, name_result_locator)
    print(result)
    if result is None:
        return False
    else:
        return True
    driver.close()


if __name__ == '__main__':
    result = test_login_administrator()
    print(result)
    # data = DealExcel().read('address_book')[4]
    # print(data[0]['new_employ_name'])
    # print(data[0]['employ_email'])
    # print(data[0]['employ_address'])
