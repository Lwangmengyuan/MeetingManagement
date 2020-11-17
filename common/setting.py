# conding: utf-8
# 作者: 杨佳
# 创建时间: 2020/9/22 21:44
# 文件: setting
import os
import time


'''
    配置文件类，所有的配置信息都写在该类中
'''
class Settings:
    # 当前日期
    day = str(time.strftime("%Y-%m-%d"))
    # 当前时间
    base_name = str(time.strftime("%Y%m%d-%H%M%S"))

    BASE_PATH = os.path.abspath(__file__)
    BASE_DIRECTORY = os.path.dirname(os.path.dirname(BASE_PATH))
    bases_path = os.path.dirname(BASE_PATH)
    cases_path = os.path.join(BASE_DIRECTORY, r"cases%s" % os.sep)
    data_path = os.path.join(BASE_DIRECTORY, r"data%s" % os.sep)
    pages_path = os.path.join(BASE_DIRECTORY, r"pages%s" % os.sep)
    script_path = os.path.join(BASE_DIRECTORY, r"script%s" % os.sep)
    log_path = os.path.join(BASE_DIRECTORY, r"log%s%s%s" % (os.sep, day, os.sep))
    # 日志路径，不存在则创建
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    report_path = os.path.join(BASE_DIRECTORY, r"report%s%s%s" % (os.sep, base_name, os.sep))
    # 报告路径，不存在则创建
    # report_path = './report/%s' % base_name
    if not os.path.exists(report_path):
        os.makedirs(report_path)

    # browsermob_server_address = r"E:\Program Files\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat"
    excel_path = data_path+'case.xlsx'
    excel_data_column = 4
