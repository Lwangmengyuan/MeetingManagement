# coding: utf-8
import time


class RandomData:
    def __init__(self):
        self.current = str(time.strftime("%Y%m%d%H%M"))
        self.now_time = self.current[4:]
        self.diff_time = str(int(self.now_time) + 1)

    # 按当前时间生成公司名称
    def random_company_name(self):
        return 'Company' + self.now_time

    # 按当前时间生成地址
    def random_address(self, role):
        if role == 'admin':
            return 'CAddress' + self.now_time
        else:
            return 'EAddress' + self.now_time

    # 按当前时间生成姓名
    def random_name(self, role):
        if role == 'admin':
            return 'admin' + self.now_time
        else:
            return 'employ' + self.now_time

    # 按当前时间生成邮箱
    def random_email(self, role):
        if role == 'admin':
            return '131' + self.now_time + '@qq.com'
        else:
            return '131' + self.diff_time + '@qq.com'

    # 按当前时间生成手机号
    def random_phone(self, role):
        if role == 'admin':
            return '131' + self.now_time
        else:
            return '131' + self.diff_time

    # 按当前时间生成部门名称
    def random_department(self):
        return 'department' + self.now_time
