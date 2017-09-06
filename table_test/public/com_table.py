#coding=utf-8
from selenium import webdriver
import time
import datetime
'''获取横向最终表和竖向最终表'''
start=datetime.datetime.now()  #开始时间
driver=webdriver.Firefox()
driver.get('http://192.168.60.167:8080/SPPS/powerCurve/shortAction.action')
driver.find_element_by_id('loginName').send_keys('admin')
driver.find_element_by_id('password').send_keys('123456')
login=driver.find_element_by_xpath('//input[@type="submit"]').click()
click_list=['功率曲线展示','历史曲线']
# click_list=['功率曲线展示','预测曲线','短期预测曲线']
for i in click_list:
    driver.find_element_by_link_text(i).click()
driver.find_element_by_id('beginDate').click()
js = "$('input[id=beginDate]').attr('readonly','')"  
driver.execute_script(js)
driver.find_element_by_id('beginDate').clear()
driver.find_element_by_id('beginDate').send_keys('2017-06-24')  #输入查询开始时间
# time.sleep(2)
driver.find_element_by_id('endDate').click()
js = "$('input[id=endDate]').attr('readonly','')"  
driver.execute_script(js)
driver.find_element_by_id('endDate').clear()
driver.find_element_by_id('endDate').send_keys('2017-06-25')  #输入查询结束时间
# time.sleep(2)
driver.find_element_by_id('search').click()
time.sleep(2)
hang='/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr'
lie=hang+'[1]/td'
tr=driver.find_elements_by_xpath(hang)  #288 行数
td=driver.find_elements_by_xpath(lie) #7 列数
# tr=driver.find_elements_by_xpath('/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr')  #288 竖列
# td=driver.find_elements_by_xpath('/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td') #7 横列
print(len(tr),len(td))
list_henchu=[]   #获取横向列表
for i in range(1,len(tr)+1):
    for k in range(1,len(td)+1):
        m = hang+'[' + str(i) + ']' + '/td[' + str(k) + ']'
        # m='/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr['+str(i)+']'+'/td['+str(k)+']'
        # print(driver.find_element_by_xpath(m).text)
        try:
            list_henchu.append(float(driver.find_element_by_xpath(m).text))
        except:
            list_henchu.append(driver.find_element_by_xpath(m).text)
print("list横向初始值是：",list_henchu)
list_qie=[0]
list_henzhong=[]
for i in range(1,len(tr)+1):
    list_qie.append(len(td)*i)
for i in list_qie:
    list_henzhong.append(list_henchu[i:i+len(td)])
list_henzhong.pop()
print("横向最终值",list_henzhong)


list_suchu=[]    #获取竖向列表
for k in range(1,len(td)+1):
    for i in range(1,len(tr)+1):
        m=hang+'['+str(i)+']'+'/td['+str(k)+']'
        # m = '/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[' + str(i) + ']' + '/td[' + str(k) + ']'
        # print(driver.find_element_by_xpath(m).text)
        try:
            list_suchu.append(float(driver.find_element_by_xpath(m).text))
        except:
            list_suchu.append(driver.find_element_by_xpath(m).text)
print("list竖向初始值是：",list_suchu)
list_qie=[0]
list_suzhong=[]
for i in range(1,len(td)+1):
    list_qie.append(len(tr)*i)
for i in list_qie:
    list_suzhong.append(list_suchu[i:i+len(tr)])
list_suzhong.pop()
print("竖向最终值",list_suzhong) #展示竖向列表
driver.close()
end=datetime.datetime.now()
print(end-start)