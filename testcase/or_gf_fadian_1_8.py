#coding=utf-8
from conf import getpath,menu
getpath()
import unittest
import time
from club.table_test.public.start import start,choose
from club.table_test.public.menu import menu
from club.table_test.public.set_date import set_date,now_time,now_date,yes_date,set_date_one
from club.table_test.public.get_heng import get_heng
from club.table_test.public.get_col import get_col,del_list_tup,get_col_two
from club.table_test.public.get_oracle import get_oracle_h
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = choose('firefox')
    def test_1_llfd(self):
        '''实时状态监控 > 发电量曲线 > 理论发电量'''
        driver=self.driver
        driver.maximize_window()
        start(driver,'http://192.168.60.21:8080/SPPS/weatherInfo/temCurveAction.action')
        click_list = ['实时状态监控', '发电量曲线'] #点击菜单
        menu(driver,click_list)
        if now_time()[0]!=1:
            print("waiting 70")
            time.sleep(70)
        driver.find_element_by_id('search').click() #搜索
        time.sleep(2)
        hang='/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr'
        global list_heng
        list_heng=get_heng(driver,hang) #获取表格数据
        list_llfd_yuan = get_col_two(list_heng, 2).copy()  # 将表格数据生成列表
        list_llfd = del_list_tup(list_llfd_yuan, ' ')
        if list_llfd == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.FOCA_TIME,a.THEORY_GENER_NUM \
FROM GF_SPPS_PROD_THEORY a WHERE a.FOCA_DATE='now_date()' and mod(to_char(to_date(a.foca_time,'HH24:mi:ss'),'mi'),15)=0 ORDER BY a.FOCA_TIME asc"
            sql = sql_kk.replace("now_date()", now_date())
            list_sql = get_oracle_h(sql, 2)  # 查询数据库
            print('理论发电量表格数据为:', list_llfd)
            print('理论发电量sql数据为', list_sql)
            print('\n')
            self.assertEqual(list_llfd, list_sql)
    def test_2_ycfd(self):
        '''实时状态监控 > 发电量曲线 > 预测发电量'''
        list_ycfd_yuan = get_col_two(list_heng, 3)
        list_ycfd = del_list_tup(list_ycfd_yuan, ' ')
        if list_ycfd == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.FOCA_TIME,a.FOCA_THEORY_GENER_NUM \
FROM GF_SPPS_PROD_THEORY a WHERE a.FOCA_DATE='now_date()' and mod(to_char(to_date(a.foca_time,'HH24:mi:ss'),'mi'),15)=0 ORDER BY a.FOCA_TIME asc"
            sql = sql_kk.replace("now_date()", now_date())
            list_ycfd_sql = get_oracle_h(sql, 2)
            print('预测发电量表格数据为:', list_ycfd)
            print('预测发电量sql数据为', list_ycfd_sql)
            print('\n')
            self.assertEqual(list_ycfd, list_ycfd_sql)
    def test_3_rlj(self):
        '''实时状态监控 > 发电量曲线 > 日累计发电量'''
        list_rlj_yuan = get_col_two(list_heng, 4)
        list_rlj = del_list_tup(list_rlj_yuan, ' ')
        if list_rlj == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.FOCA_TIME,a.POWER_GENERATION \
FROM GF_SPPS_PROD_THEORY a WHERE a.FOCA_DATE='now_date()' and mod(to_char(to_date(a.foca_time,'HH24:mi:ss'),'mi'),15)=0 ORDER BY a.FOCA_TIME asc"
            sql = sql_kk.replace("now_date()", now_date())
            list_rlj_sql = get_oracle_h(sql, 2)
            print('日累计发电量表格数据为:', list_rlj)
            print('日累计发电量sql数据为', list_rlj_sql)
            print('\n')
            self.assertEqual(list_rlj, list_rlj_sql)

    def test_4_llfd_y(self):
        '''实时状态监控 > 发电量曲线 > 理论发电量'''
        driver = self.driver
        driver.maximize_window()
        start(driver, 'http://192.168.60.21:8080/SPPS/weatherInfo/temCurveAction.action')
        click_list = ['实时状态监控', '发电量曲线']  # 点击菜单
        menu(driver, click_list)
        if now_time()[0] != 1:
            print("waiting 70")
            time.sleep(70)
        set_date_one(driver,yes_date())
        driver.find_element_by_id('search').click()  # 搜索
        time.sleep(2)
        hang = '/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr'
        global list_heng
        list_heng = get_heng(driver, hang)  # 获取表格数据
        list_llfd_yuan = get_col_two(list_heng, 2).copy()  # 将表格数据生成列表
        list_llfd = del_list_tup(list_llfd_yuan, ' ')
        if list_llfd == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.FOCA_TIME,a.THEORY_GENER_NUM \
FROM GF_SPPS_PROD_THEORY a WHERE a.FOCA_DATE='now_date()' and mod(to_char(to_date(a.foca_time,'HH24:mi:ss'),'mi'),15)=0 ORDER BY a.FOCA_TIME asc"
            sql = sql_kk.replace("now_date()", yes_date())
            list_sql = get_oracle_h(sql, 2)  # 查询数据库
            print('理论发电量表格数据为:', list_llfd)
            print('理论发电量sql数据为', list_sql)
            print('\n')
            self.assertEqual(list_llfd, list_sql)

    def test_5_ycfd_y(self):
        '''实时状态监控 > 发电量曲线 > 预测发电量'''
        list_ycfd_yuan = get_col_two(list_heng, 3)
        list_ycfd = del_list_tup(list_ycfd_yuan, ' ')
        if list_ycfd == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.FOCA_TIME,a.FOCA_THEORY_GENER_NUM \
FROM GF_SPPS_PROD_THEORY a WHERE a.FOCA_DATE='now_date()' and mod(to_char(to_date(a.foca_time,'HH24:mi:ss'),'mi'),15)=0 ORDER BY a.FOCA_TIME asc"
            sql = sql_kk.replace("now_date()", yes_date())
            list_ycfd_sql = get_oracle_h(sql, 2)
            print('预测发电量表格数据为:', list_ycfd)
            print('预测发电量sql数据为', list_ycfd_sql)
            print('\n')
            self.assertEqual(list_ycfd, list_ycfd_sql)

    def test_6_rlj_y(self):
        '''实时状态监控 > 发电量曲线 > 日累计发电量'''
        list_rlj_yuan = get_col_two(list_heng, 4)
        list_rlj = del_list_tup(list_rlj_yuan, ' ')
        if list_rlj == []:
            print("列表查询数据为空，无法比较")
        else:
            sql_kk = "SELECT a.FOCA_TIME,a.POWER_GENERATION \
FROM GF_SPPS_PROD_THEORY a WHERE a.FOCA_DATE='now_date()' and mod(to_char(to_date(a.foca_time,'HH24:mi:ss'),'mi'),15)=0 ORDER BY a.FOCA_TIME asc"
            sql = sql_kk.replace("now_date()", yes_date())
            list_rlj_sql = get_oracle_h(sql, 2)
            print('日累计发电量表格数据为:', list_rlj)
            print('日累计发电量sql数据为', list_rlj_sql)
            print('\n')
            self.assertEqual(list_rlj, list_rlj_sql)
    def tearDown(self):
        self.driver.close()
        time.sleep(1)
if __name__ == '__main__':
    unittest.main()
