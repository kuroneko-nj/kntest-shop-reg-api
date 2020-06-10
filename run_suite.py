import time
import unittest
from BeautifulReport import BeautifulReport
import app

suite = unittest.TestLoader().discover(app.BASE_PATH+'/script',pattern="test*.py")
file_name = "/report{}.html".format(time.strftime('%Y%m%d-%H%M%S'))
BeautifulReport(suite).report(filename=file_name,description='TPSHOP注册接口测试',log_path='./report')