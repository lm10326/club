#coding=utf-8
import os
import xlrd
import xlwt
import pymysql
import datetime
import cx_Oracle
from listcom2 import comh
def get_excelvale(row,col): #返回固定excel下某一单元格内容
    workbook = xlrd.open_workbook(r'E:\workspace\table_test\src\public\conf.xlsx')
    sheet1 = workbook.sheet_by_name('sheet1')
    cellvalue=sheet1.cell(row,col).value
    return cellvalue
#    print(sheet1.cell(row,col).value)
#print(get_excelvale(3,2)) #调试函数
#   

# def dir_name(name1,name2):   #获取某一路径下包含关键字的绝对路径   旧方法
# #     dir=r'E:\workspace\pytest\src\zr'
#     dir='../file'
#     name=get_excelvale(name1,name2)
#     for filename in os.listdir(dir):
#         if name in filename:
#             dirname=filename
# #            print (filename)
#     return dir+'\\'+dirname  #返回文件名


def dir_name(name1,name2):  #获取某一路径下包含关键字的绝对路径   新方法
    dir=r'E:\workspace\pytest\src\file'
    name=get_excelvale(name1,name2)
    for root,dirs,files in os.walk(dir):
        for file in files:
            if name in file:
                dirname=os.path.join(root,file)
#     print(dirname)
    return dirname
# dir_name(25,8)

def dir_yname(name1,name2):  #获取某一样例路径
    dir=r'E:\workspace\pytest\src\yang'
    name=get_excelvale(name1,name2)
    for root,dirs,files in os.walk(dir):
        for file in files:
            if name in file:
                dirname=os.path.join(root,file)
#     print(dirname)
    return dirname

# def file_name(name1,name2):   #获取某一关键字下的文件名  旧方法
# #     dir=r'E:\workspace\pytest\src\zr'
#     dir='../file'
#     name=get_excelvale(name1,name2)
#     for filename in os.listdir(dir):
#         if name in filename:
#             dirname=filename
# #            print (filename)
#     return dirname  #返回文件名
# #file_name('FJ')  


def file_name(name1,name2):   #获取某一生成文件的文件名  新方法
    dir=r'E:\workspace\pytest\src\file'
    name=get_excelvale(name1,name2)
    for root,dirs,files in os.walk(dir):
        for file in files:
            if name in file:
                dirname=file
#                 print (dirname)
    return dirname  #返回文件名
# file_name(25,8)

def file_yname(name1,name2):   #获取某一样例的文件名
    dir=r'E:\workspace\pytest\src\yang'
    name=get_excelvale(name1,name2)
    for root,dirs,files in os.walk(dir):
        for file in files:
            if name in file:
                dirname=file
#                 print (dirname)
    return dirname  #返回文件名

def get_file(name1,name2,code1,code2,front1,front2,back1,back2): #获取关键字文件第一行某两列之间的数据，返回为一列表，传关键字，
    code=get_excelvale(code1,code2)
    dir=dir_name(name1,name2)
    if get_excelvale(front1,front2)!='':
        front=int(get_excelvale(front1,front2))-1
    else:
        front=1
    if get_excelvale(back1,back2)!='':
        back=int(get_excelvale(back1,back2))
    else:
        back=''
    print(dir)
#    print(code)                  
    fo = open(dir,"r+",encoding=code)
    line = fo.readlines()
    list1=[]
    for i in line:
        if '#1' in i:
            list1=i
            break
    if list1==[]:
        print("#1 is not exit")
    list1=str(list1).split()
    if back=='':
        list=list1[front:]
    else:
        list=list1[front:back]
    line.reverse()
    for i in line:
        if "#" in i:
            last=i
            break
    last2=((last.split()[0]).split("#"))[1] #获取文件除头尾信息的总行数
    int(last2)
    list.append(last2)
    list1=[]
    for i in list:
        try:
            list1.append(float(i))
        except:
            list1.append(i)

    print("文件生成列表：",list1)
    fo.close()
    return list1
#      
#kk=get_file('24B',0,4)
# 
def get_mysql(host1,host2,sql1,sql2,n1,n2): #查询mysql数据库,传数据库地址，sql查询，保留小数位数
    host=get_excelvale(host1,host2)
    conn = pymysql.connect(host=host,port=3306,user='rpps',passwd='rpps',db='rpps',charset='utf8')
    cur = conn.cursor()
    sql=get_excelvale(sql1,sql2)
#    print(sql)
    cur.execute(sql)  #设置查询参数
    col=cur.execute(sql) #获取总行数
    list1=list(cur.fetchall()[0])  #获取第一行元素,结果为元组组成的元组
    # print(list1)
    for i in list1: #将日期类型转成字符串类型
        if isinstance(i,datetime.timedelta):
            list1[list1.index(i)]=str(i)
        if isinstance(i,datetime.date):
            list1[list1.index(i)]=str(i)
    for i in list1: #将0:11:00转成00：11:00类型
        try:
            if ':' in i[0:2]:
                list1[list1.index(i)]='0'+i
        except:
            pass
    list1.append(col)
#     print(list1)
    n=int(get_excelvale(n1,n2))       #excel数据返回的值是float型需转成int
    for i in list1:
        try:
            list1[list1.index(i)]=round(float(i),n)
        except:
            pass
#             print("hh")
    print("mysql查询列表：",list1) 
    cur.close()
    conn.close()
    return list1


def get_oracle(host1,host2,sql1,sql2,n1,n2): #查询oracle数据库
    username="gf_spps_dr"
    userpwd="gf_spps_dr"
    host=get_excelvale(host1,host2)
    port=1521
    dbname="IMSBASE"
    dsn=cx_Oracle.makedsn(host, port, dbname)
    connection=cx_Oracle.connect(username, userpwd, dsn)
    cursor = connection.cursor()
    sql=get_excelvale(sql1,sql2)
#     sql = "SELECT * FROM GF_SPPS_MINUTE_THEORY ORDER BY FOCA_TIME ASC"
#     print(sql)
    cursor.execute(sql)
    
    result = cursor.fetchall() #结果为元组组成的列表
    count = cursor.rowcount    #获取查询总数
    list=[]
    list1=[]
    if count!=0:   
        m=str(result[0]) #第一个元组
#         print(m)
        for i in result[0]:
            i=str(i)
            list.append((i.split())[0])
        for i in list:
            try:
                list1.append(float(i))
            except:
                list1.append(i)
        list1.append(count)
        print(list1)
    else:
        print("查询结果为空")
    n=int(get_excelvale(n1,n2))       #excel数据返回的值是float型需转成int
    for i in list1:
        try:
            list1[list1.index(i)]=round(float(i),n)
        except:
            pass
    print("oracle查询列表：",list1) 
    cursor.close()
    return list1
print(get_oracle(23,2,23,4,23,5))





