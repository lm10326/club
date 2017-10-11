from selenium import webdriver
import time
import re
driver=webdriver.Firefox()
driver.maximize_window()
driver.get("http://192.168.150.70:8080/Eeeweb/")
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("password").send_keys("drhnyczzgood123")
driver.find_element_by_class_name("emailCode").send_keys("1")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/dl/dd[4]/input").click()
time.sleep(3)
try:
    driver.get("http://192.168.150.70:8080/Eeeweb/E3/index.html#/jdgf_dlhzm_sjzc_czgl")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/ul/li[1]/span/span").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/ul/li[1]/ul/li[1]/span/span").click()
    time.sleep(2)
    driver.find_element_by_xpath("//i[@class='glyphicon glyphicon-add']").click()
finally:
    driver.close()