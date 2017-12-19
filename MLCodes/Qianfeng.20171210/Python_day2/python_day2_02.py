#!/usr/bin/python
#-*- coding:utf-8 -*-
import numpy as np
if __name__ == '__main__':
    # 一、创建Array
    my_list = [1, 2, 3]
    x = np.array(my_list)
    print('列表：', my_list)
    print('Array: ', x)
    # 向量
    m = np.array([[1, 2, 3], [4, 5, 6]])
    print(m)
    print('shape: ', m.shape)
    n = np.arange(0, 30, 2)
    print(n)
    n = n.reshape(3, 5)
    print('reshape后: ')
    print(n)
    print('ones:\n', np.ones((3, 2)))
    print('zeros:\n', np.zeros((3, 2)))
    print('eye:\n', np.eye(3))
    print('diag:\n', np.diag(my_list))

    print('*操作：\n', np.array([1, 2, 3] * 3))
    print('repeat：\n', np.repeat([1, 2, 3], 3))
    p1 = np.ones((3, 3))
    print(p1)
    p2 = np.arange(9).reshape(3, 3)
    print(p2)
    print('纵向叠加: \n', np.vstack((p1, p2)))
    print('横向叠加: \n', np.hstack((p1, p2)))

    # 二、Array操作
    print('p1: \n', p1)
    print('p2: \n', p2)

    print('p1 + p2 = \n', p1 + p2)
    print('p1 * p2 = \n', p1 * p2)
    print('p2^2 = \n', p2 ** 2)


    p3 = np.arange(6).reshape(2, 3)
    print('p3形状: ', p3.shape)
    print(p3)
    p4 = p3.T
    print('转置后p3形状: ', p4.shape)
    print(p4)

    print('p3数据类型:', p3.dtype)
    print(p3)

    p5 = p3.astype('float')
    print('p5数据类型:', p5.dtype)
    print(p5)


    a = np.array([-4, -2, 1, 3, 5])
    print('sum: ', a.sum())
    print('min: ', a.min())
    print('max: ', a.max())
    print('mean: ', a.mean())
    print('std: ', a.std())
    print('argmax: ', a.argmax())
    print('argmin: ', a.argmin())

#     三、索引与切片

    # 一维array
    s = np.arange(13) ** 2
    print('s: ', s)
    print('s[0]: ', s[0])
    print('s[4]: ', s[4])
    print('s[0:3]: ', s[0:3])
    print('s[[0, 2, 4]]: ', s[[0, 2, 4]])

    # 二维array
    r = np.arange(36).reshape((6, 6))
    print('r: \n', r)
    print('r[2, 2]: \n', r[2, 2])
    print('r[3, 3:6]: \n', r[3, 3:6])


    # 过滤
    print(r[r > 30])

    # 将大于30的数赋值为30
    r[r > 30] = 30000.123
    print(r)

    r2 = r[:3, :3]
    print(r2)


    # 将r2内容设置为0
    r2[:] = 0

    # 查看r的内容
    print(r)


    # 四、遍历Array

    t = np.random.randint(0, 10, (4, 3))
    print(t)

    for row in t:
        print(row)

    # 使用enumerate()
    for i, row in enumerate(t):
        print('row {} is {}'.format(i, row))

    t2 = t ** 2
    print(t2)

    # 使用zip对两个array进行遍历计算
    for i, j in zip(t, t2):
        print('{} + {} = {}'.format(i, j, i + j))