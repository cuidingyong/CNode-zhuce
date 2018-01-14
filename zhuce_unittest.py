import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from canshu import Excel_Zhuce
from yuansu import Zhuce

class Zhuce_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,10)
        self.driver.get(Excel_Zhuce.url)

    def test1(self):
        self.wait.until(Zhuce.zhuce_into).click()
        try:
            assert Excel_Zhuce.perfact[0] in self.wait.until(Zhuce.jianchadian1).text
        except:
            print('failed')

    def test2(self):
        self.wait.until(Zhuce.zhuce_into).click()
        self.wait.until(Zhuce.username).send_keys(Excel_Zhuce.user[0])
        self.wait.until(Zhuce.password).send_keys(Excel_Zhuce.passwd[0])
        self.wait.until(Zhuce.re_password).send_keys(Excel_Zhuce.re_passwd[0])
        self.wait.until(Zhuce.email).send_keys(Excel_Zhuce.email[0])
        self.wait.until(Zhuce.zhuce_click).click()
        try:
            assert Excel_Zhuce.perfact[1] in self.wait.until(Zhuce.tishi).text
        except:
            print('failed')

    def test3(self):
        self.wait.until(Zhuce.zhuce_into).click()
        self.wait.until(Zhuce.username).send_keys(Excel_Zhuce.user[1])
        self.wait.until(Zhuce.password).send_keys(Excel_Zhuce.passwd[1])
        self.wait.until(Zhuce.re_password).send_keys(Excel_Zhuce.re_passwd[1])
        self.wait.until(Zhuce.email).send_keys(Excel_Zhuce.email[1])
        self.wait.until(Zhuce.zhuce_click).click()
        try:
            assert Excel_Zhuce.perfact[2] in self.wait.until(Zhuce.tishi).text
        except:
            print('failed')

    def test4(self):
        self.wait.until(Zhuce.zhuce_into).click()
        self.wait.until(Zhuce.username).send_keys(Excel_Zhuce.user[2])
        self.wait.until(Zhuce.password).send_keys(Excel_Zhuce.passwd[2])
        self.wait.until(Zhuce.re_password).send_keys(Excel_Zhuce.re_passwd[2])
        self.wait.until(Zhuce.email).send_keys(Excel_Zhuce.email[2])
        self.wait.until(Zhuce.zhuce_click).click()
        try:
            assert Excel_Zhuce.perfact[3] in self.wait.until(Zhuce.tishi).text
        except:
            print('failed')

    # def test5(self):
    #     self.wait.until(Zhuce.zhuce_into).click()
    #     self.wait.until(Zhuce.username).send_keys(Excel_Zhuce.user[3])
    #     self.wait.until(Zhuce.password).send_keys(Excel_Zhuce.passwd[3])
    #     self.wait.until(Zhuce.re_password).send_keys(Excel_Zhuce.re_passwd[3])
    #     self.wait.until(Zhuce.email).send_keys(Excel_Zhuce.email[3])
    #     self.wait.until(Zhuce.zhuce_click).click()
    #     try:
    #         assert Excel_Zhuce.perfact[4] in self.wait.until(Zhuce.tishi).text
    #     except:
    #         print('failed')

    def test6(self):
        self.wait.until(Zhuce.zhuce_into).click()
        self.wait.until(Zhuce.username).send_keys(Excel_Zhuce.user[4])
        self.wait.until(Zhuce.password).send_keys(Excel_Zhuce.passwd[4])
        self.wait.until(Zhuce.re_password).send_keys(Excel_Zhuce.re_passwd[4])
        self.wait.until(Zhuce.email).send_keys(Excel_Zhuce.email[4])
        self.wait.until(Zhuce.zhuce_click).click()
        try:
            assert Excel_Zhuce.perfact[5] in self.wait.until(Zhuce.tishi).text
        except:
            print('failed')

    def tearDown(self):
        self.driver.quit()

test_cases = unittest.TestLoader().loadTestsFromTestCase(Zhuce_Test)
testunit = unittest.TestSuite()
testunit.addTests(test_cases)
fp = open('D:\python学习\网易云\百度\CNode\\result.html','wb')
runner = HTMLTestRunner(stream=fp,title='choi\'s测试报告',description='测试结果')
runner.run(testunit)
fp.close()





