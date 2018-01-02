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
    def test_1_sjgl(self):
        '''功率曲线展示 > 短期上报曲线 > 实际功率'''
        driver=self.driver
        driver.maximize_window()
        start(driver,'http://192.168.60.21:8080/SPPS/weatherInfo/temCurveAction.action')
        click_list = ['功率曲线展示', '上报曲线'] #点击菜单
        menu(driver,click_list)
        if now_time()[0]!=1:
            print("waiting 70")
            time.sleep(70)
        driver.find_element_by_id('search').click() #搜索
        time.sleep(2)
        hang='/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr'
        global list_heng
        list_heng=get_heng(driver,hang) #获取表格数据
        list_sjgl_yuan = get_col(list_heng, 3).copy()  # 将表格数据生成列表
        list_sjgl = del_list_tup(list_sjgl_yuan, ' ')
        if list_sjgl == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.GATHER_DATE,a.GATHER_TIME,a.POWER_VALUE FROM GF_SPPS_POWER_HIS a \
WHERE a.GATHER_DATE='now_date()' ORDER BY a.GATHER_TIME asc"
            sql = sql_kk.replace("now_date()", now_date())
            list_sql = get_oracle_h(sql, 2)  # 查询数据库
            print('实际功率表格数据为:', list_sjgl)
            print('实际功率sql数据为', list_sql)
            print('\n')
            self.assertEqual(list_sjgl, list_sql)
    def test_2_llgl(self):
        '''功率曲线展示 > 短期上报曲线 > 理论功率'''
        list_llgl_yuan = get_col(list_heng, 4)
        list_llgl = del_list_tup(list_llgl_yuan, ' ')
        if list_llgl == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.FOCA_DATE,a.FOCA_TIME,a.THEORY_NUM FROM GF_SPPS_PROD_THEORY a \
WHERE a.FOCA_DATE='now_date()' and mod(to_char(to_date(a.foca_time,'HH24:mi:ss'),'mi'),15)=0 ORDER BY a.FOCA_TIME asc"
            sql = sql_kk.replace("now_date()", now_date())
            list_llgl_sql = get_oracle_h(sql, 2)
            print('理论功率表格数据为:', list_llgl)
            print('理论功率sql数据为', list_llgl_sql)
            print('\n')
            self.assertEqual(list_llgl, list_llgl_sql)
    def test_3_15min(self):
        '''功率曲线展示 > 短期上报曲线 > 15min预测功率'''
        list_15min_yuan = get_col(list_heng, 5)
        list_15min = del_list_tup(list_15min_yuan, ' ')
        if list_15min == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.PRE_DATE,a.PRE_TIME,a.PRE_POWER \
FROM SPPS_PREDICT_CDQ_HIS a WHERE POINT='15' AND PRE_DATE='now_date()'  ORDER BY PRE_TIME asc "
            sql = sql_kk.replace("now_date()", now_date())
            list_15min_sql = get_oracle_h(sql, 2)
            print('15min预测功率表格数据为:', list_15min)
            print('15min预测功率sql数据为', list_15min_sql)
            print('\n')
            self.assertEqual(list_15min, list_15min_sql)
    def test_4_1h(self):
        '''功率曲线展示 > 短期上报曲线 > 1h预测功率'''
        list_1h_yuan = get_col(list_heng, 6)
        list_1h = del_list_tup(list_1h_yuan, ' ')
        if list_1h == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.PRE_DATE,a.PRE_TIME,a.PRE_POWER \
FROM SPPS_PREDICT_CDQ_HIS a WHERE POINT='60' AND PRE_DATE='now_date()'  ORDER BY PRE_TIME asc"
            sql = sql_kk.replace("now_date()", now_date())
            list_1h_sql = get_oracle_h(sql, 2)
            print('1h理论功率表格数据为:', list_1h)
            print('1h理论功率sql数据为', list_1h_sql)
            print('\n')
            self.assertEqual(list_1h, list_1h_sql)
    def test_5_4h(self):
        '''功率曲线展示 > 短期上报曲线 > 4h预测功率'''
        list_4h_yuan = get_col(list_heng, 7)
        list_4h = del_list_tup(list_4h_yuan, ' ')
        if list_4h == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.PRE_DATE,a.PRE_TIME,a.PRE_POWER \
FROM SPPS_PREDICT_CDQ_HIS a WHERE POINT='240' AND PRE_DATE='now_date()'  ORDER BY PRE_TIME asc"
            sql = sql_kk.replace("now_date()", now_date())
            list_4h_sql = get_oracle_h(sql, 2)
            print('4h理论功率表格数据为:', list_4h)
            print('4h理论功率sql数据为', list_4h_sql)
            print('\n')
            self.assertEqual(list_4h, list_4h_sql)

    def test_6_sjgl(self):
        '''功率曲线展示 > 短期上报曲线 > 实际功率>2天'''
        driver = self.driver
        driver.maximize_window()
        start(driver, 'http://192.168.60.21:8080/SPPS/weatherInfo/temCurveAction.action')
        click_list = ['功率曲线展示', '上报曲线']  # 点击菜单
        menu(driver, click_list)
        if now_time()[0] != 1:
            print("waiting 70")
            time.sleep(70)
        set_date(driver,yes_date(),now_date())
        driver.find_element_by_id('search').click()  # 搜索
        time.sleep(2)
        hang = '/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr'
        global list_heng
        list_heng = get_heng(driver, hang)  # 获取表格数据
        list_sjgl_yuan = get_col(list_heng, 3).copy()  # 将表格数据生成列表
        list_sjgl = del_list_tup(list_sjgl_yuan, ' ')
        if list_sjgl == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.GATHER_DATE,a.GATHER_TIME,a.POWER_VALUE FROM GF_SPPS_POWER_HIS a \
