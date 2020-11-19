# -*- coding: utf-8 -*-
# @Author : 杨佳
# @Time : 2020/11/17 19:02
# @File : file_isexist.py

import os


def is_exist(path):
    if os.path.exists(path):
        return True
    else:
        return False


def creat_path(path):
    if is_exist(path):
        os.mkdir(path)


if __name__ == '__main__':
    res = is_exist('F:\Code\python\MeetingManagement\common\log.py1')
    print(res)