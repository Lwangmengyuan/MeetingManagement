# coding: utf-8
import redis
import time

'''
    获取登录或者注册验证码
'''


class GetVerifyCode:
    def get_keylst(self):
        ip = '10.104.15.82'
        auth = 'tcl2020-cloud'
        r = redis.Redis(host=ip, port=6379, db=12, password=auth)
        return r.keys('*'), r

    def get_register_code(self, phone):
        flag = 'account_register_cei7y6v2_' + str(phone)
        code = ''
        try:
            lst, r = self.get_keylst()
            for verifily in lst:
                if flag in str(verifily):
                    byte_code = r.get(verifily)[-6:]
                    code = bytes.decode(byte_code)
        except:
            return None
        else:
            return code

    def get_login_code(self, phone):
        flag = 'account_login_cei7y6v2_' + str(phone)
        code = ''
        try:
            lst, r = self.get_keylst()
            for verifily in lst:
                if flag in str(verifily):
                    byte_code = r.get(verifily)[-6:]
                    code = bytes.decode(byte_code)
        except:
            return None
        else:
            return code

    def get_login_register(self, phone, flag):
        count = 0
        if flag == 'l':
            while count < 20:
                res = self.get_login_code(phone)
                if res:
                    break
                count += 1
                time.sleep(3)
        elif flag == 'r':
            while count < 20:
                res = self.get_register_code(phone)
                time.sleep(3)
                if res:
                    break
                count += 1
        return res

    def removal(val):
        str1 = ""
        if not val:
            return
        for i in val:
            if i in str1:
                str1 += i
        return str1


if __name__ == '__main__':
    GVC = GetVerifyCode()
    print(GVC.get_login_register('18352538378', 'l'))
