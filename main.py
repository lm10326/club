#coding=utf-8
import unittest
import HTMLTestRunner #生成测试报告
import time
# from common import sendmail, conf #导入公共模块：发送邮件，配置文件
testcasedir='testcase' #测试用例目录名
def creatsuitel():
    testunit=unittest.TestSuite()
    #discover 方法定义
    discover=unittest.defaultTestLoader.discover(testcasedir,pattern ='bak_*.py',top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
    return testunit


print(creatsuitel())
if __name__ == '__main__':
    alltestnames = creatsuitel()
    #定义个报告存放路径，支持相对路径
    nowtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    # filename = "E:\\ch_workspace\\club\\report\\result"+ nowtime +".html"
    filename = "E:\\ch_workspace\\club\\report\\result"  + ".html"
    fp = open(filename, 'wb')
    #定义测试报告
    runner =HTMLTestRunner.HTMLTestRunner(
                                      stream=fp,
                                      title=u'测试报告',
                                      description=u'用例执行情况：')

    #执行测试用例
    runner.run(alltestnames)
    fp.close()
    #读取测试报告内容
#     fp = open(filename, 'rb')
#     mailbody = fp.read()
#     fp.close()
#     #发送邮件
#     sendmail.sendmail(conf.getConfig("email","subject")+"["+ nowtime +"]", mailbody)

