from yuansu import YS_Zhuce
from waits import *


class Baisc_Zhuce(object):

    def __init__(self,i):
        self.i = i
        self.driver = Wait.driver
        self.wait = Wait.wait

    def basic_zhuce(self):
        self.wait.until(YS_Zhuce.zhuce_into).click()
        self.wait.until(YS_Zhuce.username).send_keys(Excel_Zhuce.user[self.i])
        self.wait.until(YS_Zhuce.password).send_keys(Excel_Zhuce.passwd[self.i])
        self.wait.until(YS_Zhuce.re_password).send_keys(Excel_Zhuce.re_passwd[self.i])
        self.wait.until(YS_Zhuce.email).send_keys(Excel_Zhuce.email[self.i])
        self.wait.until(YS_Zhuce.zhuce_click).click()


# Baisc_Zhuce(1).basic_zhuce()