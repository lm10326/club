#coding=utf-8
from selenium.webdriver.support.ui import Select
import sys
def getpath():
    return sys.path.append('E:\\ch_workspace')

def menu(driver,itsmenu): #循环点击菜单，进入相应页面
    for i in itsmenu:
        driver.find_element_by_link_text(i).click()

'''点击集电线列表'''
def jidianxian(driver,id="select2",jidianxian="集电线1"):
    Select(driver.find_element_by_id(id)).select_by_visible_text(jidianxian)
# driver=webdriver.Firefox()
# driver.maximize_window()
# driver.get('http://192.168.60.36:8080/SPPS/powerCurve/shortAction.action')
# driver.find_element_by_id('loginName').send_keys('admin')
# driver.find_element_by_id('password').send_keys('123456')
# login=driver.find_element_by_xpath('//input[@type="submit"]').click()
# click_list=["功率曲线展示","预测曲线","短期预测曲线"]
# for i in click_list:
#     driver.find_element_by_link_text(i).click()
# jd_list=["集电线1","全部"]
# for i in jd_list:
#     jidianxian(driver,"select2",i)
#     time.sleep(2)
# driver.close()