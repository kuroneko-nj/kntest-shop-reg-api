import requests

import app


class TpshopRegApi:
    def __init__(self):
        self.reg_verify_url = app.BASE_PAGE + '/index.php/Home/User/verify/type/user_reg.html'
        self.reg_url = app.BASE_PAGE + '/index.php/Home/User/reg.html'
        # self.session = requests.Session()

    def get_reg_verify(self,session):
        """获取登陆验证码接口"""
        return session.get(url=self.reg_verify_url)

    def get_reg(self, session,reg_data):
        """获取注册接口"""
        return session.post(url=self.reg_url, data=reg_data)
