#!/usr/bin/python
#-*- coding:utf-8 -*-
import numpy as np
if __name__ == '__main__':
# 1.0 创建array数组，通过array函数传递list对象
    L = [1,2,3,4,5,6,7]
    print('L = ',L)
    a = np.array(L)
    print('a = ',a)
    print(type(L),type(a))
#
# 1.1 若传递多层嵌套的list，将创建多维数组
    b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print(b)
    print(a.shape , b.shape)
#  1.2 强行修改shape
    b.shape = 4,3
    print(b)
    b.shape = 2,-1
    print(b)
# 1.3 使用reshape方法，，可以修改尺寸的新数组
    c = b.reshape(4,-1)
    print('b的是：\n',b)
    print('c的是：\n',c)

# 1.4 数组的元素可以通过dtype的属性获得1
    print(b.dtype)
    print(c.dtype)

#1.5 数组的元素可以通过dtype的属性获得2

    d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]],dtype = np.float)
    print(d)
    f = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]],dtype = np.complex)
    print(f)
#1.6 若改变元素的类型，可以使用astype安全的转换
    g = d.astype(np.int)
    print(g)
    d.dtype = np.int
    print(d)

#2.0 使用创建函数
    a = np.arange(1,10,0.5)
    print(a)
    print(type(a),a.dtype)
#     2.1 linspace 函数
    b = np.linspace(1,10,10)
    print(b)

    c = np.linspace(1,10,endpoint=False)
    print(c)

#     2.2 logspace 等比数列

    # d = np.logspace(0,10,endpoint=True,base=2)
    # print(d)
    # np.set_printoptions(suppress=True,linewidth=150)
    # e = np.logspace(0,10,11,endpoint=True,base=2)
    # print(e)

#     2.3 使用fromstring，等比函数可以从字节创建数组
    f = 'abcdefg'
    f = 'ABCDEFG'
    g = np.fromstring(f,dtype = np.int8)
    print(g)

#     3.0 存取
    a = np.arange(10)
    print(a)
    print(a[3])
#     3.1 获取某个元素
    print(a[3:6])
    print(a[:5])
    print(a[3:])
    print(a[1:9:2])
    print(a[::-1])
#     3.1 整数/布尔数组存取 ???

    a = np.logspace(0,9,10,base=2)
    print(a)
    i = np.arange(0,10,2)
    print(i)
    b  = a[i]
    print(b)

    b[2] = 1.6
    print(b)
    print(a)

    a = np.random.rand(10)
    print(a)
    print(a>0.5)
    a[a>0.5] = 0.5
    print(a)
    # 3.2 标准的矩阵
    a = np.arange(0,60,10)
    print(a)
    b = a.reshape(-1,1)
    print(b)
    # # 合并以上代码
    c = a+b
    print(c)
    i = np.arange(0,60,10).reshape(-1,1)+np.arange(6)
    # print(i)


# 3.3 二维数组的切片
    print (i[[0,1,2],[2,3,4]])
    print(i[4,[2,3,4]])
    print(i[4:,[2,3,4]])
    #     4.2 元素去重
    a = np.array((1,2,2,3,3,4,5,6,7,7))
    print ("原数组:",a)
    b = np.unique(a)
    print ("去重后:",b)
