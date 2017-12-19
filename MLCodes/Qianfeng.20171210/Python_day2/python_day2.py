#!/usr/bin/python
#-*- coding:utf-8 -*-
import datetime as dt
import time as tm

    # 一、list
if __name__ == '__main__':

    L = [1 , 'a' , 2 , 'b']
    print(type(L))


#    1.修改前list
    print('修改前：',L)

#    2. 末尾添加元素
    L.append(4)
    print('添加后：',L)

#     3.遍历list
    print('遍历list（for循环）')
    for item in L:
        print(item)
    # 4.通过索引遍历list

    print('遍历list(while循环)：')
    i = 0
    while i != len(L):
        print(L[i])
        i += 1

    # 5.列表合并
    print('列表合并（+）:',[1,2]+[3,4])
#     6.列表重复
    print('列表重复（*）:',[L] * 5)

#     7.判断元素是否在列表中
    print('判断元素存在（in）:', L in [1,2])


# 二、tuple

    t = (1,'a',2,'b')
    print(type(t))

#     1.0 元祖的内容不能修改，否则会报错
#     t[0] = 3
    print(t)
#     2.遍历tuple
    print('遍历list（for循环）：')
    for item in t:
        print(item)
#   3.遍历索引遍历tuple
    print('遍历tuple(while循环):')
    i = 0
    while i != len(t):
        print(t[i])
        i += 1

#     4. 解包 unpack
    a , b , c , d = t
    print('unpack:',c)

# 确保unpack接收的变量个数和tuple的长度相同，否则报错
# 经常出现在函数返回值的赋值时
# a, b, c = t

# 三、dict
    d = {'千锋':'www.1000phone.com',
         '百度':'http://www.baidu.com',
         '阿里巴巴':'www.alibaba.com',
         '腾讯':'https://www.tencent.com'
         }
    print('通过key获取value:',d['千锋'])

#     1. 遍历key
    print('遍历key:')
    for key in d.keys():
        print(key)
#    2. 遍历value
    for value in d.values():
        print(value)

#     3. 遍历item
    print('遍历item:')
    for key , value in d.items():
        print(key+':'+value)

#     4. format输出格式
    print('format输出格式：')
    for key , value in d.items():
        print('{}的网址是{}'.format(key , value))


# 四、set
    print('创建set:')
    my_set = {1,2,3}
    print(my_set)
    my_set = set([1,2,3,2])
    print(my_set)

    print('添加单个元素：')
    my_set.add(3)
    print('添加3:',my_set)

    my_set.add(4)
    print('添加4:',my_set)

    print('添加多个元素：')
    my_set.update([4,5,6])
    print(my_set)


# 五、Python日期时间处理

#     1. 从1970年1月1日算起
    print('当前时间：',tm.time())
#
    dt_now = dt.datetime.fromtimestamp(tm.time())
    print(dt_now)
    print('{}年{}月{}日'.format(dt_now.year, dt_now.month, dt_now.day))
# import datetime as dt 拿到年、月、日

#     日期计算
    delta = dt.timedelta(days = 100)
    # 年月日的100天

    print('今天的前100天：',dt.date.today() - delta)
    print(dt.date.today() > dt.date.today() - delta)
#     今天是否大于前100天的当天日期

print(dt.datetime.fromtimestamp(tm.time()))
dt_now = dt.datetime.fromtimestamp(tm.time())
print('{}年{}月{}日'.format(dt_now.year , dt_now.month , dt_now.day))




