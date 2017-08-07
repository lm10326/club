#coding=utf-8
import unittest
from appium import webdriver
import time
import HTMLTestRunner
# import sys
# sys.path.append(r'D:\selenium_use_case\05selenium+python\appium_code\kkh\public')
# import setup
class cac(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.ios.minicalc'
        desired_caps['appActivity'] = '.Calculator'
        desired_caps['noReset'] = 'True'
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', setup.setUp())
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def test_cac(self):
        u'''计算器测试报告'''
        driver =self.driver
        # time.sleep(5)
        print(driver.current_activity)
        driver.find_element_by_id('com.ios.minicalc:id/digit9').click()
        driver.find_element_by_accessibility_id('除').click()
        # driver.find_element_by_xpath("//android.widget.Button[contains(@text,'除')]").click()
        # driver.find_element_by_xpath("//android.widget.Button[contains(@text,'1')]").click()
        time.sleep(3)
        # driver.find_element_by_name("1").click() #1.5后失效不可再用name定位

        # driver.find_element_by_xpath("//android.widget.Button[contains(@text,'1')]").click() #xpath定位

        # driver.find_element_by_android_uiautomator('new UiSelector().text("1")').click() #uiautomator定位

        #driver.find_element_by_accessibility_id('1').click() #content-desc用，本例是失败的

        # els = driver.find_elements_by_class_name('android.widget.Button')  #classname定位，查询元素是否包含某一文字
        # for i in els:
        #     print(i.get_attribute('text'))
        # mytest=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout' \
        #                                   '/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/' \
        #                                   'android.widget.ViewSwitcher/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.EditText').get_attribute('text')
        # print(mytest)
        # assert test == "1,602"
        # self.assertEqual(test,'1,602')
    def tearDown(self):
        # pass
        self.driver.close_app()
        # self.driver.quit()
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