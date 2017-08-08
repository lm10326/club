#coding=utf-8
list1=['你好',23,'ddd',2322]
list2=['你好',3,'dd2d']
def comh(list1,list2): #比较两个列表，并指出哪个元素不同
    list=[]
    if len(list1)<len(list2):
        print("第二个列表比第一个列表长")
        for i in range(len(list1)):
            if list1[i]!=list2[i]:
#                 list.append(i)
                print("第"+str(i+1)+"个元素不相等")
            else :
                pass
        b=0
    elif len(list1)>len(list2):
        print("第一个列表比第二个列表长")
        for i in range(len(list2)):
            if list2[i]!=list1[i]:
#                 list.append(i)
                print("第"+str(i+1)+"个元素不相等")
            else :
                pass
        b=0
    else:
        for i in range(len(list2)):
            if list2[i]!=list1[i]:
                list.append(i)
                print("第"+str(i+1)+"个元素不相等")
            else :
                pass
            b=1
    if list==[] and b==1:
        print("两个列表相等")
        a=1
    else :
        print("两个列表不相等")
        print(list)
        a=0
    return a
if __name__ == '__main__':
    if comh(list1, list2):
        print("ok")
    else:
        print("false")
        
    