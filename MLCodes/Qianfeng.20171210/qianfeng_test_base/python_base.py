#!/usr/bin/python
#-*- coding:utf-8 -*-

"""
1.工程方向
"""
def test():
    print('Today is cool')

"""
2.空4个格 Tab
"""

 # 1.逻辑符的判断

# print(True and False)
# print(True or False)

# 1.1.不等号的表示
# print(2 != 3)
# print(2<>3)

# <> != 是等价的

# 1.2 赋值

# def test():
     # count = 8;
     # count = count + 9
     # count+=9
     # print(count)
    # x = y = z = 1
    # x , y ,z = 1 ,'a string' ,3.14
    # x ,z = z , x
    # print x , z

# test()
"""
定义的变量，数值可变，数据类型不可变
“Python推断机制”
"""

# 1.3 拼接1
# pystr = 'PYTHON'
# iscool = 'IS COOL'
# print(pystr+" \t"+iscool)

# 1.4 拼接2，取值
"""
集合取、赋值，该数据是起始值， 终止值结束
1.从索引位置第0个开始数，计算机程序
2.-1 ， 集合里的最后一个元素
"""
# pystr = 'python'
# print('前2个元素',pystr[:2])
# print(pystr[-1])
# print(type(pystr))

# 2.元祖
# aTuple = 3.14, 234 , -3e44 ,'shuaige'
# print (aTuple[:3])
# print(aTuple[-1])
# print(aTuple[2:])


# 2.1 list
# aList = [3.14, 234 , -3e44 ,'shuaige']
# print(aList[:])
# 用冒号取全部的元素
# print(aList[::-1])
# ::-1 倒序
# print(aList[1:])
# print(aList[::-2])
# 一个是最后元素， 另一个是步长


# 2.2 dict
# aDict = {'name':"shuaige"}
# aDict['score'] = 99
# print(aDict)
# for key in aDict:
#     print(key , aDict[key])


# 3.字符串转换
# a = int('666')
# print(a)
# b = str(666)
# print(b)

# 3.1 字符串的长度
# A = 'abcdef'
# B = len(A)
# # print(B)
# c = range(1,9,2)
# print(c)

# 3.2 enumerrate()获取序列
# aDict = {'name':'shuaige'}
# aDict['socre'] = 99
# print(aDict)
# for (index , key) in enumerate(aDict):
#     print(index , key , aDict[key])

# 3.3 isinstance(对象， 类型)
# print(isinstance(444 , int))
# print(isinstance(4.44 , float))
# print(isinstance(aDict , dict))

# 3.3 删除操作
# aList = [123 ,3.14 ,'a string' ,-3e55]
# # del aList[:3]
# # print(aList)
# del aList[2:]
# print(aList)

# 4.数学运算
# print(cmp(4 , 3))
# print(cmp(3,3))
# print(cmp(5,6))

# 4.1 round()四舍五入
# print(round(4444.45))
# print(round(4444.55))
# print(round(4444.34))
# 小数点后一位
















