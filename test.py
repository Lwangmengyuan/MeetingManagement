# coding: utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from common.deal_excel import DealExcel
from common.get_verify_code import GetVerifyCode
from common.random_data import RandomData


def test_login_administrator():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://10.104.10.90/')
    # 定位手机号输入框，并输入手机号
    driver.find_element(By.XPATH, '//*[@id="warp3"]/div[1]/input').send_keys('18352538378')
    time.sleep(2)
    # 定位获取验证码按钮，并点击
    driver.find_element(By.XPATH, '//*[@id="warp3"]/div[2]/button').click()
    time.sleep(20)
    # 获取验证码
    verify_code = GetVerifyCode().get_login_register('18352538378', 'l')
    # 定位验证码输入框，并填写验证码
    driver.find_element(By.XPATH, '//*[@id="warp3"]/div[2]/input').send_keys(verify_code)
    # 判断隐私条款是否同意，不同意则勾选
    accept_element = driver.find_element(By.XPATH, '//*[@id="logo"]/div[2]/label/span/span').click()
    # if not accept_element.is_selected():
    #     accept_element.click()
    # 定位登录按钮，并点击
    driver.find_element(By.XPATH, '//*[@id="button1"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="app"]/section/section/aside/div/ul/div/li[4]').click()
    # driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div/div[2]/div[1]/div[1]/i[1]').click()
    # time.sleep(5)

    employ_name = '//*[@id="app"]/section/section/section/main/div/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[3]/div'
    driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div/div[1]/div/input').send_keys('王梦园')
    driver.find_element_by_xpath('//*[@id="app"]/section/section/section/main/div/div/div[1]/button[1]').click()
    time.sleep(5)
    result = driver.find_element_by_xpath(employ_name)
    if result:
        if result.text == '王梦园':
            print('True')
        else:
            print('False')
    driver.close()


if __name__ == '__main__':
    # test_login_administrator()
    rd = RandomData()
    department_name = {"department_name": rd.random_department()}
    print(department_name)
