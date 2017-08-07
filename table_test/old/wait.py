#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
try:
    WebDriverWait(driver, 10).until(lambda  driver:driver.find_element_by_id('lg').is_displayed())
except Exception as e:
    print(e)
print(WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'kw'))))
driver.close()