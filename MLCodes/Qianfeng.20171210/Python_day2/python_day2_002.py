#!/usr/bin/python
#-*- coding:utf-8 -*-
import numpy as np
if __name__ == '__main__':
    # 1.0 创建array数组，通过array函数传递对象
    # L = [1,2,3,4,5]
    # print('L = ',L)
    # a = np.array(L)
    # print('a = ', a )
    # print(type(L),type(a))
    # 1.1 若传递多层嵌套的list，将常建对维数组

    b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    # print('b = \n',b)
    # print('b=',b.shape)

    # 1.2 强行修改shape
    # b.shape = 4,3
#     b.shape = 2,6
#     print('b未修改前是：\n',b)
#     print('b修改后是：\n',b)

# 1.3 使用reshape方法，重新修改尺寸的新数组
    c = b.reshape(2,6)
#     print('b修改后是：\n',c)
#     1.4 数组的元素可以通过dtype的属性获取1

    # print(b.dtype)
    # print(c.dtype)

#     1.5 数组的元素可以通过dtype的属性获取2
    d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]],dtype = np.float)
#     print(d)
    e = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]],dtype = np.complex)
#     print(e)

#     1.6 若改变元素的类型，可以使用astype安全转换
#     f= d.astype(np.int)
#     print('d未被修改前是：\n',d)
#     print(f)

#     2.0 使用创建函数
#     a = range(2,9,0.5)
#     print(a)
#     print('报错',a)
    b = np.arange(1,10,0.5)
    # print(b)

#
#     2.1 linspace函数
    c = np.linspace(0,10,10)
#     print(c)
#     等差函数，第二位数-第一位，就是等差值
#     d = np.linspace(1,10,endpoint=False)
#     print(d)
#     保留小数点后2位
#   2.2 logspace等比函数
#     e = np.logspace(0,10,endpoint=False,base=2)
#     print(e)
#     f = np.logspace(0,10,11,endpoint=False , base=2)
#     print(f)


# 2.3 使用fromstring，等比函数可以从字节常建数组
#     f = 'abcdef'
#     f = 'ABCDEF'
#     g = np.fromstring(f , dtype = np.int8)
#     print(g)

#    3.0 存取
#     a = np.arange(10)
#     print(a)
#     print(a[3])
#     print(a[-1])
#     print(a[:5])
#     3.1 获取某个元素
#     print(a[1:9:2])
#     print(a[::-1])


# 3.2 整数的布尔类型存取
#     a = np.logspace(0,9,10,base=2)
#     print(a)
#     index = np.arange(0,10,2)
#     print(index)
#     b = a[index]
#     print(b)
#     b[2] = 1.6
#     # print(a)
    # print(b)

    # a = np.random.rand(10)
    # print(a)
    # print(a>0.5)
    # a[a>0.5] = 0.5
    # print(a)
# 3.2 标准的矩阵
#     a = np.arange(0,60,10)
#     print(a)
#
#     b = a.reshape(-1,1)
#     print(b)
    # 合并以上代码
    # c = a + b
    # print(c)
    i = np.arange(0,60,10).reshape(-1,1)+np.arange(6)
    print(i)

#   3.3 二维数组的切片
    print(i[[0,1,2],[2,3,4]])
    print(i[4,[2,3,4]])
    print(i[4:,[2,3,4]])

#     3.4 去重
#     a = np.array((1,2,3,33,33,4,5,55,6))
#     print('原数组是：\n',a)
#     b = np.unique(a)
#     print('去重后是：\n',b)

