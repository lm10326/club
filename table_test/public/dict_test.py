#coding=utf-8
import operator
dict1={"aa":3,"bb":4,"cc":2}
dict2={"aa":3,"bb":4,"cc":2}
dict3={"bb":4,"cc":2,"aa":3}
def cmp_dic_real(dict1,dict2): #纯字典比较，不关注字典key的位置，可以直接if dict1==dict2,所以本方法笨
    i=0
    k=0
    flag=0
    if len(dict1)!=len(dict2):
        print("两个字典值不相同")
    else:
        for key1 in dict1.keys():
            for key2 in dict2.keys():
                if key1==key2:
                    if (dict1[key1]==dict2[key2]):
                        i+=1
        for key2 in dict2.keys():
            for key1 in dict1.keys():
                if key2==key1:
                    if (dict1[key1]==dict2[key2]):
                        k+=1
        if (k==i) and (k==len(dict2)):
            flag=1
    print(flag)
    return flag

def com_dic_l(dict1,dict2): #按顺序比较字典中的值
    list1_val=[]
    list2_val=[]
    flag=0
    for i in dict1.values():
        list1_val.append(i)
    for k in dict2.values():
        list2_val.append(k)
    if dict1.keys()==dict2.keys() and list1_val==list2_val:
        flag=1
    return flag

def com_dict_new_real(dict1,dict2): #比较简单的比较法，对比两个字典是否相等，完全字典比较
    flag=0
    if dict1==dict2:
        flag=1
    return flag
#
if __name__ == '__main__':
    list1=[2,4,5]
    list2=list1.copy() #不随1变
    list3=list1 #随1变化
    list1.pop()
    print(list1,list2,list3)
    print(com_dict_new_real(dict2,dict3))
    list5=[dict2,dict1]
    list6=[dict1,dict3]
    print(operator.eq(dict1,dict3))
    print(operator.eq(list5,list6))