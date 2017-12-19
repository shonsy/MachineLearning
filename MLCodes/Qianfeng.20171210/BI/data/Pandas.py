#!/usr/bin/python
#-*- coding:utf-8 -*-
import pandas as pd
"""
一、Pandas进阶及技巧
"""

country1 = pd.Series({
                    "Name":"中国",
                    'Language':"Chinese",
                    'Area':'9.60M km2',
                    'Happiness Rank':83,
}

)
country2 = pd.Series({
                    "Name":"美国",
                    'Language':"English（US）",
                    'Area':'9.834M km2',
                    'Happiness Rank':14,
}

)
country3 = pd.Series({
                    "Name":"澳大利亚",
                    'Language':"English(AU)",
                    'Area':'9.60M km2',
                    'Happiness Rank':83,
}

)

df = pd.DataFrame([country1 , country2 , country3],index=['CH','US','AU'])
print(df)

print('==============CH/US/AU=============================')

"""
添加数据
1.如果个数小于要求的个数，会自动进行‘广播’操作
2.如果大于要求的个数，会报错的
"""
df['Location'] = '地球'
print(df)


df['Region'] = ['亚洲' ,'北美洲','大洋洲']

print("===========================添加数据========================")

"""
二、Pandas索引
1.行索引
2.列索引
"""
print('loc:')
print(df.loc['CH'])
# 按行排序，列名作为index ， 行向量作为数据

print('===========================行索引=============================')


# 列索引
print(df['Area'])
print(type(df['Area']))

# 混合索引

print(df[['Name' , 'Area']])

print('=============================列索引===============================')

# 混合索引，注意语法上的区别

print('先取行， 再取列')
print(df.loc['CH']['Area'])
print('先取列，再取行')
print(df['Area'].loc['CH'])
print(df['Area'].iloc[0])

print('=========================行，列转换=================================')

print(df.T)
print('================================================')

"""
三、删除数据
"""
print(df.drop('CH'))
print(df)
"""
注意：drop操作只是将修改后的数据copy一份，
而不会对原始数据进行修改
"""
print('==================================================')
print(df.drop(['CH'],inplace=True))
print(df)
print('===============================================')
"""
如果使用了inplace = True，会在原始数据上
进行修改，同时不会返回copy
"""

del df['Name']
print(df)

print('===========================================')


"""
四、DataFrame的加载与操作
"""
report_2015_df = pd.read_csv('2015.csv')
# pd.read_csv 本质就是把任何数据转换成数组

print('2015年数据预览')
print(report_2015_df.head())
print(report_2015_df.info())

print('=====================================================================')

# 使用index_col指定需要读取的索引列
report_2016_df = pd.read_csv('2016.csv',index_col = 'Country',usecols=['Country','Happiness Rank' ,'Happiness Score','Region' ])


print(report_2016_df.head())
print('列名（column）:',report_2016_df.columns)
print('行名（index）:',report_2016_df.index)


print('========================================================')

# 重置index，注意Inplce加与不加的区别

print(report_2016_df.reset_index().head())
print('========================reset_index()===================')


report_2016_redf = report_2016_df.rename(columns={"Region":"地区","Happiness Rank":"幸福排名",

                              "Happiness Score":"幸福指数",
                              })
print(report_2016_redf.head())

print('==================================')


"""
五、Boolean Mask：返回值：True / False
作用：数据清洗
"""
only_western_eurpe_10 = (report_2016_redf['地区'] == 'Western Europe')&(report_2016_redf['幸福排名'] <= 10)
print(only_western_eurpe_10)

print('===========================Boolean Mask=================')


"""
六、数据清洗
"""

log_data = pd.read_csv('log.csv')
print(log_data.head())

print(log_data.fillna(1))
# print(log_data.dropna())
# 此方法慎用
print(log_data.ffill())
print(log_data.bfill())


print('===================================================')

"""
七、数据合并
"""

staff_df = pd.DataFrame([
                        {'姓名':'张三',"部门":'研发部'},
                        {'姓名':'李四',"部门":'财务部'},
                        {'姓名':'赵六',"部门":'市场部'}
])

stu_df = pd.DataFrame([
                        {'姓名':'张三',"专业":'计算机'},
                        {'姓名':'李四',"专业":'会计'},
                        {'姓名':'王五',"专业":'市场营销'}
])


print(staff_df)
print()
print(stu_df)

print('=========================================')
print(pd.merge(staff_df , stu_df , how='outer' , on = '姓名'))
# outr外连接，就是，把2张表进行合并(取并集) ， on就是键（列）
print(staff_df.merge(stu_df ,how='outer' , on = '姓名'))
print('===================================================')

# 内连接
print(pd.merge(staff_df,stu_df , how='inner' , on = '姓名'))
# inner 内连接，就是，把2张表进行取交集，on 就是键（列）

print(staff_df.merge(stu_df , how='inner' , on ='姓名'))

print('=====================================================')

# print(pd.merge(staff_df ,stu_df , how ='right' , on='姓名'))
# print(staff_df.merge(stu_df ,how='right',on='姓名'))

