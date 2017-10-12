#coding=utf-8
import logging
import time
import datetime
def set_date(driver,datebegin='2017-09-06',dateafter='2017-09-06'): #设置开始时间和结束时间，查询当天
    driver.find_element_by_id('beginDate').click()
    js = "$('input[id=beginDate]').removeAttr('readonly')"
    driver.execute_script(js)
    driver.find_element_by_id('beginDate').clear()
    driver.find_element_by_id('beginDate').send_keys(datebegin)  #输入查询开始时间
    # time.sleep(2)
    driver.find_element_by_id('endDate').click()
    js = "$('input[id=endDate]').removeAttr('readonly')"
    driver.execute_script(js)
    driver.find_element_by_id('endDate').clear()
    driver.find_element_by_id('endDate').send_keys(dateafter)  #输入查询结束时间

def set_date_tom(driver,datebegin='2017-09-06',dateafter='2017-09-06'): #设置开始时间和结束时间，查询区间
    driver.find_element_by_id('beginDate').click()
    js = "$('input[id=beginDate]').removeAttr('readonly')"
    driver.execute_script(js)
    driver.find_element_by_id('beginDate').clear()
    driver.find_element_by_id('beginDate').send_keys(datebegin)  #输入查询开始时间
    # time.sleep(2)
    driver.find_element_by_id('endDate').click()
    js = "$('input[id=endDate]').removeAttr('readonly')"
    driver.execute_script(js)
    driver.find_element_by_id('endDate').clear()
    driver.find_element_by_id('endDate').send_keys(dateafter)  #输入查询结束时间

def now_date(): #获取当前日期
    now = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    return now

def tom_date():#获取明天日期
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    return str(tomorrow)

def yes_date():#获取昨天时间
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    return str(yesterday)

def now_time(): #获取当前时间
   now = time.strftime("%M",time.localtime(time.time()))
   min_15=int(now)%15
   min_5=int(now)%5
   flag_15=0
   if min_15>0 and min_15<14:flag_15=1
   flag_5=0
   if min_5>0 and min_5<4:flag_5=1
   return flag_15,flag_5

if __name__ == '__main__':
    print(now_date())
    print(now_time())
    print(tom_date())



# logger=logging.getLogger()
# logger.setLevel(logging.DEBUG)
# ch = logging.StreamHandler()
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# ch.setFormatter(formatter)
# logger.addHandler(ch)
# logging.debug("hh")