from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
Example:
            from selenium.webdriver.support.ui import WebDriverWait \n
            element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId")) \n
            is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).\ \n
                        until_not(lambda x: x.find_element_by_id("someId").is_displayed())
'''

class Base():

    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        self.times = 10
        self.t = 0.5


    def findelement(self,locator):
        element = WebDriverWait(self.driver,self.times,self.t).until(lambda x: x.find_element(*locator))
        return element

    def sendkeys(self,locator,text):
        ele = self.findelement(locator)
        ele.send_keys(text)

    def click(self,cloator):
        ele = self.findelement(cloator)
        ele.click()

    def text_in_element(self,locator,text_):
        try:
            element = WebDriverWait(self.driver,self.times,self.t).until(EC.text_to_be_present_in_element(locator,text_))
            return element
        except:
            return False