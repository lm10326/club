#coding=utf-8

# from dictlist import get_list
# def pr_list(a,list):
#     for i in list:
#         print(i)
#     print(a)
# list_get=(get_list()['历史曲线']).split(',')
# pr_list(4,list_get)


list3=[['2e',22,5,2],[6,24,68,6]] #获取二维数组某一元素的行列
# for i in list3:
#     for k in i:
#         if k==2:
#             print(list3.index(i),i.index(k))

for i in range(len(list3)):
    for k in range(len(list3[i])):
        if list3[i][k]==6:
            print(i,k)
            break
print(list3[0][k])