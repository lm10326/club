#coding=utf-8
from conf import getpath,menu
from selenium import webdriver
getpath()
import time
import re
from club.table_test.public.get_heng import get_heng
from club.table_test.public.get_col import get_col
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
driver.get("http://192.168.150.70:8080/Eeeweb/E3/index.html#/jdgf_scgl_znyc_qxgl")
time.sleep(3)
try:
    pagetext=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/div[4]/ul/li[2]/span").text
    pagere=r"\d+"
    pageall=int(re.findall(pagere,pagetext)[0])
    list_heng=[]
    if pageall>=11:
        print(pageall)
        for i in range(10):
            print(i+1)
            try:
                list_heng.extend(get_heng(driver,'/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/div[3]/table/tbody/tr'))
            except Exception as e:
                print(e)
            driver.find_element_by_partial_link_text("下一页").click()
            time.sleep(2)
            print(list_heng)
    else:
        print(pageall)
        for i in range(pageall):
            print(i+1)
            try:
                list_heng.extend(get_heng(driver,'/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/div[3]/table/tbody/tr'))
            except Exception as e:
                print(e)
            driver.find_element_by_partial_link_text("下一页").click()
            time.sleep(2)
            print(list_heng)
    list_wen_yuan = get_col(list_heng, 4).copy()
    print(list_wen_yuan)

    # driver.find_element_by_xpath("//input[@values='beginDate']").click()
    # js = "$('input[values=beginDate]').removeAttr('readonly')"
    # driver.execute_script(js)
    # driver.find_element_by_xpath("//input[@values='beginDate']").clear()
    # driver.find_element_by_xpath("//input[@values='beginDate']").send_keys("2017-10-10")  # 输入查询开始时间

    time.sleep(2)
finally:
    driver.close()
