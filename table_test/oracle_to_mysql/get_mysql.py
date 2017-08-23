#coding=utf-8
import pymysql
import datetime
def get_mysql_h(host,sql,n=2): #查询mysql数据库,传数据库地址，sql查询，保留小数位数
#     host=get_excelvale(host1,host2)
#     conn = pymysql.connect(host=host,port=3306,user='rpps',passwd='rpps',db='rpps',charset='utf8')
    conn = pymysql.connect(host=host,port=3306,user='root',passwd='root123456',db='imsbase',charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)  #设置查询参数
    col=cur.execute(sql) #获取总行数
    list_c=list(cur.fetchall())
    # print("初始查询值",list_c)
#     list_mc=[('0:23:22', 12.345, 3.232),(datetime.datetime(2017, 6, 13, 0, 4), 12.345, 3.232), (datetime.datetime(2017, 6, 13, 14, 4), 3.232, 4.3532),(datetime.datetime(2017, 6, 13, 14, 4), 4.262, 22.987), (datetime.datetime(2017, 6, 13, 14, 5), 0.0, 0.0)]
    listx=[]  #元组组成的列表变成列表组成的列表，并保留n位小数
    if col!=0:
        for i in list_c:
            listx.append(list(i))
        # print("转成列表组成的列表",listx)
        for i in listx:
            for k in i:
                try:
                    i[i.index(k)]=round(float(k),n)
                except:
                    pass
    #     print(listx)
         
        for i in listx: #将datetime转成字符串型
            for k in i:
                try:
                    if isinstance(k,datetime.timedelta):
                        i[i.index(k)]=str(k)
                    if isinstance(k,datetime.date):
                        i[i.index(k)]=str(k)
                except:
                    pass
    #     print(listx)
        for i in listx: #将特殊时间转换
            for k in i:
                try:
                    if ':' in k[0:2]:
                        i[i.index(k)]='0'+k
                except:
                    pass
        # print("mysqle行组成的列表:",listx)
    else:
        print("查询结果为空")
        listx=col
    cur.close()
    conn.close()
    return listx
def get_mysql_l(host,sql,n=2): #查询mysql数据库,传数据库地址，sql查询，保留小数位数
    conn = pymysql.connect(host=host,port=3306,user='rpps',passwd='rpps',db='rpps',charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)  #设置查询参数
    col=cur.execute(sql) #获取总行数
    list_c=list(cur.fetchall())
    print("初始查询值",list_c)
#     list_mc=[('0:23:22', 12.345, 3.232),(datetime.datetime(2017, 6, 13, 0, 4), 12.345, 3.232), (datetime.datetime(2017, 6, 13, 14, 4), 3.232, 4.3532),(datetime.datetime(2017, 6, 13, 14, 4), 4.262, 22.987), (datetime.datetime(2017, 6, 13, 14, 5), 0.0, 0.0)]
    listx=[]  #元组组成的列表变成列表组成的列表，并保留n位小数
    if col!=0:
        for i in list_c:
            listx.append(list(i))
#         print("转成列表组成的列表",listx)
        for i in listx:
            for k in i:
                try:
                    i[i.index(k)]=round(float(k),n)
                except:
                    pass
    #     print(listx)
         
        for i in listx: #将datetime转成字符串型
            for k in i:
                try:
                    if isinstance(k,datetime.timedelta):
                        i[i.index(k)]=str(k)
                    if isinstance(k,datetime.date):
                        i[i.index(k)]=str(k)
                except:
                    pass
    #     print(listx)
        for i in listx: #将特殊时间转换
            for k in i:
                try:
                    if ':' in k[0:2]:
                        i[i.index(k)]='0'+k
                except:
                    pass
        print("行组成列表",listx)
        list3=[] 
        list_q=[0]
        list_z=[]
        for i in range(len(listx[0])):  #生成转置无列表列表
            for k in range(len(listx)):
                list3.append(listx[k][i])
#         print("转置原始列表",list3)
            
        for i in range(1,len(listx[0])+1):#切片列表
            list_q.append(len(listx)*i)
#         print("切片 列表",list_q)
            
        for i in list_q:
            list_z.append(list3[i:i+len(listx)])#最终转置列表
        list_z.pop()
        print("竖向列表",list_z)
    else:
        print("查询结果为空")
        listx=col
    cur.close()
    conn.close()
    return listx

def get_mysql_one(host,sql,n):
    #     host=get_excelvale(host1,host2)
    conn = pymysql.connect(host=host,port=3306,user='rpps',passwd='rpps',db='rpps',charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)  #设置查询参数
    col=cur.execute(sql) #获取总行数
    list_c=list(cur.fetchall())
    print("初始查询值",list_c)
    listx=[]
    for i in list_c:
        for k in i:
            listx.append(k)
    print("列表的值",listx)
    for i in listx:
        try:
            listx[listx.index(i)]=round(float(i),n)
        except:
            pass
    print("单列小数列表",listx)
    for i in listx:
        try:
            if isinstance(i,datetime.timedelta):
                listx[listx.index(i)]=str(i)
            if isinstance(i,datetime.date):
                listx[listx.index(i)]=str(i)
        except:
            pass
    print("单列列表",listx)
    for i in listx: #处理0点时间
        try:
            if ':' in i[0:2]:
                listx[listx.index(i)]='0'+k
        except:
            pass

# get_mysql_h('192.168.60.35','SELECT ctime,speed ,direction FROM rpps_data_calstation ORDER BY ctime asc limit 2',2)
# get_mysql_l('192.168.60.35','SELECT ctime,speed ,direction FROM rpps_data_calstation ORDER BY ctime asc limit 2',2)
# get_mysql_one('192.168.60.35','SELECT ctime FROM rpps_data_calstation ORDER BY ctime asc limit 2',2)
sqldate="\"2017-08-04\""
sql_old="SELECT a.PRE_DATE,a.PRE_TIME,a.ARI_TEM,a.WIND_SPEED,a.HUMIDITY,a.PRESSURE,a.TOTAL_IRRAD,a.DIRECT_IRRAD,a.DIFFUSE_IRRAD,a.GROUP_ID \
FROM GF_SPPS_NWP_DEAL a WHERE a.PRE_DATE=sqldate ORDER BY a.PRE_TIME"

# sql=sql_old.replace("sqldate",sqldate)
# get_mysql_h('192.168.60.167',sql)
