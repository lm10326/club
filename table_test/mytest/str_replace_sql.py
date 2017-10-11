#coding=utf-8
from conf import getpath,menu
getpath()
import unittest
import time
from club.table_test.public.start import start,choose
# from club.table_test.public.menu import menu
from club.table_test.public.set_date import set_date,now_time,now_date
from club.table_test.public.get_heng import get_heng
from club.table_test.public.get_col import get_col,del_list_tup
from club.table_test.public.get_oracle import get_oracle_h
print(now_date())
# now
sql="SELECT a.PRE_DATE,a.PRE_TIME,a.ARI_TEM FROM GF_SPPS_NWP_DEAL a WHERE PRE_DATE='now_date()' ORDER BY PRE_TIME asc"
sql_kk=sql.replace("now_date()",now_date())
print(sql_kk)
list_shiche_sql=get_oracle_h('192.168.60.36',sql_kk,2)
print('实测监测温度表格数据为:',list_shiche_sql)
print('\n')
            # self.assertEqual(list_shiche,list_shiche_sql)
    # def tearDown(self):
    #     self.driver.close()
if __name__ == '__main__':
    unittest.main()
