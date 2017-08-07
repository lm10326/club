#coding=utf-8
# with open('1.txt','w+') as f:
#     kk2=f.readlines()
#     for i in range(5):
#         f.write('\n')
#         f.write(str(i))
# f=open('1.txt','a+')
# kk2=f.read()
# f.write('3')
# kk1=f.read()
# with open('1.txt','w+') as f:
#     for i in 'range(1,5)':
#         f.write('\n')
#         f.write(str(i))
#     kk2=f.readlines()
#     

with open('1.txt','r') as f:
    dd=f.readlines()
with open('1.txt','w+') as f:
    print(dd)
    for i in dd:
        if '2' in i:
            i=i.replace('2','A')
        f.write(i)
    kk1=f.readlines()
    
a='23'
try:
    print(a)
except Exception as e:
    print('k')
    

# # print(kk)
# print(kk2)
# print(kk)