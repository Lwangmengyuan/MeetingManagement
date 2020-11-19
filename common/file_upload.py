# -*- coding: utf-8 -*-
# @Author : 杨佳
# @Time : 2020/11/17 18:24
# @File : file_upload.py
import time
from pywinauto import Desktop
from common.file_isexist import is_exist
from common.log import do_log


def File_Upload(path_list:list):
    """
    文件上传
    :param path_list: 文件名必须为列表类型
    :return: None
    """
    if isinstance(path_list,list):
        path_str = ""
        for path in path_list:
            if is_exist(path):
                path_str += '"'+path+'"'
        if path_str:
            app = Desktop()
            # 窗口
            dialog = app['打开']  # 根据名字找到弹出窗口
            # 窗口上的控件
            time.sleep(1)
            dialog["Edit"].type_keys(path_str)  # 在输入框中输入值
            dialog["Button"].click()
    else:
        do_log.info('文件路径填写错误')


if __name__ == '__main__':
    path_list = [r'F:\Code\python\MeetingManagement\common\base_page.py', r'F:\Code\python\MeetingManagement\common\file_upload.py']
    s = File_Upload(path_list)
    print(s)