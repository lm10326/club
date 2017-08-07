#coding=utf-8
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import HTMLTestRunner
# import sys
# sys.path.append(r'D:\selenium_use_case\05selenium+python\appium_code\kkh\public')
# import setup
def find_toast(message, timeout, poll_frequency, driver):
    message = '//*[@text=\'{}\']'.format(message)
    element = WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located((By.XPATH, message)))
    print(element.text) #获取元素文本
class cac(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.android2.calculator3'
        desired_caps['appActivity'] = 'com.android2.calculator3.Calculator'
        desired_caps['automationName'] = 'Uiautomator2'
        self.driver = webdriver.Remote('http://localhost:4728/wd/hub',desired_caps)
    def test_cac(self):
        u'''计算器测试报告'''
        driver =self.driver
        try:
            driver.find_element_by_id("com.android2.calculator3:id/del").click()
        except:
            driver.find_element_by_id("com.android2.calculator3:id/clear").click()
        # driver.find_element_by_name("1").click()
        # driver.find_element_by_id("com.android2.calculator3:id/digit1").click()
        # driver.find_element_by_xpath("//android.widget.Button[contains(@text,'1')]").click()
        # driver.find_element_by_android_uiautomator('new UiSelector().text("1")').click()
        # driver.find_element_by_id("com.android2.calculator3:id/digit5").click()
        # driver.find_element_by_id("com.android2.calculator3:id/digit9").click()
        # driver.find_element_by_id("com.android2.calculator3:id/del").click()
        # driver.find_element_by_id("com.android2.calculator3:id/digit9").click()
        # driver.find_element_by_id("com.android2.calculator3:id/digit5").click()
        # driver.find_element_by_id("com.android2.calculator3:id/plus").click()
        # driver.find_element_by_id("com.android2.calculator3:id/digit6").click()
        # driver.find_element_by_id("com.android2.calculator3:id/equal").click()
        # test = driver.find_element_by_class_name("android.widget.EditText").get_attribute('text')
        # assert test == "1,602"
        # self.assertEqual(test,'1,602')
        find_toast('+', 3, 0.5, driver)
    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()
    # testunit=unittest.TestSuite()
    # testunit.addTest(unittest.makeSuite(cac))
    # filename = 'D:\\selenium_use_case\\05selenium+python\\appium_code\\kkh\\result2.html'
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title=u'Cac测试报告',
    #     description=u'用例执行情况：')
    # runner.run(testunit)