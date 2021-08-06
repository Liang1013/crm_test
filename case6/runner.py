import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from  case6.common import HTMLTestRunner

import unittest

#获取用例路径
casepath = "/Users/angshao/PycharmProjects/web_pro/case6/case"
#找到类似的py文件
rule = "test*.py"


discover = unittest.defaultTestLoader.discover(start_dir=casepath,pattern=rule)
print(discover)

#获取写入报告路
reportpath = "/Users/angshao/PycharmProjects/web_pro/case6/report/"+"reprot.html"
#已二进制写入路径下
fg = open(reportpath, "wb")


reunner = HTMLTestRunner.HTMLTestRunner(stream=fg,
                                        title="CRM登陆用例",
                                        description="用户名与密码登陆")

reunner.run(discover)