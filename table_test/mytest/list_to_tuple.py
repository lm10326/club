#coding=utf-8
import datetime
'''把数据库的结果横向转化'''
# list1=[('2017-06-24', '16:46:59', 22.444, 946), ('2017-06-24', '16:46:59', 22.347, 957)]
# list2=[]  #元组组成的列表变成列表组成的列表，并保留n位小数 多组
# for i in list1:
#     list2.append(list(i))
# print(list2)
# n=2
# for i in list2:
#     for k in i:
#         try:
#             i[i.index(k)]=round(float(k),n)
#         except:
#             pass
# print(list2)
 
#下面进行转置
# list3=[] 
# list_q=[0]
# list_z=[]
# for i in range(len(list1[0])):  #生成转置无列表列表
#     for k in range(len(list1)):
#         list3.append(list1[k][i])
# print(list3)
#  
# for i in range(1,len(list1[0])+1):#切片列表
#     list_q.append(len(list1)*i)
# print(list_q)
#  
# for i in list_q:
#     list_z.append(list3[i:i+2])#最终转置列表
# list_z.pop()
# print(list_z)


# list_temp=[]  
# list_t=((2.333),(3.588))  #mysql查询demo,保留2位小数
# #list_t=[(3.44),(4.445)]  #oracle单行查询，保留2位小数
# for i in list_t:
#     list_temp.append(round(float(i),2))
# print(list_temp)
# 
# 
# list_l=[[3.44],[4.445]] #列表组成的列表保留2位小数
# list_teml=[]
# list_z=[]
# for i in list_l:
#     list_teml=list_teml+list(i)
# print(list_teml)
# for i in list_teml:
#     list_z.append(round(float(i),2))
# print(list_z)

# list_c=[('0:23:22', 12.345, 3.232),(datetime.datetime(2017, 6, 13, 0, 4), 12.345, 3.232), (datetime.datetime(2017, 6, 13, 14, 4), 3.232, 4.3532),(datetime.datetime(2017, 6, 13, 14, 4), 4.262, 22.987), (datetime.datetime(2017, 6, 13, 14, 5), 0.0, 0.0)]
# list_c=[(2.23),(23.232),(23.22)]
list_c=(datetime.datetime(2017, 6, 13, 0, 4),datetime.datetime(2017, 6, 13, 0, 4))
# list_c=[('kkk'),('2017-09-09')]
listx=[]  #元组组成的列表变成列表组成的列表，并保留n位小数
if isinstance(list_c[0],tuple):
    for i in list_c:
        listx.append(list(i))
    a=1
#     print(listx)
else:
    for i in list_c:
        listx.append(i)
#     print(listx)
    a=2
if a==1:     
    n=2
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
        
    for i in listx: #处理0点时间，生成非转置列表
        for k in i:
            try:
                if ':' in k[0:2]:
                    i[i.index(k)]='0'+k
            except:
                pass
    print("横向列表",listx)
       
    list3=[] 
    list_q=[0]
    list_z=[]
    for i in range(len(listx[0])):  #生成转置无列表列表
        for k in range(len(listx)):
            list3.append(listx[k][i])
    print("转置原始列表",list3)
        
    for i in range(1,len(listx[0])+1):#切片列表
        list_q.append(len(listx)*i)
    print("切片 列表",list_q)
        
    for i in list_q:
        list_z.append(list3[i:i+len(listx)])#最终转置列表
    list_z.pop()
    print("竖向列表",list_z)
else:
    n=2
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


# list_x=[]
# list_t=[[22.232300000000002], [22.135]]
# for i in list_t:
#     for k in i:
#         list_x.append(k)
# print(list_x)