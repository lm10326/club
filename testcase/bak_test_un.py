import unittest


class MyTestCase(unittest.TestCase):
    def test_table(self):
        # coding=utf-8
        # oracle_talbe_old = {"GF_SPPS_COLLECTION_DATA",
        #                     "GF_SPPS_MONITOR_LOG",
        #                     "GF_SPPS_NWP_DEAL",
        #                     "SPPS_POWER_NBQ",
        #                     "GF_SPPS_NWP_HIS",
        #                     "GF_SPPS_PLAN_POWER_DEAL",
        #                     "GF_SPPS_PLAN_POWER_HIS",
        #                     "GF_SPPS_PLAN_POWER_SS_DEAL",
        #                     "GF_SPPS_PLAN_POWER_SS_HIS",
        #                     "GF_SPPS_POWER_HIS",
        #                     "GF_SPPS_POWER_REAL",
        #                     "GF_SPPS_PREDICT_NWP_DEAL",
        #                     "GF_SPPS_PREDICT_NWP_HIS",
        #                     "GF_SPPS_PROD_THEORY",
        #                     "GF_SPPS_PROD_THEORY_LOG",
        #                     "GF_SPPS_PROD_THEORY_PARAMS",
        #                     "GF_SPPS_PVPARSING_LOG",
        #                     "GF_SPPS_ROLE",
        #                     "GF_SPPS_SYS_LOG",
        #                     "GF_SPPS_SYS_STATE",
        #                     "GF_SPPS_UP_DOWN_EXE_LOG",
        #                     "GF_SPPS_USERS",
        #                     "SPPS_FARM_PARAM_SET",
        #                     "SPPS_FZYI_MON_HIS",
        #                     "SPPS_FZYI_MON_REAL",
        #                     "SPPS_PANELS_GROUP_INFO",
        #                     "SPPS_PREDICT_CDQ_DEAL",
        #                     "SPPS_PREDICT_CDQ_HIS",
        #                     "SPPS_PTC_FARM_CONFIG",
        #                     "SPPS_PTC_FARM_INFO",
        #                     "SPPS_PTC_FLIMITH_SET",
        #                     "SPPS_PTC_PANELS_INFO",
        #                     "SPPS_PTC_STATISTICS_DAY",
        #                     "SPPS_UPLOAD_STATE",
        #                     "GF_SPPS_MINUTE_THEORY"}
        # print("原始oracle表为:", oracle_talbe_old)
        # coding=utf-8
        oracle_talbe_new = ["SPPS_UPLOAD_STATE",
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
"GF_SPPS_MINUTE_THEORY",
"GF_SPPS_COLLECTION_DATA"]
        oracle_talbe_new.sort()
        mysql_table=["GF_SPPS_COLLECTION_DATA",
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
"GF_SPPS_MINUTE_THEORY_BAK2",
"GF_SPPS_MINUTE_THEORY1"]
        mysql_table.sort()
        # print("新oracle表为:", oracle_talbe_new)
        # print("新mysqle表为:",mysql_table)
        print('\n')
        print("新oracle"+"和"+"新mysql"+"测试")
        list=[]
        # self.assertEqual(oracle_talbe_new, mysql_table)
        try:
            self.assertEqual(oracle_talbe_new, mysql_table)
        except Exception as e:
            print(e)
            list.append("新oracle"+"和"+"新mysql"+"不相等")

        list1=["mm","nn"]
        list2 = ["mm", "nn"]
        i=list1[0]
        p=list1[1]
        print('\n')
        print(list1[0]+"和"+list2[1]+"测试")
        try:
            self.assertEqual(list1[0],list2[1])
        except Exception as e:
            print(e)
            list.append(list1[0]+"和"+list2[1]+"不相等") #变量可用于循环
        self.assertEqual(list,[])

if __name__ == '__main__':
    unittest.main()