WHERE a.GATHER_DATE in ('yes_date()','now_date()') ORDER BY a.GATHER_DATE,a.GATHER_TIME asc"
            sql = sql_kk.replace("now_date()", now_date())
            sql=sql.replace("yes_date()", yes_date())
            list_sql = get_oracle_h(sql, 2)  # 查询数据库
            print('实际功率表格数据为:', list_sjgl)
            print('实际功率sql数据为', list_sql)
            print('\n')
            self.assertEqual(list_sjgl, list_sql)

    def test_7_llgl(self):
        '''功率曲线展示 > 短期上报曲线 > 理论功率>2天'''
        list_llgl_yuan = get_col(list_heng, 4)
        list_llgl = del_list_tup(list_llgl_yuan, ' ')
        if list_llgl == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.FOCA_DATE,a.FOCA_TIME,a.THEORY_NUM FROM GF_SPPS_PROD_THEORY a \
WHERE a.FOCA_DATE in ('yes_date()','now_date()') and mod(to_char(to_date(a.foca_time,'HH24:mi:ss'),'mi'),15)=0 ORDER BY a.FOCA_DATE,a.FOCA_TIME asc"
            sql = sql_kk.replace("now_date()", now_date())
            sql = sql.replace("yes_date()", yes_date())
            list_llgl_sql = get_oracle_h(sql, 2)
            print('理论功率表格数据为:', list_llgl)
            print('理论功率sql数据为', list_llgl_sql)
            print('\n')
            self.assertEqual(list_llgl, list_llgl_sql)

    def test_8_15min(self):
        '''功率曲线展示 > 短期上报曲线 > 15min预测功率>2天'''
        list_15min_yuan = get_col(list_heng, 5)
        list_15min = del_list_tup(list_15min_yuan, ' ')
        if list_15min == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.PRE_DATE,a.PRE_TIME,a.PRE_POWER \
FROM SPPS_PREDICT_CDQ_HIS a WHERE POINT='15' AND PRE_DATE in ('yes_date()','now_date()') ORDER BY a.PRE_DATE,a.PRE_TIME asc "
            sql = sql_kk.replace("now_date()", now_date())
            sql = sql.replace("yes_date()", yes_date())
            list_15min_sql = get_oracle_h(sql, 2)
            print('15min预测功率表格数据为:', list_15min)
            print('15min预测功率sql数据为', list_15min_sql)
            print('\n')
            self.assertEqual(list_15min, list_15min_sql)

    def test_9_1h(self):
        '''功率曲线展示 > 短期上报曲线 > 1h预测功率>2天'''
        list_1h_yuan = get_col(list_heng, 6)
        list_1h = del_list_tup(list_1h_yuan, ' ')
        if list_1h == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.PRE_DATE,a.PRE_TIME,a.PRE_POWER \
FROM SPPS_PREDICT_CDQ_HIS a WHERE POINT='60' AND PRE_DATE in ('yes_date()','now_date()') ORDER BY a.PRE_DATE,a.PRE_TIME asc"
            sql = sql_kk.replace("now_date()", now_date())
            sql = sql.replace("yes_date()", yes_date())
            list_1h_sql = get_oracle_h(sql, 2)
            print('1h理论功率表格数据为:', list_1h)
            print('1h理论功率sql数据为', list_1h_sql)
            print('\n')
            self.assertEqual(list_1h, list_1h_sql)

    def test_9_0_4h(self):
        '''功率曲线展示 > 短期上报曲线 > 4h预测功率>2天'''
        list_4h_yuan = get_col(list_heng, 7)
        list_4h = del_list_tup(list_4h_yuan, ' ')
        if list_4h == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.PRE_DATE,a.PRE_TIME,a.PRE_POWER \
FROM SPPS_PREDICT_CDQ_HIS a WHERE POINT='240' AND PRE_DATE in ('yes_date()','now_date()') ORDER BY a.PRE_DATE,a.PRE_TIME asc"
            sql = sql_kk.replace("now_date()", now_date())
            sql = sql.replace("yes_date()", yes_date())
            list_4h_sql = get_oracle_h(sql, 2)
            print('4h理论功率表格数据为:', list_4h)
            print('4h理论功率sql数据为', list_4h_sql)
            print('\n')
            self.assertEqual(list_4h, list_4h_sql)
    def tearDown(self):
        self.driver.close()
        # self.driver.quit()
        time.sleep(1)
if __name__ == '__main__':
    unittest.main()
