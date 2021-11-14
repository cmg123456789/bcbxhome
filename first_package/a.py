# -*- coding:UTF-8 -*-
# import sys
# print(sys.getdefaultencoding())
#
#
# print('abcd',end='')
#
#
#
# print('ADASJJD',end='-')
# print('哎呦')
#
# print(123,end = '。')
 #-*- conding=UTF-8 -*-


# import sys
# print (sys.maxsize)
# print (float('inf'))
# print (type(float('inf')))

# print (sys.getdefaultenconding())


# name = input('请输入您的姓名：')
# class_num = int(input('请输入你的班级：'))
# print ('%s，您好! 欢迎来到边策边学第%d期。'%(name,class_num))

# print(2+1,2*4,6-9,int(15/3))
# print(0%3)
# print (-3//2)
# print (2**10)
#
# print(2<3,10>5,0==0,7<=7,6>=6,5!=4)
#
#
# # print (2<5 and not 3<1)
# # print('cng' == 'cmg')
# print ('a'<'Z')
# print (r'D:\learn python\learn\a.py')



# a = [1,5,3,7,4]
# a.clear()
# print(a)
# b = (1,5,3,7,4)
# c = 'asdb'
#
#
# print (sorted(c,reverse=True))

#
#
# b = (4,3,2,7)
# print(sorted(b,reverse=True))








# a = (2,'f',['a',1,True])
# a[2].
# print(a)

# a = {'ip':'127.0.0.1'}
#
#
#
# a['port'] = 8080
# print (a)
#
# print(a.keys())
# print(a.values())
# print (a.items())

#
# a = ' '
# b = ('a','2','True')
# c =a.join(b)
# print(c)
#
# a ='aa- bb- cc- dd'
# b = a.split(' ')
# print(b)

# a = 'a-3-True//b'
# b = a.split('/')
# print(b)
# print(b[1])

# url = 'http://www.che168.com/beijing/baoma/#pvareaid=105905'
# url_list = url.split('/')
# print(url_list)
# url_dict = {}
# url_dict['city'] = url_list[3]
# url_dict['logo'] = url_list[4]
# url_dict[url_list[-1].split('#')[1].split('=')[0]] = url_list[-1].split('#')[1].split('=')[1]
# # url_dict[url_list[-1][1:9]] = url_list[-1][-6:]
# print(url_dict)


# a = '   hello word'
#
# print (a.strip('w'))
#
# a = 'hello world my name is cmg'
# print (a.startswith('llo',3,10))
#
# a ="'23457551'12"
# print(a.replace('world','python'))
# print(a.isdigit())
#
# a = ('ABC',123)
# c = ('123',)
# print (a>c)

# print(id('cmg'),type('cmg'),'cmg')
# a = 'cmg'
# print(id(a),type(a),a)
#
# l = float(input('请输入长方形的长：'))
# k = float(input('请输入长方形的宽：'))
# zhouchang = (l+k)*2
# mianji = l*k
# if l!=k:
#     print ('这是个长方形，长方形的周长为%.2f,面积为%.2f'%(zhouchang,mianji))
# else:
#     print('这是个正方形，正方形的周长为%.2f'%zhouchang)


# if l<k:
#     if l>0:
#         print (l)
#     else:
#         print(l+k)
# else:
#     print(zhouchang)


# num = int(input('请输入一个数字：'))
# while num<3:
#     print('请继续输入：%d'%num)
#     # num = num+1
#     num +=1
#     if num==100:
#         break


# dict = {'ip':'127.0.0.1','port':'3307','name':'cmg'}
# dict = ('a',3,' ',True)
# for n in dict:
#     print(n)
# for k in dict.keys():
#     print('key:',k)
# for v in dict.values():
#     print ('value',v)
# for i in dict.items():
#     print ('item',i)
#
#
# for k,v in dict.items():
#     print('key:',k)
#     print('value:',v)


# for n in range(0,10,2):
#     print (n)

