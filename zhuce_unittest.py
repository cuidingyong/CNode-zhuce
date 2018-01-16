import unittest
from HTMLTestRunner import HTMLTestRunner
from canshu import Excel_Zhuce
from yuansu import YS_Zhuce
from fangfa import Baisc_Zhuce
from waits import Wait
from duanyan import *
from getpath import *

class Zhuce_Test(unittest.TestCase):

    def setUp(self):
        self.driver = Wait.driver
        self.wait = Wait.wait
        self.driver.get(Excel_Zhuce.url)

    def test0(self):
        self.wait.until(YS_Zhuce.zhuce_into).click()
        # assert Excel_Zhuce.perfact[0] in self.wait.until(YS_Zhuce.jianchadian1).text
        assert_equal(Excel_Zhuce.perfact[0],self.wait.until(YS_Zhuce.jianchadian1).text)

    def test1(self):
        Baisc_Zhuce(1).basic_zhuce()
        assert_in(Excel_Zhuce.perfact[1],self.wait.until(YS_Zhuce.tishi).text)

    def test2(self):
        Baisc_Zhuce(2).basic_zhuce()
        assert_in(Excel_Zhuce.perfact[2],self.wait.until(YS_Zhuce.tishi).text)


    def test3(self):
        Baisc_Zhuce(3).basic_zhuce()
        assert_in(Excel_Zhuce.perfact[3],self.wait.until(YS_Zhuce.tishi).text)

    def test4(self):
        Baisc_Zhuce(4).basic_zhuce()
        assert_in(Excel_Zhuce.perfact[4], self.wait.until(YS_Zhuce.tishi).text)

    def test5(self):
        Baisc_Zhuce(5).basic_zhuce()
        assert_in(Excel_Zhuce.perfact[5], self.wait.until(YS_Zhuce.tishi).text)

    def test6(self):
        #当有案例执行失败时，使用tearDown关闭浏览器会无法生成测试报告
        self.driver.quit()

    def tearDown(self):
        pass

def suite():
    test_cases = unittest.TestLoader().loadTestsFromTestCase(Zhuce_Test)
    testunit = unittest.TestSuite()
    testunit.addTest(test_cases)
    return testunit

if __name__ == '__main__':
    fp = open(getpath('result.html'),'wb')
    runner = HTMLTestRunner(stream=fp,title='choi\'s测试报告',description='测试结果')
    runner.run(suite())
    fp.close()






