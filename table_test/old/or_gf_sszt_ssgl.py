#coding=utf-8
from conf import getpath,menu
getpath()
import unittest
import time
from club.table_test.public.start import start,choose
# from club.table_test.public.menu import menu
from club.table_test.public.set_date import set_date
from club.table_test.public.get_heng import get_heng
from club.table_test.public.get_col import get_col,del_list_tup
from club.table_test.public.get_oracle import get_oracle_h
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = choose('firefox')
    def test_1_tianqi(self):
        '''气象信息展示 > 温度曲线 >天气预报'''
        driver=self.driver
        driver.maximize_window()
        start(driver,'http://192.168.60.36:8080/SPPS/weatherInfo/temCurveAction.action')
        click_list = ['气象信息展示', '温度曲线'] #点击菜单
        menu(driver,click_list)
        set_date(driver)
        driver.find_element_by_id('search').click() #搜索
        time.sleep(2)
        hang='/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr'
        global list_heng
        list_heng=get_heng(driver,hang) #获取表格数据
        list_wen_yuan=get_col(list_heng,3).copy() #将表格数据生成列表
        list_wen=del_list_tup(list_wen_yuan,' ')
        if list_wen==[]:
            print("列表查询数据为空，无法比较")
        else:
            list_sql=get_oracle_h('192.168.60.36',"SELECT a.PRE_DATE,a.PRE_TIME,a.ARI_TEM \
            FROM GF_SPPS_NWP_DEAL a WHERE PRE_DATE='2017-09-06' ORDER BY PRE_TIME asc", 2)#查询数据库
            print('表格数据为:',list_wen)
            print('sql查询值为',list_sql)
            print('\n')
            self.assertEqual(list_wen,list_sql)
    def test_2_shiche(self):
        '''气象信息展示 > 温度曲线 >实测监测温度'''
        list_shiche_yuan=get_col(list_heng,4)
        list_shiche=del_list_tup(list_shiche_yuan,' ')
        if list_shiche==[]:
            print("列表查询数据为空，无法比较")
        else:
            list_shiche_sql=get_oracle_h('192.168.60.36',"SELECT a.COLLECTION_DATE,a.COLLECTION_TIME,a.ARI_TEM \
            FROM SPPS_FZYI_MON_HIS a WHERE a.COLLECTION_DATE='2017-09-06' ORDER BY a.COLLECTION_TIME",2)
            print('实测监测温度表格数据为:',list_shiche)
            print('实测监测温度sql查询值为',list_shiche_sql)
            print('\n')
            self.assertEqual(list_shiche,list_shiche_sql)
    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()
