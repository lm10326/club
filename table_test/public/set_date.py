#coding=utf-8
def set_date(driver,datebegin,dateafter): #设置开始时间和结束时间
    driver.find_element_by_id('beginDate').click()
    js = "$('input[id=beginDate]').attr('readonly','')"
    driver.execute_script(js)
    driver.find_element_by_id('beginDate').clear()
    driver.find_element_by_id('beginDate').send_keys(datebegin)  #输入查询开始时间
    # time.sleep(2)
    driver.find_element_by_id('endDate').click()
    js = "$('input[id=endDate]').attr('readonly','')"
    driver.execute_script(js)
    driver.find_element_by_id('endDate').clear()
    driver.find_element_by_id('endDate').send_keys(dateafter)  #输入查询结束时间