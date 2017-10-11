#coding=utf-8
from conf import getpath,menu
getpath()
import unittest
import time
from club.table_test.public.start import start,choose
from club.table_test.public.menu import menu
from club.table_test.public.set_date import set_date,now_time,now_date
from club.table_test.public.get_heng import get_heng
from club.table_test.public.get_col import get_col,del_list_tup,get_col_two
from club.table_test.public.get_oracle import get_oracle_h
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = choose('firefox')
    def test_1_dq(self):
        '''实时状态监控 > 实时功率曲线 > 短期'''
        driver=self.driver
        driver.maximize_window()
        start(driver,'http://192.168.60.21:8080/SPPS/weatherInfo/temCurveAction.action')
        click_list = ['实时状态监控', '实时功率曲线'] #点击菜单
        menu(driver,click_list)
        if now_time()[0]!=1:
            time.sleep(130)
            print("waiting 130")
        else:
            driver.find_element_by_id('search').click() #搜索
            time.sleep(2)
            hang='/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr'
            global list_heng
            today=now_date()
            list_heng=get_heng(driver,hang) #获取表格数据
            list_dq_yuan=get_col_two(list_heng,2).copy() #将表格数据生成列表
            list_dq=del_list_tup(list_dq_yuan,' ')
            if list_dq==[]:
                print("列表查询数据为空，无法比较")
            else:
                sql_kk="SELECT PRE_TIME,PRE_POWER FROM gf_spps_predict_nwp_deal WHERE PRE_DATE='now_date()' ORDER BY PRE_TIME"
                sql=sql_kk.replace("now_date()",now_date())
                list_sql=get_oracle_h('192.168.60.21',sql, 2)#查询数据库
                print('短期表格数据为:',list_dq)
                print('短期sql数据为',list_sql)
                print('\n')
                self.assertEqual(list_dq,list_sql)
    def test_2_cdq(self):
        '''实时状态监控 > 实时功率曲线 > 超短期'''
        list_cdq_yuan=get_col_two(list_heng,3)
        list_cdq=del_list_tup(list_cdq_yuan,' ')
        if list_cdq==[]:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk="SELECT PRE_TIME,PRE_POWER FROM SPPS_PREDICT_CDQ_DEAL WHERE PRE_DATE='now_date()' ORDER BY PRE_TIME"
            sql = sql_kk.replace("now_date()", now_date())
            list_cdq_sql=get_oracle_h('192.168.60.21',sql,2)
            print('超短期表格数据为:',list_cdq)
            print('超短期sql数据为',list_cdq_sql)
            print('\n')
            self.assertEqual(list_cdq,list_cdq_sql)
    def test_3_zyg(self):
        '''实时状态监控 > 实时功率曲线 > 总有功'''
        list_zyg_yuan = get_col_two(list_heng, 4)
        list_zyg = del_list_tup(list_zyg_yuan, ' ')
        if list_zyg == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT GATHER_TIME,POWER_VALUE FROM gf_spps_power_his WHERE GATHER_DATE='now_date()' ORDER BY GATHER_TIME"
            sql = sql_kk.replace("now_date()", now_date())
            list_zyg_sql = get_oracle_h('192.168.60.21', sql, 2)
            print('总有功表格数据为:', list_zyg)
            print('总有功sql数据为', list_zyg_sql)
            print('\n')
            self.assertEqual(list_zyg, list_zyg_sql)
    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()
