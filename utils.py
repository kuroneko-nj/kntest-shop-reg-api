import json
import logging
from logging import handlers

import app


def base_logging_config():
    # 2 在函数中，设置日志器
    logger = logging.getLogger()
    # 3 设置日志等级
    logger.setLevel(logging.INFO)
    # 4 设置控制台处理器
    sh = logging.StreamHandler()
    # 5 设置文件处理器（文件处理的作用是设置保存日志的文件地址的：需要使用项目根目录定位到日志文件）
    log_path = app.BASE_PATH + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename=log_path, when='M', interval=1,
                                                   backupCount=3, encoding='utf-8')
    # 6 设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt=fmt)
    # 7 将格式化器添加到文件处理器和控制台处理当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 8 将文件处理器和控制台处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)


def assert_reg(self, http_code, status, msg, mobile, response):
    """注册用的断言"""
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(status, response.json().get('status'))
    self.assertIn(msg, response.json().get('msg'))
    # 正向用例查看手机号跟输入是否一致
    if status == 1:
        self.assertEqual(mobile, response.json().get('result').get('mobile'))


def get_test_data(path):
    """从json文件中提取测试数据"""
    with open(path, encoding="utf-8") as f:
        test_data = []
        data_dict = (json.load(f).values())
        for data in data_dict:
            test_data.append(list(data.values()))
        return test_data


if __name__ == '__main__':
    get_test_data("./data/reg_data.json")
