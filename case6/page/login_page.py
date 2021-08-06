from case6.common.base import Base
from selenium import webdriver

'''
ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
'''

class loginPage(Base):

    username = ("id","id_username")
    password = ("id","id_password")
    submit = ("css selector",".btn-large")

    nickname = ("css selector",".nick-name")
    loginfail = ("css selector",".alert-error")


    def loginname(self,user):
        self.sendkeys(self.username,user)

    def loginpaw(self,psw):
        self.sendkeys(self.password,psw)

    def loginsubmit(self):
        self.click(self.submit)

    def is_logins(self,user,psw):
        self.loginname(user)
        self.loginpaw(psw)
        self.loginsubmit()

    def is_login_success(self,text):
        return self.text_in_element(self.nickname,text)

    def is_login_fail(self,text):
        return self.text_in_element(self.loginfail,text)



if __name__ == "__main__":
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    driver.get("http://crm.maimiaotech.com/auth/login/?next=/")
    loginn = loginPage(driver)
    loginn.is_logins("李昂","")
    #t = loginn.is_login_success("李昂")
    t = loginn.is_login_fail("请修正下面的错误。")
    print(t)
    driver.quit()
