#coding=utf-8
def get_col(driver,hang): #生成横向列表
    hang = '/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr'
    lie = hang + '[1]/td'
    tr = driver.find_elements_by_xpath(hang)  # 288 行数
    td = driver.find_elements_by_xpath(lie)  # 7 列数
    # tr=driver.find_elements_by_xpath('/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr')  #288 竖列
    # td=driver.find_elements_by_xpath('/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td') #7 横列
    print(len(tr), len(td))
    list_henchu = []  # 获取横向列表
    for i in range(1, len(tr) + 1):
        for k in range(1, len(td) + 1):
            m = hang + '[' + str(i) + ']' + '/td[' + str(k) + ']'
            # m='/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/table/tbody/tr['+str(i)+']'+'/td['+str(k)+']'
            # print(driver.find_element_by_xpath(m).text)
            try:
                list_henchu.append(float(driver.find_element_by_xpath(m).text))
            except:
                list_henchu.append(driver.find_element_by_xpath(m).text)
    print("list横向初始值是：", list_henchu)
    list_qie = [0]
    list_henzhong = []
    for i in range(1, len(tr) + 1):
        list_qie.append(len(td) * i)
    for i in list_qie:
        list_henzhong.append(list_henchu[i:i + len(td)])
    list_henzhong.pop()
    print("横向最终值", list_henzhong)