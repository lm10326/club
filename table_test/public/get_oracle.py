#coding=utf-8
import cx_Oracle
import decimal
def get_oracle_h(host,sql,n): #查询oracle数据库多列，返回由列表组成的列表，列表元素为查询的几列
    username="gf_spps_dr"
    userpwd="gf_spps_dr"
    host=host
    port=1521
    dbname="IMSBASE"
    dsn=cx_Oracle.makedsn(host, port, dbname)
    connection=cx_Oracle.connect(username, userpwd, dsn)
    cursor = connection.cursor()
    sql=sql
#     sql = "SELECT * FROM GF_SPPS_MINUTE_THEORY ORDER BY FOCA_TIME ASC"
#     print(sql)
    cursor.execute(sql)
    result = cursor.fetchall() #结果为元组组成的列表
    # print("原始",result) #显示原始列表
#     print('\n')
    list_s=[]
    for i in result:
        list_s.append(list(i))
#     print("列表",list_s)  #将结果转换成由列表组成的列表
#     print('\n')
    count = cursor.rowcount    #获取查询总数
    if count!=0:
        for i in list_s:
            for k in i:
                try:
                    i[i.index(k)]=round(float(k)+0.0001,n)
                except:
                    pass   
        # print("行组成的列表:",list_s)
    else:
        print("查询结果为空")
        list_s=count
    cursor.close()
    return list_s

def get_oracle_one(host,sql,n): #查询oracle数据库一列，返回列表，列表为查询元素所有列，由行组成的数组
    username="gf_spps_dr"
    userpwd="gf_spps_dr"
    host=host
    port=1521
    dbname="IMSBASE"
    dsn=cx_Oracle.makedsn(host, port, dbname)
    connection=cx_Oracle.connect(username, userpwd, dsn)
    cursor = connection.cursor()
    sql=sql
#     sql = "SELECT * FROM GF_SPPS_MINUTE_THEORY ORDER BY FOCA_TIME ASC"
#     print(sql)
    cursor.execute(sql)
    result = cursor.fetchall() #结果为元组组成的列表
    print("原始",result) #显示原始列表
#     print('\n')
    list_s=[]
    list_x=[]
    for i in result:
        list_x.append(list(i))
#     print("列表",list_s)  #将结果转换成由列表组成的列表
#     print('\n')
    for i in list_x:
        for k in i:
            list_s.append(k)
    count = cursor.rowcount    #获取查询总数
    print(list_s)
    if count!=0:
        for i in list_s:
#             print(i)
            try:
                list_s[list_s.index(i)]=round(float(i),n)
            except:
                pass
        # print("保留两位小数",list_s)
        for i in list_s:
            try:
                if isinstance(i,datetime.timedelta):
                    list_s[list_s.index(i)]=str(i)
                if isinstance(i,datetime.date):
                    list_s[list_s.index(i)]=str(i)
            except:
                pass
        print(list_s)
        for i in list_s: #处理0点时间
            try:
                if ':' in i[0:2]:
                    list_s[list_s.index(i)]='0'+i
            except:
                pass
#         print('小数处理后的列表为：',list_z)
    else:
        list_s=count
    return list_s

def get_oracle_l(host,sql,n): #查询oracle数据库多列，返回由列表组成的列表，列表元素为查询的几列,由列组成的数组
    username="gf_spps_dr"
    userpwd="gf_spps_dr"
    host=host
    port=1521
    dbname="IMSBASE"
    dsn=cx_Oracle.makedsn(host, port, dbname)
    connection=cx_Oracle.connect(username, userpwd, dsn)
    cursor = connection.cursor()
    sql=sql
#     sql = "SELECT * FROM GF_SPPS_MINUTE_THEORY ORDER BY FOCA_TIME ASC"
#     print(sql)
    cursor.execute(sql)
    result = cursor.fetchall() #结果为元组组成的列表
    print("原始",result) #显示原始列表
#     print('\n')
    list_s=[]
    for i in result:
        list_s.append(list(i))
#     print("列表",list_s)  #将结果转换成由列表组成的列表
#     print('\n')
    count = cursor.rowcount    #获取查询总数
    if count!=0:
        for i in list_s:
            for k in i:
                try:
                    i[i.index(k)]=round(float(k),n)
                except:
                    pass   
#         print("小数处理后的列表:",list_s)
        list3=[] 
        list_q=[0]
        list_z=[]
        for i in range(len(list_s[0])):  #生成转置无列表列表
            for k in range(len(list_s)):
                list3.append(list_s[k][i])
#         print(list3)
           
        for i in range(1,len(list_s[0])+1):#切片列表
            list_q.append(len(list_s)*i)
#         print(list_q)
           
        for i in list_q:
            list_z.append(list3[i:i+len(list_s)])#最终转置列表
        list_z.pop()
        print("列组成的列表",list_z)
    else:
        print("查询结果为空")
        list_z=count
    cursor.close()
    return list_z
if __name__ == '__main__':
    get_oracle_l('192.168.60.36', "select GET_DATE,GET_TIME,ARI_TEM,TOTAL_IRRAD FROM GF_SPPS_NWP_DEAL where rownum<=2", 2)
    get_oracle_h('192.168.60.36', "select GET_DATE,GET_TIME,ARI_TEM,TOTAL_IRRAD FROM GF_SPPS_NWP_DEAL where rownum<=2", 2)
# get_oracle_one('192.168.60.36', "select GET_DATE FROM GF_SPPS_NWP_DEAL where rownum<=2", 2)
# print(operator.eq(m,m))