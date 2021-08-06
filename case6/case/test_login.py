from selenium import webdriver
from case6.page.login_page import loginPage

import unittest
import ddt

testdates = [
    {"user":"李昂","psw":"La123456","expect":"李昂"},
    {"user":"李昂","psw":"","expect":"请修正下面的错误。"},
]

@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        cls.driver.get("http://crm.maimiaotech.com/auth/login/?next=/")
        cls.loginn = loginPage(cls.driver)

    def login_case(self,uanme,paw,text):
        self.loginn.is_logins(uanme,paw)
        t = self.loginn.is_login_success(text)
        if True == t:
            print("登陆：", t)
            self.assertTrue(t)
        else:
            f = self.loginn.is_login_fail(text)
            print("用例二：", f)
            self.assertTrue(f)

    @ddt.data(*testdates)
    def test_login_A(self,data):
        '''
        登陆成功/登陆失败测试用例
        :param data:
        :return:
        '''
        self.login_case(data["user"],data["psw"],data["expect"])

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        self.driver.delete_all_cookies()
        self.driver.refresh()

if __name__ == "__main__":
    unittest.main()