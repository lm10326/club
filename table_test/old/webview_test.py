#coding=utf-8
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
def find_toast(message, timeout, poll_frequency, driver):
    message = '//*[@text=\'{}\']'.format(message)
    element = WebDriverWait(driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located((By.XPATH, message)))
    print(element.text) #获取元素文本
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.testerhome.webview'
desired_caps['appActivity'] = 'com.testerhome.webview.MainActivity'
desired_caps['noReset'] = 'True'
desired_caps['automationName'] = 'Uiautomator2' #这个条件必须加上
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# m=driver.find_element_by_android_uiautomator('new UiSelector().text("click toast")').get_attribute('text')
# m2=driver.find_element_by_android_uiautomator('new UiSelector().text("click toast")').get_attribute('name')
# driver.find_element_by_android_uiautomator('new UiSelector().text("click toast")').click()
# m=driver.find_element_by_android_uiautomator('new UiSelector().text("click toast")').get_attribute('text')
# print(m,m2)
# driver.find_element_by_android_uiautomator('click toast').click()
# driver.find_element_by_xpath("//android.widget.Button[contains(@text,'click toast')]").click() #xpath定位
# print(driver.contexts)
time.sleep(2)
print(driver.contexts)
driver.switch_to.context('WEBVIEW_com.testerhome.webview')
try:
    driver.find_element_by_accessibility_id('小说 Link').click()
except Exception as e:
    print(e)

# print(driver.page_source)
# driver.find_element_by_partial_link_text("小说").click()
# driver.find_element_by_xpath("//[contains(text(),'小说')]").click()
# el=driver.find_elements_by_xpath('android.view.View')
# for i in el:
#     print(i)
# print(len(el))
# for i in el:
#     if i.get_attribute('name')=="小说 Link":
#         i.click()
#     else:
#         print(i.get_attribute("name"))

driver.switch_to.context('NATIVE_APP')
el=driver.find_elements_by_class_name('android.widget.Button')
for i in el:
    print(i)
print(len(el))
# driver.find_element_by_id('com.testerhome.webview:id/clickToToastActivity').click()
driver.find_element_by_xpath("//android.widget.Button[contains(@text,'click toast')]").click()
driver.find_element_by_id("com.testerhome.webview:id/toast").click()
find_toast('Toast Test',3,0.5,driver)
# driver.switch_to.context('WEBVIEW_com.testerhome.webview')
# print(driver.current_context)
# driver.switch_to.context('NATIVE_APP')
# print(driver.current_context)
# driver.find_element_by_id('com.testerhome.webview:id/toast')
driver.quit()