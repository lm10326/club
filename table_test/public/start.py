#coding=utf-8
from selenium import webdriver
import time
'''配置浏览器和url'''
def choose(browser): #选择浏览器
    if browser=='firefox':
        driver=webdriver.Firefox()
    elif browser=='ie':
        driver=webdriver.Ie()
    elif browser=='chrome':
        driver=webdriver.Chrome()
    else:
        driver=webdriver.Opera()
    return driver

def start(driver,url='http://192.168.60.167:8080/SPPS/powerCurve/shortAction.action'): #启动浏览器
    print(time.time)
    driver.get(url)
    driver.find_element_by_id('loginName').send_keys('admin')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_xpath('//input[@type="submit"]').click()

if __name__ == '__main__':
    driver=choose('firefox')
    start(driver)