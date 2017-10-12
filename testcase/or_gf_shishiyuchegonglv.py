#coding=utf-8
from conf import getpath,menu
getpath()
import unittest
import time
from club.table_test.public.start import start,choose
from club.table_test.public.menu import menu
from club.table_test.public.set_date import set_date,now_time,now_date,yes_date
from club.table_test.public.get_heng import get_heng
from club.table_test.public.get_col import get_col,del_list_tup,get_col_two
from club.table_test.public.get_oracle import get_oracle_h
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = choose('firefox')
    def test_1_cdq(self):
        '''实时状态监控 > 预测理论功率曲线 > 超短期'''
        driver=self.driver
        driver.maximize_window()
        start(driver,'http://192.168.60.21:8080/SPPS/weatherInfo/temCurveAction.action')
        click_list = ['实时状态监控', '预测理论功率曲线'] #点击菜单
        menu(driver,click_list)
        if now_time()[0]!=1:
            print("waiting 70")
            time.sleep(70)
        set_date(driver,now_date(),now_date())
        driver.find_element_by_id('search').click() #搜索
        time.sleep(2)
        hang='/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr'
        global list_heng
        list_heng=get_heng(driver,hang) #获取表格数据
        list_cdq_yuan = get_col_two(list_heng, 2).copy()  # 将表格数据生成列表
        list_cdq = del_list_tup(list_cdq_yuan, ' ')
        if list_cdq == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.PRE_TIME,a.PRE_POWER FROM SPPS_PREDICT_CDQ_DEAL a WHERE PRE_DATE='now_date()' ORDER BY PRE_TIME"
            sql = sql_kk.replace("now_date()", now_date())
            list_sql = get_oracle_h(sql, 2)  # 查询数据库
            print('超短期表格数据为:', list_cdq)
            print('超短期sql数据为', list_sql)
            print('\n')
            self.assertEqual(list_cdq, list_sql)
    def test_2_ycll(self):
        '''实时状态监控 > 预测理论功率曲线 > 预测理论功率'''
        list_ycll_yuan = get_col_two(list_heng, 3)
        list_ycll = del_list_tup(list_ycll_yuan, ' ')
        if list_ycll == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.PRE_TIME,a.PRE_POWER FROM SPPS_PREDICT_CDQ_DEAL_PH a WHERE PRE_DATE='now_date()' ORDER BY PRE_TIME"
            sql = sql_kk.replace("now_date()", now_date())
            list_ycll_sql = get_oracle_h(sql, 2)
            print('预测理论功率表格数据为:', list_ycll)
            print('预测理论功率sql数据为', list_ycll_sql)
            print('\n')
            self.assertEqual(list_ycll, list_ycll_sql)
    def test_3_zyg(self):
        '''实时状态监控 > 实时功率曲线 > 总有功'''
        list_zyg_yuan = get_col_two(list_heng, 4)
        list_zyg = del_list_tup(list_zyg_yuan, ' ')
        if list_zyg == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.GATHER_TIME,a.POWER_VALUE FROM GF_SPPS_POWER_HIS a WHERE a.GATHER_DATE='now_date()' ORDER BY a.GATHER_TIME"
            sql = sql_kk.replace("now_date()", now_date())
            list_zyg_sql = get_oracle_h(sql, 2)
            print('总有功表格数据为:', list_zyg)
            print('总有功sql数据为', list_zyg_sql)
            print('\n')
            self.assertEqual(list_zyg, list_zyg_sql)
    def test_4_cdq(self):
        '''实时状态监控 > 预测理论功率曲线 > 超短期 > 两天'''
        driver=self.driver
        driver.maximize_window()
        start(driver,'http://192.168.60.21:8080/SPPS/weatherInfo/temCurveAction.action')
        click_list = ['实时状态监控', '预测理论功率曲线'] #点击菜单
        menu(driver,click_list)
        if now_time()[0]!=1:
            print("waiting 70")
            time.sleep(70)
        set_date(driver,yes_date(),now_date())
        driver.find_element_by_id('search').click() #搜索
        time.sleep(2)
        hang='/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr'
        global list_heng
        list_heng=get_heng(driver,hang) #获取表格数据
        list_cdq_yuan = get_col_two(list_heng, 2).copy()  # 将表格数据生成列表
        list_cdq = del_list_tup(list_cdq_yuan, ' ')
        if list_cdq == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.PRE_TIME,a.PRE_POWER FROM SPPS_PREDICT_CDQ_DEAL a WHERE PRE_DATE" \
                     " in('yes_date()','now_date()') ORDER BY a.PRE_DATE,a.PRE_TIME"
            sql = sql_kk.replace("now_date()", now_date())
            sql = sql.replace("yes_date()", yes_date())
            list_sql = get_oracle_h(sql, 2)  # 查询数据库
            print('超短期表格数据为:', list_cdq)
            print('超短期sql数据为', list_sql)
            print('\n')
            self.assertEqual(list_cdq, list_sql)
    def test_5_ycll(self):
        '''实时状态监控 > 预测理论功率曲线 > 预测理论功率 > 两天'''
        list_ycll_yuan = get_col_two(list_heng, 3)
        list_ycll = del_list_tup(list_ycll_yuan, ' ')
        if list_ycll == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.PRE_TIME,a.PRE_POWER \
FROM SPPS_PREDICT_CDQ_DEAL_PH a WHERE PRE_DATE in('yes_date()','now_date()') ORDER BY a.PRE_DATE,a.PRE_TIME"
            sql = sql_kk.replace("now_date()", now_date())
            sql=sql.replace("yes_date()",yes_date())
            list_ycll_sql = get_oracle_h(sql, 2)
            print('预测理论功率表格数据为:', list_ycll)
            print('预测理论功率sql数据为', list_ycll_sql)
            print('\n')
            self.assertEqual(list_ycll, list_ycll_sql)
    def test_6_zyg(self):
        '''实时状态监控 > 预测理论功率曲线 > 总有功 > 两天'''
        list_zyg_yuan = get_col_two(list_heng, 4)
        list_zyg = del_list_tup(list_zyg_yuan, ' ')
        if list_zyg == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.GATHER_TIME,a.POWER_VALUE FROM GF_SPPS_POWER_HIS a WHERE " \
                     "a.GATHER_DATE in('yes_date()','now_date()') ORDER BY a.GATHER_DATE,a.GATHER_TIME"
            sql = sql_kk.replace("now_date()", now_date())
            sql = sql.replace("yes_date()", yes_date())
            list_zyg_sql = get_oracle_h(sql, 2)
            print('总有功表格数据为:', list_zyg)
            print('总有功sql数据为', list_zyg_sql)
            print('\n')
            self.assertEqual(list_zyg, list_zyg_sql)
    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()
