# coding:utf-8
from selenium import webdriver


class OperateBrowser:
    def __init__(self):
        self.driver = None

    def open_browser(self, browser_type='chrome'):
        self.driver = webdriver.Chrome()
        self.driver.get('http://10.104.10.90/')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        return self.driver

    def close_browser(self):
        self.driver.close()
