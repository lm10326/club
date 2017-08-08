#coding=utf-8
from setpath import getpath
getpath()
import unittest
import time
from club.table_test.public.start import start,choose
from club.table_test.public.menu import menu
from club.table_test.public.set_date import set_date
from club.table_test.public.get_heng import get_heng
from club.table_test.public.get_col import get_col,deltup
from club.table_test.public.get_oracle import get_oracle_h
from club.table_test.public.list_com import comh
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = choose('firefox')
    def test_something(self):
        '''气象信息展示 > 温度曲线'''
        driver=self.driver
        start(driver)
        click_list = ['气象信息展示', '温度曲线']
        menu(driver,click_list)
        set_date(driver,'2017-08-08','2017-08-08')
        driver.find_element_by_id('search').click()
        time.sleep(2)
        hang='/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr'
        self.list_heng=get_heng(driver,hang).copy()
        list_wen=get_col(self.list_heng,3).copy() #获取最终列表
        list_sql=get_oracle_h('192.168.60.36',"SELECT a.PRE_DATE,a.PRE_TIME,a.ARI_TEM \
        FROM GF_SPPS_NWP_DEAL a WHERE PRE_DATE='2017-08-08' ORDER BY PRE_TIME asc", 2)
        print(list_wen)
        print(list_sql)
        list_wen.pop()
        self.assertEqual(list_wen,list_sql)
    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()
