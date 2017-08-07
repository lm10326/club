#coding=utf-8
from selenium import webdriver
import time
def menu(driver,itsmenu): #循环点击菜单，进入相应页面
    for i in itsmenu:
        driver.find_element_by_link_text(i).click()

