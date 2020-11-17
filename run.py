# coding:utf-8
import os
from common.setting import Settings


if __name__ == '__main__':
    s = Settings()
    report_path = s.report_path
    os.system('pytest ./testcases/test_login.py --alluredir=%s' % report_path)
    os.system('allure serve %s' % report_path)
