import unittest

import requests
from parameterized import parameterized

import app
from api.TpshopLogin_api import TpshopLoginApi
from api.TpshopReg_api import TpshopRegApi
from utils import assert_reg, get_test_data


class TestTpshopReg(unittest.TestCase):
    __session = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.tp_reg_api = TpshopRegApi()
        cls.tp_login_api = TpshopLoginApi()

    def setUp(self) -> None:
        if self.__session is None:
            self.__session = requests.Session()

    def tearDown(self) -> None:
        self.__session.close()

    @parameterized.expand(get_test_data(app.BASE_PATH+'/data/reg_data.json'))
    def test_reg(self, reg_data, http_code, status, msg):
        """注册用例"""
        # 获取注册验证码
        response_reg_verify = self.tp_reg_api.get_reg_verify(self.__session)
        # 断言注册验证码获取成功
        self.assertIn("image", response_reg_verify.headers.get('Content-Type'))
        # 获取注册接口
        response_reg = self.tp_reg_api.get_reg(self.__session, reg_data)
        # 断言注册成功-status，msg，响应状态码与预期是否一致
        print(response_reg.status_code)
        if response_reg.json().get('status') == 1:
            print(response_reg.json().get('result').get('mobile'))
        print(response_reg.json().get('status'))
        print(response_reg.json().get('msg'))
        assert_reg(self, http_code, status, msg, reg_data.get('username'), response_reg)
        # 如果注册成功,执行登陆,否则不登录
        if (response_reg.json().get('msg')) == "注册成功":
            # 获取登陆验证码
            response_login_verify = self.tp_login_api.get_login_verify(self.__session)
            # 断言登陆验证码获取成功
            self.assertIn("image", response_login_verify.headers.get('Content-Type'))
            # 获取登陆接口
            login_data = {'username': reg_data.get('username'), 'verify_code': reg_data.get('verify_code'),
                          'password': reg_data.get('password')}
            response_login = self.tp_login_api.get_login(self.__session, login_data)
            # 断言登陆成功-断言status，msg，响应状态码与预期是否一致
            print("登陆:", response_login.status_code)
            print("登陆:", response_login.json().get('result').get('mobile'))
            print("登陆:", response_login.json().get('status'))
            print("登陆:", response_login.json().get('msg'))
            assert_reg(self, http_code, status, msg, reg_data.get('username'), response_login)
        else:
            print("反向用例,不做登陆")
