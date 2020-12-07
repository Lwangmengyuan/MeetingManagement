# coding: utf-8
import redis

'''
    获取登录或者注册验证码
'''


class GetVerifyCode:
    def get_keylst(self):
        # ip = '10.104.15.82'
        ip = '10.88.65.240'
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
        if flag == 'l':
            return self.get_login_code(phone)
        elif flag == 'r':
            return self.get_register_code(phone)

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
