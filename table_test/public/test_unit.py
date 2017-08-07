#coding=utf-8
from selenium import webdriver
import start
import unittest
import time
from get_col import get_col
from get_col import deltup
'''聚合打开浏览器和选择浏览器'''
starttime=time.time()
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = start.choose('firefox')
    def test_something(self):
        driver=self.driver
        start.start(driver)
        click_list = ['功率曲线展示', '历史曲线']
        # click_list=['功率曲线展示','预测曲线','短期预测曲线']
        for i in click_list:
            driver.find_element_by_link_text(i).click()
        driver.find_element_by_id('beginDate').click()
        js = "$('input[id=beginDate]').attr('readonly','')"
        driver.execute_script(js)
        driver.find_element_by_id('beginDate').clear()
        driver.find_element_by_id('beginDate').send_keys('2017-06-24')  # 输入查询开始时间
        # time.sleep(2)
        driver.find_element_by_id('endDate').click()
        js = "$('input[id=endDate]').attr('readonly','')"
        driver.execute_script(js)
        driver.find_element_by_id('endDate').clear()
        driver.find_element_by_id('endDate').send_keys('2017-06-25')  # 输入查询结束时间
        # time.sleep(2)
        driver.find_element_by_id('search').click()
        time.sleep(2)
        hang = '/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr'
        lie = hang + '[1]/td'
        tr = driver.find_elements_by_xpath(hang)  # 288 行数
        td = driver.find_elements_by_xpath(lie)  # 7 列数
        print(len(tr), len(td))
        list_henchu = []  # 获取横向列表
        for i in range(1, len(tr) + 1):
            for k in range(1, len(td) + 1):
                m = hang + '[' + str(i) + ']' + '/td[' + str(k) + ']'
                try:
                    list_henchu.append(float(driver.find_element_by_xpath(m).text))
                except:
                    list_henchu.append(driver.find_element_by_xpath(m).text)
        print("list横向初始值是：", list_henchu)
        list_qie = [0]
        list_henzhong = []
        for i in range(1, len(tr) + 1):
            list_qie.append(len(td) * i)
        for i in list_qie:
            list_henzhong.append(list_henchu[i:i + len(td)])
        list_henzhong.pop()
        print("横向最终值", list_henzhong)
        print('第一,三列值',get_col(list_henzhong,3))
        print('去除空格',deltup(get_col(list_henzhong,3),' '))
    def tearDown(self):
        self.driver.close()
        endtime = time.time()
        print(endtime-starttime)
if __name__ == '__main__':
    unittest.main()


