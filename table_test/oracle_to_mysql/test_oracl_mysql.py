import unittest
from club.table_test.oracle_to_mysql.get_mysql import get_mysql_h
from club.table_test.oracle_to_mysql.get_oracle import get_oracle_h
class MyTestCase(unittest.TestCase):
    def test_something(self):
        table_list = ["GF_SPPS_COLLECTION_DATA",
                 "SPPS_UPLOAD_STATE",
                 "SPPS_PTC_STATISTICS_DAY",
                 "SPPS_PTC_PANELS_INFO",
                 "SPPS_PTC_FLIMITH_SET",
                 "SPPS_PTC_FARM_INFO",
                 "SPPS_PTC_FARM_CONFIG",
                 "SPPS_PREDICT_CDQ_HIS_PH_BAK",
                 "SPPS_PREDICT_CDQ_HIS_PH",
                 "SPPS_PREDICT_CDQ_HIS_BAK",
                 "SPPS_PREDICT_CDQ_HIS",
                 "SPPS_PREDICT_CDQ_DEAL_PH_BAK",
                 "SPPS_PREDICT_CDQ_DEAL_PH",
                 "SPPS_PREDICT_CDQ_DEAL_BAK",
                 "SPPS_PREDICT_CDQ_DEAL",
                 "SPPS_POWER_NBQ_BAK",
                 "SPPS_POWER_NBQ",
                 "SPPS_PANELS_GROUP_INFO",
                 "SPPS_FZYI_MON_REAL_BAK",
                 "SPPS_FZYI_MON_REAL",
                 "SPPS_FZYI_MON_HIS_BAK",
                 "SPPS_FZYI_MON_HIS",
                 "SPPS_FSTJ_SUM",
                 "SPPS_FARM_PARAM_SET",
                 "REPORT_REALTIME_BAK",
                 "REPORT_REALTIME",
                 "GF_SPPS_VERSION_SMALL",
                 "GF_SPPS_VERSION",
                 "GF_SPPS_USERS",
                 "GF_SPPS_UP_DOWN_EXE_LOG",
                 "GF_SPPS_SYS_STATE",
                 "GF_SPPS_SYS_LOG",
                 "GF_SPPS_ROLE",
                 "GF_SPPS_PVPARSING_LOG",
                 "GF_SPPS_PROD_THEORY_PARAMS",
                 "GF_SPPS_PROD_THEORY_LOG",
                 "GF_SPPS_PROD_THEORY_BAK",
                 "GF_SPPS_PROD_THEORY",
                 "GF_SPPS_PREDICT_NWP_HIS_BAK",
                 "GF_SPPS_PREDICT_NWP_HIS",
                 "GF_SPPS_PREDICT_NWP_DEAL_BAK",
                 "GF_SPPS_PREDICT_NWP_DEAL",
                 "GF_SPPS_POWER_REAL_BAK",
                 "GF_SPPS_POWER_REAL",
                 "GF_SPPS_POWER_HIS_BAK",
                 "GF_SPPS_POWER_HIS",
                 "GF_SPPS_PLAN_POWER_SS_HIS",
                 "GF_SPPS_PLAN_POWER_SS_DEAL",
                 "GF_SPPS_PLAN_POWER_HIS",
                 "GF_SPPS_PLAN_POWER_DEAL",
                 "GF_SPPS_NWP_HIS_BAK",
                 "GF_SPPS_NWP_HIS",
                 "GF_SPPS_NWP_DEAL_BAK",
                 "GF_SPPS_NWP_DEAL",
                 "GF_SPPS_MONITOR_LOG",
                 "GF_SPPS_MINUTE_THEORY_BAK",
                 "GF_SPPS_MINUTE_THEORY"]
        list_result=[]
        for table_name in table_list:
            sql='''select * from '''+table_name
            # print(sql)
            print("\n")
            print(str(table_list.index(table_name))+" oracle查询",sql)
            list_oracle=get_oracle_h("192.168.60.36", sql, 10)
            # print("mysql查询",sql)
            list_mysql=get_mysql_h("192.168.60.36",sql,10)
            try:
                self.assertEqual(list_mysql,list_oracle)
            except Exception as e:
                print(e)
                list_result.append(table_name+''' is not equal''')
        self.assertEqual(list_result,[])
if __name__ == '__main__':
    unittest.main()
