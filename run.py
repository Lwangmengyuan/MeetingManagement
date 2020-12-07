# coding:utf-8
import os
from common.setting import Settings


if __name__ == '__main__':
    s = Settings()
    report_path = s.report_path
    # 更新测试数据
    os.system('python ./common/update_data.py')
    # 执行测试用例
    os.system('pytest ./testcases/ --alluredir=%s' % report_path)
    os.system('allure serve %s' % report_path)
