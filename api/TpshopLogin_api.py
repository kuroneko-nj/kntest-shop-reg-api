import app


class TpshopLoginApi:
    def __init__(self):
        self.login_verify_url = app.BASE_PAGE + '/index.php?m=Home&c=User&a=verify'
        self.login_url = app.BASE_PAGE + '/index.php?m=Home&c=User&a=do_login'
        # self.session = requests.Session()

    def get_login_verify(self, session):
        """获取登陆验证码接口"""
        return session.get(url=self.login_verify_url)

    def get_login(self, session, login_data):
        """获取登陆接口"""
        return session.post(url=self.login_url, data=login_data)
