#coding=utf-8
from conf import getpath,menu
from selenium import webdriver
from club.table_test.public.get_heng import get_heng
getpath()
import unittest
import time
import re
from club.table_test.public.start import start,choose
from club.table_test.public.get_col import get_col,del_list_tup
from club.table_test.public.zhu_table import get_table
# driver = choose('firefox')
#http://192.168.150.70:8080/Eeeweb/E3/index.html#/jdgf_dlhzm_sjzc_czgl
# drhnyczzgood123
driver=webdriver.Firefox()
driver.maximize_window()
driver.get("http://192.168.150.70:8080/Eeeweb/")
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("drhnyczzgood123")
driver.find_element_by_class_name("emailCode").send_keys("1")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/dl/dd[4]/input").click()
time.sleep(3)
driver.get("http://192.168.150.70:8080/Eeeweb/E3/index.html#/jdgf_scgl_znyc_ycpc")
time.sleep(3)
driver.find_element_by_partial_link_text('日均准确率').click()
driver.implicitly_wait(3)
try:
    list_heng=get_table(driver,xpath_page='//*[@id="day"]/div/div[2]/div[4]/ul/li[2]/span',xpath_table='//*[@id="day"]/div/div[2]/div[3]/table/tbody/tr')
    list_wen_yuan = get_col(list_heng, 4).copy()
    print(list_wen_yuan)

    # driver.find_element_by_xpath("//input[@values='beginDate']").click()
    # js = "$('input[values=beginDate]').removeAttr('readonly')"
    # driver.execute_script(js)
    # driver.find_element_by_xpath("//input[@values='beginDate']").clear()
    # driver.find_element_by_xpath("//input[@values='beginDate']").send_keys("2017-10-10")  # 输入查询开始时间

#     time.sleep(2)
finally:
    driver.close()
