# coding: utf-8
import time
from common.base_page import BasePage
from common.get_verify_code import GetVerifyCode
from pages.login_page import LoginPage


class RegisterPage(BasePage):
    # 注册链接
    register_link_locator = ('xpath', '//*[@id="warp3"]/div[3]')
    # 公司管理员选项
    admin_select_locator = ('xpath', '//*[@id="app"]/div/div/div[2]/label/span[1]')
    # 公司员工选项
    employ_select_locator = ('xpath', '//*[@id="app"]/div/div/div[3]/label/span[1]')
    # 完成
    complete_btn_locator = ('xpath', '//*[@id="app"]/div/div/div[4]/button')
    # 管理员注册
    # 公司名称输入框
    admin_company_locator = ('xpath', '//*[@id="app"]/div/div/div[2]/form/div[1]/div/div/input')
    # 公司地址输入框
    admin_address_locator = ('xpath', '//*[@id="app"]/div/div/div[2]/form/div[2]/div/div/input')
    # 行业类型选择
    industry_type_locator = ('xpath', '//*[@id="app"]/div/div/div[2]/form/div[3]/div/div/div[1]/span/span/i')
    industry_select_locator = ('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li[1]')
    # 人员规模选择
    staff_size_locator = ('xpath', '//*[@id="app"]/div/div/div[2]/form/div[4]/div/div/div[1]/span/span/i')
    staff_select_locator = ('xpath', '/html/body/div[3]/div[1]/div[1]/ul/li[2]')
    next_locator = ('xpath', '//*[@id="button1"]')
    # 姓名输入框
    admin_name_locator = ('xpath', '//*[@id="app"]/div/div/div[2]/div[1]/input')
    # 邮箱输入框
    admin_email_locator = ('xpath', '//*[@id="app"]/div/div/div[2]/div[2]/input')
    # 手机号输入框
    admin_phone_locator = ('xpath', '//*[@id="app"]/div/div/div[2]/div[3]/input')
    # 验证码获取按钮
    admin_get_code_locator = ('xpath', '//*[@id="app"]/div/div/div[2]/div[4]/button')
    # 验证码输入框
    admin_verification_code_locator = ('xpath', '//*[@id="app"]/div/div/div[2]/div[4]/input')
    # 完成按钮
    admin_complete_btn_locator = ('xpath', '//*[@id="app"]/div/div/div[2]/button[2]')
    # 普通员工注册
    # 姓名输入框
    employ_name_locator = ('xpath', '//*[@id="app"]/div/div/div/form/div[1]/div/div[1]/input')
    # 公司名称输入框
    employ_company_locator = ('xpath', '//*[@id="app"]/div/div/div/form/div[2]/div/div/div/input')
    # 公司选定
    employ_company_select_locator = ('xpath', '/html/body/div[2]/div[1]/div[1]/ul/li')
    # 邮箱输入框
    employ_email_locator = ('xpath', '//*[@id="app"]/div/div/div/form/div[3]/div/div/input')
    # 地址输入框
    employ_address_locator = ('xpath', '//*[@id="app"]/div/div/div/form/div[4]/div/div/input')
    # 联系电话输入框
    employ_phone_locator = ('xpath', '//*[@id="app"]/div/div/div/form/div[5]/div/div[1]/input')
    # 验证码获取按钮
    employ_get_code_locator = ('xpath', '//*[@id="app"]/div/div/div/form/div[6]/div/button')
    # 验证码输入框
    employ_verification_code_locator = ('xpath', '//*[@id="app"]/div/div/div/form/div[6]/div/div/input')
    # 完成按钮
    employ_complete_btn_locator = ('xpath', '//*[@id="app"]/div/div/div/div[2]/button')
    # 创建成功
    admin_create_success = ('xpath', '//*[@id="app"]/div/div/div[2]/div')
    employ_create_success = ('xpath', '//*[@id="app"]/div/div/div/div')
    # 进入系统按钮
    enter_system = ('xpath', '//*[@id="button1"]')
    # employ_enter_system = ('xpath', '//*[@id="button1"]')
    # 会议管理系统地址
    url = 'http://10.104.10.90/'

    def get(self):
        l = LoginPage(self.driver)
        l.get().click_register()
        return self

    def admin_register(self, info):
        # 选择公司管理员，点击【完成】
        self.find(self.admin_select_locator).click()
        self.find(self.complete_btn_locator).click()
        # 输入公司名称
        self.find(self.admin_company_locator).send_keys(info['company_name'])
        # 输入公司地址
        self.find(self.admin_address_locator).send_keys(info['company_address'])
        # 选择行业类型：互联网
        self.select_element(self.industry_type_locator, self.industry_select_locator)
        # 选择人员规模：50~100
        self.select_element(self.staff_size_locator, self.staff_select_locator)
        # 点击【下一步】
        self.find(self.next_locator).click()
        # 输入管理员姓名
        self.find(self.admin_name_locator).send_keys(info['admin_name'])
        # 输入管理员邮箱
        self.find(self.admin_email_locator).send_keys(info['admin_email'])
        # 输入手机号
        self.find(self.admin_phone_locator).send_keys(info['admin_phone'])
        # 生成验证码
        self.find(self.admin_get_code_locator).click()
        # 等待后台生成验证码
        # TO-DO：待优化
        time.sleep(20)
        # 获取验证码
        code = GetVerifyCode().get_login_register(info['admin_phone'], 'r')
        # 输入验证码
        self.find(self.admin_verification_code_locator).send_keys(code)
        # 点击完成
        self.find(self.admin_complete_btn_locator).click()
        return self

    def employ_register(self, info):
        # 选择公司员工，点击【完成】
        self.find(self.employ_select_locator).click()
        self.find(self.complete_btn_locator).click()
        # 输入姓名
        self.find(self.employ_name_locator).send_keys(info['employ_name'])
        # 输入企业名称
        self.find(self.employ_company_locator).send_keys(info['company_name'])
        # 选中企业
        self.wait_element_visible(self.employ_company_select_locator).click()
        # 输入普通员工邮箱
        self.find(self.employ_email_locator).send_keys(info['employ_email'])
        # 输入地址
        self.find(self.employ_address_locator).send_keys(info['employ_address'])
        # 输入手机号
        self.find(self.employ_phone_locator).send_keys(info['employ_phone'])
        # 生成验证码
        self.find(self.employ_get_code_locator).click()
        # 等待后台生成验证码
        # TO-DO：待优化
        time.sleep(20)
        # 获取验证码
        code = GetVerifyCode().get_login_register(info['employ_phone'], 'r')
        # 输入验证码
        self.find(self.employ_verification_code_locator).send_keys(code)
        # 点击完成
        self.find(self.employ_complete_btn_locator).click()
        return self

    # 判断管理员是否注册成功
    def admin_register_info(self):
        if self.find(self.admin_create_success) and self.find(self.enter_system):
            self.find(self.enter_system).click()
            return True
        else:
            return False

    # 判断普通用户是否注册成功
    def employ_register_info(self):
        if self.find(self.employ_create_success) and self.find(self.enter_system):
            self.find(self.enter_system).click()
            return True
        else:
            return False