# a,b = -10,0
# print (abs(a),abs(b))
#
# s,y = divmod(5,3)
# print(s,y)
#
# a = 1.78941246
# print(round(a,0))



# for n in range(55,100):
#     # print(n)
#     if n%3==0:
#         print(n)
#         break
#     # else:
#     #     print(n)

#生成【0,4）区间的数的平方集，将结果放进列表中
# list = []
# for n in range(0,4):
#     list.append(n**2)
# print(list)

#找出【0，8)区间的奇数，结果放进列表
# list = []
# for n in range(0,8):
#     if n%2!=0:
#         list.append(n)
# print(list)

def get_list(x=1,y=10):
    '''生成某个区间的偶数和奇数列表'''
    evens = []
    odds = []
    for a in range(x,y):
        if a%2 == 0:
            evens.append(a)
        else:
            odds.append(a)
    return evens,odds






# a,_= get_list(1,10)
# print(a)

def showmyself(name,**infs):
    '''做一个自我介绍'''
    list= []
    list.append('我的名字叫%s,' % name)
    for inf_k,inf_v in infs.items():
        list.append('我的%s是%s，'%(inf_k,inf_v))
    list.append('谢谢大家')
    return list


# a = showmyself('cmg',性别='男',城市='陕西',年龄='27')
# print(a)

def delete_list_x(list_demo,*x_t):
    '''删除某个列表中的所有某些x'''
    # print(x_t)
    for x in x_t:
        n = list_demo.count(x)
        # print(n)
        for a in range(n):
            list_demo.remove(x)
    return list_demo

# a = [2,4,5,1,7,3,2,5,2]
# delete_list_x(a,2,5)
# print(a)






# handle = open(r'D:\learn python\learn\123','r',encoding='utf-8')   #绝对路径存在转义符，前边加r取消转义
# print(type(handle))   #IO句柄类型
# # print(handle.read(3))    #读取固定长度的内容
# print('------------')
# # print(handle.readline())    #读一行，前边读第一行中读取得剩下的。
# print(handle.readlines()[2])   #将剩下的全部读取，放在列表里。
#
#
# handle.close()     #文件句柄在内存里打开，看不见，看完后关闭文件，释放内存。


# for line in handle:
#     print(line.strip())   #加strip取消多余换行
#
# handle.close()

# handle = open('123','w',encoding='utf-8')
# handle.write('哎呦不错\n')
# handle.close()

# a = input('python的难易程度是：')
# with open('123','w',encoding='utf-8') as handle:
#     handle.write('pyhon好%s啊'%a)
# handle = open('123','r',encoding='utf-8')
# print(handle.read())


# a = 'adasd,3333,True,2019-01'
# for n in range(100,200):
#     b= a.replace('3333',str(n))
#     print(b)


          #--------批量insert数据----------
# sql_demo = "INSERT INTO `learn`.`food` (`food_id`, `admin_id`, `create_time`, `food_desc`, `food_icon`, `food_name`, `food_price`, `food_status`, `food_stock`, `leimu_type`, `update_time`) VALUES (99, 4, null, '店长推荐', 'https:sfaksnf', '盐水鸭', 100.00, 1, NULL, 10, null);"
#
# #withopen一个空字符，意为每次执行此代码，将原有文本内容清空覆盖写进去：
# with open('diancan','w',encoding='utf-8') as insert_food:
#     insert_food.write('')
#
# for n in range(1,100):
#     sql_demo_1 = sql_demo.replace('99',str(n))
#     sql_demo_2 = sql_demo_1.replace('盐水鸭','盐水鸭_%d'%n)
#     # print(sql_demo_2)
#     with open('diancan','a',encoding='utf-8') as insert_food:
#         insert_food.write(sql_demo_2+'\n')


# list_a = [1,2,4,9]
# try:
#     print(list_a[1])
#     file = open('cmg','r')
# except Exception as error:
#     print(list_a[2])
#     print(type(error))
#     print(error)

# if __name__ =='__main__':
#     print('ad')
















































