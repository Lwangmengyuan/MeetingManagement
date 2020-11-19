# -*- coding: utf-8 -*-
# @Author : 杨佳
# @Time : 2020/11/18 15:44
# @File : test_company.py

import pytest
import time
from common.deal_excel import DealExcel
from pages.company_page import CompanyPage
from common.log import do_log
import common.file_contrast as fc


# do_excel = DealExcel()
# test_data = do_excel.read('companya')
# 测试文件上传用例
@pytest.mark.success
# @pytest.mark.parametrize("data",test_data[0])
def test_02_picture_upload(browser):
    c = CompanyPage(browser)
    # 上传图片
    c.get()
    time.sleep(1)
    c.upload_image([r'F:\Code\python\MeetingManagement\resource\upload_source\1.png'])
    time.sleep(1)
    count = 0
    acture_val = ''

    while count < 60:
        # 执行完上传后，每隔1s 去判断acture_val 是否获取到
        # 如果1min 后还没有获取到就表示上传失败了
        acture_val = c.get_upload_info()
        if acture_val:
            break
        count += 1
        time.sleep(1)
    try:
        assert '上传成功' in acture_val
        do_log.info("上传测试用例通过")
    except AssertionError as e:
        c.scapture('upload_pic')
        do_log.error(f"上传测试用例不通过:{e}")
        raise e

@pytest.mark.success
def test_03_picture_show(browser):
    c = CompanyPage(browser)
    c.get()
    picurl = c.get_picurl()
    filepath = fc.load_file(picurl,r'F:\Code\python\MeetingManagement\resource\load_source\\')
    acture_val = fc.picture_contrast(filepath,r'F:\Code\python\MeetingManagement\resource\upload_source\1.jpg')
    try:
        assert True == acture_val
        do_log.info("图片展示用例通过")
    except AssertionError as e:
        c.scapture('show_pic')
        do_log.error(f"图片展示用例不通过:{e}")
        raise e
