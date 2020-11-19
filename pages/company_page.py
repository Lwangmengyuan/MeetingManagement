# -*- coding: utf-8 -*-
# @Author : 杨佳
# @Time : 2020/11/17 20:05
# @File : company_page.py
from common.base_page import BasePage
from common.file_upload import File_Upload


class CompanyPage(BasePage):
    # 定位修改图片按钮元素
    modify_image_locator = ('xpath', '//*[@id="app"]/section/section/section/main/div/div/div[1]/div/div[1]/div[2]/div[2]/button')
    # 定位上传图片组件元素
    upload_image_locator = ('xpath', '//*[@id="app"]/section/section/section/main/div/div/div[2]/div/div[2]/div/div/div/div')
    # 定位image标签
    image_show_locator = ('xpath', '//*[@id="app"]/section/section/section/main/div/div/div[1]/div/div[1]/div[2]/div[1]/img')
    # 定位上传成功标签
    upload_success_locator = ('xpath', '/html/body/div[2]/p')

    url = 'http://10.104.10.90/#/homePage/enterprise'

    def get(self):
        self.driver.get(self.url)
        return self

    def upload_image(self,path_list):
        self.click_element(self.modify_image_locator)
        self.click_element(self.upload_image_locator)
        File_Upload(path_list)
        return self

    def get_upload_info(self):
        upload_success_elem = self.wait_element_visible(self.upload_success_locator)
        if upload_success_elem:
            text = upload_success_elem.text
            return text
        return None

    def get_picurl(self):
        image_show_elem = self.wait_element_visible(self.image_show_locator)
        if image_show_elem:
            picurl = image_show_elem.get_attribute('src')
            return picurl
        return None