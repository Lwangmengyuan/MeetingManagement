# -*- coding: utf-8 -*-
# @Author : 杨佳
# @Time : 2020/11/17 19:52
# @File : home_page.py
from common.base_page import BasePage

class HomePage(BasePage):
    # 定位首页元素
    home_locator = ('xpath', '//*[@id="app"]/section/section/aside/div/ul/div/li[1]/span')
    # 定位会议预约元素
    metting_order_locator = ('xpath', '//*[@id="app"]/section/section/aside/div/ul/div/li[2]/span')
    # 定位会议室管理元素
    mettingroom_locator = ('xpath', '//*[@id="app"]/section/section/aside/div/ul/div/li[3]/span')
    # 定位通讯录元素
    address_list_locator = ('xpath', '//*[@id="app"]/section/section/aside/div/ul/div/li[4]/span')
    # 定位企业管理元素
    company_management_locator = ('xpath', '//*[@id="app"]/section/section/aside/div/ul/div/li[5]/span')

    # 点击首页目录元素
    def home_catalog(self):
        self.click_element(self.home_locator)
        return self

    # 点击会议预约目录元素
    def metting_order_catalog(self):
        self.click_element(self.metting_order_locator)
        return self

    # 点击会议室管理目录元素
    def mettingroom_catalog(self):
        self.click_element(self.mettingroom_locator)
        return self

    # 点击通讯录目录元素
    def address_list_catalog(self):
        self.click_element(self.address_list_locator)
        return self

    # 点击企业管理目录元素
    def company_managment_catalog(self):
        self.click_element(self.company_management_locator)
        return self