#coding=utf-8
from conf import getpath
getpath()
import unittest
import time
from club.table_test.public.start import start,choose
from club.table_test.public.menu import menu
from club.table_test.public.set_date import set_date
from club.table_test.public.get_heng import get_heng
from club.table_test.public.get_col import get_col,deltup
from club.table_test.public.get_oracle import get_oracle_h
def gf_liuchen(click_list,datelist,its_xpath):#浏览器，菜单列表，是否点日历，日历列表，xpath,数据库列表
    driver = choose("firefox")
    driver.maximize_window()
    start(driver)
    # click_list = ['气象信息展示', '温度曲线'] #点击菜单
    menu(driver,click_list)
    if datelist[0]==1:
        set_date(driver,datelist[1],datelist[2])
    else:
        pass
    driver.find_element_by_id('search').click() #搜索
    time.sleep(2)
    hang=its_xpath
    # hang='/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr'
    list_heng=get_heng(driver,hang).copy() #获取表格数据
    list_wen=get_col(list_heng,n).copy() #将表格数据生成列表
    # list_sql=get_oracle_h('192.168.60.36',"SELECT a.PRE_DATE,a.PRE_TIME,a.ARI_TEM \
    # FROM GF_SPPS_NWP_DEAL a WHERE PRE_DATE='2017-08-08' ORDER BY PRE_TIME asc", 2)#查询数据库
    list_sql=get_oracle_h(list_oracle[0],list_oracle[1],list_oracle[2])
    print(list_wen)
    print(list_sql)
    list_wen.pop()
    return list_wen,list_sql,driver

# assertEqual(list_wen,list_sql)
# driver.close()
if __name__ == '__main__':
    browser="firefox"
    click_list = ['气象信息展示', '温度曲线']
    datelist=[1,'2017-08-08','2017-08-08']
    its_xpath='/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr'
    list_oracle=['192.168.60.36',"SELECT a.PRE_DATE,a.PRE_TIME,a.ARI_TEM FROM "
                                 "GF_SPPS_NWP_DEAL a WHERE PRE_DATE='2017-08-08' ORDER BY PRE_TIME asc", 2]
    list_wen,list_sql,driver=gf_liuchen(browser, click_list,datelist, its_xpath, list_oracle,3)
    assert list_wen,list_sql
    driver.close()
