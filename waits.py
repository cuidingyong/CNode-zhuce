from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from canshu import Excel_Zhuce

class Wait(object):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get(Excel_Zhuce.url)