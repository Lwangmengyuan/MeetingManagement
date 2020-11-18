# _*_conding:utf-8_*_
# 作者: 杨佳
# 创建时间: 2020/9/3 21:39
# 文件: login
import time
from common.get_verify_code import GetVerifyCode
from common.base_page import BasePage


# 继承BasePage
# 登录页面逻辑：1.登录，2.点击隐私条款，3.点击注册按钮
class LoginPage(BasePage):
    # 隐私条款
    privacy_policy_locator = ('xpath', '//*[@id="logo"]/div[2]/label/span/span')
    # 手机号输入框
    phone_locator = ('xpath', '//*[@id="warp3"]/div[1]/input')
    # 验证码获取按钮
    get_code_locator = ('xpath', '//*[@id="warp3"]/div[2]/button')
    # 验证码输入框
    verification_code_locator = ('xpath', '//*[@id="warp3"]/div[2]/input')
    # 登录按钮
    login_btn_locator = ('xpath', '//*[@id="button1"]')
    # 注册按钮
    register_btn_locator = ('xpath', '//*[@id="warp3"]/div[3]')
    # 退出按钮
    sign_out_btn_locator = ('xpath', '//*[@id="headerdiv"]/div[1]/span[2]')
    # 退出确认按钮
    confirm_btn_locator = ('xpath', '/html/body/div[2]/div/div[3]/button[2]')
    # 首页
    home_locator = ('xpath', '//*[@id="app"]/section/section/aside/div/ul/div/li[1]/span')
    # 通讯录
    address_book_locator = ('xpath', '// *[ @ id = "app"] / section / section / aside / div / ul / div / li[4] / span')
    # 新增用户按钮
    add_user_btn_locator = ('xpath', '//*[@id="app"]/section/section/section/main/div/div/div[1]/button[2]/span')
    # 会议管理系统地址
    url = 'http://10.104.10.90/'

    # 打开登录首页
    def get(self):
        self.driver.get(self.url)
        return self

    def login(self, phone):
        # 定位电话号码输入框
        phone_elem = self.find(self.phone_locator)
        phone_elem.send_keys(phone)
        # 定位获取验证码按钮
        get_code_elem = self.find(self.get_code_locator)
        get_code_elem.click()
        # 等待后台生成验证码
        # TO-DO：待优化
        time.sleep(20)
        # 获取验证码
        code = GetVerifyCode().get_login_register(phone, 'l')
        # 输入正确的验证码
        code_elem = self.find(self.verification_code_locator)
        code_elem.send_keys(code)
        # 点击登录
        self.find(self.login_btn_locator).click()
        return self

    # 勾选隐私条款
    def click_privacy_policy(self):
        privacy_policy_elem = self.find(self.privacy_policy_locator)
        privacy_policy_elem.click()
        return self

    # 点击注册按钮
    def click_register(self):
        register_elem = self.find(self.register_btn_locator)
        self.driver.execute_script("arguments[0].click();", register_elem)
        return self

    # 点击退出按钮
    def click_sign_out(self):
        self.wait_element_visible(self.sign_out_btn_locator).click()
        self.wait_element_visible(self.confirm_btn_locator).click()
        return self

    # 判断管理员是否登录成功
    def admin_login_info(self):
        if self.find(self.home_locator):
            self.find(self.address_book_locator).click()
            if self.find(self.add_user_btn_locator):
                return True
            else:
                return False

    # 判断普通用户是否登录成功
    def employ_login_info(self):
        if self.find(self.home_locator):
            self.find(self.address_book_locator).click()
            if not self.find(self.add_user_btn_locator):
                return True
            else:
                return False

    # 判断退出登录是否成功
    def sign_out_info(self):
        if self.find(self.login_btn_locator):
            return True
        else:
            return False
