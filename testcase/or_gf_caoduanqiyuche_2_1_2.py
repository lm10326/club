#coding=utf-8
from conf import getpath,menu
getpath()
import unittest
import time
from club.table_test.public.start import start,choose
from club.table_test.public.menu import menu
from club.table_test.public.set_date import set_date,now_time,now_date,yes_date,set_date_one,tom_date,hou_date
from club.table_test.public.get_heng import get_heng
from club.table_test.public.get_col import get_col,del_list_tup,get_col_two
from club.table_test.public.get_oracle import get_oracle_h
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = choose('firefox')
    def test_1_ycgl(self):
        '''功率曲线展示 > 预测曲线 > 超短期预测曲线 > 预测功率'''
        driver=self.driver
        driver.maximize_window()
        start(driver,'http://192.168.60.21:8080/SPPS/weatherInfo/temCurveAction.action')
        click_list = ['功率曲线展示', '预测曲线','超短期预测曲线'] #点击菜单
        menu(driver,click_list)
        if now_time()[0]!=1:
            print("waiting 70")
            time.sleep(70)
        driver.find_element_by_id('search').click() #搜索
        time.sleep(2)
        hang='/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr'
        global list_heng
        list_heng=get_heng(driver,hang) #获取表格数据
        list_ycgl_yuan = get_col(list_heng, 3).copy()  # 将表格数据生成列表
        list_ycgl = del_list_tup(list_ycgl_yuan, ' ')
        if list_ycgl == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.PRE_DATE, a.PRE_TIME, a.PRE_POWER FROM SPPS_PREDICT_CDQ_DEAL a WHERE " \
                     "PRE_DATE = 'tom_date()' and a.pre_date || ' ' || a.pre_time >to_char(sysdate - 0 / 24, 'yyyy-mm-dd hh24:mi:ss') ORDER BY PRE_TIME "
            sql = sql_kk.replace("tom_date()", now_date())
            list_sql = get_oracle_h(sql, 2)  # 查询数据库
            print('超短期预测表格数据为:', list_ycgl)
            print('超短期预测sql数据为', list_sql)
            print('\n')
            self.assertEqual(list_ycgl, list_sql)

    def tearDown(self):
        self.driver.close()
        time.sleep(1)
if __name__ == '__main__':
    unittest.main()
