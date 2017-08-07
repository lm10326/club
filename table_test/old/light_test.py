#coding=utf-8
from selenium import webdriver
import re
import time
# import datetime
# start=datetime.datetime.now()  #开始时间
driver=webdriver.Firefox()
driver.get('http://192.168.60.36:8080/SPPS/powerCurve/shortAction.action')
# driver.maximize_window()
driver.find_element_by_id('loginName').send_keys('admin')
driver.find_element_by_id('password').send_keys('123456')
login=driver.find_element_by_xpath('//input[@type="submit"]').click()
# time.sleep(3)
driver.implicitly_wait(3)
# driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@class,'foot')]")) #切换frame，通过xpath
driver.switch_to.frame(0) #切换frame通过frame索引
pic=driver.find_element_by_id('img1').get_attribute('src') #天气预报
pic_tianqi=re.search(r'[a-z]+\w+\.gif',pic).group()  #获取灯的状态
print(pic_tianqi)

pic=driver.find_element_by_id('img2').get_attribute('src') #实时功率
pic_sisi=re.search(r'[a-z]+\w+\.gif',pic).group()
print(pic_sisi)

pic=driver.find_element_by_id('img3').get_attribute('src') #短期预测功率
pic_dq=re.search(r'[a-z]+\w+\.gif',pic).group()
print(pic_dq)

pic=driver.find_element_by_id('img4').get_attribute('src') #超短期预测功率
pic_lilung=re.search(r'[a-z]+\w+\.gif',pic).group()
print(pic_lilung)

pic=driver.find_element_by_id('img5').get_attribute('src') #实际理论功率
pic_sj=re.search(r'[a-z]+\w+\.gif',pic).group()
print(pic_sj)

sj=driver.find_element_by_id('power').text #实际功率的值
sj_word=re.search('\d\.\w+',sj).group()
print(sj_word)
driver.close()